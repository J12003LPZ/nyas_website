from flask import Flask, Blueprint, render_template, url_for, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Define main blueprint
main = Blueprint('main', __name__)


def get_products():
    url = 'https://ihegxecyygqpltrxjrmj.supabase.co/rest/v1/items?select=*'
    headers = {
        'apikey': os.getenv("SUPABASE_API_KEY"),
        'Authorization': os.getenv('SUPABASE_AUTHORIZATION')
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle error (log it, return a default list, etc.)
        print(f"Error fetching data from Supabase: {response.status_code}")
        return []


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/adopt-new-yorks-past')
def new_yorks_past():
    products = get_products()
    return render_template('main/adopt_new_yorks_past.html', products=products)


@main.route('/board-of-directors')
def boardofdirectors():
    return render_template('main/board-of-directors.html')


@main.route('/projects')
def projects():
    return render_template('projects.html')


@main.route('/events')
def events():
    images = [
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636694/New%20York%20Archival%20Society/Events/image-asset__5_kgogfp.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636694/New%20York%20Archival%20Society/Events/image-asset__4_o9ot2b.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636694/New%20York%20Archival%20Society/Events/image-asset__3_i1ok61.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636693/New%20York%20Archival%20Society/Events/bpb_02227_e4jldi.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636693/New%20York%20Archival%20Society/Events/image-asset__2_juoyhk.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636693/New%20York%20Archival%20Society/Events/image-asset__1_sddqgn.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636693/New%20York%20Archival%20Society/Events/image-asset_wfhtow.jpg",
        "https://res.cloudinary.com/djozxyart/image/upload/v1692636693/New%20York%20Archival%20Society/Events/animalsnip3_ixci3h.jpg",

    ]
    return render_template('main/events.html', images=images)


@main.route('/contact')
def contact():
    return render_template('main/contact.html')


@main.route('/koch-congressional-project')
def koch_congressional_project():
    return render_template('main/koch_congressional_project.html')


@main.route('/about')
def about():
    return render_template('main/about.html')


@main.route('/contribute')
def contribute():
    return render_template('error/ComingSoon.html')


@main.app_errorhandler(404)
def http_error_handler(error):
    return render_template("error/404NotFound.html"), 404
