# Function to print out properties of each DataFrame:
def print_props(df_list, prop = '.head()'):

    for df in df_list:
        if (prop == '.head()'):
            title = '\tFirst 5 rows of DataFrame: '
            data = df.head()
            
        elif (prop == '.tail()'):
            title = '\tLast 5 rows in DataFrame: '
            data = df.tail()
            
        elif (prop == '.columns'):
            title = '\tColumn Features of DataFrame: '
            data = df.columns
            
        elif (prop == '.dtypes'):
            title = '\tData Types of DataFrame: '
            data = df.dtypes
            
        elif (prop == '.shape'):
            title = '\tShape of DataFrame: '
            data = df.shape
            
        elif (prop == '.isnull().sum()'):
            title = '\tNull Values in DataFrame: '
            data = df.isnull().sum()
            
        elif (prop == '.describe()'):
            title = '\tSummary Statistics of DataFrame: '
            data = df.describe()
        
        print(title + df.name)
        print('----------------------------------------')
        print(data)
        print()