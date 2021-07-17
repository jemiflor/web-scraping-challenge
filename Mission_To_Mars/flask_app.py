# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:52:47 2021

@author: jemif
"""
from flask import Flask, jsonify, render_template
import scrape_mars
import pymongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
#################################################
# Initialize PyMongo to work with MongoDBs
#################################################
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#################################################
# Define database and collection
#################################################
mongo_Db = client.mars_db


#################################################
# Flask Routes
#################################################

@app.route("/")
def get_mars_html():
    print("Server received request for 'get_mars_html' page...")
    result = mongo_Db.marsinfo.find_one()
    return render_template('mission_to_mars_template.html', marsdata=result)

@app.route("/scrape")
def get_mars_details():
    print("Server received request for 'get_mars_details' page...")
    
    mongo_Db.marsinfo.drop()

    result = scrape_mars.scrape()
    output = jsonify(result) 
    mongo_Db.marsinfo.insert_one(result)
    
    return output 


if __name__ == "__main__":
    app.run(debug=True)