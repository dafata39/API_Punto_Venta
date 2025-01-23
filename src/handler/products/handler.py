import json

def list(event, context):
    """
    Lambda function to handle product requests.
    This function simulates fetching products from a database (mock data).
    """
    # Mock de productos
    mock_products = [
        {"id": 1, "name": "Laptop", "price": 1500.0, "stock": 10},
        {"id": 2, "name": "Smartphone", "price": 800.0, "stock": 25},
        {"id": 3, "name": "Tablet", "price": 600.0, "stock": 15},
        {"id": 4, "name": "Smartwatch", "price": 200.0, "stock": 30},
    ]

    # Respuesta con todos los productos
    body = {
        "message": "Products fetched successfully!",
        "products": mock_products,
    }
    status_code = 200

    response = {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        },
    }

    return response
