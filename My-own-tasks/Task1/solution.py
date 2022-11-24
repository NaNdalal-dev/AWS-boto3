
import boto3 as b3
import pandas as pd

try:
	df = pd.read_csv('dummy_data.csv')
	print(df.loc[0])


except Exception as e:
	print(e)