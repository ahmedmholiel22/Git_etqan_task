# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Trainning',
    'version': '10',
    'summary': 'Trainning Task',
    'sequence': 100,
    'description': """Trainning Task""",
    'category': 'Productivity',
    'website': 'https://www.holiel.com',
    'depends': ['base'],
    'data': [
        'views/groups.xml',
        'security/ir.model.access.csv',
        'views/customer_contract.xml',
        'views/res_partner.xml',
        # 'report/report.xml',
        # 'report/customer_detail.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
