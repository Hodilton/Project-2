import tkinter as tk
from tkinter import messagebox, Toplevel

class DisplayBase:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        self.frame = tk.Frame(self.parent)

        self.initialize_display()
        self.update_listbox()

    def initialize_display(self):
        self.create_top_frame()
        self.create_bottom_frame()
        self.create_buttons()

    def create_top_frame(self):
        self.top_frame = tk.Frame(self.frame)
        self.top_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(self.top_frame, height=15, width=150)
        self.scrollbar = tk.Scrollbar(self.top_frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_bottom_frame(self):
        self.bottom_frame = tk.Frame(self.frame)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_buttons(self):
        self.add_button = tk.Button(self.bottom_frame, text="Добавить", command=self.open_add_window)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = tk.Button(self.bottom_frame, text="Обновить", command=self.open_update_window)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.bottom_frame, text="Удалить", command=self.delete_item)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()



    def open_form_window(self, mode):
        self.form_window = Toplevel(self.parent)
        self.form_window.title("Добавление" if mode == "add" else "Обновление")
        self.form_window.geometry(self.form_window_geometry)
        self.form_window.grab_set()

        self.create_form()

        if mode == "update":
            self.fill_form_with_selected_item()

        button_frame = tk.Frame(self.form_window)
        button_frame.grid(row=2, columnspan=2, pady=10)

        if mode == "add":
            tk.Button(button_frame, text="Добавить", command=self.add_item).pack(side=tk.LEFT, padx=5)
        else:
            tk.Button(button_frame, text="Обновить", command=self.update_item).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Отмена", command=self.form_window.destroy).pack(side=tk.LEFT, padx=5)

    def create_form(self):
        pass

    def fill_form_with_selected_item(self):
        pass

    def open_add_window(self):
        self.open_form_window(mode="add")

    def open_update_window(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.id_to_update = self.listbox.get(selected_index).split(":")[0].strip()
            self.open_form_window(mode="update")
        else:
            messagebox.showerror("Ошибка", "Выберите элемент для обновления")


    def add_item(self):
        pass

    def update_item(self):
        pass

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.id_to_delete = self.listbox.get(selected_index).split(':')[0].strip()
            self.update_listbox()
        else:
            tk.messagebox.showerror("Ошибка", "Выберите элемент для удаления")



    def update_data(self):
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
