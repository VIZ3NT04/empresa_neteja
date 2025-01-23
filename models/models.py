# -*- coding: utf-8 -*-

from odoo import models, fields, api


class treballador(models.Model):
    _name = 'empresa_neteja.treballador'
    _description = 'empresa_neteja.treballador'

    nom = fields.Char(string='Nom')
    rol = fields.Selection([
        ('1','Oficinista'),
        ('2','Barrendero')
    ],string='Rol')

class tasca(models.Model):
    _name = 'empresa_neteja.tasca'
    _description = 'empresa_neteja.tasca'

    nom = fields.Char(string='Nom')
    treballador_id = fields.Many2one('empresa_neteja.treballador',string="Treballador Assignat")
    estat = fields.Selection([
        ('1', 'pendent'),
        ('2', 'en curs'),
        ('3','completada')
    ],string='Estat')

