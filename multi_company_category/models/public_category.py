from odoo import api, fields, models


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    company_ids = fields.Many2many(
        string="Companies",
        comodel_name="res.company",
        default=lambda self: self._default_company_ids(),
    )
