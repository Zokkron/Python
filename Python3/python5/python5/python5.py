with open("text.txt", "r") as f:
    arthro = f.read()
arthro = arthro.split()
arthro = list(dict.fromkeys(arthro))
arthro = [word.strip(",").strip(".").strip("!") for word in arthro]
counter = 0
if len(arthro)!=0:  
    for b in range(len(arthro)):
        if len(arthro[b])>3:
            counter+=1
            arthro[b] = arthro[b][1:] + arthro[b][0] + "ay"
            print (arthro[b])
        if counter==0:
            print ("Kamia leksi pio megalh apo 3 grammata")