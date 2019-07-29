# Obiettivo

Identificare un codice oggetto a partire da una o più parole.

## Dati di input

* £K40I_FU/ME :  Funzione/Metodo
** "   " :  Ricerca
*** "   " :  Ricerca ovunque, ma al primo posto in cui ho dei risultati mi fermo
*** "LIN" :  Ricerca solo in descrizioni estese
*** "ALI" :  Ricerca solo negli alias
*** "SQL" :  Ricerca solo nell'archivio intestato all'oggetto (nei campi codice/descrizione)
*** "G40" :  Ricerca solo tramite la scansione della £G40
*** "ALL" :  Ricerca ovunque. A differza del metodo blank non ci si ferma al primo posto che produce un risultato
** "ALI" :  Funzioni archivio alias
*** "AGG" :  permette di aggiungere un alias
*** "SOS" :  permette di sostituire un alias
*** "RIC" :  Ricerca da alias (dato l'alias ritorna l'oggetto)
*** "OGG" :  Ricerca da oggetto (dato l'oggetto ritorna l'alias)
*** "NOR" :  Ricerca da alias (data la stringa normalizzata ritorna l'oggetto)
** "NOR" :  Normalizzazione
*** "STR" :  Normalizza una stringa, ritorna la stringa in versione normalizzata
*** "CLS" :  Esegue la scrittura/aggiornamento della stringa normalizzata di tutte le istanze di una classe.
** "RAT" :  Ritorno Rating di un codice/descrizione
*** "   " :  Dati in input un codice o una descrizione ed una descrizione di confronto restituisce il rating di corrispodenza fra la seconda descrizione e la descrizione del codice o la prima descrizione passata.

* £K40I_TP :  Codice del Tipo oggetto in cui si vuole eseguire la ricerca
* £K40I_TD :  In alternativa al precedente campo è possibile passare una stringa, che verrà utilizzata per identificare il tipo oggetto
* £K40I_DE :  E' la stringa che viene utilizzata per identificare l'istanza
* £K40I_CD :  codice istanza. E' utilizzata per le funzioni ALI e RAT.
* £K40I_DI :  sulla funzione RAT mi permette di dire qual'è la stringa rispetto a cui calcolo il rating.

* £K40I_PA :  è possibile passare una serie di parametri aggiuntivi, attraverso la sintassi codiceparametro(valoreparametro). Questo l'elenco dei codici ed il loro significato : 
** MRI :  Forza una particolare forma di ricerca della parola (di defautl le fa tutte). Può avere i segenti valori : 
*** I :  inizia per
*** P :  contiene la parola con spazio avanti e diestro
*** C :  contiene la parola come sottostringa
** OAT :  in corrispondenza con il successivo parametro OAV permette di applicare un filtro ai risultati in base al valore di un'oav dell'istanza trovata. Il parametro OAT permette di definire quale codice OAV si vuole utilizzare.
** OAV :  in corrispodenza del precedente parametro permette di definire quale valore deve risultare dall'oav definito al precedente punto perchè l'istanza risulti valutata nell'elenco dei risultati.
** RIS :  se diverso da blank, attiva una risalita tale per cui, in presenza di risultati a 0, venga tolta l'ultima parola e ricalcolato il risultato.
** CTP :  se diverso da blank, attiva un controllo tale per cui se la parola di filtro o di risultato sono meno lunghe di 3 o la prima parola del filtro non coincide esattamente, il risultato viene escluso.
** DEN :  solo se diverso da blank, parte la ricerca anche se non viene passato alcuna stringa di ricerca.


