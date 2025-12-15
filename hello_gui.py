import tkinter as tk

def on_click():
    label.config(text="Hello! Thanks for clicking 😊")

app = tk.Tk()
app.title("My First GUI App")
app.geometry("300x150")

label = tk.Label(app, text="Click the button below!", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(app, text="Click Me", command=on_click)
button.pack(pady=10)

app.mainloop()
