# Copyright 2022 Hezekia Randriantsoa

from odoo import fields, models


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    company_ids = fields.Many2many(
        string="Companies",
        comodel_name="res.company",
    )
