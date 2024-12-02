import requests
import os
import chess.pgn
import subprocess
import re
from datetime import datetime

def download_all_games(username, output_file):
    url = f'https://lichess.org/api/games/user/{username}?tags=true&clocks=false&evals=false&opening=true&literate=false'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded all games for {username} to {output_file}")
    else:
        print(f"Failed to download games for {username}: {response.status_code}")
        exit()

def is_game_analyzed(game, annotated_file):
    if os.path.exists(annotated_file):
        with open(annotated_file, 'r') as f:
            annotated_pgn_content = f.read()
            # Extract the site header from the selected game
            selected_game_site = game.headers.get('Site', '')
            if selected_game_site and selected_game_site in annotated_pgn_content:
                return True
    return False

def download_recent_games(username):
    url = f'https://lichess.org/api/games/user/{username}?max=10&tags=true&clocks=false&evals=false&opening=true&literate=false'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        recent_games = []
        current_game = []
        for line in response.iter_lines():
            line = line.decode('utf-8')  # Ensure the line is decoded properly to a string
            if line.strip() == "":
                if current_game:
                    recent_games.append("\n".join(current_game))
                    current_game = []
            else:
                current_game.append(line)
        if current_game:  # Add the last game if it exists
            recent_games.append("\n".join(current_game))
        return recent_games
    else:
        print(f"Failed to download recent games for {username}: {response.status_code}")
        return None

def is_new_game(game_str, all_games):
    return game_str not in all_games

def get_game_header_info(game):
    white_player = game.headers.get('White', '? player')
    white_elo = game.headers.get('WhiteElo', '? elo')
    black_player = game.headers.get('Black', '? player')
    black_elo = game.headers.get('BlackElo', '? elo')
    result = game.headers.get('Result', '? result')
    game_type = game.headers.get('Event', '? game')
    if game_type == 'Rated blitz game':
        game_type = 'Blitz'
    if game_type == 'Rated bullet game':
        game_type = 'Bullet'
    utc_date = game.headers.get('UTCDate', '? date')
    utc_time = game.headers.get('UTCTime', '? time')
    
    return white_player, white_elo, black_player, black_elo, result, game_type, utc_date, utc_time

def sort_games_by_date(games):
    def parse_date(game):
        utc_date = game.headers.get("UTCDate", "1970.01.01")
        try:
            return datetime.strptime(utc_date, "%Y.%m.%d")
        except ValueError:
            return datetime.min  # Default to earliest date if parsing fails
    return sorted(games, key=parse_date, reverse=True)

def analyze_game(game, engine_path, annotated_file, is_batch=False):
    # Write the selected analyze_gamegame to a temporary PGN file for analysis
    temp_pgn_path = 'temp_game.pgn'
    analyze_time = 0.2 # 0.2 = 12 seconds, 0.25 = 15 seconds
    try:
        with open(temp_pgn_path, 'w') as temp_pgn:
            exporter = chess.pgn.StringExporter(headers=True, variations=True, comments=True)
            temp_pgn.write(game.accept(exporter))
    except (ValueError, IOError) as e:
        print(f"Error writing temporary PGN file: {e}")
        return

    # Command to run chess-annotator as a subprocess
    command = [
        'python3', '-m', 'annotator',
        '--file', temp_pgn_path,
        '--engine', engine_path,
        '--gametime', str(analyze_time), 
        '-t', str(400) # 1000 threads for processing
    ]

    # Run the annotator subprocess and capture the output
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        annotated_pgn_content = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running annotator subprocess: {e.stderr}")
        return

    # Replace NAG symbols with descriptions
    nag_replacements = {
        r'\$1': '!',
        r'\$2': '? (Mistake)',
        r'\$3': '!! (Brilliant)',
        r'\$4': '?? (Blunder)',
        r'\$5': '!? (Interesting)',
        r'\$6': '?! (Inaccuracy)'
    }

    for nag, description in nag_replacements.items():
        annotated_pgn_content = re.sub(nag, description, annotated_pgn_content)

    # If in batch mode, directly append the content to the annotated file
    if is_batch:
        try:
            with open(f"annotated/batch_{annotated_file}", 'a') as f:
                f.write(annotated_pgn_content + '\n\n')
            print(f"Annotated game saved to annotated/{annotated_file}")
        except (ValueError, IOError) as e:
            print(f"Error writing annotated PGN file: {e}")
    else:
    # Save the updated annotated PGN to the target file
        try:
            with open(f"annotated/{annotated_file}", 'a') as f:
                f.write(annotated_pgn_content)
            print(f"Annotated game saved to annotated/{annotated_file}")
        except (ValueError, IOError) as e:
            print(f"Error writing annotated PGN file: {e}")
        
        # file path using UTC date and time
        file_path = f'annotated/raw_{annotated_file}.pgn'
        os.rename(temp_pgn_path, file_path)

    # clean up the temporary PGN file
    if os.path.exists(temp_pgn_path):
        os.remove(temp_pgn_path)


def main():
    username = input("Enter Lichess user: ").strip() or '' # add your username here if you want
    games_file = f'games/{username}_all_games.pgn'
    annotated_file = f'{username}_annotated.pgn'
    engine_path = "" # put your stockfish enghine path here
    games_batch = 20 # how many games to display in the menu

    if not os.path.exists(games_file):
        download_all_games(username, games_file)
    else:
        print(f"Using existing game file: {games_file}")

    with open(games_file, 'r') as pgn_file:
        all_games = []
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break
            all_games.append(game)

        all_games = sort_games_by_date(all_games)
        
        while len(all_games) > 0:
            # Display the most recent number of games in a menu for the user to select from
            for index, game in enumerate(all_games[:games_batch], start=1):
                white_player, white_elo, black_player, black_elo, result, game_type, utc_date, utc_time = get_game_header_info(game)
                print(f"{index}. {white_player}({white_elo}) vs {black_player}({black_elo}), {game_type}, {result}")

            # Ask the user which game to analyze or whether they want more games or auto-import [MENU]
            game_choice = input(f"\nChoose a game to analyze (1-{games_batch}), (c)heck for new games, see the (n)ext {games_batch} games, or (a)uto analyze some games: ")

            if game_choice.lower() == 'n':
                # Skip to the next set of games
                all_games = all_games[games_batch:]
                if len(all_games) == 0:
                    print("No more games available.")
            elif game_choice.lower() == 'c':
                # Check for new games
                recent_games = download_recent_games(username)
                if recent_games:
                    new_games = [game for game in recent_games if is_new_game(game, all_games)]
                    if new_games:
                        print(f"Found {len(new_games)} new games. Downloading...")
                        with open(games_file, 'a') as f:
                            for game in new_games:
                                f.write(game + '\n\n')
                        print("New games have been added to the local file.")
                    else:
                        print("No new games found.")
            elif game_choice.lower() == 'a':
                try:
                    num_games = int(input("How many games to process? ").strip())
                except ValueError:
                    print("Invalid number. Exiting.")
                    return

                analyzed_count = 0
                for game in all_games:
                    if analyzed_count >= num_games:
                        break
                    white_player, white_elo, black_player, black_elo, result, game_type, utc_date, utc_time = get_game_header_info(game)
                    if not is_game_analyzed(game, annotated_file):
                        print(f"Analyzing game: {white_player}({white_elo}) vs {black_player}({black_elo}), {game_type}, {result} ")
                        analyze_game(game, engine_path, annotated_file, is_batch=True)
                        analyzed_count += 1
                    else:
                       print(f"{white_player}({white_elo}) vs {black_player}({black_elo}), {game_type}, {result} - already analyzed, ")
                break
            else:
                try:
                    game_index = int(game_choice) - 1
                    if 0 <= game_index < len(all_games[:games_batch]):
                        game = all_games[game_index]
                        white_player, white_elo, black_player, black_elo, result, game_type, utc_date, utc_time = get_game_header_info(game)
                        out_path = f'{white_player}_vs_{black_player}_{game_type.lower()}_{utc_date}_{utc_time}.pgn'

                        if not is_game_analyzed(game, out_path):
                            print(f"Analyzing: {white_player}({white_elo}) vs {black_player}({black_elo}), {game_type}, {result} ")
                            
                            analyze_game(game, engine_path, out_path)
                        else:
                            print(f"{white_player}({white_elo}) vs {black_player}({black_elo}), {game_type}, {result} - already analyzed, ")
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and {games_batch}.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and {games_batch}, 'n', or 'a'.")

if __name__ == "__main__":
    main()
