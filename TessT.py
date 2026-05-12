import tkinter as tk
from tkinter import ttk

players = []

root = tk.Tk()
root.title("Tournament Manager")
root.geometry("400x400")

# ===== プレイヤー追加 =====

tk.Label(root, text="Player Name").pack()

name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Player Type").pack()

type_box = ttk.Combobox(
    root,
    values=["Individual", "Team"],
    state="readonly"
)

type_box.pack()
type_box.current(0)

player_listbox = tk.Listbox(root)
player_listbox.pack(pady=10)

def add_player():

    name = name_entry.get()
    player_type = type_box.get()

    if name == "":
        return

    # データ保存
    player = {
        "name": name,
        "type": player_type
    }

    players.append(player)

    # リストに表示
    player_listbox.insert(
        tk.END,
        f"{name} ({player_type})"
    )

    # 入力欄を空にする
    name_entry.delete(0, tk.END)

tk.Button(
    root,
    text="Add Player",
    command=add_player
).pack()

root.mainloop()