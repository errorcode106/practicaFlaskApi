from ..database import DatabaseConnection

class Product:
    def __init__(self,product_id= None,product_name= None,
                 brand= None,category=None,model_year=None,list_price=None):
        
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.model_year = model_year
        self.list_price = list_price

    

class Brand:
    def __init__(self, brand_id=None, brand_name=None):
        self.brand_id = brand_id
        self.brand_name = brand_name

class Category:
    def __init__(self, category_id=None, category_name=None):
        self.category_id = category_id
        self.category_name = category_name

def get_product_id2(product_id):
        query = "SELECT p.product_id, p.product_name, b.brand_id, b.brand_name,c.category_id, c.category_name, p.model_year, p.list_price FROM products p JOIN brands b ON p.brand_id = b.brand_id JOIN categories c ON p.category_id = c.category_id WHERE p.product_id = %s;"
        params = (product_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            product = {
            "brand": {
                "brand_id": result[2],
                "brand_name": result[3]
            },
            "category": {
                "category_id": result[4],
                "category_name": result[5]
            },
            "model_year": result[6],
            "list_price": result[7],
            "product_id": result[0],
            "product_name": result[1]
            }
            return product
        else:
            return None
