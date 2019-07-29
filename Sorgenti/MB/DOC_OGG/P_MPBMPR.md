## Manutenzione Budget
La manutenzione del budget è un'applicazione specifica che si appoggia sulla struttura dell'MPS ed è studiata per gestire le quantità di un piano di budget o di previsioni con funzioni di gestione delle
quantità periodiche, di distribuzione delle variazioni sulle quantità periodiche e di valorizzazione, utilizzando costi definiti oppure valori attribuiti direttamente in sede di valorizzazione (ci sono delle funzioni per valutare gli scostamenti tra le variazioni apportate e i dati origine).
L'attività inizia con la definizione di un piano (di budget o di forecast) e generalmente la periodicità utilizzata è di tipo mensile.
La funzione di manutenzione budget prevede di dare in input il piano e la vista : 

![MP_001_31](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_31.png)
## Colonna Periodo
Mostra i periodi del piano, viisualizzabili in formato GG/MM/AAA oppure con la descrizione del mese (la data visualizzata è quella del giorno iniziale del periodo).

## Colonna Riferimento
Per la colonna "Riferimento" deve essere fatto un discorso particolare :  la colonna riferimento è uno degli elementi utilizzati dal sistema per distribuire le quantità nei periodi del piano.
Possiamo avere diversi riferimenti e richiamarli di volta in volta in base alle necessità.
I riferimenti possono anche essere costruiti partendo da fatti storici (es. :  totale venduto), impostando un carattere qualsiasi nel campo immediatamente a destra della testata "Riferimento" (in questo modo il sistema copia i valori presenti nella colonna Origine portandoli nella colonna Riferimento).
Quindi, partendo da una situazione in cui nella colonna origine sono già presenti dei valori : 

![MP_001_32](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_32.png)
basta semplicemente mettere un carattere qualsiasi nel campo del riferimento per riportare gli stessi valori dell'origine : 

![MP_001_33](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_33.png)
Con questa operazione si visualizzano nel campo riferimento i dati memorizzati nella vista piano in input, a fronte di Codice 1 / Codice 2.
Questi valori di riferimento possono essere memorizzati e richiamati in un secondo momento, se è stato inserito il carattere di ricerca "!" nel campo a destra della testata riferimento per far apparire la
finestra delle memorizzazioni multiple per utente : 

![MP_001_34](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_34.png)
Con la procedura standard si memorizzano i valori del riferimento e, sempre secondo lo standard, possono essere poi richiamati mettendo nel campo il codice della memorizzazione assegnata (in questo caso "A").
Un secondo metodo per memorizzare i valori di riferimento è copiarli da un'altra vista piano o da altri codici della stessa vista, usando il carattere di ricerca "!" oppure "?".
Il sistema presenta la seguente finestra dove inserire piano / vista / codice 1 / codice 2, da cui copiare i dati.

![MP_001_35](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_35.png)
La colonna riferimento serve per la disitribuzione di una quantità globale inserita manualmente, secondo la stessa distribuzione esistente nella colonna riferimento.
Un esempio di applicazione è nella definizione del budget delle vendite, per dare al nuovo budget la stessa distribuzione calcolata sul consuntivo dell'anno precedente applicandola al nuovo volume complessivo stabilito.

## Colonna Origine
Presenta i dati esistenti al momento, nella vista in esame. Su questa colonna (e di conseguenza sul piano) possiamo riportare i valori presenti nella colonna "Risultato" (F6 per copiare i valori risultato in origine).

![MP_001_36](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_36.png)
## Colonna Risultato
È la colonna dove compaiono in prima battuta i valori del nuovo budget, che possono essere creati con vari metodi, compreso quello manuale.
Quando l'insieme dei valori soddisfa le necessità, questi valori vengono fissati con il comando F6 nel piano / vista / codice 1 / codice 2 presenti nella testata dello schermo.
I vari metodi di creazione dei valori della colonna si possono vedere inserendo un carattere qualsiasi nel campo immediatamente a destra della testata "Risultato" : 

![MP_001_37](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_37.png)
La funzione >ADD (Sommare) crea i nuovi valori della colonna "Risultato", sommando il valore inserito nella finestra di lancio a una delle colonne "Risultato" / "Origine" / "Riferimento", in base
alla scelta utente.

![MP_001_38](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_38.png)
La funzione >SUB (Sottrarre) crea i nuovi valori della colonna "Risultato",  sottraendo il valore inserito nella finestra di lancio a una delle colonne "Risultato" / "Origine" / "Riferimento", in base alla scelta utente.

La funzione >MUL (Moltiplicare) crea i nuovi valori della colonna "Risultato", moltiplicando il valore inserito nella finestra di lancio ad una delle colonne "Risultato" / "Origine" / "Riferimento", in base alla scelta utente.

La funzione >DIV (Dividere) crea i nuovi valori della colonna "Risultato", dividendo per il valore inserito nella finestra di lancio una delle colonne "Risultato" / "Origine" / "Riferimento", in base alla
scelta utente.

La funzione >VAR (Variare) crea i nuovi valori della colonna "Risultato", applicando la variazione percentuale pari al valore inserito nella finestra di lancio a una delle colonne "Risultato" / "Origine" / "Riferimento", in base alla scelta utente.

La funzione >DIS (Distribuire) crea i nuovi valori della colonna "Risultato", distribuendo il valore inserito nella finestra di lancio secondo una delle seguenti regole : 
 * in funzione dell'origine (utilizzando la colonna "Origine" come curva di distribuzione);
 * in funzione del riferimento (utilizzando la colonna "Riferimento" come curva di distribuzione);
 * in funzione del peso di periodo (utilizzando come curva di distribuzione il peso relativo dato dal numero dei giorni lavorativi di ogni periodo);
 * in funzione del numero periodi.

La funzione >RIP (Ripresa) riporta nella colonna "Risultato" i valori presenti nella colonna "Origine" o in quella "Riferimento", in base alla scelta utente.

## Colonna Totali
Nella colonna totali è possibile valorizzare le quantità presenti nella colonna Risultato, riprendendo un Tipo/Livello Costo ( la presentazione può essere Periodica o Cumulativa con un valore fisso) : 

![MP_001_39](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_39.png)
## Colonna Scostamento
Lo scostamento viene determinato secondo i seguenti parametri di calcolo, impostati di volta in volta dall'utente : 

![MP_001_40](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_40.png)
il risultato complessivo assume una rappresentazione come da esempio seguente : 

![MP_001_41](http://localhost:3000/immagini/MBDOC_OGG-P_MPBMPR/MP_001_41.png)