print()
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
# ---tOTAL bUDGET---
t_budget = 0
for movie in movies:
    t_budget += movie[1] 
#---Avg Budget---
avg_budget = t_budget /len(movies)  
print(f"\nAverage budget = {avg_budget}")


count = 0
print("\nMovies with budget higher than average:  ")
for movie in movies:
    if movie[1] > avg_budget:
        print(f"\n{movie[0]} with a budget of {movie[1]}")
        count += 1

print(f"\nNo of high budget movies  = : {count}")
