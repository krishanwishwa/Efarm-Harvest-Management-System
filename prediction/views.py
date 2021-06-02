from django.shortcuts import render

#ML imports
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.arima_model import ARIMA
import warnings
from pandas.tseries.offsets import DateOffset
import joblib
import matplotlib
matplotlib.use('Agg')
from plotly.offline import plot
from plotly.graph_objs import Scatter
warnings.filterwarnings("ignore")


def carrotpricepredict(request):
    df=pd.read_csv('carrot price.csv')
    df.columns=["Date","Prices"]
    df['Date']=pd.to_datetime(df['Date'])
    df.set_index('Date',inplace=True)

    model = joblib.load('carrot_model.sav')
    results=model.fit()

    future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,38)]
    future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)

    #convert data to float
    df["Prices"] = df['Prices'].astype('float')

    future_datest_df["Prices"] = future_datest_df['Prices'].astype('float')
    # future_datest_df["Prices First Difference"] = future_datest_df['Prices First Difference'].astype('float')
    # future_datest_df["Seasonal First Difference"] = future_datest_df['Seasonal First Difference'].astype('float')
    # future_datest_df["forecast"] = future_datest_df['forecast'].astype('float')

    future_df=pd.concat([df,future_datest_df])
    future_df['forecast'] = results.predict(start = 107, end = 145, dynamic = False )


    fig = px.line(future_df, x=future_df.index, y=["Prices","forecast"])


    fig.update_layout(
        template='gridon',
        title='Future Price Prediction For Carrots',
        xaxis_title='Year',
        yaxis_title='Price (LKR)',
        xaxis_showgrid=True,
        yaxis_showgrid=True,
    )
    # fig.show()


    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot(px.line(future_df, x=future_df.index, y=["Prices","forecast"]),output_type='div')

    context = {
    'plot_div': plot_div

    }

    return render(request, 'predictions/carrotpricepredict.html', context)


def potatopricepredict(request):
    df=pd.read_csv('potato price.csv')
    df.columns=["Date","Prices"]
    df['Date']=pd.to_datetime(df['Date'])
    df.set_index('Date',inplace=True)

    model = joblib.load('potato_model.sav')
    results=model.fit()

    future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,38)]
    future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)

    #convert data to float
    df["Prices"] = df['Prices'].astype('float')

    future_datest_df["Prices"] = future_datest_df['Prices'].astype('float')
    # future_datest_df["Prices First Difference"] = future_datest_df['Prices First Difference'].astype('float')
    # future_datest_df["Seasonal First Difference"] = future_datest_df['Seasonal First Difference'].astype('float')
    # future_datest_df["forecast"] = future_datest_df['forecast'].astype('float')

    future_df=pd.concat([df,future_datest_df])
    future_df['forecast'] = results.predict(start = 107, end = 145, dynamic = False )


    fig = px.line(future_df, x=future_df.index, y=["Prices","forecast"])


    fig.update_layout(
        template='gridon',
        title='Future Price Prediction For Carrots',
        xaxis_title='Year',
        yaxis_title='Price (LKR)',
        xaxis_showgrid=True,
        yaxis_showgrid=True,
    )
    # fig.show()


    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot(px.line(future_df, x=future_df.index, y=["Prices","forecast"]),output_type='div')

    context = {
    'plot_div': plot_div

    }

    return render(request, 'predictions/potatopricepredict.html', context)
