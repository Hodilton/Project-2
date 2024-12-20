import tkinter as tk
from tkinter import messagebox

from .display_base import DisplayBase

class DisplayRoomClass(DisplayBase):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['room_class']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def create_form(self):
        tk.Label(self.form_window, text="Аудитория").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['class'] = tk.Entry(self.form_window, width=30)
        self.inputs['class'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Кол-во мест").grid(row=1, column=0, padx=10, pady=5)
        self.inputs['seats'] = tk.Entry(self.form_window, width=30)
        self.inputs['seats'].grid(row=1, column=1, padx=10, pady=5)

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])
            class_name, seats = selected_data[1].split("-")

            self.inputs['class'].delete(0, tk.END)
            self.inputs['class'].insert(0, class_name.strip())

            self.inputs['seats'].delete(0, tk.END)
            self.inputs['seats'].insert(0, seats.strip())

    def add_item(self):
        class_name = self.inputs['class'].get().strip()
        seats = self.inputs['seats'].get().strip()

        if class_name and seats.isdigit():
            self.db_table.insert_data((class_name, seats))
            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def update_item(self):
        class_name = self.inputs['class'].get().strip()
        seats = self.inputs['seats'].get().strip()

        if class_name and seats.isdigit():
            self.db_table.update_data((class_name, seats), (self.id_to_update,))
            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.db_table.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        super().update_listbox()

        data = self.db_table.fetch_all()

        if data:
            for row in data:
                display_string = f"{row[0]}: {row[1]} - {row[2]}"
                self.listbox.insert(tk.END, display_string)
