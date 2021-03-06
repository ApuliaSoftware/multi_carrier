# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Apulia Software S.r.l. (<info@apuliuasoftware.it>)
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

{
    'name': "Multi Carrier",
    'version': '0.1',
    'category': 'Sale',
    'description': """Adding multi carrier on invoice and picking""",
    'author': 'Apulia Software S.r.l.',
    'website': 'www.apuliasoftware.it',
    'license': 'AGPL-3',
    "depends": [
                'delivery',
                'account',
                'sale',
                'purchase',
                'stock',
                ],
    "init_xml": [],
    "update_xml": [
                    'stock/stock_view.xml',
                    'account/account_view.xml',
                    'purchase/purchase_view.xml',
                  ],  
    "demo_xml": [],
    "active": False,
    "installable": True
}
