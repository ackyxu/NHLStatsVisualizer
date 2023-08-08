from tkinter import filedialog as fd
from FrontEnd.Python.Dialog import Dialog
import os

class OpenFileDialog(Dialog):
    def __init__(self, initPath) -> None:
        super().__init__()
        self.fileTypes = (
            ("SQLite3 Database", "*.db"),
            ("All Files", "*.*")
        )
        self.initPath = initPath

    def OpenDialog(self) -> str:
        return self.OpenFileDialog()


    def OpenFileDialog(self) -> str:
            return fd.askopenfilename(
            title = "Please Select a Database",
            initialdir= self.initPath,
            filetypes=self.fileTypes
        )
