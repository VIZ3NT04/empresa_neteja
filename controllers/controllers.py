# -*- coding: utf-8 -*-
# from odoo import http


# class EmpresaNeteja(http.Controller):
#     @http.route('/empresa_neteja/empresa_neteja', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresa_neteja/empresa_neteja/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresa_neteja.listing', {
#             'root': '/empresa_neteja/empresa_neteja',
#             'objects': http.request.env['empresa_neteja.empresa_neteja'].search([]),
#         })

#     @http.route('/empresa_neteja/empresa_neteja/objects/<model("empresa_neteja.empresa_neteja"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresa_neteja.object', {
#             'object': obj
#         })

