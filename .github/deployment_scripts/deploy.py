import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_list')
parser.add_argument('branch_name')

file_path_list = parser.parse_args().file_list.split(' ')
branch_name = parser.parse_args().branch_name

import snowflake.connector
import os

user = os.environ['SNOWFLAKE_USER']
password = os.environ['SNOWFLAKE_PSWD']
account = os.environ['SNOWFLAKE_ACCOUNT']

# Cria a conexao com o snowflake
# conn = snowflake.connector.connect(
#                 user=user,
#                 password=password,
#                 account=account
#                 )


for a in user:
    print(a)

for b in password:
    print(b)

for c in account:
    print(c)