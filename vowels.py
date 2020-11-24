vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
#Traduzindo....-> Forneça uma palavra para pesquisar vogais
found=[]

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
    
        
# Este programa foi retirado do livro -> "Use a Cabeça -  Paul Barry"
# Este pequeno programa solicita ao usuário para inserir uma palavra para dizer quais são as vogais que aparecem nela
# Para que o programa insira palavras do usuário, é utilizado a função -> input
# Assim como o método in verifica se algo contém em uma ista ou em uma string; o método not in verifica se ago não contém naquele objeto, ou na lista de objetos
# Utilizamos append para inserir objetos a lista
