import streamlit as st
import yfinance as yf
import datetime


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

for ticker in ticker_list:
    stock_data = get_stock_data(ticker)

# Aktualizace seznamu tickerů
def update_ticker_list():
    new_ticker = st.text_input("Add new ticker").upper()
    if new_ticker and new_ticker not in st.session_state.ticker_list:
        st.session_state.ticker_list.append(new_ticker)

#####################################
#####################################
    
    
#GUI
#####################################
st.title("Stocks Data")

st.text_input("Modify tickers")

# Zobrazení a aktualizace seznamu tickerů
update_ticker_list()

st.write("Current tickers:", st.session_state.ticker_list)
for ticker in st.session_state.ticker_list:
    get_stock_data(ticker)