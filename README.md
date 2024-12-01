## Lichess Auto Analyzer 

This script is designed to streamline the process of downloading and analyzing chess games from [Lichess](https://lichess.org). It allows users to pull all their Lichess games, analyze selected ones, and automatically annotate them using an open-source annotation tool.

### What It Does:
- **Download Games:** Retrieves your games from Lichess using their public API, storing them in a `.pgn` file for easy reference.
- **Analyze and Annotate:** Uses Stockfish (a powerful chess engine) and the `rpdelaney-archive/python-chess-annotator` to generate detailed annotations for each selected game.
- **User Interaction:** Offers the flexibility to manually select games to analyze, automatically analyze multiple games in a batch, or check for recent games.
- **Save Annotated Games:** Annotated games are saved locally, making it easy to track your progress and review analyses.

### Key Features:
1. **Interactive Selection:** Users can choose which games they want to analyze from a list of recent games.
2. **Batch Analysis:** An option to automate the analysis of multiple games, perfect for users with large game histories.
3. **Detailed Game Annotation:** Each game is annotated with comments on good moves, blunders, and insightful moments.

### Dependencies:
- **Python Modules**: 
  - `requs`: To make HTTP requests to Lichess API.
  - `chess.pgn`: To parse and handle chess `.pgn` files.
  - `subprocess`: To run external commands for annotating games.
  - Other built-in modules like `os`, `datetime`, and `re` are used for handling files and text.
- **Stockfish**: A chess engine that must be installed on your system for game analysis.
- **Python Chess Annotator**: Utilizes `rpdelaney-archive/python-chess-annotator` for adding annotations to your games.

### How to Use:
1. **Run the Script**: When you run the script, you'll be prompted to input your Lichess username.
2. **Choose Your Action**:
   - Download your complete game history if not previously done.
   - Select recent games to analyze from the list provided.
   - Opt for batch analysis if you'd like to annotate multiple games at once.
   - Check for any newly played games and add them to your local collection.
3. **Annotations**: The script then uses Stockfish and the annotation tool to evaluate and comment on the games, saving the annotated `.pgn` files locally for review.

### Example Workflow:
- Enter your Lichess username to begin.
- Download all games or simply the recent 10 games.
- Analyze a selected game or let the script auto-analyze multiple games for you.
- View the annotated files in your local `annotated` directory to see game insights like blunders, brilliant moves, and overall evaluation.

### Requirements:
- **Stockfish Installed**: Ensure Stockfish is available on your system, as it is integral for providing accurate game analysis.
- **Python Environment**: This script runs with Python 3, and all required Python modules should be installed beforehand.

### Notes:
- **User Flexibility**: You can always choose between manual game selection or batch processing depending on your needs.
- **Annotated Files**: The annotated games are saved in `.pgn` format in a local directory called `annotated`. You'll also get separate annotations for individual games for easy reference.

This script makes chess analysis both fun and insightful, helping you learn from your games and track your progress as a player.


