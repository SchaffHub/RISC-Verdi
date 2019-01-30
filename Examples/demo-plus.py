import tkinter as tk

def myFunc(*args):
    print('Received CursorTime Change Event')
    print('Parameters:')
    for i in args:
        print('   ', i)

def rmCallback(parent):
    print('Removing callback.')
    cmd = 'RemoveEventCallback demo myFunc wvCursorTimeChange'
    parent.send('nWave', cmd)
    parent.destroy()

root = tk.Tk(className='demo')

button = tk.Button(root, text="Quit",
                   command=lambda: rmCallback(root))
button.pack()

root.createcommand('myFunc', myFunc)
send_cmd = 'AddEventCallback demo myFunc wvCursorTimeChange 1'
root.send('nWave', send_cmd)

root.protocol("WM_DELETE_WINDOW", lambda: rmCallback(root))

root.mainloop()
