mine = {"chocolate", "pasta", "salad", "tofu", "spinach"}
friend = {"pizza", "pasta", "salad", "soup", "sushi"}
print(mine | friend)
print(mine & friend)
print(mine - friend)
print(friend - mine)

# part4
en_pl = {"dog": "pies", "cat": "kot", "fish": "ryba", "horse": "koń"}
print(en_pl["dog"])
print(len(en_pl))



en_pl.update({"snake": "wąż", "cow": "krowa"})
print(en_pl)
print(list(en_pl.items()))
print(list(en_pl.keys()))
print(list(en_pl.values()))

