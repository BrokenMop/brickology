
def list():
	response.files.append(URL('static', 'css/basic.css'))
	themes = get_all_themes()
	return dict(themes = themes)

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

