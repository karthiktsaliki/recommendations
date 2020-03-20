import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import json
import psycopg2
from collections import OrderedDict
from psycopg2.extras import RealDictCursor
from flask import Flask, request
from config import config

logging.basicConfig(filename='./app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
conn = psycopg2.connect(**config())  # Start the connection along with the server or you can create a pool
app = Flask(__name__) # Flask app
params = config()


@app.route('/get_similar_users')
def get_similar_users():
    """
    @:param: user_handle the user id
    @:param: num_users number of similar users
    :return: response of similar users for the corresponding users
    """
    try:
        logging.info('Inside get_similar_users service')
        user_handle = request.args['user_handle'] if 'user_handle' in request.args else 1
        top_users = int(request.args['num_users']) if 'num_users' in request.args else 10
        columns = ['user_handle']
        for val in range(1, top_users):
            columns.append('top_'+str(val))
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT "+','.join(columns)+" FROM users where user_handle = "+str(user_handle))
        result = json.dumps(cur.fetchall())
        result = json.loads(result)[0]
        response = OrderedDict()
        similar_users = [result[str(val)] for val in columns[1:]]
        response['user_handle'] = user_handle
        response['similar_users'] = similar_users
        cur.close()
        return response
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    app.run(debug=True)  # For developer

