from bottle import route, static_file, run, template, view

@route('/')
@view('index')
def index():
    return {}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)