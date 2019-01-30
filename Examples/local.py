import tkinter as tk

def add_the_args(*args):
    return sum([int(num) for num in args])

root = tk.Tk(className='local')
root.createcommand('sum', add_the_args)
root.mainloop()
