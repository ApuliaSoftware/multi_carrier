# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andre@ (<a.gallina@cgsoftware.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
from tools.translate import _


class stock_picking_out(osv.osv):
    _inherit = "stock.picking.out"

    _columns = {
        'carrier_ids': fields.many2many(
            'delivery.carrier',
            'picking_carrier_rel',
            'picking_id',
            'carrier_id',
            'Related Carrier'),
    }


class stock_picking(osv.osv):
    _inherit = "stock.picking"

    _columns = {
        'carrier_ids': fields.many2many(
            'delivery.carrier',
            'picking_carrier_rel',
            'picking_id',
            'carrier_id',
            'Related Carrier'),
    }


class stock_invoice_onshipping(osv.osv_memory):
    _inherit = "stock.invoice.onshipping"

    def view_init(self, cr, uid, fields_list, context=None):
        return True

    def create_invoice(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        res = super(stock_invoice_onshipping, self).create_invoice(
            cr, uid, ids, context)
        picking_pool = self.pool.get('stock.picking')
        if not res:
            picking_pool.write(
                cr, uid, context['active_ids'],
                {'invoice_state': '2binvoiced'}, context)
            res = super(stock_invoice_onshipping, self).create_invoice(
                cr, uid, ids, context)
        invoice_obj = self.pool.get('account.invoice')
        for pick_id in context['active_ids']:
            picking = picking_pool.browse(cr, uid, pick_id, context)
            if picking.carrier_ids:
                carrier_ids = []
                for carrier in picking.carrier_ids:
                    carrier_ids.append(carrier.id)
                invoice_obj.write(
                    cr, uid, res[pick_id],
                    {'carrier_ids': [(6, 0, carrier_ids)]}, context)
        return res
