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

- [Stockfish](https://stockfishchess.org/)
- [`Python Chess Annotator`](https://github.com/rpdelaney-archive/python-chess-annotator) 

### Use
 **Run the Script**: Start the script and input a Lichess username to download games
 **Choose an Action**:
   - Select from recent games to analyze
   - Perform batch analysis to annotate multiple games at once
   - Check for newly played games and add them to your local collection
   - View annotated files in the `annotated` directory for detailed insights

![Example Auto Analyzer](https://github.com/user-attachments/assets/c5d32e12-b6a1-4c77-99ba-7ce7ae734cd6)
### TODO: 
- Download options (past month, past week...)
- Sort games (opening, color, wins/losses, variant, etc)
- Parse script for further pgn processing, to allow annotated games to integrate with langchain for llm interaction. 

*Bring clarity to your game, reveal patterns, and unlock deeper lines*


