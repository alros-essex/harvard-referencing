from flask import Flask, json, render_template

from db import path_to_database, init_database


db = init_database()

collections = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]


api = Flask(__name__)

@api.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@api.route('/api/v1/users', methods=['GET'])
def get_companies():
  return json.dumps(collections)

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=5000) 
    #api.run(ssl_context='adhoc')
