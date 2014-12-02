
def add():
	
	return dict()


def save():
	name=request.vars['name']
	year=request.vars['year']

	add_new_theme(name, year)

	return "1"
#	redirect(URL('add'))	
#	response.flash = 'Successfully add new theme[' + name + ']'
#	else:
#		response.flase = 'Them [' + name + '] has existed!'

