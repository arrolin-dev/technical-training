from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(string='Type',required=True)

    # Relations
    # ---------
    property_ids = fields.One2many("estate_property", "property_type_id")
    
    # Constraints
    # -----------
    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Type name should be unique.")
    ]
