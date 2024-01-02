from odoo import models, fields

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    product_name = fields.Char(related='name', string='Product Name', readonly=True)
    barcode = fields.Char(related='barcode', string='Barcode', readonly=True)
    cost_price = fields.Float(related='standard_price', string='Cost Price', readonly=True)
    sale_price = fields.Float(related='list_price', string='Sale Price', readonly=True)