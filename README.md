# NHL Stats Visualizer

This is an visualizer for stats collected from NHL's Stats API (Documentations found [here](https://gitlab.com/dword4/nhlapi)).  It uses the SQLite3 database produce by [NHL Stats API Getter](https://github.com/ackyxu/NHLStatsAPIGetter) to retrieve statistical infomation and display them with graphs in a Eel frontend.

Currently it produces various graphs of a NHL foward for a selected Regular Season year.

## Dependencies and Requirements

The app is tested to work on Python 3.11, but is should work on any Python 3.xx versions.

It uses the following external libraries:
- Python Eel (Frontend) : Uses Javascript to code the Frontend
- Seaborn and Matplotlib (Graphs)
- Scipy and Numpy (For statistical analysis)

It requires the uses of a SQLite3 Database produce by [NHL Stats API Getter](https://github.com/ackyxu/NHLStatsAPIGetter) to retrieve stored API GETs from NHL's Stats RestAPI.  This is to save time as pulling stats such as shots coordiantes for a player can take > 10 seconds.

## Usage

Set the locations of the SQLite3 Database produce by [NHL Stats API Getter](https://github.com/ackyxu/NHLStatsAPIGetter) in the `DBLOCATION` global variable found in `main.py`

To run the app, run `python main.py` from a command line terminal in the root folder.

## Future Improvement

- To add more options for aggrations of stats to be displayed (Like stats trend accross seasons for both players and league in general)
- Migrate to native Javascript Graphing Libraries to create interactive plots
- Real-time dashboard with stats from a Live NHL Game/Replay past games.
