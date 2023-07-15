import pandas as pd


# df = pd.read_csv ('file_name.csv', sep=';')
# df = pd.read_csv ('file_name.csv')
# print(df)

df = pd.read_csv('tor_nodes.csv', usecols= ['Origin', 'Destination'])
print(df.size)
print(df)
df_one_column = df.stack().reset_index(drop=True)
print(df_one_column.size)
print(df_one_column)
df__no_duplicates = df_one_column.drop_duplicates()
print(df__no_duplicates.size)
print(df__no_duplicates)
first_3000 = df__no_duplicates.head(3000)
df_final = pd.DataFrame({'Tor_URL': first_3000})
df_final.to_csv('tor_3000.csv', index=False)
