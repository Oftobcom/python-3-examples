maj= {6,4,"ali",45,23,"ali",11,4,7,5,"vali"}
print("set maj :", maj)

A={}
print("set A :", A)

B={1,2,3,4,5,3,7,1,6,8,7,9}
print("set B :", B)

print(type(B))

print(" max : ", max(B)) # Элементи калонтаринро мебарорад 

print("min :", min(B)) # Элементи хурдтаринро мебарорад

print("sum :", sum(B)) # Суммаи элементихоя мебарорад

print("sorted :", sorted(B)) # БО ТАРТИБ элементхоя мебарорад

print("all (A): ", all(A)) # True
print("all (B): ", all(B)) # True

print("any (A): ", any(A)) # Мачмуъ холи бошад  false
print("any (B): ", any(B)) # Мачмуъ пур бошад True

maj.add(8) # Илова кардан як элемент
print("set.add :", maj)

maj.update(["salom",10,11]) # Илова кардани якчанд элемент
print("set.apdate: ", maj)

maj.discard("salom") # Якто элементаша хоричкардан(удалит)
print("set.discard :", maj)

maj.remove("ali") # Якто элементаша хоричкардан(удалит)
print("set.remove: ", maj)

maj.pop() # Якумин элементаша хоричкардан(удалит) 
print("set.pop: ", maj)

maj.clear() # Мачмуро хамаи элеменхояшро хорич мекунад
print("set.clear :", maj)
