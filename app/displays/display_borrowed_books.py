import tkinter as tk
from tkinter import ttk, messagebox

from .display_base import DisplayBase

class DisplayBorrowedBooks(DisplayBase):
    def __init__(self, parent, db_manager):
        self.table_borrowed_books = db_manager.tables['borrowed_books']
        self.table_book_statuses = db_manager.tables['book_statuses']
        self.table_books = db_manager.tables['books']
        self.table_readers = db_manager.tables['readers']
        self.table_librarians = db_manager.tables['librarians']

        self.inputs = {}

        super().__init__(parent, db_manager)

    def open_form_window(self, mode):
        self.form_window_geometry = "1170x100"
        super().open_form_window(mode)

    def create_form(self):
        tk.Label(self.form_window, text="Дата выдачи").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['bb_date_from'] = tk.Entry(self.form_window, width=30)
        self.inputs['bb_date_from'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Дата сдачи").grid(row=1, column=0, padx=10, pady=5)
        self.inputs['bb_date_to'] = tk.Entry(self.form_window, width=30)
        self.inputs['bb_date_to'].grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Статус").grid(row=0, column=2, padx=10, pady=5)
        self.inputs['bs_status'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['bs_status'].grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.form_window, text="Читатель").grid(row=1, column=2, padx=10, pady=5)
        self.inputs['r_reader'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['r_reader'].grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.form_window, text="Книга").grid(row=0, column=4, padx=10, pady=5)
        self.inputs['b_book'] = ttk.Combobox(self.form_window, width=68, state="readonly")
        self.inputs['b_book'].grid(row=0, column=5, padx=10, pady=5)

        tk.Label(self.form_window, text="Сотрудник").grid(row=1, column=4, padx=10, pady=5)
        self.inputs['l_librarian'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['l_librarian'].grid(row=1, column=5, padx=10, pady=5)

        self.load_combobox_data()

    def load_combobox_data(self):
        data = self.table_book_statuses.fetch_all()
        self.inputs['bs_status']['values'] = [f"{row[1]}" for row in data]

        data = self.table_readers.fetch_all()
        self.inputs['r_reader']['values'] = [f"{row[1]} - " + " - ".join(map(str, row[2:])) for row in data]

        data = self.table_books.fetch_all()
        self.inputs['b_book']['values'] = [f"{row[1]} - " + " - ".join(map(str, row[2:])) for row in data]

        data = self.table_librarians.fetch_all()
        self.inputs['l_librarian']['values'] = [f"{row[1]} - " + " - ".join(map(str, row[2:])) for row in data]

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            data_selected = self.listbox.get(selected_index).split(":")
            self.id_update_item = int(data_selected[0])

            fields = [field.strip() for field in data_selected[1].split(" - ")]

            bb_date_from, bb_date_to, bs_status, b_book = fields[:4]
            r_last_name, r_middle_name, r_second_name = fields[4:7]
            l_last_name, l_middle_name, l_second_name = fields[7:]

            self.inputs['bb_date_from'].delete(0, tk.END)
            self.inputs['bb_date_from'].insert(0, bb_date_from.strip())

            self.inputs['bb_date_to'].delete(0, tk.END)
            self.inputs['bb_date_to'].insert(0, bb_date_to.strip())

            self.inputs['bs_status'].set(f"{bs_status}")
            self.inputs['b_book'].set(f"{b_book}")
            self.inputs['r_reader'].set(f"{r_last_name} - {r_middle_name} - {r_second_name}")
            self.inputs['l_librarian'].set(f"{l_last_name} - {l_middle_name} - {l_second_name}")

    def add_or_update_item(self, mode):
        bb_date_from = self.inputs['bb_date_from'].get().strip()
        bb_date_to = self.inputs['bb_date_to'].get().strip()
        bs_status = self.inputs['bs_status'].get().strip()

        b_book = self.inputs['b_book'].get().strip()
        b_book_parts = [part.strip() for part in b_book.split(" - ")]
        b_book_title = b_book_parts[0]
        b_publication_year = b_book_parts[-1]  # последний элемент строки

        r_reader = self.inputs['r_reader'].get().split("-")
        cl_r_reader = [part.strip() for part in r_reader]

        l_librarian = self.inputs['l_librarian'].get().split("-")
        cl_l_librarian = [part.strip() for part in l_librarian]

        if bb_date_from and bb_date_to and bs_status and b_book and cl_r_reader and cl_l_librarian:
            id_bs_data = self.table_book_statuses.find_id((bs_status,))
            id_b_data = self.table_books.find_id((b_book_title,b_publication_year))

            r_last_name, r_middle_name, r_second_name = cl_r_reader
            id_r_data = self.table_readers.find_id((r_last_name, r_middle_name, r_second_name))

            l_last_name, l_middle_name, l_second_name, l_departments = cl_l_librarian
            id_l_data = self.table_librarians.find_id((l_last_name, l_middle_name, l_second_name))

            if mode is "add":
                self.table_borrowed_books.insert_data((bb_date_from, bb_date_to, id_bs_data, id_b_data, id_r_data, id_l_data))
            elif mode is "update":
                self.table_borrowed_books.update_data((bb_date_from, bb_date_to, id_bs_data, id_b_data, id_r_data, id_l_data), (self.id_to_update,))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def delete_item(self):
        super().delete_item()

        self.table_borrowed_books.delete_data((self.id_to_delete,))
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.data = self.table_borrowed_books.fetch_all()
        super().update_listbox()
