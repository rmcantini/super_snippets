import tkinter as tk

def start_script():
  print("Starting script...")

def stop_script():
  print("Stopping script...")

root = tk.Tk()
root.geometry("200x100")

label = tk.Label(root, text="Start or Stop")
label.pack()

start_button = tk.Button(root, text="Start", command=start_script)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_script)
stop_button.pack()

root.mainloop()
