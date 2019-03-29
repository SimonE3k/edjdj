# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AccountTax(models.Model):
    _inherit = 'account.tax'
    _description = 'Tax'

    name = fields.Char(string='Tax Name', required=True,translate=True)

    description = fields.Char(string='Label on Invoices',translate=True)
