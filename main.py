#Main ToDo: GUI
#add buton
#revome buton
#file path inpot
#export botn
#export dispblay labl
#

import Competitor
from tkinter import *
Noahsdownfall = []
key = ''


def addFile():
  Noahsdownfall.append(str(pathenterer.get()))
  pathsLists.config(text="")
  for i in range(0,len(Noahsdownfall)-1):
    pathsLists.insert(END,'\n'+str(Noahsdownfall[i]))
  
def removeFile():
  Noahsdownfall.pop(len(Noahsdownfall)-1)
  pathsLists.clear()
  for i in range(0,len(Noahsdownfall)-1):
    pathsLists.insert(END,'\n'+str(Noahsdownfall[i]))
    
def addKey():
  key = str(pathenterer.get())
  keyLabel.config(text = key)
  
def removeKey():
  key = ''
  keyLabel.config(text = key)
  

screen = Tk()
rmKey = Button(screen, text = "Remove key", command = removeKey)
keyLabelIdentifier = Label(screen).config(text="Key:")
keyLabelIdentifier.grid(row=1, column = 1)
TBG = Label(screen).config(text="To be graded:")
TBG.grid(row = 3, column = 1)
addKey = Button(screen, text = "Add key path", command = addKey)
addKey.grid(row=0, column=1)
keyLabel = Label(screen)
screen.geometry("500x500")
screen.title("The Tournaments of Tournaments")
fileadder = Button(screen,text="Add grading path",command=addFile)
fileremover = Button(screen,text="Remove Last",command=removeFile)
pathenterer = Entry(screen)
exportbutton = Button(screen,text="ExportFiles",command=exportFiles)
exportlabel = Label(screen)
pathsLists = Text(screen)
fileadder.grid(row=0,column=0)
pathenterer.grid(row=1,column=0)
fileremover.grid(row=2,column=0)
exportbutton.grid(row=3,column=0)
exportlabel.grid(row=2,column=1)
pathsLists.grid(row=4,column=1)
screen.mainloop()
