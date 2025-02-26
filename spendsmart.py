import streamlit as st
import yfinance as yf
import datetime
from datetime import date
from streamlit_option_menu import option_menu
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd
import requests
import urllib.parse

st.title("Spend$mart")
select=option_menu(
    menu_title=None,
    options=['Market','Prediction','News','Contact Us'],orientation='horizontal'
        )
if select == "Prediction":
    st.title('Prediction')
    symbol = st.text_input("Enter a stock token : ",value='AAPL')

    start=st.date_input('Starting Date : ',value=datetime.datetime.today()-datetime.timedelta(days=10))
    end=st.date_input('End Date : ',value=datetime.datetime.today())
    predi=st.date_input("Prediction end date (predictions start from present date) : ",value=datetime.datetime.today()+datetime.timedelta(days=10))

    @st.cache_data
    def stock_data(symbol,start,end):
        data=yf.download(symbol,start,end)
        data.reset_index(inplace=True)
        return data

    tkdata=yf.Ticker(symbol)

    stock=stock_data(symbol,start,end)
    st.header("Stock Data")
    st.write(stock)
    
    no= predi-date.today()
    period=no.days
  
    def plot_graph():
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=stock['Date'],y=stock['Open'],name="Stock Open Price"))
        fig.add_trace(go.Scatter(x=stock['Date'],y=stock['Close'],name="Stock Close Price "))
        fig.layout.update(title_text="Stock Data Graph",xaxis_rangeslider_visible=True)
        fig.update_layout(xaxis_title="Price",yaxis_title="Date")        
        st.plotly_chart(fig)
    plot_graph()

    train=stock[['Date','Close']]
    train.columns=['ds','y']
    pro=Prophet(daily_seasonality=True)
    pro.fit(train)
    future=pro.make_future_dataframe(periods=period)
    predictions=pro.predict(future)
    st.header('Predicted Prices')
    df=pd.DataFrame(predictions['ds'])
    df1=pd.DataFrame(predictions['trend'])
    trend=pd.concat([df,df1],axis=1)
    st.write(trend)
    st.text('ds : Date')
    st.text('trend : Price of the Stock')
    
    fig1=plot_plotly(pro,predictions)
    fig1.update_traces(marker=dict(color='light blue'))
    fig1.layout.update(title_text='Prediction Price Graph')
    st.plotly_chart(fig1)

    
if select=='News':
    st.title("News")
    q=st.text_input("Enter the keyword :",value='bitcoin')
    url=f'https://newsapi.org/v2/everything?q={q}&sortBy=publishedAt&apiKey=6f737b4068ca40e9b77eefc66b716478'
    r=requests.get(url)
    r=r.json()
    articles=r['articles']
    for article in articles:
        st.header(article['title'])
        st.write(f"<h5 style=''> Published at : {article['publishedAt']}</h5>",unsafe_allow_html=True)
        if article['author']:
            st.write(article['author'])
        if article['description']==None:
            st.write("Refer The Link")
            st.write(f"{article['url']}")
        else:
            st.write(article['source']['name'])
            st.write(article['description'])
            st.write(f"See More :  {article['url']}")
            try:
                st.image(article['urlToImage'])
            except AttributeError:
                st.write("IMAGE IS NOT AVAILABLE")
            else:
                pass
    
if select=="Contact Us":
    st.title("Get in Touch With Us")
    form='''<form action = 'https://formsubmit.co/4e842a83b01a714615ee75a8fd702e56' method="POST">
Name : 
<input type = "hidden" name="_captcha" value="false">
<input type = "text" name="name" placeholder="Your Name" required>
Email : <input type = "email" name="email" placeholder="Your email" required>
Message : <textarea name="message" placeholder='Your Message Here' required></textarea>
<button type="Submit">Submit</button>
</form>'''

    st.markdown(form,unsafe_allow_html=True)

    def css():
        st.markdown("""<style> /* Style inputs with type="text", select elements and textareas */
input[type=text], select, textarea {
background-color: #36454F;
color : white;
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}
input[type=email] {width: 100%; /* Full width */
color : white;
  padding: 12px; /* Some padding */
  background-color: #36454F;
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */}

/* Style the submit button with a specific background color etc */
input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
  background-color: #45a049;
}</style>""",unsafe_allow_html=True)
    css()

    
           
if select=="Market":

    st.title("Market")
    wt=st.selectbox("Select",('Stock Token','S&P 500'))
    if wt=='Stock Token':
        sym=st.text_input('Stock',"AAPL").upper()
        resp = yf.Ticker(sym)
        info = resp.info
        name = info.get('longName')
        country = info.get('country')
        ceo = info.get('companyOfficers')[0]['name']
        currency = info.get('currency')
        summ = info.get('longBusinessSummary')
        ind = info.get('industry')
        website = info.get('website')
        rev = info.get('totalRevenue')

        st.subheader(name)
        st.write(f'**Industry** : {ind}')
        st.write(F'**Chief Executive Officer**: {ceo}')
        st.write(f'**Country** : {country}')
        st.write(f'**Currency** : {currency}')
        st.write(f'**Total Revenue** : {rev}')
        with st.expander('SUMMARY',expanded = False):
            st.write(f'{summ}')

        link_id = f"More Info about {sym}"
        button_code = f"<a href='{website}' target='_blank' style='display: inline-block; padding: 10px 20px; background-color: #1D77BF; color: white; text-align: center; text-decoration: none; margin: 4px 2px; cursor: pointer; border-radius: 10px;'>{link_id}</a>"
        st.markdown(button_code, unsafe_allow_html=True)

        start=datetime.datetime.today()-datetime.timedelta(days=3650)
        end=datetime.datetime.today()
        tkdata=yf.Ticker(sym)
        tkdf=tkdata.history(period='1d',start=start,end=end)
        def stock_data(symbol,start,end):
            data=yf.download(symbol,start,end)
            data.reset_index(inplace=True)
            return data
    
        stock=stock_data(sym,start,end)
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=stock['Date'],y=stock['Close']))
        fig.update_layout(title=sym,xaxis_title="Price",yaxis_title="Date")
        fig.layout.update(xaxis_rangeslider_visible=True)
        st.subheader("Price Graph")
        st.plotly_chart(fig)
        st.subheader("Price Chart")
        st.write(stock)

    if wt=="S&P 500":
        st.header("S&P 500")
        @st.cache_data
        def load_data():
            url='https://en.wikipedia.org/wiki/list_of_S%26P_500_companies'
            html=pd.read_html(url,header=0)
            df=html[0]
            return df
        df=load_data()
        sector=df.groupby("GICS Sector")

        sortsector = sorted(df['GICS Sector'].unique())
        selectsector=st.multiselect("Sector",sortsector,sortsector)

        df1=df[(df['GICS Sector'].isin(selectsector))]

        st.write("Number of Companies for selected Categories : "+ str(df1.shape[0]))
        st.dataframe(df1)
        data=yf.download(tickers=list(df1[:10].Symbol),period = 'ytd',interval='1d',group_by = 'ticker',auto_adjust=True,prepost=True,threads=True,proxy=None)
        def price_plot(symbol):
            df=pd.DataFrame(data[symbol].Close)
            df['Date']=df.index
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=df.Date,y=df.Close,name="Stock Close Price "))
            fig.layout.update(title_text=symbol,xaxis_rangeslider_visible=True)
            fig.update_layout(xaxis_title="Date",yaxis_title="Price")        
            st.plotly_chart(fig)
        num=st.selectbox("Number of Company Graphs : ",(1,2,3,4,5,6,7,8,9,10))
        if st.button('Graphs'):
            st.subheader(f"Graphs of Top {num} Companies")
            for i in list(df1.Symbol)[:num]:
                price_plot(i)
