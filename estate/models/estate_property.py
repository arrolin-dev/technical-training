from odoo import models, fields

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
    property_type_id = fields.many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    byer_id = fields.Many2one("res.partner",copy=False)
    #tag_ids = fields.Many2many("estate.property.tag")
    #offer_ids = fields.One2many("estate.property.offer", "property_id")


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

