######################################################################
# FIXME: some open source license
######################################################################

import re

class CodeModel():
    """Model (data) for the code image"""

    def __init__(self, listing):

        # Member variable initialization.
        self.instr_lookup = {}

        # Add each file to the list of raw code lines.
        raw_lines = []
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

