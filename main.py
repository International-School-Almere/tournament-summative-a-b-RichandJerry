#main file for the Tournament App.
players = []
events = []
scores = []
player_id_counter = 1
event_id_counter = 1
score_id_counter = 1

def calculate_points(position):
    if position == 1:
        return 10
    elif position == 2:
        return 8
    elif position == 3:
        return 6
    elif position == 4:
        return 4
    else:
        return 2


def add_player():
    global player_id_counter

    name = input("Enter player name: ")
    p_type = input("Enter type (individual/team): ")

    player = {
        "id": player_id_counter,
        "name": name,
        "type": p_type,
        "total_score": 0
    }

    players.append(player)
    player_id_counter += 1

    print("Player added correctly!\n")


def add_event():
    global event_id_counter

    name = input("Enter event name: ")
    e_type = input("Enter event type (individual/team): ")

    event = {
        "id": event_id_counter,
        "name": name,
        "type": e_type
    }

    events.append(event)
    event_id_counter += 1

    print("Event added correctly!\n")


def add_score():
    global score_id_counter

    print("\nPlayers:")
    for p in players:
        print(p["id"], "-", p["name"])

    player_id = int(input("Enter player ID: "))

    print("\nEvents:")
    for e in events:
        print(e["id"], "-", e["name"])

    event_id = int(input("Enter event ID: "))

    position = int(input("Enter position: "))
    points = calculate_points(position)

    score = {
        "id": score_id_counter,
        "player_id": player_id,
        "event_id": event_id,
        "position": position,
        "points": points
    }

    scores.append(score)
    score_id_counter += 1

    print("Score added! Points =", points, "\n")


def calculate_total_scores():
    # reset scores
    for p in players:
        p["total_score"] = 0

    for s in scores:
        for p in players:
            if p["id"] == s["player_id"]:
                p["total_score"] += s["points"]

def show_ranking():
    calculate_total_scores()

    sorted_players = sorted(players, key=lambda x: x["total_score"], reverse=True)

    print("\n= Ranking =")
    rank = 1
    for p in sorted_players:
        print(rank, "-", p["name"], "| Score:", p["total_score"])
        rank += 1
    print()

def menu():
    while True:
        print("= Score Management System =")
        print("1. Add Player")
        print("2. Add Event")
        print("3. Add Score")
        print("4. Show Ranking")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            add_event()
        elif choice == "3":
            add_score()
        elif choice == "4":
            show_ranking()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

menu()
