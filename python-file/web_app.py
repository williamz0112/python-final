# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,jsonify,render_template,Response,make_response
import json
import os
from shutil import copytree,rmtree
import pandas as pd

app = Flask(__name__)

img_list = ["首页","地区分层","世界地图","收入分层"]

@app.route('/',methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/region',methods=['GET'])
def region():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'data/region.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'region.html', the_res=data, list=img_list )

# @app.route('/area',methods=['GET'])
# def area():
#     path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'data/data.csv' ))
#     result = pd.read_csv( path, encoding='utf-8', delimiter="," )
#     data = result.to_html( )
#     return render_template( 'area.html', the_res=data, list=img_list )

@app.route('/map',methods=['GET'])
def map():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'data/map.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'map.html', the_res=data, list=img_list )

@app.route('/hierarchy',methods=['GET'])
def hierarchy():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'data/hierarchy.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'hierarchy.html', the_res=data, list=img_list )

@app.route('/jump',methods=['POST'])
def jump():
    option = request.form['option']
    if option == "地区分层":
        return redirect('/region')
    elif option == "世界地图":
        return redirect('/map')
    elif option == "收入分层":
        return redirect('/hierarchy')
    elif option == "首页":
        return redirect('/')
    else:
        return "异常"

if __name__ == '__main__':
    app.run(debug=True,port=8080)