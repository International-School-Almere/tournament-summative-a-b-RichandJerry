import tkinter as tk
from tkinter import ttk
import json

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tournament Manager")
        self.geometry("600x400")

        self.players = []
        self.events = []
        self.positions = []

        self.load_data()

        self.frames = {}

        for F in (MainMenu, AddPlayer, AddEvent, SelectEvent, AddPosition, Result, AddScore):
            frame = F(self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(MainMenu)

    def save_data(self):
        data = {
            "players": self.players,
            "events": self.events,
            "positions": self.positions
        }

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
 

    def load_data(self):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.players = data.get("players", [])
            self.events = data.get("events", [])
            self.positions = data.get("positions", [])

        except FileNotFoundError:
            self.players = []
            self.events = []
            self.positions = []

    def show_frame(self, page):
        frame = self.frames[page]

        if page == SelectEvent:
            frame.refresh()

        if page == AddScore:
            frame.refresh_events()

        if page == AddPosition:
            frame.refresh()

        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Main Menu", font=("Arial", 18)).pack(pady=20)

        tk.Button(self, text="Add Player",
                  command=lambda: master.show_frame(AddPlayer)).pack(pady=10)

        tk.Button(self, text="Add Event",
                  command=lambda: master.show_frame(AddEvent)).pack(pady=10)
        
        tk.Button(self, text="Select Event",
                  command=lambda: master.show_frame(SelectEvent)).pack(pady=10)
        
        tk.Button(self, text="Add Position",
                  command=lambda: master.show_frame(AddPosition)).pack(pady=10)

        tk.Button(self, text="Add Score",
                  command=lambda: master.show_frame(AddScore)).pack(pady=10)

        tk.Button(self, text="Result",
                  command=lambda: master.show_frame(Result)).pack(pady=10)
        
        tk.Button(self, text="Save Data",
                  command=master.save_data).pack(pady=10)
        
class AddPlayer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Add Player", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Player Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Player Type").pack()
        self.player_type = ttk.Combobox(
            self,
            values=["Individual", "Team"],
            state="readonly"
        )
        self.player_type.pack(pady=5)
        self.player_type.current(0)

        tk.Button(self, text="Add Player", command=self.add_player).pack(pady=5)
        tk.Button(self, text="Delete Player", command=self.delete_player).pack(pady=5)
        tk.Button(self, text="Edit Selected", command=self.load_selected).pack(pady=5)
        tk.Button(self, text="Update Player", command=self.update_player).pack(pady=5)

        self.player_listbox = tk.Listbox(self, width=40, height=10)
        self.player_listbox.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack()

        self.selected_index = None

    def add_player(self):
        name = self.name_entry.get()
        p_type = self.player_type.get()

        if not name:
            return

        player = {"name": name, "type": p_type}
        self.master.players.append(player)

        self.player_listbox.insert(tk.END, f"{name} ({p_type})")
        self.name_entry.delete(0, tk.END)

    def delete_player(self):
        try:
            index = self.player_listbox.curselection()[0]
        except IndexError:
            return

        del self.master.players[index]

        self.player_listbox.delete(index)

    def load_selected(self):
        try:
            index = self.player_listbox.curselection()[0]
        except IndexError:
            return

        player = self.master.players[index]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, player["name"])

        self.player_type.set(player["type"])

        self.selected_index = index

    def update_player(self):
        if self.selected_index is None:
            return

        name = self.name_entry.get()
        p_type = self.player_type.get()

        if not name:
            return

        self.master.players[self.selected_index] = {
            "name": name,
            "type": p_type
        }

        self.player_listbox.delete(self.selected_index)
        self.player_listbox.insert(self.selected_index, f"{name} ({p_type})")

        self.selected_index = None
        self.name_entry.delete(0, tk.END)

        self.player_type.set("Individual")
        self.player_type.current(0)

class AddEvent(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Add Event", font=("Arial", 16)).pack(pady=10)

        self.event_entry = tk.Entry(self)
        self.event_entry.pack(pady=5)

        tk.Button(self, text="Create Event", command=self.create_event).pack(pady=5)

        self.event_listbox = tk.Listbox(self, height=5)
        self.event_listbox.pack(pady=5)

        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def create_event(self):
        name = self.event_entry.get()

        if not name:
            return

        event = {"name": name, "players": []}
        self.master.events.append(event)

        self.event_listbox.insert(tk.END, name)
        self.event_entry.delete(0, tk.END)

class AddScore(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Add Score Rule", font=("Arial", 16)).pack(pady=10)

        self.event_box = ttk.Combobox(self, state="readonly")
        self.event_box.pack(pady=5)

        tk.Label(self, text="Position").pack()
        self.position_entry = tk.Entry(self)
        self.position_entry.pack()

        tk.Label(self, text="Points").pack()
        self.points_entry = tk.Entry(self)
        self.points_entry.pack()

        tk.Button(self, text="Save", command=self.save_score).pack(pady=5)

        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def refresh_events(self):
        event_names = [e["name"] for e in self.master.events]
        self.event_box["values"] = event_names

    def save_score(self):
        event_name = self.event_box.get()
        position = self.position_entry.get()
        points = self.points_entry.get()

        if not event_name or not position or not points:
            return

        for e in self.master.events:
            if e["name"] == event_name:

                if "points" not in e:
                    e["points"] = {}

                e["points"][int(position)] = int(points)

        self.position_entry.delete(0, tk.END)
        self.points_entry.delete(0, tk.END)

class SelectEvent(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Select Event Players", font=("Arial", 16)).pack(pady=10)

        self.event_box = ttk.Combobox(self, state="readonly")
        self.event_box.pack()
        self.event_box.bind("<<ComboboxSelected>>", self.show_players)

        self.player_box = ttk.Combobox(self, state="readonly")
        self.player_box.pack()

        tk.Button(self, text="Add Player to Event",
                  command=self.add_player).pack(pady=5)

        self.event_players_listbox = tk.Listbox(self, height=10)
        self.event_players_listbox.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def refresh(self):
        event_names = [e["name"] for e in self.master.events]
        self.event_box["values"] = event_names

        player_names = [p["name"] for p in self.master.players]
        self.player_box["values"] = player_names

    def add_player(self):
        event_name = self.event_box.get()
        player_name = self.player_box.get()

        if not event_name or not player_name:
            return

        for e in self.master.events:
            if e["name"] == event_name:
                if player_name not in e["players"]:
                    e["players"].append(player_name)

        self.show_players(None)

    def show_players(self, event):
        self.event_players_listbox.delete(0, tk.END)

        event_name = self.event_box.get()

        for e in self.master.events:
            if e["name"] == event_name:
                for p in e["players"]:
                    self.event_players_listbox.insert(tk.END, p)

class AddPosition(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Add Position", font=("Arial", 16)).pack(pady=10)

        self.event_box = ttk.Combobox(self, state="readonly")
        self.event_box.pack()
        self.event_box.bind("<<ComboboxSelected>>", self.update_players)

        self.player_box = ttk.Combobox(self, state="readonly")
        self.player_box.pack()

        tk.Label(self, text="Position").pack()
        self.position_entry = tk.Entry(self)
        self.position_entry.pack(pady=5)

        tk.Button(self, text="Save Position", command=self.save_position).pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def refresh(self):
        event_names = [e["name"] for e in self.master.events]
        self.event_box["values"] = event_names

    def update_players(self, event):
        selected_event = self.event_box.get()

        for e in self.master.events:
            if e["name"] == selected_event:
                self.player_box["values"] = e["players"]

    def save_position(self):
        event = self.event_box.get()
        player = self.player_box.get()
        position = self.position_entry.get()

        if not position:
            return

        self.master.positions.append({
            "event": event,
            "player": player,
            "position": int(position)
        })

        self.position_entry.delete(0, tk.END)

        self.show_positions()

    def show_positions(self):
        self.listbox.delete(0, tk.END)

        event = self.event_box.get()

        for p in self.master.positions:
            if p["event"] == event:
                self.listbox.insert(tk.END,
                    f"{p['player']} - {p['position']} place")

class Result(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="Results", font=("Arial", 16)).pack(pady=10)

        self.text = tk.Text(self, width=60, height=20)
        self.text.pack(pady=10)

        tk.Button(self, text="Refresh", command=self.show_all_results).pack()
        tk.Button(self, text="Back",
                  command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def show_all_results(self):
        self.text.delete("1.0", tk.END)

        for event in self.master.events:

            event_name = event["name"]
            self.text.insert(tk.END, f"\n=== {event_name} ===\n")

            totals = {}

            for p in self.master.positions:
                if p["event"] != event_name:
                    continue

                player = p["player"]
                pos = p["position"]

                points = event.get("points", {}).get(pos, 0)

                if player not in totals:
                    totals[player] = {
                        "points": 0,
                        "position": pos
                    }

                totals[player]["points"] += points

            ranking = sorted(
                totals.items(),
                key=lambda x: x[1]["points"],
                reverse=True
            )

            for i, (player, data) in enumerate(ranking, start=1):
                self.text.insert(
                    tk.END,
                    f"{i}. {player} | {data['points']} pts | {data['position']} place\n"
                )

app = App()
app.mainloop()