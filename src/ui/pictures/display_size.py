import tkinter


class DisplaySize():

    def __init__(self):

        self.root = tkinter.Tk()
        self.root.withdraw()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
