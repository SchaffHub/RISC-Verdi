######################################################################
# FIXME: some open source license
######################################################################

import tkinter as tk
from tkinter import simpledialog

from resources import view
from resources import model
from resources import config

# ====================================================================

class CodeView():
    """GUI and control for a scrolled text window with text
       highlighting and minimal contextual code coloring.  A
       CodeView should be the child of an empty frame object."""

    def __init__(self, parent, labeled_code=None):

        # Enable resize capability
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=0)
        parent.rowconfigure   (0, weight=1)
        parent.rowconfigure   (1, weight=0)
    
        # Member variable initialization.
        self.highlighted_line = None

        self.text_dump = tk.Text(parent, state='disabled',
                                 wrap=tk.NONE)
        vscroll_dump   = tk.Scrollbar(parent,
                                      command=self.text_dump.yview,
                                      orient=tk.VERTICAL)
        hscroll_dump   = tk.Scrollbar(parent,
                                      command=self.text_dump.xview,
                                      orient=tk.HORIZONTAL)
        self.text_dump.configure(yscrollcommand=vscroll_dump.set)
        self.text_dump.configure(xscrollcommand=hscroll_dump.set)

        self.text_dump.grid(row=0, column=0,
                            sticky=tk.W+tk.E+tk.N+tk.S)
        vscroll_dump.grid  (row=0, column=1,
                            sticky=tk.W+     tk.N+tk.S)
        hscroll_dump.grid  (row=1, column=0,
                            sticky=tk.W+tk.E+tk.N+tk.S)

        self.text_dump.config(background=config.code_bg)
        self.text_dump.tag_config('highlight',
                                  foreground=config.highlight_fg,
                                  background=config.highlight_bg)
        self.text_dump.tag_config('asm',
                                  foreground=config.asm_fg)
        self.text_dump.tag_config('src',
                                  foreground=config.src_fg)

        self.apply_labeled_code(labeled_code)

    def apply_labeled_code(self, labeled_code):
        if labeled_code is not None:
            self.text_dump.configure(state='normal')
            for code_line in labeled_code:
                if code_line['label'] is 'asm':
                    self.text_dump.insert(tk.END,
                                          code_line['code'],
                                          'asm')
                else:
                    self.text_dump.insert(tk.END,
                                          code_line['code'],
                                          'src')
            self.text_dump.configure(state='disabled')

    def get_tag_index_from_line(self, line):
        index1 = "%d.0" % (line+1)
        index2 = "%d.0" % (line+2)
        return (index1, index2)

    def highlight_line(self, line):
        if self.highlighted_line is not None:
            # Un-highlight the currently highlighted line.
            idx = self.get_tag_index_from_line(self.highlighted_line)
            self.text_dump.tag_remove('highlight', idx[0], idx[1])
            self.text_dump.tag_add('asm', idx[0], idx[1])

        self.highlighted_line = line
        if self.highlighted_line is not None:
            idx = self.get_tag_index_from_line(self.highlighted_line)
            self.text_dump.tag_remove('asm', idx[0], idx[1])
            self.text_dump.tag_add('highlight', idx[0], idx[1])
            self.text_dump.see(idx[0])

# ====================================================================

class MainView():
    """ GUI for main window """

    def __init__(self, callback, cleanup):

        # Keep the Tk default window until we know how to draw it.
        self.root = tk.Tk(className=config.class_name)
        self.root.withdraw()

        # Title bar embellishment.
        self.root.title(config.title)
        icon_image = tk.PhotoImage(file=config.iconfile)
        self.root.iconphoto(True, icon_image)

        # Need to keep a reference to the image to keep it from
        # being garbage collected.  Use a member variable.
        self.label_image = tk.PhotoImage(file=config.labelfile)

        self.time_str = tk.StringVar()
        self.wave_str = tk.StringVar()

        # Setup up the main window GUI widgets.
        # Enable resize capability
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=0)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=0)
        self.root.rowconfigure   (0, weight=0)
        self.root.rowconfigure   (1, weight=1)

        button_rev    = tk.Button(self.root,
                                  text=config.rev_text,
                                  font=('Helvetica', 12),
                                  command=lambda: callback('Prev'))
        button_center = tk.Button(self.root,
                                  text=config.center_text,
                                  font=('Helvetica', 12),
                                  command=lambda: callback('Center'))
        button_fwd    = tk.Button(self.root,
                                  text=config.fwd_text,
                                  font=('Helvetica', 12),
                                  command=lambda: callback('Next'))
        label_time    = tk.Label (self.root,
                                  textvariable=self.time_str)
        label_wave    = tk.Label (self.root,
                                  textvariable=self.wave_str)
        button_cg     = tk.Button(self.root,
                                  image=self.label_image,
                                  borderwidth=0,
                                  command=cleanup)
        frame_host    = tk.Frame (self.root)

        button_rev.grid   (row=0, column=0,
                           sticky=tk.W)
        button_center.grid(row=0, column=1)
        button_fwd.grid   (row=0, column=2)
        label_time.grid   (row=0, column=3,
                           sticky=tk.W, padx=10)
        label_wave.grid   (row=0, column=4,
                           sticky=tk.E, padx=5)
        button_cg.grid    (row=0, column=5,
                           sticky=tk.E, padx=5)
        frame_host.grid   (row=1, column=0,
                           sticky=tk.W+tk.E+tk.N+tk.S,
                           columnspan=6)

        self.code_view = CodeView(parent=frame_host)

        self.root.protocol("WM_DELETE_WINDOW", cleanup)

    def get_name(self):
        return self.root.winfo_name()

    def update_wave_app(self, app):
        self.wave_str.set('Wave app: ' + app)

    def recenter(self, line):
        self.code_view.highlight_line(line)

    def update_cursor_time(self, time):
        self.time_str.set('Time: ' + time)

    def apply_labeled_code(self, labeled_code):
        self.code_view.apply_labeled_code(labeled_code)

    def choose_candidate(self, title, prompt, candidates):
        dialog = RadioButtonDialog(parent=self.root,
                                   title=title,
                                   prompt=prompt,
                                   candidates=candidates)
        return dialog.result

    def go(self):
        # Display the main window now that it has
        # been properly configured.
        self.root.deiconify()
        self.root.mainloop()

    def cleanup(self):
        self.root.destroy()

# ====================================================================

class RadioButtonDialog(simpledialog.Dialog):
    """Choose an item from a list"""

    def __init__(self, title, prompt, candidates, parent):

        self.prompt     = prompt
        self.candidates = candidates

        tk.simpledialog.Dialog.__init__(self, parent, title)

    def getresult(self):
        return self.rb_var.get()

    def destroy(self):
        self.rb_var = None
        tk.simpledialog.Dialog.destroy(self)

    def body(self, parent):

        w = tk.Label(parent, text=self.prompt, justify=tk.LEFT)
        w.grid(row=0, padx=5, sticky=tk.W)

        self.rb_var = tk.StringVar()
        self.rb_var.set(self.candidates[0])

        rb_list = []
        for value, text in enumerate(self.candidates):
            rb = tk.Radiobutton(parent,
                                text=text,
                                variable=self.rb_var,
                                value=text)
            rb.grid(row=1+value, padx=5, sticky=tk.W)
            rb_list.append(rb)

        return rb_list[0]

    def validate(self):
        self.result = self.getresult()

        if self.result is None:
            return 0

        return 1
