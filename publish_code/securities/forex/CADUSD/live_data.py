from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import datetime



'''
def latest_data_60():
    username = 'StoCASHtic-ML'
    password = 'Biobio9034!'

    tv = TvDatafeed(username, password)

    securities_list = ['AUDUSD','EURGBP','EURUSD', 'USDCAD', 'USDCHF','USDCNH','USDHKD','USDJPY']
    df_all = pd.DataFrame()

    df_list =[]
    for security in securities_list:
    
        nifty_index_data = tv.get_hist(symbol=f'{security}',exchange='OANDA',interval=Interval.in_1_hour,n_bars=10000)

        df= nifty_index_data

        df =df.reset_index()
        df.rename(columns = {'datetime':f'{security}_Date','open': f'{security}_Open', 'high':f'{security}_High', 'low':f'{security}_Low', 'close':f'{security}_Close','volume':f'{security}_Volume'}, inplace=True)

        df_list.append(df)
    
    df_all = pd.concat(df_list, ignore_index =True)

   # df.set_index('Date', inplace=True)
    return df_all
#print(df)
'''

def latest_data_60():
    username = 'StoCASHtic-ML'
    password = 'Biobio9034!'

    tv = TvDatafeed(username, password)

   # securities_list = ['AUDUSD','EURGBP','EURUSD', 'USDCAD', 'USDCHF','USDCNH','USDHKD','USDJPY']
    #df_all = pd.DataFrame()

    #df_list =[]
    #for security in securities_list:
    
    security = 'CADUSD'

    nifty_index_data = tv.get_hist(symbol=f'{security}',exchange='OANDA',interval=Interval.in_1_hour,n_bars=10000)

    df= nifty_index_data

    df =df.reset_index()
    df.rename(columns = {'datetime':'Date','open': 'Open', 'high':'High', 'low':'Low', 'close':'Close','volume':'Volume'}, inplace=True)

    #df_list.append(df)
    
    #df_all = pd.concat(df_list, ignore_index =True)

   # df.set_index('Date', inplace=True)
    return df
'''
def latest_data_60():
    username = 'StoCASHtic-ML'
    password = 'Biobio9034!'

    tv = TvDatafeed(username, password)

    securities_list = ['AUDUSD','EURGBP','EURUSD', 'USDCAD', 'USDCHF','USDCNH','USDHKD','USDJPY']
    df_all = pd.DataFrame()

    df_list =[]
    for security in securities_list:

        nifty_index_data = tv.get_hist(symbol=f'{security}',exchange='OANDA',interval=Interval.in_1_hour,n_bars=10000)
    
        df = nifty_index_data
        df = df.dropna()

        #df = df.drop('Volume MA', axis =1)

       # 
        df.reset_index(inplace=True)
        df = df.rename(columns={'datetime':'Date','open':'Open', 'high':'High', 'low':'Low', 'close':'Close','volume':'Volume'})
        
       # print(df)
        df =df.set_index('Date')

               # df.index = pd.to_datetime(df.index, unit='s')
        columns_to_rename = {col: f"{security}_{col}" for col in df.columns}
        

                


                

                # Rename columns and set 'Time' as the index
        df.rename(columns=columns_to_rename, inplace=True)
               # df.set_index('Date')  
               # print(df)
                # Add the data to the combined DataFrame
        df_all = pd.concat([df_all, df], axis=1)

   # df.set_index('Date', inplace=True)
    return df_all
'''

def latest_data_5():
    username = 'StoCASHtic-ML'
    password = 'Biobio9034!'

    tv = TvDatafeed(username, password)


    nifty_index_data = tv.get_hist(symbol='EURUSD',exchange='OANDA',interval=Interval.in_5_minute,n_bars=10000)

    df= nifty_index_data

    df =df.reset_index()
    df.rename(columns = {'datetime':'Date','open': 'Open', 'high':'High', 'low':'Low', 'close':'Close','volume':'Volume'}, inplace=True)

    return df


if __name__ in "__main__":
    print(latest_data_60())