from flask import Flask, request,jsonify
import util
app = Flask(__name__)

@app.route('/get_location')
def get_location():
    response = jsonify({
        'location': util.get_locations()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/estimation', methods = ['POST'])
def estimation():
    area = request.form['area']
    sqft = float(request.form['sqft'])
    bed = float(request.form['bed'])
    bath = float(request.form['bath'])
    rooms = float(request.form['rooms'])
    park = (request.form['park'])
    type = (request.form['type'])
    regfee = float(request.form['regfee'])
    commis = float(request.form['commis'])
    age = float(request.form['age'])

    response = jsonify({
        'estimation': util.estimation(area,sqft,bed,bath,rooms,park,type,regfee,commis,age)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__=='__main__':
    print('starting python Flask server for House Prediction...')
    util.load_artifacts()
    app.run()