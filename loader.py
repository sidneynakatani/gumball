from flask import Flask, request, jsonify, redirect
from util.balancer import Balancer
from flask.ext.noextref import NoExtRef

app = Flask(__name__)
b1 = Balancer()
noext = NoExtRef(app)

@app.route('/')
def home():
    
    host =  b1.host_selector()
    b1.change_host()
    return redirect(host, 301) 


@app.route('/teste')
def teste():
    noext.hide_url('http://google.com')

if __name__ == '__main__':
    app.run(debug=True)
