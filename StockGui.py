import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "StockGui.ui")

class StockguiApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master)
        self.getFdData = ttk.Button(self.frame1)
        self.getFdData.configure(text='Get Data')
        self.getFdData.place(anchor='nw', relx='0.37', rely='0.13', x='0', y='0')
        self.getFdData.configure(command=self.fdButtonClicked)
        self.stockSymbolEntry = ttk.Entry(self.frame1)
        self.stockSymbolEntry.place(anchor='nw', relwidth='0.26', relx='0.20', x='0', y='0')
        self.stockSymbolLabel = ttk.Label(self.frame1)
        self.stockSymbolLabel.configure(text='Stock Symbol')
        self.stockSymbolLabel.place(anchor='nw', relx='0', x='0', y='0')
        self.comboboxFD = ttk.Combobox(self.frame1)
        self.comboboxFD.configure(values='BALANCE_SHEET INCOME_STATEMENT')
        self.comboboxFD.place(anchor='nw', rely='0.14', x='0', y='0')
        self.fdDataTree = ttk.Treeview(self.frame1)

        self.vsb = ttk.Scrollbar(self.frame1, orient="horizontal", command=self.fdDataTree.xview)
        self.vsb.place(anchor ='nw', rely='0.17', width=2000)

        self.fdDataTree.configure(xscrollcommand=self.vsb.set)
        self.fdDataTree.place(anchor='nw', relheight='0.55', relwidth='1.0', rely='0.19', x='0', y='0')
        self.frame1.configure(height='2000', width='2000')
        self.frame1.pack(side='right')
        self.frame1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.frame1

    def fdButtonClicked(self, widget_id):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = StockguiApp(root)
    app.run()
