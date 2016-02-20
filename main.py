from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Openr(Resource):
    def get(self):
        # TODO: implement this logic
        return {"is_door_open": True}

    def post(self):
        # TODO: trigger door, etc.
        return {"triggered_status": True}


class User(Resource):
    def get(self, id):
        return {"user": id}

    def put(self, id):
        return {"user": id}


class CreateUser(Resource):
    def post(self):
        return {"user": True}, 201

api.add_resource(Openr, '/api/openr')
api.add_resource(User, '/api/user/<int:id>')
api.add_resource(CreateUser, '/api/user')

app.debug = True
if __name__ == "__main__":
    app.run()
