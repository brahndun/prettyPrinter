# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident
from Special import *

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):
        # TODO: implement this function and any helper functions
        # you might need
        if (self.car == None):
            return None
        if not self.car.isSymbol():
            self.form = Regular()
        else:
            s = self.car.getSymbol()
            if s == "begin":
                self.form = Begin()
            elif s == 'cond':
                self.form = Cond()
            elif s == "define":
                self.form = Define()
            elif s == "if":
                self.form = If()
            elif s == "lambda":
                self.form = Lambda()
            elif s == "let":
                self.form = Let()
            elif s == "set!":
                self.form = Set()
            elif s == "quote":
                self.form = Quote()
            else:
                self.form = Regular()

    def print(self, n, p=False):
        self.form.print(self, n, p)

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr

    def setCar(self, a):
        self.car = a
        self.parseList()

    def setCdr(self, d):
        self.cdr = d
    
    def isPair(self):
        return True

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
