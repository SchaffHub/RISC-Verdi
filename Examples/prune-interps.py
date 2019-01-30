import tkinter as tk
root = tk.Tk()
base_names = {'Verdi', 'verdi', 'nWave'}
candidates = []
for interp in root.winfo_interps():
    for base_name in base_names:
        if base_name in interp:
            candidates.append(interp)
print(candidates)
