'''
A simple auto cliker.
'''

import tkinter as tk
from tkinter.constants import ANCHOR
from tkinter.messagebox import showinfo 
import pyautogui
import time
import threading

DEFAULT_CLICK_RATE = 1
INITIAL_SLEEP = 2

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.keep_clicking = True
        self.click_count = 0
        self.flag = True

    def create_widgets(self):
        # row 0
        self.click_rate_listbox = tk.Listbox(self, font='arial 16')
        self.click_rate_listbox.insert(0,0.5,1,2,3,4,5)
        self.click_rate_listbox.grid(row=0, column=0, columnspan=2, sticky='e')

        self.create_start_btn()

        self.empty_column_label = tk.Label(self, text=1*' ', bg='black', font='arial 48') # for spacing
        self.empty_column_label.grid(row=0, column=2)

        # row 1
        self.empty_row_label = tk.Label(self, text=1*' ', bg='black', font='arial 48')
        self.empty_row_label.grid(row=1, column=0)

        # row 2
        self.click_count_btn = tk.Button(self, text='click count',  font='arial 48', command=self.show_click_count)
        self.click_count_btn.grid(row=2, column=2, columnspan=2)

    def create_start_btn(self):
        self.start_btn = tk.Button(self, text='start',  font='arial 72', bg='lime', width=10, height=2, command=self.start_clicking_thread)
        self.start_btn.grid(row=0, column=3, columnspan=2)

    def create_stop_btn(self):
        self.stop_btn = tk.Button(self, text='stop', font='arial 72', bg='red', width=10, height=2, command=self.stop_clicking_thread)
        self.stop_btn.grid(row=0, column=3, columnspan=2, sticky='w')

    def start_clicking_thread(self): 
        thread = threading.Thread(target=self.start_btn_clicked)
        thread.start()

    def stop_clicking_thread(self): 
        self.flag = False
        self.start_btn.destroy()
        self.create_start_btn()
        print('STOP RUNNING THREAD')

    def start_btn_clicked(self):
        self.create_stop_btn()

        click_rate = self.click_rate_listbox.get(ANCHOR)
        if not click_rate:
            click_rate = DEFAULT_CLICK_RATE
        click_rate = click_rate ** -1
        time.sleep(INITIAL_SLEEP)
        while self.flag:
            try:
                pyautogui.click()
                self.click_count += 1
                time.sleep(click_rate)
                print('CLICK')
            except pyautogui.PyAutoGUIException:
                # emergency stop (move mouse to one of the corners)
                self.stop_clicking_thread()
        self.flag = True

    def show_click_count(self):
        showinfo('Statistics', f'Click count: {self.click_count}')

def main():
    # entry to program
    root = tk.Tk()
    app = Application(master=root)
    root.title('Auto Clicker')
    app['bg'] = 'black'
    app.mainloop()

if __name__ == '__main__':
    main()