def login(worker):
    print()

def cadastro():

def editar():

def welcome():
  print('SISTEMA EEBA')
  respostas = {
    'Cadastro' : ['CADASTRAR', 'NOVO', 'USUÁRIO', ' USUARIO', '[1]', '1'];
    'Editar' : ['EDITAR', 'INFORMAÇÕES', 'INFORMACÕES', 'INFORMAÇOES', 'INFORMACOES']  
  }
  welcome = str(input('''[1] Cadastrar novo Usuário 
[2] Editar informações
-->''')).upper().split(' ')
  if map(welcome) in respostas['Cadastro']:
    cadastro()
  elif welcome in respostas['Editar']:
    editar()

def main():
        
