import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_list')

file_path_list = parser.parse_args().file_list.split(' ')

# file_path_list = [
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\1.tables\table1.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\1.tables\table2.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\1.tables\table3.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\2.procs\proc1.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\2.procs\proc2.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\2.procs\proc3.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\2.procs\proc4.sql',
#     r'C:\Users\cgameiro\Documents\Projetos\cicd\projetoCopilot\2.procs\proc5.sql'
# ]

has_forbidden = False
was_outside = False

for file_path in file_path_list:
    print(file_path)
    with open(file_path, 'r') as file:
        contents = file.read()



    if '1.tables' in file_path:
        print('entrou em tables')
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot', 'replace']:
            if forbidden_term in contents.lower():
                has_forbidden = True

    elif '2.procs' in file_path:
        print('entrou em procs')
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot']:
            if forbidden_term in contents.lower():
                has_forbidden = True

    elif '3.funcs' in file_path:
        print('entrou em funcs')
        for forbidden_term in ['dev-dot', 'hml-dot', 'prd-dot']:
            if forbidden_term in contents.lower():
                has_forbidden = True
    
    else:
        print('entrou no else')
        was_outside = True


if has_forbidden:
    print('Foi encontrado termos proibidos nos scripts')
if was_outside:
    print('Foi encontrado modificações em arquivos fora das pastas determinadas')
if has_forbidden or was_outside:
    exit(1)