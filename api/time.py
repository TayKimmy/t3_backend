from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from model.times import Time

time_api = Blueprint('time_api', __name__,
                   url_prefix='/api/times')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(time_api)

class TimeAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate rname
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': 'Time ID is missing, or is less than 2 characters'}, 210
            totaltime = body.get('totaltime')
            if totaltime.isnumeric() == "false":
                return {'message': 'totaltime is missing/alpha, or is out of range'}, 220

            ''' #1: Key code block, setup score OBJECT '''
            uo = Time(totaltime=totaltime,
                      uid=uid
                      )
            
           
            ''' #2: Key Code block to add score to database '''
            # create score in database
            time = uo.create()
            # success returns json of score
            if time:
                return jsonify(time.read())
            # failure returns error
            return {'message': f'Format error or username "{uid}" is duplicate'}, 240

    class _Read(Resource):
        def get(self):
            times = Time.query.all()    # read/extract all scores from database
            json_ready = [time.read() for time in times]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
