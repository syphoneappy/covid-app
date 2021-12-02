from flask import *
from covid import Covid
import requests
app = Flask(__name__)

@app.route("/")
def covid():
    covid = Covid()
    countries = covid.list_countries()
    return render_template("index.html",list = countries)
@app.route("/country",methods = ['POST', 'GET'])
def country():
    if request.method == 'POST':
        Territory = request.form['list_countries']
        covid = Covid()
        countries = covid.list_countries()
        country = covid.get_status_by_country_name(Territory)
        return render_template("index.html",result = country, list = countries)
    else:
        return "error in loading page"

if __name__ == "__main__":
    app.run(debug=True)
