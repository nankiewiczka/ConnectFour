import tkinter as tk
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import StringVar


class View(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.root.configure(background='#1C1B18')
        self.__controller = None
        self.__canvas = None
        self.__canvas_frame = None
        self.__player_label = None
        self.__label_info = StringVar()
        self.__option_menu = None
        self.__canvas_logo = None
        self.__canvas_frame_logo = None
        self.__button_color = '#921414'
        self.__player_color = '#921414'
        self.__button1 = tk.Button(self, command=lambda: self.__controller.click_button(1))
        self.__button2 = tk.Button(self, command=lambda: self.__controller.click_button(2))
        self.__button3 = tk.Button(self, command=lambda: self.__controller.click_button(3))
        self.__button4 = tk.Button(self, command=lambda: self.__controller.click_button(4))
        self.__button5 = tk.Button(self, command=lambda: self.__controller.click_button(5))
        self.__button6 = tk.Button(self, command=lambda: self.__controller.click_button(6))
        self.__button7 = tk.Button(self, command=lambda: self.__controller.click_button(7))
        self.__reset_button = tk.Button(self, command=lambda: self.__controller.reset())
        self.set_buttons()
        self.set_elements()

    def create_gameboard(self, color_board):
        self.grid(row=1, columnspan=14, sticky='N', padx=90, pady=10)
        self.configure(background='#1C1B18')
        self.master.title("Connect Four")
        self.create_canvas()
        self.__create_ovals(color_board)

    def update_gameboard(self, color_board):
        self.__create_ovals(color_board)

    def start_loop(self):
        self.mainloop()

    def create_canvas(self):
        self.__canvas_frame = tk.Frame(self, bd=2, relief=tk.RAISED)
        self.__canvas = tk.Canvas(self.__canvas_frame, bg='#1C1B18', width=720, height=620)
        self.__canvas.pack()
        self.__canvas_frame.grid(row=1, columnspan=8, rowspan=6, pady=5)

    def set_buttons(self):
        self.__button1.grid(row=0, column=0, sticky='E', padx=10, pady=2)
        self.__button1.config(height=2, width=5)
        self.__button1["text"] = "\n1.\n"
        self.__button1.config(background='#0E0E0E',fg='white')
        self.__button1.config(activebackground='#1C1B18')

        self.__button2.grid(row=0, column=1, sticky='E', padx=10, pady=2)
        self.__button2.config(height=2, width=5)
        self.__button2["text"] = "\n2.\n"
        self.__button2.config(background='#0E0E0E',fg='white')
        self.__button2.config(activebackground='#1C1B18')

        self.__button3.grid(row=0, column=2, sticky='E', padx=10, pady=2)
        self.__button3.config(height=2, width=5)
        self.__button3["text"] = "\n3.\n"
        self.__button3.config(background='#0E0E0E',fg='white')
        self.__button3.config(activebackground='#1C1B18')

        self.__button4.grid(row=0, column=3, sticky='E', padx=10, pady=2)
        self.__button4.config(height=2, width=5)
        self.__button4["text"] = "\n4.\n"
        self.__button4.config(background='#0E0E0E',fg='white')
        self.__button4.config(activebackground='#1C1B18')

        self.__button5.grid(row=0, column=4, sticky='E', padx=10, pady=2)
        self.__button5.config(height=2, width=5)
        self.__button5["text"] = "\n5.\n"
        self.__button5.config(background='#0E0E0E',fg='white')
        self.__button5.config(activebackground='#1C1B18')

        self.__button6.grid(row=0, column=5, sticky='E', padx=10, pady=2)
        self.__button6.config(height=2, width=5)
        self.__button6["text"] = "\n6.\n"
        self.__button6.config(background='#0E0E0E',fg='white')
        self.__button6.config(activebackground='#1C1B18')

        self.__button7.grid(row=0, column=6, sticky='E', padx=5)
        self.__button7.config(height=2, width=5)
        self.__button7["text"] = "\n7.\n"
        self.__button7.config(background='#0E0E0E', fg='white')
        self.__button7.config(activebackground='#1C1B18')

        self.__reset_button["text"] = "RESET GAME\n"
        self.__reset_button.config(background='#0E0E0E',fg='white')
        self.__reset_button.config(activebackground='#1C1B18')
        self.__reset_button.grid(row=1, column=10, sticky='N', padx=20, pady=200)

    def set_elements(self):
        self.__label_info.set("PLAYER 1")
        self.__player_label = tk.Label(self, textvariable=self.__label_info, width=20, height=5, bg='#1C1B18', fg='white', bd=0,
                                       highlightthickness=0, font=('Helvetica', 18))
        self.__player_label.grid(row=1, column=10, sticky='N', pady=5, padx=1)

        self.__canvas_frame_logo = tk.Frame(self, bd=0, relief=tk.RAISED)
        self.__canvas_logo = tk.Canvas(self.__canvas_frame_logo, bg=self.__player_color, width=80, height=80)
        self.__canvas_logo.pack()
        self.__canvas_frame_logo.grid(row=1, column=11, sticky='N', pady=20)

        variable = StringVar(self.root)
        variable.set("Klasyczna")

        def option_menu_command(value):
            self.__controller.add_model(value)

        self.__option_menu = OptionMenu(self, variable, "Klasyczna", "Tylko w poziomie", "Tylko w pionie", "Tylko uskośne",
                                        command=option_menu_command)
        self.__option_menu.configure(width=15)
        self.__option_menu.grid(row=1, column=11, sticky='N', pady=200, padx=20)

    def add_controller(self, controller):
        self.__controller = controller

    def update_information(self):
        if self.__label_info.get() == "PLAYER 1":
            self.__label_info.set("PLAYER 2")
            self.__player_color = '#EEC111'
            self.__canvas_logo.configure(bg=self.__player_color)
        else:
            self.__label_info.set("PLAYER 1")
            self.__player_color = '#921414'
            self.__canvas_logo.configure(bg=self.__player_color)

    def reset_view(self):
        self.__label_info.set("PLAYER 1")
        self.__player_color = '#921414'
        self.__canvas_logo.configure(bg=self.__player_color)

    @staticmethod
    def show_warning_window(message):
        messagebox.showwarning("Warning", message)

    @staticmethod
    def show_message_window(message):
        messagebox.showinfo("Info", message)

    def __create_ovals(self, color_board):
        for i in range(0, 6):
            for j in range(0, 7):
                self.__canvas.create_oval(j*100+20, i*100+20, j*100+110, i*100+110,
                                          fill=color_board[i][j] if color_board[i][j] is not None else '#C1C1B5')
