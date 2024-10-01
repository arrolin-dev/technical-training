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

    _sql_constraints = [
        ("check_offer_price", "CHECK(price >= 0)",
         "The offered price must be positive.")
    ]

    # Actions
    # -------
    def action_accept_offer(self):
        # One should only accept an offer, if the state is not on 'accepted' already.
        self.status='accepted'
        for offer in self:
            offer.property_id.selling_price = offer.price
        return True

    def action_refuse_offer(self):
        self.status='refused'
        return True


    # Auto Computes
    # -------------
    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for estate in self:
            create_date = estate.create_date or fields.Date.today()
            estate.date_deadline = fields.Date.add(create_date, days=estate.validity)
    
    def _inverse_date_deadline(self):
        for estate in self:
            estate.validity = (estate.date_deadline - fields.Date.to_date(estate.create_date)).days

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            property = self.env['estate_property'].browse(vals['property_id'])
            if property.state == 'new':
                property.state = 'offer_received'
        return super().create(vals_list)

