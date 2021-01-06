from pathlib import Path

from flask import Blueprint, send_file, send_from_directory

from mathapi.resources import api_metrics
from mathapi.services.auth import login_required

views = Blueprint("views", __name__)
public_dir = Path(__file__).resolve().parent.parent / "client" / "public"


@views.route("/")
@login_required
def index():
    return send_from_directory(public_dir, "index.html")


@views.route("/<path:path>")
def app_path(path):
    return send_file(public_dir / path)


@api_metrics.exclude_all_metrics()
@views.route("/health_check")
def health_check():
    return ("", 200)
