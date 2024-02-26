#!/usr/bin/python3
"""
This module contains the index.py
"""
from models import storage
from flask import jsonify
from . import app_views


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def count():
    """Returns the numbers of the models"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
