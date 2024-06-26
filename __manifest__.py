# -*- coding: utf-8 -*-
{
    'name': "SW - External Templates",
    'summary': """
    This module enhances the external printable templates.
       """,
    'description': """
    This module enhances the external printable templates.
    """,
    'author': "Smart Way Business Solutions",
    'website': "https://www.smartway-jo.com",
    'category': 'SKY',
    'version': '12.0.1.3',
    'depends': ['base','account','stock','barcode_column','purchase_stock'],
    'data': [
      'views/account_invoice_template.xml',
      'views/delivery_templates.xml',
      'views/layout_customization.xml',
      "views/purchase_order_template.xml",
      'views/purchase_order_view.xml',
      'views/sale_order_temp.xml'
    ],
}
