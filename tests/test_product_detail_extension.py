from odoo.tests.common import TransactionCase

class TestProductDetailExtension(TransactionCase):

    def setUp(self):
        super(TestProductDetailExtension, self).setUp()
        self.ProductTemplate = self.env['product.template']
        self.SaleOrder = self.env['sale.order']
        self.PurchaseOrder = self.env['purchase.order']
        self.StockPicking = self.env['stock.picking']

        # Create a product template for testing
        self.product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'barcode': '1234567890123',
            'standard_price': 10.0,
            'list_price': 20.0,
        })

    def test_product_fields_visibility(self):
        # Check if the product fields are visible in Sale Order Line
        sale_order = self.SaleOrder.create({'partner_id': self.env.ref('base.res_partner_2').id})
        sale_order_line = sale_order.order_line.create({
            'order_id': sale_order.id,
            'product_id': self.product_template.product_variant_id.id,
            'product_uom_qty': 1,
            'price_unit': self.product_template.list_price,
        })
        self.assertEqual(sale_order_line.product_id.name, self.product_template.name)
        self.assertEqual(sale_order_line.product_id.barcode, self.product_template.barcode)
        self.assertEqual(sale_order_line.purchase_price, self.product_template.standard_price)
        self.assertEqual(sale_order_line.price_unit, self.product_template.list_price)

        # Check if the product fields are visible in Purchase Order Line
        purchase_order = self.PurchaseOrder.create({'partner_id': self.env.ref('base.res_partner_1').id})
        purchase_order_line = purchase_order.order_line.create({
            'order_id': purchase_order.id,
            'product_id': self.product_template.product_variant_id.id,
            'product_qty': 1,
            'price_unit': self.product_template.standard_price,
        })
        self.assertEqual(purchase_order_line.product_id.name, self.product_template.name)
        self.assertEqual(purchase_order_line.product_id.barcode, self.product_template.barcode)
        self.assertEqual(purchase_order_line.price_unit, self.product_template.standard_price)

        # Check if the product fields are visible in Stock Picking
        picking = self.StockPicking.create({
            'partner_id': self.env.ref('base.res_partner_1').id,
            'picking_type_id': self.env.ref('stock.picking_type_out').id,
        })
        move = picking.move_lines.create({
            'name': self.product_template.name,
            'product_id': self.product_template.product_variant_id.id,
            'product_uom_qty': 1,
            'product_uom': self.env.ref('uom.product_uom_unit').id,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'location_dest_id': self.env.ref('stock.stock_location_customers').id,
        })
        self.assertEqual(move.product_id.name, self.product_template.name)
        self.assertEqual(move.product_id.barcode, self.product_template.barcode)
        self.assertEqual(move.product_id.standard_price, self.product_template.standard_price)
        self.assertEqual(move.product_id.list_price, self.product_template.list_price)