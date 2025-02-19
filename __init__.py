from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)   
@app.route("/contact/")
def MaPremiereAPI():
    return render_template('Ma page de contact') #Ajout de la nouvelle route
  
if __name__ == "__main__":
  app.run(debug=True) #Ajout de la route /contact/

