# -*- coding: utf-8 -*-
from odoo import api, fields, models


class GarageVehicle(models.Model):
    _name = "garage.vehicle"
    _description = "Vehicles in garage"

    name = fields.Char(string='Name', required=True)
    make = fields.Char(string='Make', required=True)
    color = fields.Selection([('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')])
    year = fields.Integer(string='Year')
    type = fields.Selection([('car', 'Car'), ('motorbike', 'Motorbike')])
    is_imported = fields.Boolean(string='Is Imported ?')