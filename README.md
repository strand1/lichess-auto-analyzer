## Lichess Auto Analyzer

This script downloads and analyzes chess games from [Lichess](https://lichess.org), allowing users to retrieve their games, analyze selected ones, and automatically annotate them using [`python-chess-annotator`](https://github.com/rpdelaney-archive/python-chess-annotator).

### Features

- **Download Games:** Retrieve your Lichess games via their public API and store them in a `.pgn` file.
- **Analyze and Annotate:** Utilize Stockfish and `python-chess-annotator` to generate detailed annotations for selected games.
- **User Interaction:**
  - Manually select games to analyze.
  - Automatically analyze multiple games.
  - Check for recent games.
- **Save Annotated Games:** Save annotated games locally.

### Dependencies

- **Stockfish:** A chess engine required for game analysis.
- **Python Chess Annotator:** Leverages [`python-chess-annotator`](https://github.com/rpdelaney-archive/python-chess-annotator) for adding annotations to your games.### How to Use

1. **Run the Script**: Start the script and input your Lichess username when prompted.
2. **Choose an Action**:
   - Download your complete game history locally.
   - Select recent games to analyze from a provided list.
   - Perform batch analysis to annotate multiple games at once.
   - Check for newly played games and add them to your local collection.
   - View annotated files in the `annotated` directory for detailed insights.
3. **Annotations**: The script uses Stockfish and `python-chess-annotator` to evaluate and comment on games, saving annotated `.pgn` files locally.

![Example Auto Analyzer](https://github.com/user-attachments/assets/c5d32e12-b6a1-4c77-99ba-7ce7ae734cd6)

### Requirements

- **Stockfish Installed**: Stockfish must be installed on your system for accurate analysis.
- **Python Environment**: Requires Python 3 and the necessary Python modules installed.

### Notes

- **Annotated Files**: Annotated games are saved as `.pgn` files in a local `annotated` directory, with separate annotations for individual games.

### TODO: 
- Download options (past month, past week...)
- Sort games (opening, color, wins/losses, variant, etc)
- Parse script for further pgn processing, to allow annotated games to integrate with langchain for llm interaction. 

*Bring clarity to your game, reveal patterns, and unlock deeper lines*


