from odoo import _, api, fields, models

meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
class SaleOrderTasData(models.Model):
    _name = 'sale.order.tas.data'
    _description = 'Sale Order TAS Data'

    name = fields.Char(string='Nombre') 
    description = fields.Html(string='Descripción', copy=False) 
    # order_id = fields.Many2one('sale.order', string='Order id')

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    title = fields.Char(string="Titulo")

    sale_order_tas_data = fields.Many2many('sale.order.tas.data', string='Datos TAS')
    
    tipo_nota = fields.Many2one('sale.note.type', string='')
    notas = fields.Html(string='NOTAS', copy=False, related="tipo_nota.text")
    atencion = fields.Many2one('res.partner', store=True, string="Atencion",readonly=False, domain="[('parent_id', '=', partner_id)]")

    def get_fecha_pedido(self,date):
        if date:
            fecha = '{} de {} de {}'.format(date.day, meses[int(date.month)], date.year)
            return fecha


class SaleNoteType(models.Model):
    _name = 'sale.note.type'
    _description = 'Sale Note Type'
    
    name = fields.Char(string='Name', required=True)
    text = fields.Html(string='Text', required=True)