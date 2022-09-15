
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _check_company_auto = True

    # additional_purchase_product_ids = fields.Many2many(
    #         'product.template', 'product_additional_purchase_rel', 'src_id', 'dest_id',
    #         string='additional_purchase_product', check_company=True)