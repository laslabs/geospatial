# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley
#    Copyright: 2015 LasLabs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
{'name': 'Geospatial support for stock.quant',
 'version': '0.1',
 'category': 'GeoBI',
 'author': "LasLabs, Odoo Community Association (OCA)",
 'license': 'AGPL-3',
 'website': 'https://laslabs.com',
 'depends': [
     'base',
     'base_geoengine',
     'stock',
 ],
 'data': [
     'geo_stock_quant_view.xml'
 ],
 'installable': True,
 'application': True,
 'active': False,
}
