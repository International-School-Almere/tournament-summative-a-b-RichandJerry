#main file for the Tournament App.
Players = []
Events = []
scores = []

def add_player():
    name = input("Add Player name")
    Player_type   = input("Add player type(indevidual or team)")

    player = {
        "ID": len(Players),
        "Name": name,
        "Type": Player_type,
        "Total_Score": 0
    }