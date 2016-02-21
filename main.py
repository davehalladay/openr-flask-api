from flask import Flask
from flask_restful import Api, Resource
from io import IOController

app = Flask(__name__)
api = Api(app)
controller = IOController()


class Openr(Resource):
    def get(self):
        return {"is_door_open": controller.get_door_position()}

    def post(self):
        controller.trigger_door()
        return {"triggered_status": True}


class User(Resource):
    def get(self, id):
        return {"user": id}

    def put(self, id):
        return {"user": id}


class CreateUser(Resource):
    def post(self):
        return {"user": True}, 201


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
