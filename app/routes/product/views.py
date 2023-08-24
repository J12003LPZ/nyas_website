from app.routes.main.views import get_products
from flask import Flask, Blueprint, render_template, url_for
from supabase_py import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def get_adopter_names_by_uuids(adopter_uuids):
    adopters_response = supabase.table('adopters').select(
        'id,name,lastname').in_('id', adopter_uuids).execute()
    adopters_data = adopters_response.get('data')
    err = adopters_response.get('error')

    print(f"Adopters Response: {adopters_response}")

    if err or not adopters_data:
        print("Error fetching adopter names:", err)
        return []

    return [adopter['name'] + " " + adopter['lastname'] for adopter in adopters_data]


def get_product_with_adopters(product_id):
    response = supabase.table('items').select(
        '*').eq('id', product_id).execute()
    result = response.get('data')
    error = response.get('error')

    print(f"Supabase Response for Product: {response}")

    if error:
        print("Error fetching product:", error)
        return None

    # Ensure the result is a single item, not a list
    product = result[0] if result else None

    if product and 'adopters' in product and product['adopters']:
        adopter_uuids = product['adopters']
        adopter_names = get_adopter_names_by_uuids(adopter_uuids)
        product['adopter_names'] = adopter_names

    return product


product = Blueprint('product', __name__)


@product.route('/product/<string:id>')
def product_detail(id):
    print(f"Product Detail Route Triggered with ID: {id}")
    product_item = get_product_with_adopters(id)
    print(f"Product Item: {product_item}")
    if product_item is None:
        return render_template('404.html'), 404
    else:
        return render_template('product/product_detail.html', product=product_item)
