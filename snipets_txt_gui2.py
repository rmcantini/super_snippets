import tkinter as tk

def start_script():
  print("Starting script...")

def stop_script():
  print("Stopping script...")

root = tk.Tk()
root.geometry("200x88+960+400")
root.resizable(False, False)

label = tk.Label(root, text="Start or Stop")
label.pack(padx=8, pady=8)

start_button = tk.Button(root, text="Start", command=start_script)
start_button.pack(side="left", padx=32, pady=8)

stop_button = tk.Button(root, text="Stop", command=stop_script)
stop_button.pack(side="right", padx=32, pady=8)

root.mainloop()
