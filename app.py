from flask import Flask, request
from config import config
import psycopg2
from collections import OrderedDict
from psycopg2.extras import RealDictCursor
import json

conn = psycopg2.connect(**config())
app = Flask(__name__)
params = config()


@app.route('/get_similar_users')
def get_similar_users():
    user_handle = request.args['user_handle'] if 'user_handle' in  request.args else 1
    top_users =   int(request.args['num_users']) if 'num_users' in  request.args else 10
    columns = ['user_handle']
    for val in range(1, top_users):
        columns.append('top_'+str(val))
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT "+','.join(columns)+" FROM users where user_handle = "+str(user_handle))
    result = json.dumps(cur.fetchall())
    result = json.loads(result).pop(0)
    response = OrderedDict()
    similar_users = [result[str(val)] for val in columns[1:]]
    response['similar_users'] = similar_users
    response['user_handle'] = user_handle
    cur.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)

