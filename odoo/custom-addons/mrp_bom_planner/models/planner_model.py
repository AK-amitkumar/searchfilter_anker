from odoo import models, fields, api

class MrpBom(models.Model):
    _inherit=['mrp.bom']
    anzahl = fields.Float(string='Anzahl der herzustellenden Produkte')

    @api.onchange('anzahl', 'bom_line_ids', 'product_qty',)
    def onchange_anzahl(self):

        for line in self.bom_line_ids:
            notwendig = self.product_qty * line.product_qty * self.anzahl
            line.write({'noetig': notwendig})
            real_bestand = line.product_id.qty_available + line.product_id.incoming_qty - line.product_id.outgoing_qty
            line.write({'bestand': real_bestand})

    @api.one
    def berechne(self):
        for line in self.bom_line_ids:
            notwendig = self.product_qty * line.product_qty * self.anzahl
            line.write({'noetig': notwendig})
            #real_bestand = line.product_id.qty_available + line.product_id.incoming_qty - line.product_id.outgoing_qty
            real_bestand=line.product_id.qty_available-line.product_id.outgoing_qty
            line.write({'bestand': real_bestand})


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'
    bestand = fields.Float(string='Bestand')
    noetig = fields.Float(string='Notwendig')