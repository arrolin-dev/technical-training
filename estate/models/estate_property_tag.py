from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(string='Tag',required=True)

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Tag name should be unique.")
    ]
