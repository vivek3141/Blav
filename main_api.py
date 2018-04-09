from flask import Flask, request
from flask_restful import Resource, Api
import socket
host = str(socket.gethostbyname(socket.gethostname()))

app = Flask(__name__)
api = Api(app)

class TodoSimple(Resource):
    def get(self):
        with open("per.txt") as f:
            s = f.read()
        return str(s)

    def put(self):
        return False


api.add_resource(TodoSimple, '/')
app.run(debug=True,host=host)