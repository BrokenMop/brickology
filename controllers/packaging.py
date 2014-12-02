
def add():
	return dict()	

def save():
        name=request.vars['name']

        add_new_packaging(name)

	return "1"
