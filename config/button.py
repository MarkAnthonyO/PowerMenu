from tkinter import *

class button(Button):
    pass

    btn_font = "Font 40"
    btn_default_icon = ""
    btn_bg_color = "#5c5c5c"
    btn_fg_color = "#ffffff"

    btn_active_bg_color = "#424242"
    btn_active_fg_color = "#ffffff"

    def __init__(self, master : Misc, icon : str, command) -> None:
        if icon == "":
            icon = self.btn_default_icon
        super().__init__( 
            command = command,
            master = master,
            font = self.btn_font,
            text = icon,
            fg = self.btn_fg_color,
            bg = self.btn_bg_color,
            activebackground = self.btn_active_bg_color,
            activeforeground=  self.btn_active_fg_color
        )

