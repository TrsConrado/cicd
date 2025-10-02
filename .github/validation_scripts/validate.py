import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_list')

a = parser.parse_args().file_list

print('fcuk the world')
print(a)