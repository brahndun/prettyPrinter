# BoolLit -- Parse tree node class for representing boolean literals

import sys
from Tree import Node

class BoolLit(Node):
    __trueInstance =  None
    __falseInstance = None

    @staticmethod
    def getInstance(val):
        if val:
            if BoolLit.__trueInstance == None:
                BoolLit(True)
            return BoolLit.__trueInstance
        else:
            if BoolLit.__falseInstance == None:
                BoolLit(False)
            return BoolLit.__falseInstance

    def __init__(self, b):
        self.boolVal = b
        if b:
            if BoolLit.__trueInstance != None:
                raise Exception("Class BoolLit is a singleton")
            else:
                BoolLit.__trueInstance = self
        else:
            if BoolLit.__falseInstance != None:
                raise Exception("Class BoolLit is a singleton")
            else:
                BoolLit.__falseInstance = self

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        if n >= 0:
            sys.stdout.write('\n')

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        self.indent(n)
        if self.boolVal:
            sys.stdout.write('#t')
        else:
            sys.stdout.write('#f')
        self.endspace(n)

    def isBool(self):
        return True
    def getBool(self):
        return self.getInstance
if __name__ == "__main__":
    b = BoolLit.getInstance(True)
    b.print(0)
