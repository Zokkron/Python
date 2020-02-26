ar = int(input("Pliktrologiste enan arithmo: "))  
def f(y) #χρησιμοποιω αυτην την "συναρτηση" η αλλιως function ετσι ωστε να δεχεται καποιες συγκεκριμενες παραμετρους και να μου επιστρεφει το αποτελεσμα της ασκησης
    y = y * 3 + 1
    y = str (y)
    g = 0
    for k in range(len(y)):
        g = g + int(y[k])
    return g
rep = f(ar)
print(rep)
if rep >= 10:
    while rep >= 10:
        print (f(rep))
        rep = f(rep)