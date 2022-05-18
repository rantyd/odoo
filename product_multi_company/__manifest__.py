# Copyright 2022 Hezekia Randriantsoa

{
    "name": "Product multi-company",
    "summary": "Select individually the product template visibility on each " "company",
    "author": "Hezekia",
    "category": "Product Management",
    "version": "14.0.1.0.0",
    "license": "Other proprietary",
    "depends": ["product"],
    "data": ["views/product_template_form.xml",
             "views/product_template_tree.xml",
             "security/ir_rule.xml"],
    "application": False,
    "installable": True,
    "auto_install": False,
}
