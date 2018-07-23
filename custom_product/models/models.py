# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class CustomProductTag(models.Model):
    _name = 'custom.product.tag'
    _description = 'Product Tag'

    name = fields.Char('Tag Name', required=True, translate=True)


class CustomProductTemplate(models.Model):
	_inherit = 'product.template'

	product_tag = fields.Many2one('custom.product.tag',string='Product Tag')
	packing_size = fields.Char('Packing Size')
	# retail_price = fields.Float('Retail Price', 
	# 							digits=dp.get_precision('Product Price'), 
	# 							help="Retail price.")
