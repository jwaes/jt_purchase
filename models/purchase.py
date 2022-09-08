import logging
from random import randint, randrange
from odoo import _, api, exceptions, fields, models, modules

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = ['purchase.order']

    internal_ref = fields.Char('Internal Reference')
    