# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *

class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch

    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    @staticmethod
    def isLetter(ch):
        return ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z'

    @staticmethod
    def isSymbol(ch):
        return ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '~'  
    
    @staticmethod
    def isResSymbol(ch):
        return ch == '+' or ch == '-' or ch == '.' or ch == '@'

    @staticmethod
    def isInitial(cls, ch):
        return cls.isLetter(ch) or cls.isSymbol(ch)

    @staticmethod
    def isRest(cls, ch):
        return cls.isInitial(ch) or cls.isDigit(ch) or cls.isResSymbol(ch)
    
    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            # TODO: Skip white space and comments           
            while ch !='':
                if ch == ' ' or ch == '\t' or ch == '\n' or ch == ';' or ch == '\x0c' or ch == '\r':
                    if ch == ';':
                        ch = self.read()
                        while ch != '':
                            if ch != '\n':
                                ch = ch != '\r' and self.read()

                    ch = ch != '' and self.read()


            # Return None on EOF
            if ch == "":
                return 
            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            if ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            if ch == '"':
                self.buf = []
                # TODO: scan a string into the buffer variable buf
                ch = self.read()
                while ch != '':
                    if ch != '"':
                        self.buf.append(ch)
                        ch = self.read()
                
                if ch == '':
                    return
                return StrToken(''.join(self.buf))

            # Integer constants
            if self.isDigit(ch):
                i = ord(ch) - ord('0')
                j = self.peek()
                # TODO: scan the number and convert it to an integer
                while self.isDigit(j):
                    ch = self.read()
                    i = i * 10 + ord(ch) - ord(0)
                    j = self.peek()
                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(i)

            # Identifiers
            else:
                if ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z' or ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '~' or ch =='+' or ch == '-':
                    self.buf = []
                    if ch >= 'A':
                        if ch <= 'Z':
                            ch = ch.lower()
                    self.buf.append(ch)
                    if ch =='+' or ch == '-':
                        return IdentToken(''.join(self.buf))
                    ch.self.peek()
                    while ch != '':
                        ch = ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z' or ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '~' or ch =='+' or ch == '-' or ch >= '0' and ch <= '9' or ch == '+' or ch == '-' or ch == '.' or ch == '@' and self.read()
                        if ch >= 'A':
                            if ch <= 'Z':
                                ch = ch.lower()
                            self.buf.append(ch)
                            ch = self.peek()

                    return IdentToken(''.join(self.buf))
                sys.stderr.write("Illegal input character '" + ch + "'\n")
            return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
