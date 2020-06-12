from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        dividendGoal = request.form['dividendGoal']
        stockSymbol = request.form['stockSymbol']
        
        stock = yf.Ticker(stockSymbol)
        info = stock.info
        closeMarketValue = info['regularMarketPreviousClose']
        dividendValue = info['dividendRate']
        dividendYield = info['dividendYield']
        dividendYieldPercent = round(dividendValue * 100, 2)

        totalStockNumber = round(float(dividendGoal) / float(dividendValue))
        initialInvestment = round(float(dividendGoal) / float(dividendValue) * float(closeMarketValue), 2)
        return render_template('app.html', initialInvestment=initialInvestment, totalStocks=totalStockNumber, goal=dividendGoal)


if __name__ == ' __main__':
    app.debug = True
    app.run()