from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


# define the class and fields of the module
class CustomerContract(models.Model):
    _name = "customer.contract"
    _description = "Customer Contract"
    _rec_name = 'customer_id'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    price = fields.Float(string="Price")
    average_day_price = fields.Float('Average Day Price', compute="_compute_average_day_price")
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('end', 'Ended'), ('cancel', 'Cancelled')],
                              default='draft', string='status')
    last_change_by = fields.Many2one('res.users', string='Last Change By', required=True)

#fun of handle end_date
    @api.onchange('start_date')
    def on_change_end_date(self):
        self.end_date = False

    def _compute_average_day_price(self):
        for rec in self:
            rec.average_day_price = float(str(rec.price / (rec.end_date - rec.start_date).days))

    @api.onchange('status')
    def on_change_last_change(self):
        self.last_change_by = self.env.user.id

    @api.constrains('price')
    def _check_price(self):
        for rec in self:
            if rec.price == 0:
                raise ValidationError(_("Price Cannot Be Zero"))


