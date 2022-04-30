import tkinter


class DisplaySize():

    """The class DisplaySize has the single task to get the size of the monitor on which the program is running so that the program can scale everything correctly.

    Attributes:
        root: initiates an instance of the tkinter class Tk.
        width: width of the monitor
        height: height of the monitor
    """

    def __init__(self):
        """The constructor of the class. Calls on the Tk method "withdraw".
        """

        self.root = tkinter.Tk()
        self.root.withdraw()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
