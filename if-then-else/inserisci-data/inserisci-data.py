m = int(input("Inserisci il mese: "))
g = int(input("Inserisci il giorno: "))
err = False

if m<0 or m>12 or g<1 or g>31:
	err = True
elif m==2 and g>28:
	err = True
elif ((m==4 or m==6 or m==9 or m==11) and g>30):
	err = True
	
if err:
	print("Data errata")	
else:
	print("Data corretta")
