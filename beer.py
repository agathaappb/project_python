word = "bottles"

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num-1
        if new_num == 1:
            word = "bottle"
            print(new_num,word," of beer on the wall.")
        print()
        
# Este é a canção da cerveja, apresentada no livro " Use a Cabeça - Paul Barry"
# O grande aprendizado neste código para mim foi a adaptação da delimitação dos suítes sem utilizar chaves
# Também podemos aprender sobre as formas de utilizar a função range
# Você pode somente indicar um valor de stop -> range(5)
# Determinando um valor de início e fim -> range(2,5)
# Determinando um valor de início, fim e um degrau (que seria por exemplo contar de 2 em 2; de 3 em 3 e assim por diante)
# -> range(2,15,2)
#uma outra curiosidade é que podemos fazer uma contagem decrescente também -> range(20,0,-2)
