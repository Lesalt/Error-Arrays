import tabela as tl

#Escolhe qual matriz quer
choice = int(input("1) Matriz Error\n2) Matriz Sucessful"))

#executa a escolha 1
if(choice == 1):
    tl.MatrizError()

#executa a escolha 2
if(choice == 2):
    tl.MatrizSuccessful()