from odoo import fields, models, api
import datetime
from datetime import timedelta
from odoo.exceptions import UserError, AccessError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_geliefert = fields.Boolean(compute="_compute_is_geliefert",store=True, string="Waren da?")
    ab_frist = fields.Datetime(string='AB Frist', compute='_compute_ab_frist', store=True, index=True)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_is_geliefert(self):
        for order in self:
            if order.picking_ids and all([x.state == 'done' for x in order.picking_ids]):
                order.is_geliefert = True

    @api.depends('order_line.date_planned')
    def _compute_ab_frist(self):

        for order in self:
            #order.ab_frist = (datetime.datetime.today()+datetime.timedelta(days=2))
            # raise UserError(("Olmaz malesefe  %s" % (datetime.datetime.today()+datetime.timedelta(days=2))))
            min_date = False
            for line in order.order_line:
                if not min_date or line.date_planned < min_date:
                    min_date = line.date_planned
            if min_date:
               end_time=fields.Datetime.from_string(min_date);
               order.ab_frist=end_time + timedelta(days=2)
class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if True:
            if name:
                args = args if args else []
                args.extend(['|', ['name', 'ilike', name], ['vat', 'ilike', name]])
                name = ''
        return super(Partner, self).name_search(name=name, args=args, operator=operator, limit=limit)

class ProductTemplate(models.Model):
    _inherit = "product.template"
    verkauf_anzahl = fields.Integer(compute='_verkauf_anzahl', string='Verkaufsanzahl', store=True, index=True)

    @api.multi
    def _verkauf_anzahl(self):
        r = {}
        domain = [
            ('state', 'in', ['sale', 'done']),
            ('product_id', 'in', self.ids),
        ]
        for group in self.env['sale.report'].read_group(domain, ['product_id', 'product_uom_qty'], ['product_id']):
            r[group['product_id'][0]] = group['product_uom_qty']
        for product in self:
            product.verkauf_anzahl = r.get(product.id, 0)
        return r

