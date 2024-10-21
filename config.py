# config.py

context_variables = {
    "order_database_context": """
    Here is the schema for the order database:
    Table name: orders
    Columns: 
    - order_id (INT): Unique identifier for each order
    - product_id (INT): ID of the product ordered
    - product_name (VARCHAR): Name of the product
    - customer_name (VARCHAR): Name of the customer
    - order_date (DATE): Date of the order
    - quantity (INT): Quantity of product ordered
    - total_amount (DECIMAL): Total amount of the order
    """
}
