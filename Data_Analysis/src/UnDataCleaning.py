def UNDataCleaning(country:str, csv_name:str, indicator_num: str): #all country name has capital for first letter
    df = pd.read_csv(f'../data/{country}/UNData/{csv_name}')
    df = df[['SeriesDescription', 'TimePeriod', 'Value']]
    df.dropna(inplace=True)
    df_pivot = df.pivot(index = ['TimePeriod'],
                    columns = 'SeriesDescription',
                    values = 'Value').reset_index()
    df_pivot.columns.name = None
    df_pivot.rename(columns = {'TimePeriod': 'Year'}, inplace = True)
    df_pivot.to_csv(f'../data/{country}/UNData/{indicator_num}Tidy.csv', index = False)