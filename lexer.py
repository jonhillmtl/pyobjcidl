import os
import ply.lex as lex


class Lexer(object):
    # Regular expression rules for simple tokens
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LCURLY = r'\{'
    t_RCURLY = r'\}'
    t_COMMA = r','
    t_SEMICOLON = r';'

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    t_ignore  = ' \t\n'

    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    reserved = {
           'function' : 'FUNCTION',
           'class' : 'CLASS',
           'int' : 'INT',
           'string' : 'STRING',
           'void' : 'VOID'
    }
    tokens = ['LPAREN','RPAREN', 'RCURLY', 'LCURLY', 'COMMA', 'SEMICOLON', 'ID']
    
    def build(self,**kwargs):
        self.tokens = self.tokens + list(self.reserved.values())
        self.lexer = lex.lex(module=self, **kwargs)
        
    def __init__(self):
        pass