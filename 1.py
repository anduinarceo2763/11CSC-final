import os
print("Working directory:", os.getcwd())
print("CSS file path:", os.path.abspath("./static/style.css"))

from bottle import Bottle, route, static_file, run, template, view
app = Bottle()

@app.route('/profile')
@view('profile')
def profile():
    return {}

@app.route('/page2')
@view('page2')
def page2():
    return {}

@app.route('/page3')
@view('page3')
def page3():
    return {}

@app.route('/page4')
@view('page4')
def page4():
    return {}

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)

if __name__ == '__main__':
    import os
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('POSRT, 8080')),
        debug=False
    )