# StLit -- Parse tree node class for representing string literals

import sys
from Tree import Node

class StrLit(Node):
    def __init__(self, s):
        self.strVal = s

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        if n >= 0:
            sys.stdout.write('\n')

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        self.indent(n)
        sys.stdout.write('"' + self.strVal + '"')
        self.endspace(n)

    def isString(self):
        return True

    def getString(self):
        return self.strVal
        
if __name__ == "__main__":
    id = StrLit("foo")
    id.print(0)
