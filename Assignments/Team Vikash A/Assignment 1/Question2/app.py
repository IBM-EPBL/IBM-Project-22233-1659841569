from flask import Flask

import pandas as pd
import numpy as np
import datetime as dt
from flask_cors import CORS
from scipy import constants

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

@app.route('/')
def home():
    # Pandas
    print('----------------------------------------------------------------')
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)

    # Numpy
    print('----------------------------------------------------------------')
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    print(type(arr))

    # Datetime
    print('----------------------------------------------------------------')
    today = dt.date.today()
    print(today)

    # Scipy 
    print('----------------------------------------------------------------')
    print(constants.liter)

    print('----------------------------------------------------------------')

    return '5 packages used<br/>Pandas Numpy DateTime Scipy Flask-Cors'

if __name__ == '__main__':
    app.run()
