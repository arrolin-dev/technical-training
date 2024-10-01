from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string='Offer Price')
    status = fields.Selection(
        copy=False,
        selection=[('accepted','Accepted'),('refused','Refused')]
    )
    partner_id = fields.Many2one("res.partner",required=True)
    property_id = fields.Many2one("estate_property")

