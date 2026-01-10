

"""
Print all combinations in the form "x - y - z" using integers from 1 to 20
and count the total number of combinations.
"""
count = 0
for x in range(20):
    for y in range(20):
        for z in range(20):
            print(f"{x + 1} - {y + 1} - {z + 1}")
            count += 1
print(f"Kokku leiti {count} kombinatsiooni.")