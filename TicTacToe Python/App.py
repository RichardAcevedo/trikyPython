from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/',methods=['get','POST'])
def Index():
    return render_template('tresEnRaya.html')

@app.route('mover',method=['POST'])
def mover:
    url='http://server'
    response = requests.get(url)


if __name__=='__main__':
    app.run(port=3000,debug=True)


