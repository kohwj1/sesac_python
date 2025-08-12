from flask import Flask, render_template
from data import get_seoul_population_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    seoul_pops = get_seoul_population_data()
    return render_template('population.html', seoul_pops=seoul_pops)

if __name__ == '__main__':
    app.run(debug=True)