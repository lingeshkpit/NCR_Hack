import json
import networkx as nx
import numpy as np
from numpy.linalg import norm
import math
from indoorGraph import indoorGraph
from flask import Flask, render_template, url_for, request, redirect, Response
G = ""  # Global var
app = Flask(__name__)

def Get_Post_data(Get_data):
    Json_data = Get_data.decode('utf8').replace("'", '"')
    return json.loads(Json_data)


# indoorGraph.hello_p()

@app.route('/', methods=["GET", "POST"])
def home():
    global G
    resp = Response('Welcome to Indoor Graph')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    G = indoorGraph(stores ="./Jsons/S1.json",corridors="./Jsons/C1.json")
    print(G.showGraph(G.graph))
    return resp

# @app.route('/createGraph', methods=["GET", "POST"])
# def create_Graph():
#     global graph
#     if (request.method == "POST"):
#         path = request.json['path']
#     if (request.method == "GET"):
#         path = request.json['path']
#     graph = indoorGraph.createGraph(path)
#     resp = Response("Graph created")
#     resp.headers['Access-Control-Allow-Origin'] = '*'
    # return resp

if ( __name__ == "__main__" ):
    app.run(debug=True)