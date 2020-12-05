from flask import Flask,render_template,request,flash
import requests


app = Flask(__name__)
app.config["SECRET KEY"] = 'asadadaad'

country = ' '
cases = {}

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        global country
        country = request.form.get('countryName')
        url = 'https://covid-19.dataflowkit.com/v1/{}'
        res = requests.get(url.format(country)).json()

        global cases
        cases = {
        "Country": country,
        "Active_cases": res['Active Cases_text'],
        "Total_cases": res['Total Cases_text'],
        "Total_deaths": res['Total Deaths_text'],
        "Total_recovered": res['Total Recovered_text']
        }
    return render_template("index.html",cases=cases,country=country)



if __name__ == "__main__":
    app.run(debug=True)