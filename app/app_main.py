import tkinter as tk
from tkinter import ttk

from app.frames.frame_base import FrameBase

class Application:
    def __init__(self, frames_config, db_manager):
        try:
            self.root = tk.Tk()
            self.root.title("Manager")
            self.db_manager = db_manager

            self.frames_config = frames_config
            self.notebook = None
            self.frames = None

            self.setup()

        except Exception as e:
            print(e)

    def setup(self):
        self.initialize_application(self.frames_config)

    def run(self):
        self.root.mainloop()

    def initialize_application(self, frames_config):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.frames = {}

        for tab_name, displays_config in frames_config.items():
            tab_frame = tk.Frame(self.notebook)
            tab_gui = FrameBase(tab_frame, displays_config, self.db_manager)

            self.notebook.add(tab_frame, text=tab_name)
            self.frames[tab_name] = tab_gui
