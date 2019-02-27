"""
Copyright 2018-2019 Dover Microsystems, Inc.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import re

class CodeModel():
    """Model (data) for the code image"""

    def __init__(self, listings):

        # Member variable initialization.
        self.instr_lookup = {}

        # Add each file to the list of raw code lines.
        raw_lines = []
        for listing in listings:
            with open(listing, 'r') as f:
                raw_lines.extend(f.readlines())

        # Process the raw text to extract the instruction pointers
        # and build a lookup table indexed by an instruction pointer.
        self.labeled_code = []
        for line_number, line_text in enumerate(raw_lines):
            # Determine if the line text begins with an
            #instruction pointer.
            re_instr_ptr = re.match(r'^\s*([0-9a-fA-F]+):', line_text)
            label = 'src'
            if re_instr_ptr:
                instr_ptr = re_instr_ptr.group(1)
                self.instr_lookup[instr_ptr] = line_number
                label = 'asm'
            new_code = {'label': label, 'code': line_text}
            self.labeled_code.append(new_code)

    def get_labeled_code(self):
        return self.labeled_code

    def get_line_from_instr_ptr(self, instr_ptr):
        """Look up the code line number with instruction pointer"""
        line = None
        if instr_ptr in self.instr_lookup:
            line = self.instr_lookup[instr_ptr]
        return line

