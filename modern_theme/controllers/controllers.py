# -*- coding: utf-8 -*-
# from odoo import http


# class ModernTheme(http.Controller):
#     @http.route('/modern_theme/modern_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modern_theme/modern_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modern_theme.listing', {
#             'root': '/modern_theme/modern_theme',
#             'objects': http.request.env['modern_theme.modern_theme'].search([]),
#         })

#     @http.route('/modern_theme/modern_theme/objects/<model("modern_theme.modern_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modern_theme.object', {
#             'object': obj
#         })
