import tkinter as tk
root = tk.Tk(className='remote')
print('The sum is', root.send('local', 'sum 1 2 3'))

