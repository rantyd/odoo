# Copyright 2022 Hezekia Randriantsoa

from odoo import fields, models


class ProductPublicCategoryInherit(models.Model):
    _inherit = "product.public.category"

    company_ids = fields.Many2many(
        string="Companies",
        comodel_name="res.company",
    )
