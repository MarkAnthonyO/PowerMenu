import tkinter as tk

App = tk.Tk()
App.title("PowerMenu")
App.resizable(False, False)

offBtn = tk.Button(
    App,
    font="Font 40", #Font awesome 40
    text="",
    fg="#ffffff",
    bg="#000000"
).grid(
    row=0,
    column=0
)

App.mainloop()