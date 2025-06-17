# Python CRUD Application for Inventory Warehouse Stock Management

A comprehensive Python application for managing inventory warehouse stock data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project helps organizations efficiently manage office supply inventory by tracking stock levels, updating item data, and applying discounts. It reduces stockouts, avoids overstocking, and supports better planning for purchasing and usage.

**Benefits:**

  * Improved stock accuracy: Manual updates with timestamp tracking ensure data consistency and reduce human error.
  * Faster inventory operations: Simple, menu-driven interface speeds up stock checks, additions, and updates.
  * Reduced overstock & stockouts: Real-time monitoring helps maintain optimal stock levels based on usage.
  * Streamlined decision-making: Data views by name or category support better procurement and restocking strategies.
  * Cost efficiency through discounts: A built-in discount system encourages stock turnover for older items.
  * Minimal training required: Intuitive CLI design makes it easy for staff to use without extensive training.

**Target Users:**

This application is designed for inventory administrators in office supply stores, educational institutions, or administrative departments who need a simple and efficient system to manage office stationery (ATK) inventory accurately.

## Features

* **Create:**
    * Add new ATK (office supplies) items to the inventory system, specifying details such as item name, category, quantity, price, and entry date.
    * Automatically generate unique item codes based on category initials.
    * Validate input data to ensure correct formats (e.g., numeric values for quantity and price).
* **Read:**
    * Search for specific items by name.
    * Filter inventory items by category for quicker access.
    * Display all item data in a structured table format using tabulate, showing name, stock, category, price, and dates.
    * Highlight items with zero stock to monitor availability.
* **Update:**
    * Edit existing ATK data including name, category, quantity, and price.
    * Add or subtract stock quantities with real-time update tracking.
    * Automatically update the "last modified" date after changes.
* **Delete:**
    * Remove items from the inventory using their item codes.
    * Include confirmation prompts to prevent unintended deletions.
* **Diccount Management:**
    * Identify items stored for more than 60 days to apply automatic discount eligibility.
    * Apply dynamic discount percentages (10%, 20%, or 30%) based on purchase quantity.
    * Display a detailed discount transaction summary including total price after discount.
* **User Interaction:**
    * Simple and interactive command-line menu system for navigating all features.
    * Display appropriate error or confirmation messages for every user action.

## Installation

1. **Prerequisites:**
    * Python version 3.7 or later
    * Additional dependencies:
        * `pip install tabulate`

2. **Installation:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/python-inventory-crud.git
    cd python-inventory-crud
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add new ATK items to the inventory by providing details such as name, category, quantity, and price. An automatic item code is generated based on the category.
    * **Read:** View all inventory data or search for specific ATK items by name, code, or category. The data is displayed in a clear tabular format for easy readability.
    * **Update:** Modify existing item data including stock levels, prices, and item information. Also includes submenus for updating specific fields like stock addition or general data changes.
    * **Delete:** Remove items from the inventory that are no longer used or discontinued. The deletion is positioned under the discount management menu for structured flow.
    * **Reports:** Generate on-screen reports for inventory including all items, low stock warnings, and discounted items. All updates include timestamps for tracking.

## Data Model

This project uses an in-memory Python dictionary structure to simulate a product inventory database. The following fields are defined for each item:

* **Products:**
    * `kode` (String, Unique): Automatically generated item code based on the category (e.g., "ATKA1").
    * `nama` (String): Name of the ATK item (e.g., "Pulpen Biru").
    * `kategori` (String): Category of the item (e.g., "Alat Tulis", "Kertas", etc.).
    * `stok` (Integer): Current stock level of the item.
    * `harga` (Integer): Price of the item in Rupiah.
    * `diskon` (Integer, optional): Discount percentage applied to the item (default is 0).
    * `tanggal_masuk` (String): Entry date of the item into inventory (format: DD-MM-YYYY).
    * `tanggal_update` (String): Last update date of the item's stock or data (format: DD-MM-YYYY).
