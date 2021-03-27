from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success', methods=['GET','POST'])
def success(): 
    if request.method == 'POST':
        deg = eval(request.form['degree'])
        typC = request.form['test']
            
        result = [0,0,0]
        out_conv = [' ',' ',' ']

        if typC.upper() == "C":
            if deg < -273.15:
                return 'Error: wrong Celsius degree!'
            result[2] = deg
            out_conv[2] = "Celsius"

            result[0] = round((9 * deg) / 5 + 32, 2)
            out_conv[0] = "Fahrenheit"
            result[1] = round(deg + 273.15, 2)
            out_conv[1] = "Kelvin"

        elif typC.upper() == "F":
            if deg < -459.67:
                return 'Error: wrong Fahrenheit degree!'
            result[2] = deg
            out_conv[2] = "Fahrenheit"

            result[0] = round((deg - 32) * 5 / 9, 2)
            out_conv[0] = "Celsius"
            result[1] = round((deg + 459.67) * 5 / 9, 2)
            out_conv[1] = "Kelvin"

        elif typC.upper() == "K":
            if deg < 0:
                return 'Error: wrong Kelvin degree!'
            result[2] = deg
            out_conv[2] = "Kelvin"

            result[0] = round(deg - 273.15, 2)
            out_conv[0] = "Celsius"
            result[1] = round(deg * 1.8 - 459.67, 2)
            out_conv[1] = "Fahrenheit"

        else:
            return 'Input proper convention.'

        tm2 = 'The temperature {} deg {}:'.format(result[2],out_conv[2])
        tm0 = '&emsp; In {} is {} degrees'.format(out_conv[0],result[0])
        tm1 = '&emsp; In {} is {} degrees'.format(out_conv[1],result[1])
        return (tm2 + '</br>' + tm0 + '</br>' + tm1)


@app.route('/')
def form():
    return render_template('tconv.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 6050)
