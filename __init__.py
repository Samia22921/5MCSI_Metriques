from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm1
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"
  
if __name__ == "__main__":
  app.run(debug=True) #Ajout de la route /contact/

                                                                                                                                       
app = Flask(__name__)   
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
                                                                                                                                       
  

