from flask import jsonify, Blueprint, request
from src.models.PostsModel import PostsModel

main = Blueprint("Posts_blueprint", __name__)

@main.route("/get-all")
def get_all():
    try:
        results = PostsModel.getAll()
        posts = []
        for result in results:
            post = {
                "id": result[0],
                "user_id": result[1],
                "theme_id": result[2],
                "title": result[3],
                "content": result[4],
                "posted_date": result[5],
            }
            posts.append(post)

        return jsonify(posts)

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/get-one/<id>")
def get_one(id):
    try: 
        result = PostsModel.getOne(id)
        post = {
            "id": result[0],
            "user_id": result[1],
            "theme_id": result[2],
            "title": result[3],
            "content": result[4],
            "posted_date": result[5],
        }

        return jsonify(post)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500



@main.route('/insert', methods=['POST'])
def save_post():
    try:
        user_id = request.form.get("user_id")
        theme_id = request.form.get("theme_id")
        title = request.form.get("title")
        content = request.form.get("content")

        PostsModel.savePost(user_id, theme_id, title, content)
        return "Saved successfully"

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    

@main.route('/update', methods=['PUT'])
def update_post():
    try:
        id = request.form.get("id")
        title = request.form.get("title")
        content = request.form.get("content")

        PostsModel.updatePost(id, title, content)
        return "Row updated successfully"

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<id>", methods=['DELETE'])
def delete_post(id):
    try:
        PostsModel.deletePost(id)
        return "Row deleted successfully"

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
