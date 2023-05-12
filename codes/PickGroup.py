from random import randint, seed

grupos = []

seed(95) #47 v 95

total_de_grupos = 6

while len(grupos) < total_de_grupos:
    n = randint(1, total_de_grupos)
    if n not in grupos:
        grupos.append(n)

print(grupos)

# [3, 1, 4, 5, 6, 2] for episode 47 (DBKAI)
# [5, 6, 2, 4, 1, 3] for episode 95 (DBZ)