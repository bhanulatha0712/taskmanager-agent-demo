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
    data = request.get_json()
    task = storage.create_task(data["title"], data.get("description"))
    return jsonify(task), 201


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    storage.delete_task(task_id)
    return "", 204
