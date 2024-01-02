{
    'name': 'Product Detail Extension',
    'version': '1.0',
    'category': 'Sales',
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'summary': 'Extends product details visibility across various Odoo views',
    'description': """
Product Detail Extension Module
==============================
This module extends the visibility of product name, barcode, cost price, and sale price fields across Purchase order lines, Sale order lines, and Stock pickings.
""",
    'depends': ['base', 'sale_management', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_line_views.xml',
        'views/sale_order_line_views.xml',
        'views/stock_picking_views.xml',
        'data/init_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}