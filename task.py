import time
import os
import commands
from flask import Flask, jsonify, abort, make_response, session, app
from flask import Response
import requests
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
def ServerStatus():

    with open("task.json", 'r+') as f:
        dict1 = eval(f.read())
    dict2 = str(dict1)
    return dict2




@app.route('/api/kil', methods = ['PUT'])
def put():
    conn_id = request.args.get('connid')
    print(conn_id)
    #  print(conn_id)
    #  print(type(conn_id))
    with open("task.json", 'r+') as f:
        dict1 = eval(f.read())

    print(dict1)
    dict1.pop(conn_id)
    print(dict1)
    f = open("task.json", "w")
    f.write(json.dumps(dict1, f))

    with open("task.json", 'r+') as f:
        dict1 = eval(f.read())
    dict2 = str(dict1)
    print( dict2)

    #  return "{status:killed}"
    return redirect(url_for('status'))
    #  return (resp.text, resp.status_code, resp.headers.items())

#  @app.route('/api/status', method=['GET'])
#  def status(self):
#      #  if self.conn_id
#      return "hello world"



   #  return "hello "



if __name__ == '__main__':
    app.run(debug=True)
