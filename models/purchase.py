import logging
from random import randint, randrange
from odoo import _, api, exceptions, fields, models, modules

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = ['purchase.order']

    internal_ref = fields.Char('Internal Reference')

#     def write(self, vals):
#         res = super().write(vals)
#         return res

# class PurchaseOrderLine(models.Model):
#     _inherit = ['purchase.order.line']

#     additional_products_presented = fields.Boolean('additional_products_presented', default=False)