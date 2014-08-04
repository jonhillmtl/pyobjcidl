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
	errors = 0
				 
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
				  | STRING ID SEMICOLON
				  | MUTABLE_ARRAY ID SEMICOLON
				  | ARRAY ID SEMICOLON
				  | MUTABLE_DICT ID SEMICOLON
				  | DICT ID SEMICOLON
				  | BOOLEAN ID SEMICOLON'''
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
		self.errors = lexer.errors
		
		# print self.classes		