# Funzioni descrizioni estese
# Obiettivo
Raccogliere tutte le funzioni sulle descrizioni estese. In particolare : 
 * ricavare la migliore descrizione di un oggetto in una lingua
 * ottenere descrizioni come risultato di calcolo
 * accedere alla gestione

Per il dettaglio delle funzioni inserire "/" nel campo funzione.

## Funzioni
Per l'utilizzo delle desrizioni estese sono previste funzioni standard richiamabili all'interno dei programmi.
Queste funzioni si possono vedere e provare con la seguente videata : 

![C£DESC_03](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£8/CXDESC_03.png)Confermando con il tasto INVIO, si aprirà la lista delle funzioni previste e inserendo la barra / nel campo funzione si vedranno sia funzioni che metodi : 

![C£DESC_04](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£8/CXDESC_04.png)
## Lettura
La funzione consente di leggere le descrizioni di base ed estese associate ad un oggetto.
Ad esempio è possibile includere questa funzione nel programma di stampa di una bolla, di una fattura o di un ordine per fare in modo che, in caso il cliente o il fornitore sia straniero, la descrizione associata all'oggetto articolo venga stampata nella lingua corrispondente.
La lettura standard avviene in questo modo : 

![C£_DES_05](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£8/CX_DES_05.png)
Un altro possibile utilizzo è quello di un articolo configurato in cui una parte di descrizione è uguale per tutti gli articoli figli e un'altra è specifica per ogni articolo :  alla lingua ** associamo la descrizione di base e alla lingua "ITA" le descrizioni estese specifiche di ogni singolo codice articolo.
La lettura è eseguita mediante il metodo di risalita, che avviene secondo la definizione di una lingua primaria e una lingua secondaria.

![C£_DES_06](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£8/CX_DES_06.png)
# Elenco
Dato un oggetto, la funzione fornisce l'elenco delle descrizioni nelle varie lingue.
L'elenco può essere : 

- >Completo (viene fornito un elenco delle descrizioni estese e di base);

- >Ridotto (viene fornito un elenco delle descrizioni di base).


# Scansione
Dopo il posizionamento, viene scansionato il primo elemento della lista dei codici lingua, ordinati alfabeticamente.
Successivamente, viene effettuata, in modo sequenziale, la scansione delle descrizioni estese in lingua associate all'oggetto, secondo l'ordine alfabetico dei codici lingua della tabella LIN.

![C£_DES_07](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£8/CX_DES_07.png)
# Note particolari
 * Lettura con risalita; ottiene la descrizione ricercando una lingua primaria, in mancanza di questa una lingua secondaria. Se manca una descrizione specifica in una di queste lingue si verifica l'esistenza di un metodo di "calcolo della descrizione" e in questo caso lo si richiama. Se al termine non abbiamo nessuna descrizione utilizzeremo la descrizione standard dell'oggetto.
 * Calcolo di una descrizione; chiameremo descrizione calcolata quella ottenuta mediante il richiamo di uno specifico programma scritto dall'utente e che costruisce la descrizione mediante un algoritmo che compone la descrizione di particolari caratteristiche dell'oggetto stesso di cui si vuole la descrizione estesa.

Con l'applicazione viene fornito un prototipo di tale programma di nome C£LIN_00.
