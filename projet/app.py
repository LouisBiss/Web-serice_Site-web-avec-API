from flask import Flask, render_template, url_for,request
import requests
from subprocess import run,PIPE

#http://localhost:5000/


api_meteo="ca23fcc55c22040a9da579da69e0c2a7"
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meteo', methods=['POST'])
def meteo_local():
    if request.method == 'POST':
        ville= request.form['ville']
        
        data=get(ville,api_meteo)
        temp="{0:2f}".format(data["main"]["temp"]) #"{0:2f}" transforme temp en string avec deux décimales max
        feels_like="{0:2f}".format(data["main"]["feels_like"])
        weather=(data["weather"][0]["main"])
        lieux=data["name"]
        vent=data["wind"]["speed"]
        description=data["weather"][0]["description"]
        
        return render_template('meteo.html', lieux=lieux, temp=temp, weather=weather, feels_like=feels_like, vent=vent,description=description)
        


def get(city_name, api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)
    r=requests.get(api_url)
    return   r.json() 

print(get("Paris", api_meteo))


if __name__=="__main__":
    app.run(debug=True)