from datetime import datetime
import time
import random

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for x in range(5):

    right_this_minute = datetime.today().minute

    # Isso é um comentário

    if right_this_minute in odds:
        print("This minute seems a little odd. ")
    #Traduzindo -> Este minuto parece um pouco estranho

    else:
        print("Not an odd minute.")
    #Traduzindo -> Nem um minuto estranho

    wait_time = random.randint(1,60)
    time.sleep(wait_time)

    # Este foi o primeiro programa python ensinado no livro -> Use a cabeça! Python - Autor: Paul Barry
    # Neste pequeno trecho de código podemos aprender muita coisa com poucas linhas de código, como por exemplo:
    # As duas maneiras de importar uma função de um módulo
    # Realização de testes no python shell antes de acrescentar no código principal
    # Como o pyhton declara uma variável
    # Um pouco de lista
    # Uso de for / if / else / elif / print / in
    # Este último (in) é muito útil quando se precisa saber se algo contem em uma lista ou em uma variável para a execução de uma condicional
    # No Python Shell  utilizar o din (nome do módulo) para saber quais funções pertence aquele módulo
    # Também caso não saiba usar a função desejada, basta digitar no shell o comando help ( função) e ele te mostra a documentação daquela função.
    # funções randint -> retorna um número inteiro aleatório, no intervalo pré-definido na função
    # função sleep -> quando se quer dar uma pausa durante a execução do código
    # E a fazer comentários como este ♥    
