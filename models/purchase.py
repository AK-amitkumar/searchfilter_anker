from odoo import fields, models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_geliefert = fields.Boolean(compute="_compute_is_geliefert",store=True)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_is_geliefert(self):
        for order in self:
            if order.picking_ids and all([x.state == 'done' for x in order.picking_ids]):
                order.is_geliefert = True