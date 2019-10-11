from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='My Calculator')

@app.route('/calculation', methods=['GET', 'POST'])
def calculation():
    if request.method =='POST':
        form = request.form
        loanAmount = float(form['A']) 
        periodicPayments = float(form['n']) * 12.0
        interestRate = float(form['i']) / 100.0 / 12.0
        discountFactor = (((1.0 + interestRate) ** periodicPayments)-1.0) / ( interestRate * ( 1.0 + interestRate) ** periodicPayments)
        calc = loanAmount / discountFactor
        answer = '${:,.2f}'.format(calc)
        return render_template('index.html', display=answer, pageTitle='My Calculator')
    
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)