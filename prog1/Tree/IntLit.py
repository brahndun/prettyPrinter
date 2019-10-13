# IntLit -- Parse tree node class for representing integer literals

import sys
from Tree import Node

class IntLit(Node):
    def __init__(self, i):
        self.intVal = i

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        if n >= 0:
            sys.stdout.write('\n')

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        self.indent(n)
        sys.stdout.write(str(self.intVal))
        self.endspace(n)

    def isNumber(self):
        return True

    def getNumber(self):
        return self.intVal

if __name__ == "__main__":
    id = IntLit(42)
    id.print(0)
