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
    def printBegin(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(begin\n')
            Printer._Printer__endspace(t, abs(n) + 4)
        else:
            Printer.printRegular(t, n, p)

    @staticmethod
    def printCond(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(cond\n')
            Printer._Printer__endspace(t, abs(n) + 4)
        else:
            Printer.printRegular(t, n, p)

    @staticmethod
    def printDefine(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('define')
            t1 = t.getCdr()
            if t1.isPair():
                t2 = t1.getCar()
                if t2.isPair():
                    sys.stdout.write(' ')
                    t2.print(-(abs(n) + 4), False)
                    sys.stdout.write('\n')
                    Printer._Printer__printRest(t1, abs(n) + 4)
                else:
                    Printer.printRegular(t1, -(abs(n)+ 4), True)
                    sys.stdout.write('\n')
            else:
                Printer._Printer__printRest(t, -(abs(n) + 4))
                sys.stdout.write('\n')
        else:
            Printer.printRegular(t, n, p)

    @staticmethod
    def printIf(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(if)')

    @staticmethod
    def printLambda(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(lambda')

    @staticmethod
    def printLet(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(let)')

    @staticmethod
    def printQuote(t, n, p):
        if not p:
            t1 = t.getCdr()
            if t1.isPair():
                Printer._Printer__indent(n)
                sys.stdout.write("'")
                t1.getCar().print(-(abs(n) + 1), False)
                Printer._Printer__endspace(n)
            else:
                Printer.printRegular(t, n, p)
        else:
            Printer.printRegular(t, n, p)

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

    @staticmethod
    def printSet(t, n, p):
        if not p:
            Printer._Printer__indent(n)
            sys.stdout.write('(set)')
            Printer._Printer__printRest(t, -(abs(n) + 4))
            sys.stdout.write('\n')
        else:
            Printer.printRegular(t, n, p)



    @staticmethod
    def printBooLit(n, boolVal):
        Printer._Printer__indent(n)
        if boolVal:
            sys.stdout.write('#t')
        else:
            sys.stdout.write('#f')
            Printer._Printer__endspace(n)

    @staticmethod
    def printIdent(n, name):
        Printer._Printer__indent(n)
        sys.stdout.write(name)
        Printer._Printer__endspace(n)

    @staticmethod
    def printIntLit(n, intVal):
        Printer._Printer__indent(n)
        sys.stdout.write(str(intVal))
        Printer._Printer__endspace(n)

    @staticmethod
    def printNil(n, p):
        Printer._Printer__indent(n - 4)
        if p:
            sys.stdout.write(')')
        else:
            sys.stdout.write('()')
        Printer._Printer__endspace(n)

    @staticmethod
    def printStrLit(n, strVal):
        Printer._Printer__indent(n)
        sys.stdout.write('"' + strVal + '"')
        Printer._Printer__endspace(n)
    
    

    

    

    


    
            