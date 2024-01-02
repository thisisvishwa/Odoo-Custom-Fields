# User Guide

## Overview

This document serves as a user guide for the Product Detail Extension Module for Odoo 16 Community Edition. This module enhances the visibility of product details, specifically the Product name, Barcode, Cost, and Sale price, across various transactional documents within the Odoo system.

## Installation

To install this module, follow these steps:

1. Navigate to the Odoo Apps dashboard.
2. Click on the "Import Module" button and select the `product_detail_extension_module.zip` file.
3. Once uploaded, click on the "Install" button next to the module listing.

Alternatively, you can copy the module to the Odoo addons directory and update the app list from the Odoo backend.

## Configuration

No additional configuration is required after installation. The module automatically applies the necessary changes to the relevant views.

## Usage

Once installed, the module extends the following views to include the new fields:

- Purchase Order Lines
- Sale Order Lines
- Stock Picking

These fields will be visible and in a read-only format to prevent any accidental modification of product information.

### Viewing Extended Product Details

To view the extended product details:

1. Open any Purchase Order, Sale Order, or Stock Picking.
2. Look for the product line items.
3. The additional fields (Product name, Barcode, Cost, and Sale price) will be displayed alongside the standard product information.

## Support and Updates

For support or to request updates, please refer to the `documentation/support_guide.md` file for contact information and procedures.

## Known Limitations

This module does not modify the core behavior of the `product.template` model. It only extends the visibility of certain fields. Customization for third-party apps or non-standard Odoo modules is not covered by this module.

## Contributing

If you wish to contribute to the development of this module, please refer to the `documentation/contribution_guide.md`.

## Credits

This module was developed by [Your Company Name]. We thank our contributors and the Odoo community for their suggestions and feedback.

## License

This module is licensed under the [License Type]. Please see the `LICENSE` file in the root directory for the full license text.