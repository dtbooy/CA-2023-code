from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>Hello, Goodbye!</h3>'

@app.route('/spam')
def eggs():
    person= {'name': 'John', 'age':25}
    return person, 201 # Change status code with second element in return
    # Flask automatically converts dictionary to JSON when we return it

@app.route('/hello/<name>') # defines <name> as variable
def hello(name): # pass <name> into function
    # Request saves all the request details in a variable (need to import request from flask)
    # print(request.headers)
    # name = request.args.get('name')
    return { 'message': f'Hello {name}'}


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return {'result': (num1) + (num2) }
    # try:
        # num1 = (request.args.get('num1', type=int))
        # num2 = (request.args.get('num2', type=int))
        # return {'result': (num1) + (num2) }
    # except TypeError:
    #     return {'Error' : "num1 and num2 required and must be integers"}

@app.errorhandler(TypeError) # can use server errors (eg 404) or python errors (eg: type error)
def type_error(error):
    return { "error" : str(error) }, 400

# Customer Error handler 
# Put this after all routes 
@app.errorhandler(404) # can use server errors (eg 404) or python errors (eg: type error)
def not_found(error):
    return { "error" : str(error) }, 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Default port is 5000