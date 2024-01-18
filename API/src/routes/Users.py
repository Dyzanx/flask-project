from flask import Blueprint, jsonify, request
from src.models.UsersModel import UsersModel

main = Blueprint("users_blueprint", __name__)

@main.route("/get-all")
def get_users():
    try:
        results = UsersModel.getUsers()
        users = []
        for result in results:
            user = {
                "id": result[0],
                "name": result[1],
                "lastname": result[2],
                "email": result[3],
                "password": result[4],
                "username": result[5]
            }
            users.append(user)

        return jsonify(users)
    
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@main.route("/save/", methods=['POST'])
def save():
    try:
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        if name and lastname and email and password and username:
            
            UsersModel.saveUser(name, lastname, email, password, username)
            return "Guardado correctamente en la base de datos"
        else: 
            return jsonify({"message": "You mus send all form data to register an user"})

        
    except Exception as ex:
        print(ex)
        return jsonify({"message": str(ex)}), 500

@main.route("/get-one")
def get_one():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = UsersModel.getOne(email, password)
        response = {
            "id": user[0],
            "name": user[1],
            "lastname": user[2],
            "email": user[3],
            "password": user[4],
            "username": user[5]
        }

        return jsonify(response)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/update", methods=["PUT"])
def update():
    try:
        id = request.form.get("id")
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        username = request.form.get("username")

        UsersModel.updateUser(id, name, lastname, email, username)
        return "User successfully updated"

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500