def add():
	themes = get_all_themes()
        return dict(themes=themes)


def save():
        theme=request.vars['theme']
	name=request.vars['name']
	year=request.vars['year']

	add_new_sub_theme(theme, name, year)

        return "1"
