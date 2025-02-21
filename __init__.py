from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)   
 
@app.route('/contact/')
def contact():
    return render_template('contact.html') #Ma page de Contact modification

if __name__ == "__main__":
  app.run(debug=True)    


                                                                                                                                       



                                                                                                                                       


