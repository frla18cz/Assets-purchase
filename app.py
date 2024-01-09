import streamlit as st
import yfinance as yf
import datetime
import tickers


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
    

data = []

# Funkce pro uložení změn do souboru
def save_tickers_to_file(tickers):
    with open('tickers.py', 'w') as file:
        file.write(f"tickers = {tickers}\n")

def get_stock_data(ticker):
    data = yf.download(ticker, start=end_date - datetime.timedelta(days=10), end=current_date)
    last_close_price = data['Close'][-1]
    last_close_date = data.index[-1]
    shares_to_buy = purchase_value/last_close_price
    if testmode == True:
        print(ticker)
        print(f"Last close date: {last_close_date}\nLast close price: {round(last_close_price,2)}")

        st.write(f"|**Ticker:** {ticker}, Close Price: {round(last_close_price,2)}, Date: ({last_close_date})|................**Shares to buy: {round(shares_to_buy)}**")
    


    
#GUI
#####################################
# GUI
st.title("Stocks Data")



#####################################
# Načtení hodnot tickerů
default_tickers = ", ".join(tickers.tickers)

# Textové pole ve Streamlit s předvyplněnou hodnotou
user_input = st.text_input("Stocks Ticker List", value=default_tickers)

purchase_value = st.number_input("Purchase USD value for each stock. |8 shares|", value=3446)


# Zpracování odeslání formuláře
if st.button('Apply'):
    # Převedení uživatelského vstupu zpět na seznam
    updated_tickers = user_input.split(", ")
    # Uložení změn do souboru
    save_tickers_to_file(updated_tickers)
    st.success("Tickers updated successfully!")

    for ticker in tickers.tickers:
        stock_data = get_stock_data(ticker)


