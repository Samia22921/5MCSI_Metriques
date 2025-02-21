from flask import Flask, render_template
                                                                                                                                       
app = Flask(__name__)   
 
@app.route('/contact/')
def contact():
    return render_template('contact.html') #Ma page de Contact modification

if __name__ == "__main__":
  app.run(debug=True)    


                                                                                                                                       



                                                                                                                                       


