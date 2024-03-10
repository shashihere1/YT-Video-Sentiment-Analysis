from app import app

# This might be where you have additional logic or routes specific to 'index'
# For example:
@app.route('/index')
def index():
    return 'This is the index page'

if __name__ == '__main__':
    app.run(debug=True)
