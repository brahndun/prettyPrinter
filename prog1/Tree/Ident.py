# Ident -- Parse tree node class for representing identifiers

import sys
from Tree import Node

class Ident(Node):
    def __init__(self, n):
        self.name = n

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        if n >= 0:
            sys.stdout.write('\n')

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        self.indent(n)
        sys.stdout.write(self.name)
        self.endspace(n)

    def isSymbol(self):
        return True

    def getSymbol(self):
        return self.name

if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
