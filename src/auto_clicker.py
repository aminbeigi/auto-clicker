"""
A simple autocliker.
"""

import tkinter as tk
from tkinter.messagebox import showinfo 
import pyautogui
import time

running = False

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.keep_clicking = True
        self.click_count = 0

    def create_widgets(self):
        # row 0
        self.fast_btn = tk.Entry(self, font='arial 24', bg='red', width=10)
        self.fast_btn.grid(row=0, column=0, columnspan=2, sticky='e')

        self.start_btn = tk.Button(self, text="start",  font='arial 72', bg='lime', width=10, height=2, command=self.start_btn_clicked)
        self.start_btn.grid(row=0, column=3, columnspan=2)

        self.empty_column_label = tk.Label(self, text=1*' ', bg='black', font='arial 48')
        self.empty_column_label.grid(row=0, column=2)

        # row 1
        self.empty_row_label = tk.Label(self, text=1*' ', bg='black', font='arial 48')
        self.empty_row_label.grid(row=1, column=0)

        # row 2
        self.click_count_btn = tk.Button(self, text="click count",  font='arial 48', command=self.show_click_count)
        self.click_count_btn.grid(row=2, column=0, columnspan=2)

        self.about_btn = tk.Button(self, text="about",  font='arial 48', command=self.show_about)
        self.about_btn.grid(row=2, column=3, columnspan=2)        


    def start_btn_clicked(self):
        self.start_btn = tk.Button(self, text="stop", font='arial 72', bg='red', width=10, height=2)
        self.start_btn.grid(row=0, column=3, columnspan=2, sticky='w')

        while running:
            time.sleep(3)
            pyautogui.click()
            self.click_count += 1
            print(self.click_count)
    
    def show_click_count(self):
        showinfo('Statistics', f"Click count: {self.click_count}")

    def show_about(self):
        showinfo('speed', f"Fast: 2 clicks a second\nNormal: 2 clicks every 4 second")
    

# entry to program
def main():
    root = tk.Tk()
    app = Application(master=root)
    root.title("Auto Clicker")
    #root.iconbitmap('images/icon.ico')
    app['bg'] = "black"
    app.mainloop()

if __name__ == '__main__':
    main()