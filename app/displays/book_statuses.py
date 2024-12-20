import tkinter as tk
from tkinter import messagebox

from .display_base import DisplayBase

class DisplayBookStatuses(DisplayBase):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['book_statuses']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "400x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Название статуса").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['b_status_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['b_status_name'].grid(row=0, column=1, padx=10, pady=5)

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])
            g_name = selected_data[1]

            self.inputs['b_status_name'].delete(0, tk.END)
            self.inputs['b_status_name'].insert(0, g_name)

    def add_item(self):
        b_status_name = self.inputs['b_status_name'].get()

        if b_status_name:
            self.db_table.insert_data((b_status_name, ))
            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def update_item(self):
        b_status_name = self.inputs['b_status_name'].get()

        if b_status_name:
            self.db_table.update_data((b_status_name, ), (self.id_to_update,))
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
                display_string = f"{row[0]}: {row[1]}"
                self.listbox.insert(tk.END, display_string)
