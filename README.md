# Out of the Park Baseball HTML2CSV Converter
# What Is The Tool?
The Out of the Park Baseball HTML2CSV converter is a tool that takes the game's standard html export file and converts it into a more readable/customizable data set. The tool also includes an option to search for undervalued hitters and starting pitchers. No relievers as of now unfortunately.

To set up the tool, extract the zip file and run the exe. That's it! 

To get htmls from the game is a bit more complicated, although still very easy. Simply go in Out of the Park Baseball, click the league tab, then click reports and info>list all players. From there, decide if you want to evaluate pitchers, hitters, or both. If you are going to evaluate pitchers, use the "Pitching Stats 1" view. If you are going to evaluate hitters, use the "Batting Stats 1" view.

I recommend using filters. For hitters, I use a filter where the hitter must have at least 100 plate appearances. For starting pitchers, the pitcher must have at least 10 starts. If you don't use these filters, you could get some wonky results. I might build in filters directly into the tool in the future, but for now the filters in game will have to do.

Next, click report>write report to disk. Then navigate to your league save folder>news>html>temp and get the most recent file. Then paste it into the tool's directory and rename it to whatever you want.

Finally, launch the tool, select your html file, choose the league size, and then click the applicable option. The tool's in-app prompts should guide you from there.

# Troubleshooting/Debugging
If something is wrong with your CSV, first make sure that you were using the correct view. Re-extract the html and try again. If that doesn't work, send the html my way. You can reach me on discord, reddit, or the ootp forums. 

Another problem might come if your html is somehow corrupted. So I always recommend getting a fresh html from the game if something goes wrong. If you see a python error in the console, reach out to me because it is likely an issue on my end.

If the program either doesn't output any players or puts out more than 30 players, that's an issue. Make sure that you select the correct league size. If you still see an issue, send me the html/csv.
