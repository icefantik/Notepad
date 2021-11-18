from tkinter import *
from tkinter import filedialog
import ParamsHelpWindow

text = None
pathTextFile = ""
class WorkOnFile:
    """Класс для работы с файлами"""
    def CreateFile(self):
        """Функция создания файла"""
        global pathTextFile
        pathTextFile = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        # Разбивает путь к текстовому файлу
        arrPath = pathTextFile.split('/')
        # Проверяем наличие расширения файла перед его созданием
        if arrPath[len(arrPath) - 1][-4:] != ".txt":
            pathTextFile += ".txt"
        open(pathTextFile, "w+")
    def OpenFile(self):
        """Функция открытия файла"""
        global pathTextFile
        oldPath = pathTextFile
        pathTextFile = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if (pathTextFile != ""):
            text.delete("1.0", END)
            with open(pathTextFile, "r") as file:
                s = file.read()
            text.insert(END, s)
        else:
            pathTextFile = oldPath
    def SaveFile(self):
        """Функция записи в файл"""
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
        """Функция создания и записи в файл"""
        self.CreateFile()
        self.SaveFile()

class Interface(WorkOnFile):
    """Класс создания интерфейса приложения"""
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
        """Создание окна и задание параметров экрана"""
        self.window = Tk()
        self.window.title(self.WINDOW_TITLE)
        self.window.geometry(self.WINDOW_GEOMETRY)
        self.topMenu()
        self.entryText()
        self.window.mainloop()

    def topMenu(self):
        """Создание верхнего меню"""
        # Объект меню для секций
        mainmenu = Menu(self.window)
        self.window.config(menu=mainmenu)

        fileMenu = Menu(mainmenu, tearoff=0)
        # Добавление пунктов в меню для работы с фалом
        fileMenu.add_command(label=self.TEXT_CREATE_FILE, command=self.CreateFile)
        fileMenu.add_command(label=self.TEXT_OPEN_FILE, command=self.OpenFile)
        fileMenu.add_command(label=self.TEXT_SAVE_FILE, command=self.SaveFile)
        fileMenu.add_command(label=self.TEXT_SAVEAS_FILE, command=self.SaveFileAs)
        fileMenu.add_command(label=self.TEXT_END_FILE, command=self.window.quit)
        mainmenu.add_cascade(label=self.TEXT_FILE, menu=fileMenu)

        # Добавление пункта для окна "О программе"
        helpMenu = Menu(mainmenu, tearoff=0)
        helpMenu.add_command(label=self.TEXT_ABOUT_PROG, command=self.OpenHelpWindow)
        mainmenu.add_cascade(label=self.TEXT_HELP, menu=helpMenu)

    def OpenHelpWindow(self):
        """Cоздаётся окно для пункта меню "О программе" """
        def exitBtn():
            """Функция закрытия окна"""
            helpWindow.destroy()
            helpWindow.update()
        helpWindow = Toplevel(self.window)
        helpWindow.geometry(ParamsHelpWindow.helpWindowGeometry)
        # Фиксирование размеров окна
        helpWindow.resizable(width=False, height=False)
        Label(helpWindow, text=ParamsHelpWindow.textHelpWindow, width=45, height=0).place(x=0, y=0) # Текст в окне программы
        # Кнопка для выхода из окна о "О программе"
        Button(helpWindow, text="Ok", command=exitBtn, width=10, height=1).place(x=240, y=200)

    ENTRY_WIDTH = 0
    ENTRY_HEIGHT = 0
    def entryText(self):
        """Функция создаёт поле для ввода на весь экран"""
        global text
        self.parseWinGeometry()
        text = Text(width=self.ENTRY_WIDTH, height=self.ENTRY_HEIGHT)
        text.pack()

    def parseWinGeometry(self):
        geometry = self.WINDOW_GEOMETRY.split('x')
        self.ENTRY_WIDTH = int(geometry[0])
        self.ENTRY_HEIGHT = int(geometry[1])