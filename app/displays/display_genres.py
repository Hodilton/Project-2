import tkinter as tk
from tkinter import messagebox

from .display_base import DisplayBase

class DisplayGenres(DisplayBase):
    def __init__(self, parent, db_manager):
        self.table_genres = db_manager.tables['genres']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "400x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Название жанра").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['genres'] = tk.Entry(self.form_window, width=30)
        self.inputs['genres'].grid(row=0, column=1, padx=10, pady=5)

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])
            g_name = selected_data[1]

            self.inputs['genres'].delete(0, tk.END)
            self.inputs['genres'].insert(0, g_name)

    def add_or_update_item(self, mode):
        g_genres_name = self.inputs['genres'].get().strip()

        if g_genres_name:
            if mode is "add":
                self.table_genres.insert_data((g_genres_name,))
            elif mode is "update":
                self.table_genres.update_data((g_genres_name, ), (self.id_to_update,))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.table_genres.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.data = self.table_genres.fetch_all()
        super().update_listbox()
