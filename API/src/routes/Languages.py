from flask import Blueprint, jsonify
from src.models.LanguagesModel import LanguagesModel

main = Blueprint("languages_blueprint", __name__)

@main.route("/")
def get_languages():
    try:
        languages = LanguagesModel.getLanguages()
        return jsonify(languages)

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@main.route("/language/<id>")
def get_language(id):
    try:
        language = LanguagesModel.getLanguage(id)
        return jsonify(language)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@main.route("/insert/<name>/<description>", methods=["POST"])
def insert_language(name, description):
    try:
        LanguagesModel.saveLanguage(name, description)
        return "Inserted successfully"
    except Exception as ex:
        raise Exception(ex)
    

@main.route("/update/<id>/<name>/<description>", methods=['PUT'])
def update_language(id, name, description):
    try:
        LanguagesModel.updateLanguage(id, name, description)
        return "Row updated succesfully"
    except Exception as ex:
        raise Exception(ex)


@main.route("/delete/<id>", methods=['DELETE'])
def delete_language(id):
    try:
        LanguagesModel.deleteLanguage(id)
        return "Deleted succesfully"
    except Exception as ex:
        raise Exception(ex)

