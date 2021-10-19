# questa e' la vera password dell'utente
pwd = "1234"

# in questa variabile memorizzo il numero di tentativi errati dell'utente
# inizializzo questa variabile a 0 (all'inizio non ci sono tentativi errati)
tentativiErrati = 0

# legge da tastiera il nome dell'utente
print ("inserisci il tuo username: ");
username = input();

# legge da tastiera la password dell'utente, e la memorizza nella variabile pwdIn
print ("ciao, " + username + ", adesso inserisci la password: ");
pwdIn = input();

# controlla se l'utente ha inserito la password corretta
# usando il costrutto condizionale (if-then-else)

if pwdIn == pwd:
    # caso if: esegui i comandi qui sotto se la condizione pwdIn == pwd e' vera
    # l'indentazione e' importante!!!
    print (username + ", la tua password e' corretta");
else:
    # caso else: esegui i comandi qui sotto se la condizione pwdIn == pwd e' falsa
    # anche qui l'indentazione e' importante!!!
    print (username + ", hai inserito la password sbagliata, riprova:");
    
    # incremento il numero di tentativi errati
    tentativiErrati = tentativiErrati + 1
    
    # l'utente puo' fare un altro tentativo per inserire la password
    pwdIn = input();
    
    # controlla se stavolta la password e' corretta
    if pwdIn == pwd:
      print (username + ", la tua password e' corretta");
    else: 
      print ("Hai sbagliato di nuovo: da questo momento sarai bannato a vita!");
      # incremento il numero di tentativi errati
      tentativiErrati = tentativiErrati + 1

print ("Il numero di tentativi errati e' ")
print (tentativiErrati)
