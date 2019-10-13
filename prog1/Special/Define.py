# Define -- Parse tree node strategy for printing the special form define

import sys
from Special import Special

class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        for _ in range(n):
            sys.stdout.write('\n')

    def printRest(self, t, n):
        t1 = t.getCdr()
        if t1.isNull() or t1.isPair():
            t1.print(n, True)
        else:
            if n >= 0:
                self.indent(n)
            else:
                sys.stdout.write(' ')
            sys.stdout.write('. ')
            t1.print(-abs(n), False)
            if n >= 0:
                sys.stdout.write('\n')
                self.indent(n - 4)
            sys.stdout.write(')')
            self.endspace(n)

    def regular(self, t, n, p):
        if not p:
            self.indent(n)
            sys.stdout.write('(')
            t.getCar().print(-(abs(n) + 4), False)
            self.printRest(t, -(abs(n) +4))
            self.endspace(n)
        elif n < 0:
            sys.stdout.write(' ')
        else:
            t.getCar().print(n, False)
            self.printRest(t, n)
    def print(self, t, n, p):
        # TODO: Implement this function.
        if not p:
            self.indent(n)
            sys.stdout.write('(define')
            t1 = t.getCdr()
            if t1.isPair():
                t2 = t1.getCar
                if t2.isPair():
                    sys.stdout.write(' ')
                    t2.print(-(abs(n) + 4), False)
                    sys.stdout.write('\n')
                    self.printRest(t1, abs(n)+ 4)
                else:
                    self.regular(t1, -(abs(n) +4), True)
                    sys.stdout.write('\n')
            else:
                self.printRest(t, -(abs(n) + 4))
                sys.stdout.write('\n')
        else:
            self.regular(t, n, p)