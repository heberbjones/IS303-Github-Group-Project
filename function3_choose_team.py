# Author: Jake Gardanier

def choose_team(remove_team=None):

    teams = [
        "BYU",
        "Utah",
        "Stanford",
        "UCLA",
        "USC",
        "Washington"
    ]

    # Remove the home team if selecting opponent
    if remove_team in teams:
        teams.remove(remove_team)

    print("\nChoose a Team:")

    for i in range(len(teams)):
        print(f"{i+1}. {teams[i]}")

    choice = int(input("Enter the number of the team: "))

    selected_team = teams[choice - 1]

    return selected_team