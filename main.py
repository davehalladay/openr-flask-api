from flask import Flask
from flask_restful import Api, Resource, reqparse
# from io import IOController
import database

app = Flask(__name__)
api = Api(app)
# controller = IOController()

user_parser = reqparse.RequestParser()
user_parser.add_argument("name", required=True, help="User name is required")
user_parser.add_argument("email")
user_parser.add_argument("password", required=True, help="Password is required")
user_parser.add_argument("is_admin")

class Openr(Resource):
    def get(self):
        return {"is_door_open": True}

    def post(self):
        # controller.trigger_door()
        return {"triggered_status": True}


class User(Resource):
    def get(self, id):
        return {"user": id}

    def put(self, id):
        args = user_parser.parse_args()

        return {"user": id}


class CreateUser(Resource):
    def post(self):
        args = user_parser.parse_args()
        return {"user": database.create_user(args["name"], args["password"], is_admin=args.get("is_admin"),
                                             email=args.get("email"))}, 201


class ListUsers(Resource):
    def get(self):
        return ["user"]

api.add_resource(Openr, '/api/openr')
api.add_resource(User, '/api/user/<int:id>')
api.add_resource(CreateUser, '/api/user')
api.add_resource(ListUsers, '/api/users')

app.debug = True
if __name__ == "__main__":
    app.run()
