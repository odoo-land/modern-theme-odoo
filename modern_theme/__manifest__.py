# -*- coding: utf-8 -*-
{
    'name': "Modern Theme - Odoo",
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': """
        Odoo Land Modern Theme""",

    'description': """
        Odoo Land Modern Theme
    """,

    'author': "Fadoo, Odoo Land",
    "maintainer": ["milad-sadeghi"],
    'website': "http://www.odooland.com",
    'category': 'Themes',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail'],
    'assets': {
        'web._assets_primary_variables': [
            'modern_theme/static/src/scss/primary_variables_custom.scss',
        ],
        'web.assets_backend': [
            'modern_theme/static/src/css/main.css',
            'modern_theme/static/src/css/navbar.css',
            'modern_theme/static/src/css/header.css',
            'modern_theme/static/src/css/form.css',
            'modern_theme/static/src/css/card.css',
            'modern_theme/static/src/css/list.css',
            'modern_theme/static/src/css/activity.css',
            'modern_theme/static/src/css/kanban.css',
            'modern_theme/static/src/css/mail.css',
            'modern_theme/static/src/css/calendar.css',
            'modern_theme/static/src/css/pivot.css',
            'modern_theme/static/src/css/chatter.css',
            'modern_theme/static/src/components/message/message.js',
        ],
        'web.assets_qweb': [
            'modern_theme/static/src/xml/mail.xml',
        ],

    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
