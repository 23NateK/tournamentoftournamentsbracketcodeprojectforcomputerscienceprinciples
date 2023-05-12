#Main ToDo: GUI
#add buton
#revome buton
#file path inpot
#export botn
#export dispblay labl
#

from tkinter import *
pathsList = []


def addFile():
  pathsList.append(str(pathenterer.get()))
  pathsLists.config(text="")
  for i in range(0,len(pathsList)-1):
    pathsLists.insert(END,'\n'+str(pathsList[i]))
  
def removeFile():
  pathsList.pop(len(pathsList)-1))
  pathsLists.clear()
  for i in range(0,len(pathsList)-1):
    pathsLists.insert(END,'\n'+str(pathsList[i]))
def exportFiles():
  print("yes")

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
