from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.basketballs import *

basketball_api = Blueprint('basketball_api', __name__,
                   url_prefix='/api/basketballs')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(basketball_api)

class BasketballsAPI:
    # not implemented
    class _Create(Resource):
        def post(self, Basketball):
            pass
            
    # getBasketballs()
    class _Read(Resource):
        def get(self):
            return jsonify(getBasketball())

    # getBasketball(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getBasketballs(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:Basketball>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://petitepandas.duckdns.org/' # run from web
    url = server + "/api/basketballs"
    responses = []  # responses list

    # get count of Basketballs on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read Basketball by id
        ) 
    # obtain a random Basketball
    responses.append(
        requests.get(url+"/random")  # read a random Basketball
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")