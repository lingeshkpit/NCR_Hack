import json
import networkx as nx
from flask import Flask, render_template, url_for, request, redirect, Response
import numpy as np
import math
graph = ""  # Global var

def Get_Post_data(Get_data):
    Json_data = Get_data.decode('utf8').replace("'", '"')
    return json.loads(Json_data)

class indoorGraph:
    def createGraph(path):
        G = nx.Graph()
        with open(path) as f:
            graph = json.load(f, parse_int=str)
            for node in graph['node']:
                G.add_node(node['Id'], 
                    title = node['Title'], 
                    position = (node['X'], node['Y'], node['Z']))
            for edge in graph['edge']:
                x1,y1,z1 = map(int,G.nodes[edge['node'][0]]['position'])
                x2,y2,z2 = map(int,G.nodes[edge['node'][1]]['position'])
                G.add_edge(edge['node'][0], edge['node'][1], weight = int(abs((x1-x2) +(y1-y2) +(z1-z2))))
        return G
    def computeShortestPath(G, nodes):
        path = nx.bidirectional_dijkstra(G, nodes[0], nodes[1],weight="weight")
        return path

    def showLayout(G):
        pos = {}
        for node in G.nodes(data = True):
            pos[node[0]] = [int(p) for p in node[1]['position'][0:2]]
        nx.draw(G, pos = pos)

    def getNodeId(G, nodeTitle):
        for node in G.nodes(data = True):
            if(node[1]['title'] == nodeTitle):
                return node[0]
        return False

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    resp = Response('Welcome to Indoor Graph')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/createGraph', methods=["GET", "POST"])
def create_Graph():
    global graph
    if (request.method == "POST"):
        path = request.json['path']
    if (request.method == "GET"):
        path = request.json['path']
    graph = indoorGraph.createGraph(path)
    resp = Response("Graph created")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if ( __name__ == "__main__" ):
    app.run(debug=True)
