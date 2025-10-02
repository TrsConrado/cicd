import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_list')

a = parser.parse_args().file_list
a_list = a.split(' ')
print('fcuk the world')
for file in a_list:
    print(f'Arquivo {file} modificado')