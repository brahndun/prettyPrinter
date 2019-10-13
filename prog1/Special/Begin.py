# Begin -- Parse tree node strategy for printing the special form begin

import sys
from Special import Special
from Format import Printer

class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        if not p:
            Printer.Printerindent(n)
            sys.stdout.write('(begin\n')
            Printer.PrinterprintRest(t, abs(n) + 4)
        else:
            Printer.Printer