import os
print("Working directory:", os.getcwd())
print("CSS file path:", os.path.abspath("./static/style.css"))

from bottle import route, static_file, run, template, view

@route('/')
@view('index')
def index():
    return {}

@route('/page2')
@view('page2')
def page2():
    return {}

@route('/page3')
@view('page3')
def page3():
    return {}

@route('/page4')
@view('page4')
def page4():
    return {}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)