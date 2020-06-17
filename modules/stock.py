import yfinance as yf

class Stock:
    def __init__(self, dividendGoal, stockSymbol):
        self.dividendGoal=dividendGoal
        self.stockSymbol=stockSymbol
        try:
            self.stock = yf.Ticker(self.stockSymbol)
            self.info = self.stock.info
            self.closeMarketValue = self.info['regularMarketPreviousClose']
            self.dividendValue = self.info['dividendRate']
            self.dividendYield = self.info['dividendYield']
        except:
            print("Something went wrong accessing yfinance data")
        

    def get_dividend_goal(self):
        return self.dividendGoal

    def get_stock_symbol(self):
        return self.stockSymbol

    def get_dividend_percentage(self):
        return round(self.dividendValue * 100, 2)
    
    def get_total_stocks_number(self):
        return round(float(self.dividendGoal) / float(self.dividendValue))

    def get_initial_investment(self):
        return round(float(self.dividendGoal) / float(self.dividendValue) * float(self.closeMarketValue), 2)