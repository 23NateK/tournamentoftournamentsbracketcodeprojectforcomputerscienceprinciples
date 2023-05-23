# tournament of tournaments bracket code project for computer science principles
This project will take a key and responses from students and teachers and will score each of them. It outputs the results to './results.txt'. It uses tkinter for a GUI.
## GUI:
Note: when inputting paths, you can relative paths if you would like.

To use the GUI:
1. In the input box (under the 'Add grading path' button) type in the path to the key file
2. Click the 'Add key path' button
3. In the input box type in the path to a response to be graded, and click the 'Add grading path' button. Do this for each response to be graded
4. Click the 'ExportFiles' button to export the results of the scoring to './results.txt'
## Files:
* main.py - This is mostly used for the tkinter GUI. The program should be started with this file.
* Competitor.py - This defines a Competitor class to represent teachers and students. The class stores their names and scores.
* exportSystem.py - This defines a function to export the results to a file
* importResponse.py - This defines a function to importing a response (or the key) from a file
* score.py - This defines a function to score a list of competitors with the key
* testKey.txt - This is an example key
* testResponse.txt - This is an example response
## Bugs:
* The first response inputted will not show up in the 'To be graded' box
* It may not score it correctly (unsure)
