import tkinter as tk
from tkinter import messagebox, ttk

from .display_base import DisplayBase

class DisplayLibrarians(DisplayBase):
    def __init__(self, parent, db_manager):
        self.table_librarians = db_manager.tables['librarians']
        self.table_departments = db_manager.tables['departments']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "1170x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Фамилия").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['l_last_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['l_last_name'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Имя").grid(row=0, column=2, padx=10, pady=5)
        self.inputs['l_middle_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['l_middle_name'].grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.form_window, text="Отчество").grid(row=0, column=4, padx=10, pady=5)
        self.inputs['l_second_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['l_second_name'].grid(row=0, column=5, padx=10, pady=5)

        tk.Label(self.form_window, text="Должность").grid(row=0, column=6, padx=10, pady=5)
        self.inputs['d_department'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['d_department'].grid(row=0, column=7, padx=10, pady=5)

        self.load_combobox_data()

    def load_combobox_data(self):
        data = self.table_departments.fetch_all()
        self.inputs['d_department']['values'] = [f"{row[1]}" for row in data]

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])
            l_last_name, l_middle_name, l_second_name, d_department = selected_data[1].split("-")

            self.inputs['l_last_name'].delete(0, tk.END)
            self.inputs['l_last_name'].insert(0, l_last_name.strip())

            self.inputs['l_middle_name'].delete(0, tk.END)
            self.inputs['l_middle_name'].insert(0, l_middle_name.strip())

            self.inputs['l_second_name'].delete(0, tk.END)
            self.inputs['l_second_name'].insert(0, l_second_name.strip())

            self.inputs['d_department'].set(f"{d_department}")

    def add_or_update_item(self, mode):
        l_last_name = self.inputs['l_last_name'].get().strip()
        l_middle_name = self.inputs['l_middle_name'].get().strip()
        l_second_name = self.inputs['l_second_name'].get().strip()

        d_department = self.inputs['d_department'].get().strip()

        if l_last_name and l_middle_name and l_second_name and d_department:
            id_d_department = self.table_departments.find_id((d_department,))

            if mode is "add":
                self.table_librarians.insert_data((l_last_name, l_middle_name, l_second_name, id_d_department))
            elif mode is "update":
                self.table_librarians.update_data((l_last_name, l_middle_name, l_second_name, id_d_department), (self.id_to_update,))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.table_librarians.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.data = self.table_librarians.fetch_all()
        super().update_listbox()
