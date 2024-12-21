import tkinter as tk
from tkinter import messagebox

from .display_base import DisplayBase

class DisplayReaders(DisplayBase):
    def __init__(self, parent, db_manager):
        self.table_readers = db_manager.tables['readers']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "900x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Фамилия").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['r_last_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['r_last_name'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Имя").grid(row=0, column=2, padx=10, pady=5)
        self.inputs['r_middle_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['r_middle_name'].grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.form_window, text="Отчество").grid(row=0, column=4, padx=10, pady=5)
        self.inputs['r_second_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['r_second_name'].grid(row=0, column=5, padx=10, pady=5)

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])
            r_last_name, r_middle_name, r_second_name = selected_data[1].split("-")

            self.inputs['r_last_name'].delete(0, tk.END)
            self.inputs['r_last_name'].insert(0, r_last_name.strip())

            self.inputs['r_middle_name'].delete(0, tk.END)
            self.inputs['r_middle_name'].insert(0, r_middle_name.strip())

            self.inputs['r_second_name'].delete(0, tk.END)
            self.inputs['r_second_name'].insert(0, r_second_name.strip())

    def add_or_update_item(self, mode):
        r_last_name = self.inputs['r_last_name'].get().strip()
        r_middle_name = self.inputs['r_middle_name'].get().strip()
        r_second_name = self.inputs['r_second_name'].get().strip()

        if r_last_name and r_middle_name and r_second_name:
            if mode is "add":
                self.table_readers.insert_data((r_last_name, r_middle_name, r_second_name))
            elif mode is "update":
                self.table_readers.update_data((r_last_name, r_middle_name, r_second_name), (self.id_to_update,))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.table_readers.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.data = self.table_readers.fetch_all()
        super().update_listbox()
