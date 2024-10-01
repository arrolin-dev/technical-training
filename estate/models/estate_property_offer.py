from odoo import models, fields, api

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

    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    validity = fields.Integer(default=7)

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for estate in self:
            create_date = estate.create_date or fields.Date.today()
            estate.date_deadline = fields.Date.add(create_date, days=estate.validity)
    
    def _inverse_date_deadline(self):
        for estate in self:
            estate.validity = (estate.date_deadline - fields.Data.to_date(estate.create_date)).days

