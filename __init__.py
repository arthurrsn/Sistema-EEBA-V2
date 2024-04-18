def login():
    

def cadastro():

def editar():

def welcome() -> str:
    '''
    '''
  print('SISTEMA EEBA')
  respostas = {
    'Cadastro' : ['CADASTRAR', 'NOVO', 'USUÁRIO', ' USUARIO', '[1]', '1'];
    'Editar' : ['EDITAR', 'INFORMAÇÕES', 'INFORMACÕES', 'INFORMAÇOES', 'INFORMACOES', '2', '[2]']  
  }
  welcome = str(input('''[1] Cadastrar novo Usuário 
[2] Editar informações
-->''')).upper().split(' ')
  if map(welcome) in respostas['Cadastro']:
    return 'CADASTRO'
  elif welcome in respostas['Editar']:
    return 'EDITAR'

def main():
    login()
