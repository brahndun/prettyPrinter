# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from prog1.Tokens import TokenType
from prog1.Tree import*

class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        # TODO: write code for parsing an exp
         return self.parseExpR(self.scanner.getNextToken())

    def parseRest(self):
        # TODO: write code for parsing a rest
        t = self.scanner.getNextToken()
        if t == None:
            return None
        if t.getType() == TokenType.RPAREN:
            return Nil()
        else:
            return Cons(self.parseExp(), self.parseRest())

    # TODO: Add any additional methods you might need
    def parseExpR(self, t):
        t = self.scanner.getNextToken()
        #if (t.getType() == ):
        #elif (t.getType() ==):
        if t.getType() == TokenType.LPAREN:
            return self.parseRest()
        elif t.getType() == TokenType.FALSE:
            return BoolLit(False)
        elif t.getType() == TokenType.TRUE:
            return BoolLit(True)
        elif t.getType() == TokenType.IDENT:
            return Ident(t.getSymbol())
        elif t.getType() == TokenType.INT:
            return IntLit(t.getNumber())
        elif t.getType() == TokenType.STR:
            return StrLit(t.getString())
        elif t.getType() == TokenType.QUOTE:
            return Cons(Ident("\'"), self.parseExp())
        elif t.getType() == TokenType.DOT:
            return Cons(StrLit("."), self.parseExp())

        return Nil()
    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
