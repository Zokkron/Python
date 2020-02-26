ar = int(input("Eisagete enan arithmo: "))
if len(str(ar)) == 16:
    _str = str(ar) #χρησιμοποιω την μεταβλητη _str για να μετατρεψω ενα object σε ενα string
    sum = 0
    for n in range (len(_str)):
        x = ar % 10
        ar = ar % 10
        if 1 % 2 == 1:
            x = x * 2
            if x > 9: #αν το ψηφιο της μεταβλητης χ ειναι μεγαλυτερο του 9 τοτε προσθετουμε τα 2 μελη του αριμθου χρησιμοποιωντας το div και το mod
                x = x % 10 + x // 10 
                sum = sum + x
            result = sum % 10
    if result == 0:
        print ("O arithmos einai egkyros")
    else:
        print ("O arithmos den einai egkyros")
else:
    print ("O arithmos den periexei 16 psifia")