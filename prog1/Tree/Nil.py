# Nil -- Parse tree node class for representing the empty list

import sys
from Tree import Node

class Nil(Node):
    __instance = None

    @staticmethod
    def getInstance():
        if Nil.__instance == None:
            Nil()
        return Nil.__instance

    def __init__(self):
        if Nil.__instance != None:
            raise Exception("Class Nil is a singleton")
        else:
            Nil.__instance = self

    def indent(self, n):
        for _ in range(n):
            sys.stdout.write(' ')

    def endspace(self, n):
        if n >= 0:
            sys.stdout.write('\n')

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        self.indent(n)
        if p:
            sys.stdout.write(')')
        else:
            sys.stdout.write('()')
        self.endspace(n)

    def isNull(self):
        return True
        
if __name__ == "__main__":
    n = Nil.getInstance()
    n.print(0)
