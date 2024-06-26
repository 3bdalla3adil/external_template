# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PuchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    
    deadline_date = fields.Date("Deadline Date")
    note = fields.Text("Note")
    shipping_address_id = fields.Many2one("res.partner", string="Shipping Address")
     
class SaleOrder(models.Model):
    _inherit = "sale.order"
     
   
    print_with_img = fields.Boolean("Print With Image")
    notes = fields.Text("Notes")
     
class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    
    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val.pop("comment",False)
        return super(AccountInvoice, self).create(vals_list)
    
    
class Currency(models.Model):
    _inherit = "res.currency"
    
      
    @api.multi
    def amount_to_text(self, amount):
        word = super(Currency, self).amount_to_text(amount)
        return word+" Only."
