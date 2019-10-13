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
            if self.form == "begin":
                return Begin()
            elif self.form == 'cond':
                return Cond()
            elif self.form == "define":
                return Define()
            elif self.form == "if":
                return If()
            elif self.form == "lambda":
                return Lambda()
            elif self.form == "let":
                return Let()
            elif self.form == "set!":
                return Set()
            elif self.form == "quote":
                return Quote()
            else:
                self.form = Regular()

    def print(self, n, p=False):
        self.form.print(self, n, p)

    def getCar(self):
        return self.getCar

    def getCdr(self):
        return self.getCdr

    def setCar(self, a):
        self.setCar(a)
        self.parseList()

    def setCdr(self, d):
        self.cdr = d
    
    def isPair(self):
        return True

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
