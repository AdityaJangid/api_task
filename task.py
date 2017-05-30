import pickle
from datetime import timedelta
import time
import os
import commands
from flask import Flask, jsonify, abort, make_response, session, app
from flask import Response
from flask import request
import json

app = Flask(__name__)

#  tasks = {
#
#          #  'id': 1,
#          #  'title': u'Buy groceries',
#          #  'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#          #  'done': False
#          '19': '80',
#          '90': '30',
#
#      }
#
#  @app.route('/api/serverStatus', methods=['GET'])
#  def get_tasks():
#      return jsonify({connid: timeout})
#
# 
#  @app.route('/api/request?connid=<int:connid>&timeout=<int:timeout>', methods=['GET'])
#  def get_task(task_id):
#      task = [task for task in tasks if task['id'] == task_id]
#      if len(task) == 0:
#          abort(404)
#      return jsonify({'task': task[0]})
#
#
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



#  @app.route('/api/request?connid=<int:conn_id>&timeout=<int:time_out>', methods=['GET'])
@app.route('/api/request', methods=['GET'])
def get_data():
    con_id = request.args.get('connid')
    tim_out = request.args.get('timeout')
    tim = int(tim_out)
    print(con_id)
    print(tim_out)
    #  float_time = float(tim_out)
    some_dict = {con_id:tim_out}
    f = open("task.json","r+")
    if len(f.readlines())>0:
        f.seek(-1,2)
        f.write(json.dumps(some_dict).replace('{', ',' ))
        #  print('1')
        f.close()
    else:
        f.write(json.dumps(some_dict, f))
        #  print("2")
        f.close()
        #  f.write(os.linesep)
    #  time.sleep(float_time)
    time.sleep(tim)

    return "{status:ok}"
    #  print(type(con_id))
    #  print(type(tim_out))
    #  session.permanent=True
    #  app.permanent_session_lifetime = timedelta(minutes=tim_out)
    #  with open('data.txt','wb') as connid_timeout:
    #      pickle.dump(some_dict, connid_timeout, protocol=pickle.HIGHEST_PROTOCOL)
        #  connid_timeout.write(con_id + ':' + tim_out + os.linesep)


#  def append_record(record):
#
#      # demonstrate a program writing multiple records
#      with open('data.txt','r') as  main_dict:
#
#          some_dict = {con_id:tim_out}
#          append_record(some_dict)
    #  f1 = open("test.json","w")
    #  f1.write(json.dumps(some_dict))
    #  f1.close()
#

    #  task.update({connid:timeout})



@app.route('/api/serverStatus', methods = ['GET'])
def api_hello():
    #  data = {
    #      'hello'  : 'world',
    #      'number' : 3,
    #  }
    #  SITE_ROOT = "/home/aditya/python/flask/api-task/flask/"

#      json_url = os.path.join(SITE_ROOT,'static', 'task.json')
    a = commands.getoutput("cat task.json")
    print(a)
#      #  with app.open_resource('static/task.json') as blog_file:
#      data = json.load(open(json_url))
    #  tasks = open("task.json",'r')
    #  js = json.dumps(tasks )
    #  resp = Response(js, status=200, mimetype='application/json')
    #  resp.headers['Link'] = 'http://luisrei.com'
#
#
    return a




if __name__ == '__main__':
    app.run(debug=True)
