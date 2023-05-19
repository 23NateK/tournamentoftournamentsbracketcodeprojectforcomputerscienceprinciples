#Main ToDo: GUI
#add buton
#revome buton
#file path inpot
#export botn
#export dispblay labl
#

import Competitor
from exportSystem import exportFile
from importResponse import importResponse
from score import score
from tkinter import *
Noahsdownfall = []
key = ''


def addFile():
  Noahsdownfall.append(str(pathenterer.get()))
  pathsLists.delete('1.0', 'end')
  for i in range(0,len(Noahsdownfall)-1):
    pathsLists.insert(END,'\n'+str(Noahsdownfall[i]))

def removeFile():
  Noahsdownfall.pop(len(Noahsdownfall)-1)
  pathsLists.delete('1.0', 'end')
  for i in range(0,len(Noahsdownfall)-1):
    pathsLists.insert(END,'\n'+str(Noahsdownfall[i]))

def addKey():
  key = str(pathenterer.get())
  keyLabel.config(text = key)

def removeKey():
  key = ''
  keyLabel.config(text = key)

def exportProcess():
  brackets = []
  for i in Noahsdownfall:
    brackets.append(importResponse(i))
  exportFile(score(brackets, key), 'results.txt')



screen = Tk()
rmKey = Button(screen, text = "Remove key", command = removeKey)
pathsLists = Text(screen)
keyLabelIdentifier = Label(screen)
keyLabelIdentifier.config(text = "Key:")
keyLabelIdentifier.grid(row=1, column = 1)
TBG = Label(screen)
TBG.config(text="To be graded:")
TBG.grid(row = 3, column = 1)
addKey = Button(screen, text = "Add key path", command = addKey)
addKey.grid(row=0, column=1)
keyLabel = Label(screen)
keyLabel.grid(row = 2, column = 1)
screen.geometry("500x500")
screen.title("The Tournaments of Tournaments")
fileadder = Button(screen,text="Add grading path",command=addFile)
fileremover = Button(screen,text="Remove Last",command=removeFile)
pathenterer = Entry(screen)
exportbutton = Button(screen,text="ExportFiles",command=exportProcess)
exportlabel = Label(screen)
fileadder.grid(row=0,column=0)
pathenterer.grid(row=1,column=0)
fileremover.grid(row=2,column=0)
exportbutton.grid(row=3,column=0)
exportlabel.grid(row=2,column=1)
pathsLists.grid(row=4,column=1)
screen.mainloop()
