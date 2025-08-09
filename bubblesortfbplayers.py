print("Welcome to the Bubble Sort of Football Players' Goals!")

players_goals = [
    (759, "Lionel Messi"),
    (805, "Cristiano Ronaldo"),
    (368, "Neymar Jr."),
    (505, "Robert Lewandowski"),
    (231, "Kylian Mbappé"),
    (70, "Paul Pogba"),
    (160, "Eden Hazard"),
    (253, "Wayne Rooney"),
    (128, "Sergio Ramos"),
    (86, "Kevin De Bruyne"),
    (52, "Virgil van Dijk"),
    (147, "Manuel Neuer"),
    (70, "Sergio Busquets"),
    (122, "Son Heung-min"),
    (572, "Zlatan Ibrahimović")
]

print("Players and their goals scored:")
print("-" * 40)

print(f"{'Player':<25} {'Goals Scored'}")
print("-" * 40)

for goals, player in players_goals:
    print(f"{player:<25} {goals:>12}")

print("-" * 40)


print("Sorting players based on their goals scored in descending order...\n")
def bubble_sort_players(player_stats):
    n = len(player_stats)
    for i in range(n):
        for j in range(0, n-i-1):
            if player_stats[j][0] < player_stats[j+1][0]:
                player_stats[j], player_stats[j+1] = player_stats[j+1], player_stats[j]
    return player_stats

sorted_players = bubble_sort_players(players_goals)

print("-" * 40)

print(f"{'Player':<25} {'Goals Scored'}")
print("-" * 40)

for goals, player in sorted_players:
    print(f"{player:<25} {goals:>12}")

print("-" * 40)



