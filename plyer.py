import os
from lexer import Lexer 
import ply.yacc as yacc
        
def _dump_p(p):
    for i in p:
        print i
    
class Function(object):        
    name = ''
    arguments = []
    def __repr__(self):
        return "func: %s %s" % (self.name, self.arguments)
    
class Class(object):
    name = ''
    functions = []
    
    def __repr__(self):
        return "class %s: %s %s" % (self.name, self.members, self.functions)
        
class Argument(object):
    name = ''
    type = ''
    
    def __repr__(self):
        return "arg: %s %s" % (self.type, self.name)
        
class Member(object):
    name = ''
    type = ''
    def __repr__(self):
        return "mem: %s %s" % (self.type, self.name)
    
class Plyer(object):
    start = 'classlist'
    classes = []
    functions = []
    arguments = []
    members = []
                 
    def p_argument_expr(self, p):
        '''argument : INT ID
                  | STRING ID'''
        a = Argument()
        a.type = p[1]
        a.name = p[2]
        self.arguments.append(a)
                        
    def p_argumentlist_expr(self, p):
        '''argumentlist : argument
                        | argumentlist COMMA argument'''
        pass # _dump_p(p)
        
    def p_return(self, p):
        '''return : INT
                  | STRING
                  | VOID'''
        pass # _dump_p(p)
        
    def p_function_expr(self, p):
        'function : FUNCTION return ID LPAREN argumentlist RPAREN SEMICOLON'
        f = Function()
        f.name = p[3]
        f.arguments = self.arguments
        self.arguments = []
        self.functions.append(f)
                
    def p_functionlist_expr(self,p):
        '''functionlist : 
                        | function 
                        | functionlist function'''
        pass # _dump_p(p)
        
    def p_class_expr(self, p):
        'class : CLASS ID LCURLY memberlist functionlist RCURLY SEMICOLON'
        c = Class()
        c.name = p[2]
        c.functions = self.functions
        c.members = self.members
        self.functions = []
        self.members = []
        self.classes.append(c)
        
    def p_classlist_expr(self, p):
        '''classlist : class 
                      | classlist class'''
         
       
    def p_member_expr(self, p):
        '''member : INT ID SEMICOLON
                  | STRING ID SEMICOLON'''
        m = Member()
        m.type = p[1]
        m.name = p[2]
        self.members.append(m) 
    
    def p_memberlist_expr(self, p):
        '''memberlist : 
                      | member 
                      | memberlist member'''
        pass
                
    def p_error(self, p):
        print "Syntax error in input %s" % p

    def feed(self, text):
        lexer = Lexer()
        lexer.build()
        
        # TODO is this a hack
        self.tokens = lexer.tokens
        
        parser = yacc.yacc(module=self)
        parser.parse(text,lexer=lexer.lexer)
        
        print self.classes
    
    """
    def output_to_objc(self, objcfile):
        output = ''
        for c in self.classes:
            objcfile.write('#import <Foundation/Foundation.h>\n\n')
            objcfile.write("@interface %s : NSObject\n{\n" % c.name)
            for m in c.members:
                if m.type == 'int':
                    objcfile.write('\t%s %s;\n' % (m.type,m. name))
                elif m.type == 'string':
                    objcfile.write('\tNSString * %s;\n' % (m. name))
            objcfile.write('}\n')
            objcfile.write('\n\n')
            for f in c.functions:
                objcfile.write('-(id) %s;\n' % f.name)
            objcfile.write('@end')
        
    def output_to_py(self, pyfile):
        output = ''
        for c in self.classes:
            output += "class %s:\n" % c.name
            for m in c.members:
                output += '\t%s = None\n' % m.name
            output += '\n\n'
            for f in c.functions:
                output += '\tdef %s(self' % f.name
                for a in f.arguments:
                    output += ', %s' % a.name
                output += '): pass\n'
        pyfile.write(output)
    """
        
    def output(self, sourcefile, pydir, objcdir):
        base = os.path.basename(sourcefile)
        base = os.path.splitext(base)[0]
        print base
        
        pydest = "%s.py" % (os.path.join(pydir, base))
        print pydest
        pyfile = open(pydest, 'w+')
        self.output_to_py(pyfile)
        pyfile.close()
        
        objcdest = "%s.h" % (os.path.join(objcdir, base))
        print objcdest
        objcfile = open(objcdest, 'w+')
        self.output_to_objc(objcfile)
        objcfile.close()
        