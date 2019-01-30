# File: demo.py
import tkinter as tk

def myFunc(*args):
    print('Received CursorTime Change Event')
    print('Parameters:')
    for i in args:
        print('   ', i)

root = tk.Tk(className='demo')

button = tk.Button(root, text='Quit', command=root.destroy)
button.pack()

root.createcommand('myFunc', myFunc)
send_cmd = 'AddEventCallback demo myFunc wvCursorTimeChange 1'
root.send('nWave', send_cmd)

root.mainloop()
