from flask import Blueprint, jsonify, request

from app import storage

bp = Blueprint("tasks", __name__)


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(storage.list_tasks())


@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = storage.get_task(task_id)
    if task is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "request body must be a JSON object"}), 400

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title is required"}), 400

    task = storage.create_task(title.strip(), data.get("description"))
    return jsonify(task), 201


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    storage.delete_task(task_id)
    return "", 204
