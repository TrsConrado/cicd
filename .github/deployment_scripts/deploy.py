import argparse
from codecs import open
import snowflake.connector
import os

parser = argparse.ArgumentParser()
parser.add_argument('file_list')
parser.add_argument('branch_name')

file_path_list = parser.parse_args().file_list.split(' ')
branch_name = parser.parse_args().branch_name

print(branch_name)

user = os.environ['SNOWFLAKE_USER']
password = os.environ['SNOWFLAKE_PSWD']
account = os.environ['SNOWFLAKE_ACCOUNT']
warehouse = os.environ['SNOWFLAKE_WAREHOUSE']
database = os.environ['SNOWFLAKE_WAREHOUSE']
role = os.environ['SNOWFLAKE_ROLE']

# with snowflake.connector.connect(
#     user=user,
#     password=password,
#     account=account,
#     warehouse= warehouse,
#     database=database,
#     role=role
#     ) as conn:

#     for chgd_file_path in file_path_list:
#         with open(chgd_file_path, 'r', encoding='latin-1') as f:
#             for cur in conn.execute_stream(f):
#                 for ret in cur:
#                     print(ret)