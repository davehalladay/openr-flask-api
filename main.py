from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from piface_io import IOController
import database

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
controller = IOController()


@auth.verify_password
def verify_password(user_name, password):
    return database.verify_password(user_name, password)


class Openr(Resource):
    @auth.login_required
    def get(self):
        return {"is_door_open": controller.get_door_position()}

    @auth.login_required
    def post(self):
        controller.trigger_door()
        return {"triggered_status": True}


class User(Resource):
    @auth.login_required
    def get(self, id):
        user = database.get_user(id)
        if user:
            return {
                "name": user.name,
                "email": user.email,
                "created_at": str(user.created_at),
                "updated_at": str(user.updated_at),
                "is_admin": user.is_admin
            }
        else:
            return dict(error="User not found"), 404

    @auth.login_required
    def put(self, id):
        user_parser = reqparse.RequestParser()
        user_parser.add_argument("name")
        user_parser.add_argument("email")
        user_parser.add_argument("password")
        user_parser.add_argument("is_admin")
        args = user_parser.parse_args()
        return {"success": database.update_user(id, **args)}

    @auth.login_required
    def delete(self, id):
        return database.delete_user(id), 204


class CreateUser(Resource):
    @auth.login_required
    def post(self):
        user_parser = reqparse.RequestParser()
        user_parser.add_argument("name", required=True, help="User name is required")
        user_parser.add_argument("email")
        user_parser.add_argument("password", required=True, help="Password is required")
        user_parser.add_argument("is_admin")
        args = user_parser.parse_args()
        return {"user": database.create_user(args["name"], args["password"], is_admin=args.get("is_admin"),
                                             email=args.get("email"))}, 201


class ListUsers(Resource):
    @auth.login_required
    def get(self):
        return ["user"]

api.add_resource(Openr, '/api/openr')
api.add_resource(User, '/api/user/<int:id>')
api.add_resource(CreateUser, '/api/user')
api.add_resource(ListUsers, '/api/users')

app.debug = True
if __name__ == "__main__":
    app.run()
