from odoo import _, models, fields, api
from odoo.exceptions import UserError

class EstateProperty(models.Model):

    # Private Attributes
    # ------------------
    _name = "estate_property"
    _description = "Estate Property"

    # Special Attributes
    # ------------------
    name = fields.Char(string='Title',required=True, default="Unknown")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],
        default='new'
    )
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)


    # Relationships
    # -------------
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    byer_id = fields.Many2one("res.partner",string="Byer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")


    # Public Attributes
    # -----------------
    description = fields.Text()
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From',copy=False,default=fields.Date.add(value = fields.Date.today(),months=3))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price',readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )

    # Computed fields
    # ---------------
    total_area = fields.Float(compute="_compute_total_area", store=True)
    best_price = fields.Float(compute='_compute_best_price')

    # Actions
    # -------
    def action_sell_property(self):
        for property in self:
            if property.state == 'cancelled':
                raise UserError(_("Cancelled properties cannot be sold"))
            property.state = 'sold'

    def action_cancel_property(self):
        self.state = 'cancelled'


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for property in self:
            if property.offer_ids:
                property.best_price = max(property.offer_ids.mapped('price'))
            else:
                property.best_price = 0
    
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=100
            self.garden_orientation = 'north'
        else:
            self.garden_area = self.garden_orientation = False
    


