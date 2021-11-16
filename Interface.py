from tkinter import *
from tkinter import filedialog
import ParamsHelpWindow

text = None
pathTextFile = ""
class WorkOnFile:
    def CreateFile(self):
        global pathTextFile
        pathTextFile = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        arrPath = pathTextFile.split('/')
        if arrPath[len(arrPath) - 1][-4:] != ".txt":
            pathTextFile += ".txt"
        open(pathTextFile, "w+")

    def OpenFile(self):
        global pathTextFile
        if pathTextFile == "":
            self.CreateFile()
        else:
            pathTextFile = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    def SaveFile(self):
        global text
        global pathTextFile
        if text != None and pathTextFile != "":
            arrPath = pathTextFile.split('/')
            textFromForm = text.get(1.0, END)
            file = open(pathTextFile, "w+")
            file.write(str(textFromForm))
        if pathTextFile == "":
            self.CreateFile()
            self.SaveFile()
    def SaveFileAs(self):
        self.CreateFile()
        self.SaveFile()

class Interfece(WorkOnFile):
    WINDOW_TITLE = "Notepad"
    WINDOW_GEOMETRY = "720x350"
    TEXT_FILE = "File"
    TEXT_CREATE_FILE = "Create"
    TEXT_OPEN_FILE = "Open"
    TEXT_SAVE_FILE = "Save"
    TEXT_SAVEAS_FILE = "Save as"
    TEXT_END_FILE = "Exit"
    TEXT_HELP = "Help"
    TEXT_ABOUT_PROG = "About programm"
    def __init__(self):
        self.window = Tk()
        self.window.title(self.WINDOW_TITLE)
        self.window.geometry(self.WINDOW_GEOMETRY)
        self.topMenu()
        self.entryText()
        self.window.mainloop()

    def topMenu(self):
        mainmenu = Menu(self.window)  # создаем объект меню для секций
        self.window.config(menu=mainmenu)

        fileMenu = Menu(mainmenu, tearoff=0)
        fileMenu.add_command(label=self.TEXT_CREATE_FILE, command=self.CreateFile)
        fileMenu.add_command(label=self.TEXT_OPEN_FILE, command=self.OpenFile)
        fileMenu.add_command(label=self.TEXT_SAVE_FILE, command=self.SaveFile)
        fileMenu.add_command(label=self.TEXT_SAVEAS_FILE, command=self.SaveFileAs)
        fileMenu.add_command(label=self.TEXT_END_FILE, command=self.window.quit)
        mainmenu.add_cascade(label=self.TEXT_FILE, menu=fileMenu)

        helpMenu = Menu(mainmenu, tearoff=0)
        helpMenu.add_command(label=self.TEXT_ABOUT_PROG, command=self.OpenHelpWindow)
        mainmenu.add_cascade(label=self.TEXT_HELP, menu=helpMenu)

    def OpenHelpWindow(self): # Функция создаёт окно, где будет написано окно о программе
        helpWindow = Toplevel(self.window)
        helpWindow.geometry(ParamsHelpWindow.helpWindowGeometry)
        helpWindow.resizable(width=False, height=False)
        Label(helpWindow, text=ParamsHelpWindow.textHelpWindow).place(x=0, y=3) # Лайбл для текста в окне о программа
        Button(helpWindow, text="Ok", command=helpWindow.quit)

    ENTRY_WIDTH = 0
    ENTRY_HEIGHT = 0
    def entryText(self):
        global text
        self.parseWinGeometry()
        text = Text(width=self.ENTRY_WIDTH, height=self.ENTRY_HEIGHT)
        text.pack()

    def parseWinGeometry(self):
        geometry = self.WINDOW_GEOMETRY.split('x')
        self.ENTRY_WIDTH = int(geometry[0])
        self.ENTRY_HEIGHT = int(geometry[1])