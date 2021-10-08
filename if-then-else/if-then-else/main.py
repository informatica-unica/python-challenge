# questa e' la vera password dell'utente
pwd = "1234"

# legge da tastiera il nome dell'utente
print ("inserisci il tuo username: ");
username = input();

# legge da tastiera la password dell'utente
print ("ciao, " + username + ", adesso inserisci la password: ");
pwdIn = input();

# controlla se l'utente ha inserito la password corretta

if pwdIn == pwd:
    # la password inserita e' corretta
    print (username + ", la tua password e' corretta");
else:
    # la password inserita e' sbagliata
    print (username + ", hai inserito la password sbagliata!");
    print ("Da questo momento sarai bannato a vita!");

