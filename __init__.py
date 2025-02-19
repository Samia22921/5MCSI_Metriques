from flask import Flask, 
                                                                                                                                       
app = Flask(__name__)   
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"
                                                                                                                                      
  
if __name__ == "__main__":
  app.run(debug=True) #Ajout de la route /contact/
