import streamlit as st
import yfinance as yf
import datetime
import tickers


# Inicializace session state pro udržení seznamu tickerů
if 'ticker_list' not in st.session_state:
    st.session_state.ticker_list = ["AAPL", "MSFT", "GOOG", "AMZN"]

testmode = True

#####################################
# Aktuální datum
current_date = datetime.date.today()

# Datum předchozího dne
end_date = current_date - datetime.timedelta(days=1)

if testmode == True:
    print(end_date)
#####################################
#####################################
    

#####################################
ticker_list = "AAPL", "MSFT", "GOOG", "AMZN"


data = []

def get_stock_data(ticker):
    data = yf.download(ticker, start=end_date - datetime.timedelta(days=10), end=current_date)
    last_close_price = data['Close'][-1]
    last_close_date = data.index[-1]
    if testmode == True:
        print(ticker)
        print(f"Last close date: {last_close_date}\nLast close price: {round(last_close_price,2)}")






    




    
#GUI
#####################################
# GUI
st.title("Stocks Data")

tickers.tickers = st.text_input("Stocks Ticker List", value=tickers, height=200)


# Zobrazení a aktualizace seznamu tickerů


# Získání a zobrazení dat
current_date = datetime.date.today()
end_date = current_date - datetime.timedelta(days=1)




# #
# #####################################
# for ticker in ticker_list:
#     stock_data = get_stock_data(ticker)
# #####################################