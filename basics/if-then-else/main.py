pwd = "1234"

print ("inserisci il tuo username: ");
username = input();

print ("ciao, " + username + ", adesso inserisci la password: ");
pwdIn = input();

if pwdIn == pwd:
    # la password inserita e' corretta
    print (username + ", la tua password e' corretta");
else:
    # la password inserita e' sbagliata
    print (username + ", hai inserito la password sbagliata!");
    print ("Da questo momento sarai bannato a vita!");

