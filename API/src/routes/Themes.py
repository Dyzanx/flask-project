from flask import Blueprint, jsonify, request
from src.models.ThemesModel import ThemesModel

main = Blueprint("themes_blueprint", __name__)

@main.route("/get-all")
def get_themes():
    try: 
        results = ThemesModel.getAll()
        themes = []
        for result in results:
            theme = {
                "id": result[0],
                "name": result[1],
                "date": result[2]
            }
            themes.append(theme)

        return jsonify(themes)
    except Exception as ex:
        print(ex)
        return jsonify({"message": str(ex)}), 500

@main.route("/get-one/<id>")
def get_one(id):
    try:
        result = ThemesModel.getOne(id)
        theme = {
            "id": result[0],
            "name": result[1],
            "date": result[2]
        }

        return jsonify(theme)
    except Exception as ex:
        print(ex)
        return jsonify({"message": str(ex)}), 500


@main.route("/insert", methods=['POST'])
def insert():
    try:
        name = request.form.get("name")
        ThemesModel.insert(name)

        return "Saved succesfully"
    except Exception as ex:
        return jsonify({"mesasge": str(ex)}), 500


@main.route("/update", methods=['PUT'])
def update():
    try:
        id = request.form.get("id")
        name = request.form.get("name")

        if id and name:
            ThemesModel.updateTheme(id, name)
            return "Updated succesfully"
        else:
            return "You must send all data to update"

    except Exception as ex:
        return jsonify({"mesasge": str(ex)}), 500
    
@main.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    try: 
        ThemesModel.deleteTheme(id)
        return "Deleted successfully"
    except Exception as ex:
        return jsonify({"mesasge": str(ex)}), 500