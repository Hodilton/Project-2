import tkinter as tk


class FrameBase:
    def __init__(self, root, displays_config, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.displays = {}

        self.main_frame = None
        self.selector_frame = None
        self.display_frame = None

        self.create_main_frame()
        self.initialize_displays(displays_config)
        self.create_selector_buttons(displays_config)

        self.current_display = None
        self.switch_display(next(iter(displays_config)))

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_selector_frame()
        self.create_display_frame()

    def create_selector_frame(self):
        self.selector_frame = tk.Frame(self.main_frame)
        self.selector_frame.pack(side=tk.LEFT, fill=tk.Y)

    def create_display_frame(self):
        self.display_frame = tk.Frame(self.main_frame)
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def initialize_displays(self, displays_config):
        for key, display_config in displays_config.items():
            display_class = display_config['class']

            try:
                self.displays[key] = display_class(self.display_frame, self.db_manager)

            except Exception as e:
                print(e)

    def create_selector_buttons(self, displays_config):
        for key, display_config in displays_config.items():
            button = tk.Button(
                self.selector_frame,
                text=display_config['name'],
                command=lambda display_key=key: self.switch_display(display_key)
            )
            button.pack(fill=tk.X)

    def switch_display(self, display_key):
        self.hide_all_displays()

        self.current_display = self.displays[display_key]
        self.current_display.show()
        self.current_display.update_data()

    def hide_all_displays(self):
        for display in self.displays.values():
            display.hide()
