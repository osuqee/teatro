# -*- coding: utf-8 -*-
{
	 'name': "teatro",
    'summary': """base de datos de teatro""",
    'description': """
        base de datos de teatro descripcion
    """,
    'author': "Eduardo Losilla Forradellas",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'TEATRO',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
	# 'vistas/matches.xml',
	# 'vistas/maps.xml',
	# 'vistas/characters.xml',
    ],
}
