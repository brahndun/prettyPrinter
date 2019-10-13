import sys

class Printer:

    @staticmethod
    def __indent(n):
        for _ in range(n):
            sys.stdout.write(' ')

    @staticmethod
    def __endspace(n):
        if n >= 0:
            sys.stdout.write('\n')

    @staticmethod
    def __printRest(t, n):
        d = t.getCdr()
        if d.isNull() or d.isPair():
            d.print(n, True)
        else:
            if n >= 0:
                Printer._Printer__indent(n)
            else:
                sys.stdout.write(' ')
            sys.stdout.write('. ')
            d.print(-abs(n), False)
            if n >= 0:
                sys.stdout.write('\n')
                Printer._Printer__indent(n - 4)
            sys.stdout.write(')')
            Printer._Printer__endspace(n)

    @staticmethod
    def printBooLit(n, boolVal):
        Printer._Printer__indent(n)
        if boolVal:
            sys.stdout.write('#t')
        else:
            sys.stdout.write('#f')
            Printer._Printer__endspace(n)

    @staticmethod
    def printIntLit(n, intVal):
        Printer._Printer__indent(n)
        sys.stdout.write(str(intVal))
        Printer._Printer__endspace(n)

    @staticmethod
    def printStrLit(n, strVal):
        Printer._Printer__indent(n)
        sys.stdout.write('"' + strVal + '"')
        Printer._Printer__endspace(n)

    @staticmethod
    def printRegular(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(')
            t.getCar().print(-(abs(n) + 4), False)
            Printer._Printer__printRest(t, -(abs(n) + 4))
            Printer._Printer__endspace(n)
        elif n < 0:
            sys.stdout.write(' ')
        else:
            t.getCar().print(n, False)
            Printer._Printer__printRest(t, n)
            