import tkinter as tk
from tkinter import ttk, messagebox

from .display_base import DisplayBase

class DisplayBooks(DisplayBase):
    def __init__(self, parent, db_manager):
        self.table_books = db_manager.tables['books']
        self.table_authors = db_manager.tables['authors']
        self.table_genres = db_manager.tables['genres']

        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "900x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Название книги").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['b_books_name'] = tk.Entry(self.form_window, width=30)
        self.inputs['b_books_name'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Жанр").grid(row=1, column=0, padx=10, pady=5)
        self.inputs['g_genres_name'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['g_genres_name'].grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Автор").grid(row=1, column=2, padx=10, pady=5)
        self.inputs['a_authors_name'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['a_authors_name'].grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.form_window, text="Год").grid(row=0, column=2, padx=10, pady=5)
        self.inputs['b_year'] = tk.Entry(self.form_window, width=30)
        self.inputs['b_year'].grid(row=0, column=3, padx=10, pady=5)

        self.load_combobox_data()

    def load_combobox_data(self):
        data = self.table_genres.fetch_all()
        self.inputs['g_genres_name']['values'] = [f"{row[1]}" for row in data]

        data = self.table_authors.fetch_all()
        self.inputs['a_authors_name']['values'] = [f"{row[1]} - {row[2]}- {row[3]}" for row in data]

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            data_selected = self.listbox.get(selected_index).split(":")
            self.id_update_item = int(data_selected[0])

            b_books_name, a_genres_name, a_last_name,  a_middle_name, a_second_name, b_year = data_selected[1].split("-")

            self.inputs['b_books_name'].delete(0, tk.END)
            self.inputs['b_books_name'].insert(0, b_books_name.strip())

            self.inputs['g_genres_name'].set(f"{a_genres_name}")
            self.inputs['a_authors_name'].set(f"{a_last_name} - {a_middle_name} - {a_second_name}")

            self.inputs['b_year'].delete(0, tk.END)
            self.inputs['b_year'].insert(0, b_year.strip())

    def add_item(self):
        b_books_name = self.inputs['b_books_name'].get().strip()

        g_genres_name = self.inputs['g_genres_name'].get()

        a_authors_name = self.inputs['a_authors_name'].get().split("-")
        cl_a_authors_name = [part.strip() for part in a_authors_name]

        b_year = self.inputs['b_year'].get().strip()

        if b_books_name and g_genres_name and cl_a_authors_name and b_year.isdigit():
            id_g_data = self.table_genres.find_id((g_genres_name,))

            a_last_name,  a_middle_name, a_second_name = cl_a_authors_name
            id_a_data = self.table_authors.find_id((a_last_name, a_middle_name, a_second_name))

            self.table_books.insert_data((b_books_name, id_g_data, id_a_data, b_year))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def update_item(self):
        b_books_name = self.inputs['b_books_name'].get().strip()

        g_genres_name = self.inputs['g_genres_name'].get()

        a_authors_name = self.inputs['a_authors_name'].get().split("-")
        cl_a_authors_name = [part.strip() for part in a_authors_name]

        b_year = self.inputs['b_year'].get().strip()

        if b_books_name and g_genres_name and cl_a_authors_name and b_year.isdigit():
            id_g_data = self.table_genres.find_id((g_genres_name,))

            a_last_name, a_middle_name, a_second_name = cl_a_authors_name
            id_a_data = self.table_authors.find_id((a_last_name, a_middle_name, a_second_name))

            self.table_books.update_data((b_books_name, id_g_data, id_a_data, b_year), (self.id_to_update,))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.table_books.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        super().update_listbox()

        data = self.table_books.fetch_all()
        if data:
            for row in data:
                b_id, b_books_name, a_genres_name, a_last_name,  a_middle_name, a_second_name, b_year = row
                display_string = f"{b_id}: {b_books_name} - {a_genres_name} - {a_last_name} - {a_middle_name} - {a_second_name} - {b_year}"

                self.listbox.insert(tk.END, display_string)
