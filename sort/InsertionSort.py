array = [7, 2, 5, 1, 9, 3] # Ένα παράδειγμα ενός πίνακα αριθμών
print("Πίνακας:", array)

# Εφαρμογή του αλγορίθμου ταξινόμησης με εισαγωγή
for i in range(1, len(array)):
    value = array[i]
    j = i
    while j > 0 and array[j - 1] > value:
        array[j] = array[j - 1]
        j = j - 1
    array[j] = value
    print(i,"η :", array)

print("Ο ταξινομημένος πίνακας:", array)
