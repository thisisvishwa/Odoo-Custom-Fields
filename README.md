# Product Detail Extension Module for Odoo 16 Community Edition

## Overview

This module enhances the visibility of product details in Odoo 16 Community Edition by displaying additional fields such as Product name, Barcode, Cost, and Sale price in various views. It is designed to provide users with more information in Purchase order lines, Sale order lines, and Stock pickings, among other areas where product details are shown.

## Installation

To install this module, follow these steps:

1. Download the module from the Odoo app store or copy it to your addons directory.
2. Activate the developer mode in Odoo.
3. Go to Apps menu and click on 'Update Apps List'.
4. In the search bar, remove the 'Apps' filter and search for 'Product Detail Extension'.
5. Click on the 'Install' button to install the module.

For a detailed installation guide, please refer to the [installation_guide.md](documentation/installation_guide.md).

## Configuration

No additional configuration is required after installation.

## Usage

Once installed, the module automatically adds the Product name, Barcode, Cost, and Sale price fields to the Purchase order lines, Sale order lines, and Stock pickings. These fields are related to the `product.template` model and are displayed in a read-only format to maintain data integrity.

For more information on how to use this module, please see the [user_guide.md](documentation/user_guide.md).

## Contributing

If you would like to contribute to the development of this module, please send your pull requests to the repository or contact the module's maintainers.

## Credits

This module was developed by [Your Company Name]. We thank our contributors, developers, and maintainers for their efforts.

## License

This software is licensed under the [LICENSE](LICENSE) file included with the source code of this module.