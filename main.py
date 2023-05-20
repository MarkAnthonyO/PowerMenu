import array
import tkinter as tk
from tkinter import messagebox
from button import button

app = tk.Tk()
app.title("powermenu")
app.resizable(False, False)

def on_click_off_btn():
    if messagebox.askyesno(message="¿Esta seguro que quiere apagar el equipo?", title="Apagar"):
        app.quit()

def on_click_restart_btn():
    if messagebox.askyesno(message="¿Esta seguro que quiere reiniciar el equipo?", title="Reiniciar"):
        app.quit()

def on_click_logout_btn():
    print("hola")

off_btn : button = button(
    master  = app,
    icon    = "",
    command = on_click_off_btn,
)

restart_btn : button = button(
    master  = app,
    icon    = "",
    command = on_click_restart_btn
)

logout_btn : button = button(
    master  = app,
    icon    = "",
    command = on_click_logout_btn
)

buttons : list[button] =  [
    off_btn,
    restart_btn,
    logout_btn
]

i : int = 0

for btn in buttons:
    btn.grid(row = 0, column=i)
    i += 1

def on_press_keyboard(evt):
    app.quit()

app.bind("<Escape>", on_press_keyboard)

app.eval('tk::PlaceWindow . center')

app.mainloop()