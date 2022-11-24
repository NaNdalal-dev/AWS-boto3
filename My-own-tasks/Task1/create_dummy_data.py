#pip install pandas
import pandas as pd

#Employee attributes ID,Name and Email.
emp_ids = [i for i in range(1,1001)]
user_name = [f'User{id}' for id in emp_ids]
user_mails = [f'{name}@mail.com' for name in user_name]

#Creating DataFrame
data = {
	'Id':emp_ids,
	'Name':user_name,
	'Email':user_mails
}

df = pd.DataFrame(data)

#Converting DataFrame to CSV file

df.to_csv('dummy_data.csv',index=False)