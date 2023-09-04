from ..model.products import *
from flask import request
from flask import jsonify

class ProductController:
    @classmethod
    def get_product_id(cls,product_id):
        product_instance = get_product_id2(product_id)
        print(type(product_instance))
        print(product_instance)
        if product_instance:
            return jsonify(product_instance), 200
        else:
            return {"msg": "no se encontro el producto"}, 404