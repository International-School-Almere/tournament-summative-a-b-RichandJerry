import tkinter as tk
from tkinter import ttk

# プレイヤーデータ保存用
players = []

# メイン画面
root = tk.Tk()
root.title("Tournament Manager")
root.geometry("500x400")

# -------------------------
# プレイヤー追加関数
# -------------------------
def add_player():

    # 入力された名前
    name = name_entry.get()

    # 選択されたタイプ
    p_type = type_box.get()

    # 名前が空なら終了
    if name == "":
        return

    # データ追加
    player = {
        "name": name,
        "type": p_type
    }

    players.append(player)

    # Listbox に表示
    player_list.insert(
        tk.END,
        f"{name} ({p_type})"
    )

    # 入力欄を空にする
    name_entry.delete(0, tk.END)

# -------------------------
# プレイヤー削除
# -------------------------
def delete_player():

    # 選択されてる行番号取得
    select = player_list.curselection()

    # 未選択なら終了
    if not select:
        return

    index = select[0]

    # データ削除
    del players[index]

    # Listbox 削除
    player_list.delete(index)

# -------------------------
# タイトル
# -------------------------
title = tk.Label(
    root,
    text="Add Player",
    font=("Arial", 18)
)

title.pack(pady=10)

# -------------------------
# 名前入力
# -------------------------
tk.Label(root, text="Player Name").pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# -------------------------
# タイプ選択
# -------------------------
tk.Label(root, text="Player Type").pack()

type_box = ttk.Combobox(
    root,
    values=["Individual", "Team"],
    state="readonly"
)

type_box.pack(pady=5)

type_box.current(0)

# -------------------------
# ボタン
# -------------------------
tk.Button(
    root,
    text="Add Player",
    command=add_player
).pack(pady=5)

tk.Button(
    root,
    text="Delete Player",
    command=delete_player
).pack(pady=5)

# -------------------------
# プレイヤー一覧
# -------------------------
player_list = tk.Listbox(
    root,
    width=40,
    height=10
)

player_list.pack(pady=10)

root.mainloop()