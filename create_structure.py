#!/usr/bin/python3
import os

# Step 1: Create folders and empty files
os.makedirs("api/v1", exist_ok=True)
open("api/__init__.py", "a").close()
open("api/v1/__init__.py", "a").close()
open("api/v1/app.py", "w").close()

# Step 2: Create app.py content
app_py_content = """
from flask import Flask
from api.v1.views.index import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(error):
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
"""

with open("api/v1/app.py", "w") as app_file:
    app_file.write(app_py_content)

# Step 3: Create views folder and files
os.makedirs("api/v1/views", exist_ok=True)
open("api/v1/views/__init__.py", "a").close()
open("api/v1/views/index.py", "w").close()

# Step 4: Create index.py content
index_py_content = """
from flask import jsonify
from . import app_views

@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
"""

with open("api/v1/views/index.py", "w") as index_file:
    index_file.write(index_py_content)

# Step 5: Create __init__.py for views
views_init_content = """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views here to register them
from api.v1.views.index import *
"""

with open("api/v1/views/__init__.py", "w") as views_init_file:
    views_init_file.write(views_init_content)

print("API folder structure and files created successfully!")