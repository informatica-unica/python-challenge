# Questo programma illustra il comando input. 
# Il comando input legge un valore inserito dall'utente digitando sulla console.
# Tale valore viene di solito memorizzato in una variabile tramite il comando di assegnamento, per poi riusarlo successivamente nel programma.

# legge una stringa da tastiera e la assegna alla variabile nome
# per terminare l'inserimento, premi il tasto invio sulla console
nome = input("Come ti chiami? ");

# stampa un messaggio di saluto. L'operatore + concatena due stringhe
print ("ciao, " + nome);

# stampa un'altra domanda sulla console
print ("Quanti anni hai? ");

# Adesso vorrei leggere un numero da tastiera, 
# ma la funzione input() legge solo delle stringhe.
# Posso convertire la stringa in un numero intero usando l'operatore int(...)
anni = int(input());

# Abbiamo gia' visto come trasformare un numero in una stringa,
# e come concatenare il risultato ad un'altra stringa.
# Adesso mettimo tutto insieme per stampare un insulto
print (nome + ", hai " + str(anni) + " anni, ma li porti male!");
