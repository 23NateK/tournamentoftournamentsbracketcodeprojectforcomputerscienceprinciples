#Main ToDo: GUI
#add buton
#revome buton
#file path inpot
#export botn
#export dispblay labl
#

import Competitor
from tkinter import *
pathListLabel = []


def addFile():
  pathListLabel.append(str(pathenterer.get()))
  pathsLists.config(text="")
  for i in range(0,len(pathsList)-1):
    pathsLists.insert(END,'\n'+str(pathsList[i]))
  
def removeFile():
  pathListLabel.pop(len(pathsList)-1)
  pathsLists.clear()
  for i in range(0,len(pathsList)-1):
    pathsLists.insert(END,'\n'+str(pathsList[i]))
def exportFiles():
  competitorList = []
  for i in pathslist:
    text = open(i,'r')
    #make the code here to create an object named "person" that interprets the text file's name and subclass
    readables = text.readlines() #this returns a list with each row in the file being an object in that list
    line = 0
    for z in range(2,12,2):
      
      
        
      line += 1
    
  

screen = Tk()
screen.geometry("500x500")
screen.title("The Tournaments of Tournaments")
fileadder = Button(screen,text="Add",command=addFile)
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
pathsLists.grid(row=1,column=1)
screen.mainloop()
