# -*- coding: utf-8 -*-
# Copyright 2021, 2022 Odooland - Milad Sadeghi
# License LGPL-3.0 or later (https://choosealicense.com/licenses/agpl-3.0/).
{
    'name': "Modern Backend Theme",
    'version': '16.0.1.0.0',
    'sequence': 1,
    'summary': """
        Odoo Land Modern Theme""",

    'description': """
        Modern theme is a Odoo backend theme for Community edition, with the latest template design methods and support full responsive.
    """,

    'author': "Odoo Land, Fadoo",
    'maintainer': ["milad-sadeghi"],
    'website': "http://www.odooland.com",
    'support': "odooland.dev@gmail.com",
    'category': "Themes/Backend",
    'depends': ['base', 'web', 'mail'],
    'images': ['static/description/logo.png'],
    'Live_test_url':'demo.odooland.com',
    'assets': {
        'web._assets_primary_variables': [
            'modern_theme/static/src/scss/primary_variables_custom.scss',
        ],
        'web._assets_backend_helpers': [
            'modern_theme/static/src/webclient/mixins.scss',
        ],
        'web.assets_backend': [
            'modern_theme/static/src/css/main.css',
            'modern_theme/static/src/css/navbar.css',
            'modern_theme/static/src/css/header.css',
            'modern_theme/static/src/css/form.css',
            'modern_theme/static/src/css/list.css',
            'modern_theme/static/src/css/kanban.css',
            'modern_theme/static/src/css/calendar.css',
            'modern_theme/static/src/css/pivot.css',
            'modern_theme/static/src/css/graph.css',
            'modern_theme/static/src/css/activity.css',
            'modern_theme/static/src/css/mail.css',
            'modern_theme/static/src/css/card.css',
            'modern_theme/static/src/css/dashboard.css',
            'modern_theme/static/src/css/chatter.css',
            'modern_theme/static/src/css/other.css',
            'modern_theme/static/src/xml/mail.xml',
            'modern_theme/static/src/webclient/**/*.xml',
            'modern_theme/static/src/webclient/**/*.scss',
            'modern_theme/static/src/webclient/**/*.js',
        ],
        'point_of_sale.assets': [
            'modern_theme/static/src/css/pos.css',
        ]
        
    },
    'images': [
        'static/description/logo.png',
        'static/description/theme_screenshot.png',
    ],
    'price': 0.0,
    'currency': 'USD',
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
