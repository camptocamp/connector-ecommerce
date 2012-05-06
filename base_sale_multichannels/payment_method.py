# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
#    sale_automatic_workflow for OpenERP                                        #
#    Copyright (C) 2011 Akretion Sébastien BEAU <sebastien.beau@akretion.com>   #
#                                                                               #
#    This program is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU Affero General Public License as             #
#    published by the Free Software Foundation, either version 3 of the         #
#    License, or (at your option) any later version.                            #
#                                                                               #
#    This program is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#    GNU Affero General Public License for more details.                        #
#                                                                               #
#    You should have received a copy of the GNU Affero General Public License   #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                               #
#################################################################################


from osv import osv, fields
import netsvc


class payment_method(osv.osv):
    _inherit = "payment.method"
    
    _columns = {
        'automatic_update': fields.boolean('Automatic Update', 
                help=("If the order is not paid, OpenERP  will call the external system",
                     "before each order import in order to know if this order is paid")),
    }

