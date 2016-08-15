#!/opt/skype_bot/bin/python
from bottle import Bottle, run, route, request, get, post
app = Bottle()
@app.route('/listener', method='POST')
def my_listener():
    a = request.body.readlines()
    print(a)
    return a
run(app, host="0.0.0.0", port=80, debug=True)
