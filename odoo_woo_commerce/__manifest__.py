{
    'name': "Odoo WooCommerce Connector",
    'version': '16.0.7.2.3',
    'author': 'Vladyslav Otroschenko',
    'website': 'https://www.linkedin.com/in/vlad-otro/',
    'summary': 'Odoo Woocommerce connector',
    'description': """
        WooCommerce Connector
        ====================
        Odoo Woocommerce connector is used to import customers, products, sale-order from woocommerce to Odoo.
    """,

    'depends': ['base', 'web', 'sale_management', 'purchase', 'stock', 'contacts', 'sms', 'loyalty', 'delivery', 'hr_expense'],
    'external_dependencies': {
        'python': ['woocommerce','beautifulsoup4'],
    },
    'data': [
        'views/account_tax_views.xml',
        'views/product_view.xml',
        'views/product_tag_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/product_attribute_view.xml',
        'views/product_attribute_value_view.xml',
        'views/prod_attachment_views.xml',
        'views/product_category_views.xml',
        'views/woo_instance_views.xml',
        'views/woo_coupon_view.xml',
        'views/delivery_carrier_view.xml',
        'views/payment_acquirer_view.xml',
        'views/account_move_view.xml',
        'views/purchase_order_views.xml',
        'wizard/product_instance_view.xml',
        'wizard/inventory_instance_view.xml',
        'wizard/product_categ_instance_view.xml',
        'wizard/product_brand_instance_view.xml',
        'wizard/product_attr_instance_view.xml',
        'wizard/product_attr_value_instance_view.xml',
        'wizard/product_tag_instance_view.xml',
        'wizard/tax_instance_view.xml',
        'wizard/res_partner_instance_view.xml',
        'wizard/so_instance_view.xml',
        'wizard/product_variant_instance_view.xml',
        "views/product_brand_view.xml",
        'views/ir_cron.xml',
        'wizard/import_coupon_wizard_view.xml',
        'wizard/import_shipping_method_wizard_view.xml',
        'wizard/import_payment_gateway_wizard_view.xml',
        'wizard/import_order_refund_wizard_view.xml',
        'wizard/sale_order_cancel.xml',
        'views/woo_commerce_views.xml',
        'report/sale_report_inherit.xml',
        'report/purchase_order_report_inherit.xml',
        'report/purchase_quotation_report_inherit.xml',
        'report/layout_inherit.xml',
        'security/ir.model.access.csv',      
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_woo_commerce/static/src/scss/graph_widget.scss',
            'odoo_woo_commerce/static/src/**/*.js',
            'odoo_woo_commerce/static/src/**/*.xml',
            'odoo_woo_commerce/static/src/css/product.css',
        ],
    },
    'live_test_url': 'https://www.linkedin.com/in/vlad-otro/',
    'currency': 'USD',
    'price': 0.0,  # 271
    'license': 'OPL-1',
    'active': False,
    'installable': True,
    'auto_install': False,
}
