stray = str(input("Строка:"))
wildways = {}
for sym in stray:
    if sym in wildways:
        wildways[sym] += 1
        
    else:
        wildways[sym] = 1
print(max(wildways, key=wildways.get))
