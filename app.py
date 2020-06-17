from flask import Flask, render_template, request
""" import yfinance as yf """
from modules.stock import Stock

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        dividendGoal = request.form['dividendGoal']
        stockSymbol = request.form['stockSymbol']
        if dividendGoal != '' and stockSymbol != '':
            stock_one = Stock(dividendGoal, stockSymbol)

            return render_template('app.html', initialInvestment= stock_one.get_initial_investment(), totalStocks=stock_one.get_total_stocks_number(), goal=stock_one.get_dividend_goal())
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()