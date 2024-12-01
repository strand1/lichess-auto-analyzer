## Lichess Auto Analyzer 

This script is designed to download and analyze chess games from [Lichess](https://lichess.org). It allows users to pull all their Lichess games, analyze selected ones, and automatically annotate them using `rpdelaney-archive/python-chess-annotator`.

### What It Does:
- **Download Games:** Retrieves your games from Lichess using their public API, storing them in a `.pgn` file for easy reference.
- **Analyze and Annotate:** Uses Stockfish (a powerful chess engine) and the `rpdelaney-archive/python-chess-annotator` to generate detailed annotations for each selected game.
- **User Interaction:** Manually select games to analyze, Automatically analyze multiple games, and Check for recent games.
- **Save Annotated Games:** Annotated games are saved locally.

### Key Features:
1. **Interactive Selection:** Users can choose which games they want to analyze from a list of recent games.
2. **Batch Analysis:** An option to automate the analysis of multiple games, perfect for users with large game histories.
3. **Detailed Game Annotation:** Each game is annotated with comments for inaccuracies, mistakes, and blunders. 

### Dependencies:
- **Stockfish**: A chess engine that must be installed on your system for game analysis.
- **Python Chess Annotator**: Utilizes `rpdelaney-archive/python-chess-annotator` for adding annotations to your games.

### How to Use:
1. **Run the Script**: When you run the script, you'll be prompted to input your Lichess username.
2. **Choose Your Action**:
   - The user's complete game history will be downloaded locally.
   - Select recent games to analyze from the list provided.
   - Or, choose batch analysis if you'd like to annotate multiple games at once.
   - Also, you can check for any newly played games and add them to your local collection.
3. **Annotations**: The script uses Stockfish and the annotator tool to evaluate and comment on the games, saving the annotated `.pgn` files locally for review.

### Example Workflow:
- Enter your Lichess username to begin.
- Download all games or simply the recent 10 games.
- Analyze a selected game or let the script auto-analyze multiple games for you.
- View the annotated files in your local `annotated` directory to see game insights like blunders, brilliant moves, and overall evaluation.

### Requirements:
- **Stockfish Installed**: Ensure Stockfish is available on your system, as it is integral for providing accurate game analysis.
- **Python Environment**: This script runs with Python 3, and all required Python modules should be installed beforehand.

### Notes:
- **Annotated Files**: The annotated games are saved in `.pgn` format in a local directory called `annotated`. You'll also get separate annotations for individual games for easy reference.

### TODO: Will update with further pgn processing, to allow annotated games to integrate with langchain for llm interaction. 

This script makes chess analysis both fun and insightful, helping you learn from your games and track your progress as a player.


