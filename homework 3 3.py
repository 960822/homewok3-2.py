def aexp_value():
	return(num^(lambda i:IntAexp(i)))|(id^(lambda v: VarAexp(v)))

def process_group(parsed):
	((_,p),_)=parsed
	return p

 def aexp_group():
	return keyword('(') + Lazy(aexp) + keyword(')')^process_group
	
 def aexp_term():
	return aexp_value()|aexp_group()

 def process_binop(op):
	return lambda l, r:BinopAexp(op,l,r)
	
 def operator(ops):
	op_parsers = [keyword(op) for op in ops]
	parser = reduce(lambda l,r: l|r, op_parsers)
	return parser
aexp_precedence_levels = [['*','/'],['+','-'],]

 def precedence(value_parser,precedence_levels,combine):
	def op_parser(precedence_level):
		return operator(precedence_level)^combine
	parser = value_parser * op_parser(precedence_levels[0]):
		
