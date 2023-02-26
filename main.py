import sqlite3
import pandas as pd
import json
from flask import *
app = Flask(__name__)


############################################################################

# open connection to db.
def get_connection():
    conn = sqlite3.connect('C:\db\chinook.db')
    print ('çonn done')
    print('çonn done2')
    print('çonn done3')
    print('çonn done4')
    print ('test_5')
    return conn

###########################################################################


###########################################################################
@app.route('/customers', methods=['GET'])    ##http://127.0.0.1:5000/customers

def get_all_customers():

    conn=get_connection()

    df = pd.read_sql_query("SELECT firstname,lastname FROM customers", conn)
    #return (df.to_json(orient = 'records'))
    return (df.to_json(orient = 'records',force_ascii=False))
###########################################################################


############################################################################

@app.route('/artists/<artist_id>', methods=['GET']) #http://127.0.0.1:5000/artists/1
def get_Artist (artist_id):

    conn = get_connection()

    # collect tables name
    df = pd.read_sql_query("SELECT ArtistId,name FROM artists WHERE artistid=?  ",conn, params=artist_id)
    return (df.to_json(orient='records', force_ascii=False))
###########################################################################

app.run()
#get_all_customers()

