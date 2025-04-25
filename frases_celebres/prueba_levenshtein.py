import Levenshtein
#Similares
input1 = "feria"
input2 = "fiera"
#Distintas
input3 = "El futuro nuestro es"
input4 = "feria de libros"
#Distance
distancia = Levenshtein.distance(input1, input2)
distancia2 = Levenshtein.distance(input3, input4)
#Ratio
ratio = Levenshtein.ratio(input1, input2)
ratio2 = Levenshtein.ratio(input3, input4)
#set_ratio
set_ratio = Levenshtein.setratio(input1, input2)
set_ratio2 = Levenshtein.setratio(input3, input4)
#Hamming
hamming = Levenshtein.hamming(input1, input2)
hamming2 = Levenshtein.hamming(input3, input4)

'''Print de similares'''
print(f"Distancia entre '{input1}' y '{input2}': {distancia}")
print(f"Ratio entre '{input1}' y '{input2}': {ratio}")
print(f"Set Ratio entre '{input1}' y '{input2}': {set_ratio}")
print(f"Hamming entre '{input1}' y '{input2}': {hamming}")
print('--------------------------------------------------------')
'''#Print de distintas'''
print('--------------------------------------------------------')
print(f"Distancia entre '{input3}' y '{input4}': {distancia2}")
print(f"Ratio entre '{input3}' y '{input4}': {ratio2}")
print(f"Set Ratio entre '{input3}' y '{input4}': {set_ratio2}")
print(f"Hamming entre '{input3}' y '{input4}': {hamming2}")