import tkinter as tk
from tkinter import ttk, messagebox

from .display_base import DisplayBase

class DisplayRoom(DisplayBase):
    def __init__(self, parent, db_manager):
        self.db_table = db_manager.tables['room']
        self.rc_table = db_manager.tables['room_class']
        self.inputs = {}

        super().__init__(parent, db_manager)

    def create_form(self):
        tk.Label(self.form_window, text="Номер комнаты").grid(row=0, column=0, padx=10, pady=5)
        self.inputs['room_number'] = tk.Entry(self.form_window, width=30)
        self.inputs['room_number'].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_window, text="Класс комнаты").grid(row=1, column=0, padx=10, pady=5)
        self.inputs['room_class'] = ttk.Combobox(self.form_window, width=28, state="readonly")
        self.inputs['room_class'].grid(row=1, column=1, padx=10, pady=5)

        self.load_combobox_data()

    def load_combobox_data(self):
        data = self.rc_table.fetch_all()
        self.inputs['room_class']['values'] = [f"{row[1]} - {row[2]}" for row in data]

    def fill_form_with_selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index).split(":")
            self.update_item_id = int(selected_data[0])

            r_number, rc_class_name, rc_seats = selected_data[1].split("-")

            self.inputs['room_number'].delete(0, tk.END)
            self.inputs['room_number'].insert(0, r_number.strip())

            self.inputs['room_class'].set(f"{rc_class_name} - {rc_seats}")

    def add_item(self):
        room_number = self.inputs['room_number'].get().strip()

        room_class = self.inputs['room_class'].get().split("-")
        cl_room_class = [part.strip() for part in room_class]

        if room_number and cl_room_class:
            rc_class_name = cl_room_class[0]
            rc_data_id = self.rc_table.find_id((rc_class_name, ))

            self.db_table.insert_data((room_number, rc_data_id))

            self.update_listbox()
            self.form_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Введите корректные данные")

    def update_item(self):
        room_number = self.inputs['room_number'].get().strip()

        room_class = self.inputs['room_class'].get().split("-")
        cl_room_class = [part.strip() for part in room_class]

        if room_number and cl_room_class:
            rc_class_name = cl_room_class[0]
            rc_data_id = self.rc_table.find_id((rc_class_name,))

            self.db_table.update_data((room_number, rc_data_id), (self.id_to_update,))

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
                id_r, r_number, rc_class_name, rc_seats = row
                display_string = f"{id_r}: {r_number} - {rc_class_name} - {rc_seats}"

                self.listbox.insert(tk.END, display_string)
