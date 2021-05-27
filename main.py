import requests
import os
from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        user = request.form["city"]
        return redirect(url_for("weather",wtr=user))
    else:
        return render_template("weather.html")

@app.route("/<wtr>")
def weather(wtr):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"
    r = requests.get(url.format(wtr,os.getenv('TOKEN'))).json()

    weather = {
        'city' : wtr,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'longitude' : r['coord']['lon'],
        'latitude' : r['coord']['lat'],
        'max_temp' : r['main']['temp_max'],
        'min_temp' : r['main']['temp_min'],
        'coun' : r['sys']['country'],
        'humidity' : r['main']['humidity'],
        'speed' : r['wind']['speed']
    }

    return render_template("description.html",weather=weather)


if __name__ == "__main__":
    app.run(debug=True)