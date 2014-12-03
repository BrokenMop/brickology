# -*- coding: utf-8 -*-

NE = IS_NOT_EMPTY()

db.define_table(
	'lego_theme',
	Field('name'),
	Field('released_year', 'integer')
	)

db.define_table(
	'lego_sub_theme',
	Field('name'),
	Field('theme', 'reference lego_theme'),
	Field('released_year', 'integer')
	)

db.define_table(
        'packaging',
	Field('name')
        )

db.define_table(
        'age_range',
	Field('age_range')
	)


db.define_table(
	'lego_set',
	Field('set_number'),
	Field('name'),
	Field('piece', 'integer'),
	Field('minifig', 'integer'),
	Field('instruction', 'integer'),
	Field('bag', 'integer'),
	Field('separator_availability'),
	Field('packaging', 'reference packaging'),

	Field('theme', 'reference lego_theme'),
	Field('sub_theme', 'reference lego_sub_theme'),
	Field('released_year', 'integer'),
	Field('released_date_us', 'date'),
	Field('eol_date_us', 'date'),
	Field('released_date_eu', 'date'),
	Field('eol_date_eu', 'date'),
	Field('released_date_ca', 'date'),
	Field('eol_date_ca', 'date'),

	Field('age_range', 'reference age_range'),

	Field('rrp_us', 'decimal(10,3)'),
	Field('rrp_eu', 'decimal(10,3)'),
	Field('rrp_uk', 'decimal(10,3)'),
	Field('rrp_ca', 'decimal(10,3)'),


	Field('if_exclusive', 'boolean'),

	Field('box_length', 'decimal(10,2)'),
	Field('box_width', 'decimal(10,2)'),
	Field('box_height', 'decimal(10,2)'),
	Field('model_length', 'decimal(10,2)'),
	Field('model_width', 'decimal(10,2)'),
	Field('model_height', 'decimal(10,2)'),
	Field('weight', 'decimal(10,2)'),
	)


#constrains for lego_theme table
db.lego_theme.name.requires.append(NE)

#constrains for lego_set table
db.lego_set.set_number.requires.append(NE)
db.lego_set.name.requires.append(NE)
db.lego_set.packaging.requires = IS_IN_DB(db,'packaging.id','%(name)s')
db.lego_set.theme.requires = IS_IN_DB(db, 'theme.id', '%(name)s')
#constrains for packaging table
db.packaging.name.requires.append(NE)


def add_new_theme(name, year):
	count = db(name == db.lego_theme.name).count()
	if count == 0:
		db.lego_theme.insert(name=name, released_year=year)
		return True
	else:
		return False

def add_new_packaging(name):
	count = db(name == db.packaging.name).count()
	if count == 0:
		db.packaging.insert(name=name)
		return True
	else:
		return False

def get_all_themes():
	query = db.lego_theme.id > 0
	rows = db(query).select(orderby = db.lego_theme.name)
	return rows
