#Main ToDo: GUI
#add buton
#revome buton
#file path inpot
#export botn
#export dispblay labl

import tkinter
screen = Tk()
screen.title("The Tournaments of Tournaments")
fileadder = Button(screen,text="Add",command=addFile)
fileremover = Button(screen,text="Remove Last",command=removeFile)
pathenterer = Entry(screen,text="Enter File Here")
exportbutton = Button(screen,text="ExportFiles",command=exportFiles)
exportlabel = Label(screen)
