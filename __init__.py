from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)   
 
@app.route('/contact/')
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/") 
def mongraphique(): 
  return render_template("graphique.html") 
  
  # Exercice 6 : API pour récupérer les commits GitHub 
@app.route('/commits/') 
def commits(): url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits" 
  response = requests.get(url) 
commits_data = response.json() 
commit_counts = {} 
for commit in commits_data: 
  commit_date = commit['commit']['author']['date'] 
  date_object = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ') 
  minute = date_object.strftime('%Y-%m-%d %H:%M') 
  commit_counts[minute] = commit_counts.get(minute, 0) + 1 
  results = [{'minute': key, 'count': value} for key, value in commit_counts.items()] 
  return jsonify(results=results) 
  
# Exercice 6 : Route pour afficher le graphique des commits 
@app.route('/commits-graph/') def commits_graph(): 
  return render_template("commits.html") 

@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm1

                                                                                                                                       
  
if __name__ == "__main__":
  app.run(debug=True)    




                                                                                                                                       



                                                                                                                                       


