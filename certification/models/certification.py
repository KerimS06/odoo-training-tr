from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Certification(models.Model):
    _name = 'certification'
    _description = 'Certification'

    number = fields.Char()
    date = fields.Date(string='Validation Date')
    standard_id = fields.Many2one("certification.standard")
    owner_id = fields.Many2one("res.partner")
    entity_id = fields.Many2one("res.partner")
    description = fields.Text(string='Validation Detail')
    expiry_days = fields.Integer('Expiry Days', readOnly=True, compute='_compute_expiry_days')
    expiry_status = fields.Selection([
        ('expired', 'Expired'),
        ('available', 'Available')
    ],readOnly=True, compute='_compute_expiry_days',store=True)

    @api.constrains('entity_id')
    def _check_entity_id(self):
        if self.entity_id and self.entity_id.is_certification_body==False:
            raise ValidationError('it is not a certification entity')

    @api.depends('date')
    def _compute_expiry_days(self):
        if self.date:
            self.expiry_days = (self.date - fields.date.today()).days
        if self.expiry_days>0:
            self.expiry_status = 'available'
        else:
            self.expiry_status = 'expired'

    @api.multi
    def update_date_one_month(self):
        self.ensure_one()
        if self.date:
            self.date +=timedelta(days=30)


        _logger.info("New date is : {}".format(self.date))