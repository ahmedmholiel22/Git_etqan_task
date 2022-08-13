from odoo import api, fields, models, _, tools


class ResPartner(models.Model):
    _inherit = "res.partner"

    total_contracts_price = fields.Float(string='Total Contracts Price', compute="_compute_total_price")

    def _compute_total_price(self):
        record = self.env['customer.contract'].search(
            [('status', '=', 'confirm')])
        for rec in record:
            if rec.price:
                self.total_contracts_price += rec.price
