# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modern_theme(models.Model):
#     _name = 'modern_theme.modern_theme'
#     _description = 'modern_theme.modern_theme'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
