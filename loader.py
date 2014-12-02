from flask import Flask, request, jsonify, redirect, url_for, make_response
from util.balancer import Balancer
from flask.ext.noextref import NoExtRef
#from flaskext.noextref import NoExtRef

app = Flask(__name__)
b1 = Balancer()

@app.route('/')
def home():
    
    host =  b1.host_selector()
    b1.change_host()
    return redirect(host, 302) 


def teste():
#     return redirect('http://uol.com.br')
#     return noext.go_to_url('http://uol.com.br')
#     url_for('', url='http://uol.com.br')
      response = make_response(redirect('http://uol.com.br'))
      return response

noext = NoExtRef(app, rule='/go/', view_func=teste)

if __name__ == '__main__':
    app.run(debug=True)
