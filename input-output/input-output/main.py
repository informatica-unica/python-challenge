# Questo programma illustra tre costrutti di programmazione:
# assegnamento: come memorizzare un valore in una variabile
# input: come leggere un valore da tastiera (e memorizzarlo in una variabile)
# output: come scrivere un valore sulla console

# Dichiaro una variabile colorePreferito, e ci memorizzo il valore "fuxia"
# Il valore "fuxia" e' una sequenza di caratteri. 
# Le sequenze di caratteri in informatica si chiamano "stringhe"
# L'operazione di memorizzare un valore ad una variabile si chiama "assegnamento"
colorePreferito = "fuxia"

# Stampo il colore preferito sulla console
# usando l'operatore + per concatenare due stringhe 
# (ad esempio, "bisc" + "otto" = "biscotto")
print ("Il tuo preferito e' il " + colorePreferito)

# Adesso assegno il nuovo valore alla variabile colorePreferito...
colorePreferito = "vinaccia"

# ... e stampo il nuovo colore preferito sulla console
print ("No, mi sbagliavo! Il tuo preferito e' il " + colorePreferito)

# stampa "come ti chiami" sulla console
print ("come ti chiami? ");

# legge una stringa da tastiera
# e la assegna alla variabile "nome"
nome = input();

# stampa un messaggio di saluto. L''operatore + concatena due stringhe
print ("ciao, " + nome);

# stampa un'altra domanda sulla console
print ("quanti anni hai? ");

# Adesso vorrei leggere un numero da tastiera, 
# ma la funzione input() legge solo delle stringhe.
# Posso convertire la stringa in un numero intero usando l'operatore int(...)
anni = int(input());

# In questo modo, la variabile anni contiene un numero
# Posso stampare questo numero con il comando print,
print(anni)

# ...ma non posso concatenare un numero ad una string (provare a togliere il commento per vedere l'errore)
# print("hai inserito: " + anni)

# Adesso stampo un insulto
# Per concatenare anni ad una stringa, devo prima convertirlo in una stringa:
# str(anni) e' la conversione del valore numerico memorizzato nella stringa anni in una stringa
print (nome + ", hai " + str(anni) + " anni, ma li porti male!");

# Siccome anni e' un numero, posso farci delle operazioni aritmetiche
# Ad esempio, ci aggiungo 15, e assegno il nuovo valore alla variabile anni
anni = anni + 15

# Concludo con una ulteriore offesa
print ("In realta' sembra che tu abbia " + str(anni) + " anni.");
