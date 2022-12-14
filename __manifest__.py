# -*- coding: utf-8 -*-
{
    'name': "jt_purchase",

    'summary': "Purchase tweaks",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.8',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',        
        'wizard/generate_pricelist_lines.xml',
        'views/product_views.xml',
        'views/purchase_views.xml',
        
    ],
}
