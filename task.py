import time
import os
import commands
from flask import Flask, jsonify, abort, make_response, session, app
from flask import Response
from flask import request
import json

app = Flask(__name__)

app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



@app.route('/api/request', methods=['GET'])
def get_data():
    con_id = request.args.get('connid')
    tim_out = request.args.get('timeout')
    _time = int(tim_out)
    some_dict = {con_id:tim_out}
    print(some_dict)
    f = open("task.json","r+")
    if len(f.readlines())>0:
        f.seek(-1,2)
        f.write(json.dumps(some_dict).replace('{', ',' ))
        f.close()
    else:
        f.write(json.dumps(some_dict, f))
        f.close()
    time.sleep(_time)
    return "{status:ok}"

@app.route('/api/serverStatus', methods = ['GET'])
def api_hello():

    a = commands.getoutput("cat task.json")
    print(a)
    return a




if __name__ == '__main__':
    app.run(debug=True)
