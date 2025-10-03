import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_list')
parser.add_argument('branch_name')

file_path_list = parser.parse_args().file_list.split(' ')
branch_name = parser.parse_args().branch_name

print(branch_name)

has_forbidden = False
forbidden_location = {}
was_outside = False

for file_path in file_path_list:
    with open(file_path, 'r') as file:
        contents = file.read()



    if '1.tables' in file_path:
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot', 'replace']:
            if forbidden_term in contents.lower():
                has_forbidden = True
                lines = contents.lower().splitlines()
                for line_num, line in enumerate(lines):
                    column_num = line.find(forbidden_term)
                    if column_num != -1:
                        print(f'Foi encontrado o termo proibido "{forbidden_term}" no arquivo "{file_path}", na linha {line_num} e coluna {column_num}')

    elif '2.procs' in file_path:
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot']:
            if forbidden_term in contents.lower():
                has_forbidden = True
                lines = contents.lower().splitlines()
                for line_num, line in enumerate(lines):
                    column_num = line.find(forbidden_term)
                    if column_num != -1:
                        print(f'Foi encontrado o termo proibido "{forbidden_term}" no arquivo "{file_path}", na linha {line_num} e coluna {column_num}')

    elif '3.funcs' in file_path:
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot']:
            if forbidden_term in contents.lower():
                has_forbidden = True
                lines = contents.lower().splitlines()
                for line_num, line in enumerate(lines):
                    column_num = line.find(forbidden_term)
                    if column_num != -1:
                        print(f'Foi encontrado o termo proibido "{forbidden_term}" no arquivo "{file_path}", na linha {line_num+1} e coluna {column_num+1}')
    
    elif '.github/validation_scripts' in file_path:
        pass
    elif '.github/deployment_scripts' in file_path:
        pass

    else:
        was_outside = True

print('----------------------------------------------------------------------------------------')
if has_forbidden:
    print('Foi encontrado termos proibidos nos scripts')
if was_outside:
    print('Foi encontrado modificações em arquivos fora das pastas determinadas')
print('----------------------------------------------------------------------------------------')
if has_forbidden or was_outside:
    exit(1)