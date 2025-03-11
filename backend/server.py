from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

@app.route('/binho', methods=['GET'])
def binho():
    return("Binho!")
"""