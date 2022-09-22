from odoo import api, fields, models


class GeneratePricelistLines(models.TransientModel):
    _name = "product.pricelist.lines.wizard"
    _description = "Wizard to generate pricelists for all variants of a product"

    @api.model
    def default_get(self, fields):
        result = super().default_get(fields)
        product_template_id = self.env.context.get("active_id")
        if product_template_id:
            result["product_template_id"] = product_template_id
        return result

    product_template_id = fields.Many2one('product.template', string='Product template')
    partner_id = fields.Many2one('res.partner', string='Vendor')

    def generate_seller_lines(self):
        product_template_id = self.product_template_id
        if product_template_id.has_active_attributes:
            for variant in product_template_id.product_variant_ids:
                supplier_info = product_template_id.seller_ids.filtered(lambda o: o.product_id.id == variant.id and o.name.id == self.partner_id.id)
                if not supplier_info:
                    
                    supplier_vals = {
                        'product_id': variant.id,
                        'product_tmpl_id': product_template_id.id,
                        'name': self.partner_id.id,
                    }
                    s_info = self.env['product.supplierinfo'].create(supplier_vals)


