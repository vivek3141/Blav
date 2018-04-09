from flask import Flask, request
from flask_restful import Resource, Api
import socket
import numpy as np
import cv2
import test
import hasura

host = str(socket.gethostbyname(socket.gethostname()))

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        img = request.args.get('img', type=str)
        img = str(img)
        img=img.replace("...","")
        i = np.array(str(img))
        print(i)
        test.img(i)
        #print(i)
        #cv2.imshow("Test",i)
        return True

    def put(self, todo_id):
        return False


api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True,host=host)
