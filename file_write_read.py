tagi = 'То тавони дустонро гум макун\nДустони мехрубонро гум макун\n1,2,3,4,5,6,7,8\n10,11,12,13,14,15,16,17,18,19'
# Navistan
with open('dars2.txt', 'w') as tp:
    tp.write(tagi)
    
# khondan fayl 
with open('dars2.txt', 'r') as tp:
    print(tp.read())
