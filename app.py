# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def welcome():
    return render_template('index.html')  # render a template

@app.route('/researchgroup')
def researchgroup():
    return render_template('researchgroup.html')  # render a template

@app.route('/researchOutcomes')
def researchOutcomes():
    return render_template('researchOutcomes.html')  # render a template

@app.route('/researchProjects')
def researchProjects():
    return render_template('researchProjects.html')  # render a template

@app.route('/facilites')
def facilites():
    return render_template('facilites.html')  # render a template

@app.route('/news')
def news():
    return render_template('news.html')  # render a template

@app.route('/collaborations')
def collaborations():
    return render_template('collaborations.html')  # render a template

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)