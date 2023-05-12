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
  pathsLists.insert(END,'\n'+str(pathenterer.get()))
  pathsList.append(str(pathenterer.get()))
  
def removeFile():
  print("es")
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
fileremover.grid(row=0,column=1)
exportbutton.grid(row=0,column=2)
exportlabel.grid(row=1,column=1)
pathsLists.grid(row=1,column=2)
screen.mainloop()
