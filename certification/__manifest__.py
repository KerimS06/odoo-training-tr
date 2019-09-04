# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "certification",
    "summary": "Define certification for different purposes",
    "version": "12.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Beta",
    "category": "Certification Management",
    "website": "https://github.com/KerimS06",
    "author": "Hüseyin Kayayurt - Kerim Siper",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["KerimS06"],
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": ['security/certification_security.xml',
             'security/ir.model.access.csv',
             'views/certification_view.xml',
             'views/standard_view.xml',
             'views/res_partner_view.xml',
             'views/certification_bodies_view.xml',
             'reports/certification_report.xml',
             'reports/report_certification_pdf.xml',
             'reports/certification_template_pdf.xml'],
    "demo": ['demo/certification_data.xml'],

}