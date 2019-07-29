# Registrazione Vendite

## Registrazione Vendite

 :  : R03 Dal Menu Principale>Registrazione Vendite>Registrazione Vendite

La funzione permette di inserire manualmente le vendite effettuate in una determinata data e, per qualche motivo, mancanti a sistema o di normalizzare le vendite a reparto.
Può capitare che il pc cassa sia completamente fuori uso, quindi sia necessario l'utilizzo dei corrispettivi di emergenza (il negozio, ovviamente, dovrà conservare tutti i barcode degli articoli venduti).Può anche capitare che il sistema vada in errore, quindi stampi lo scontrino, ma non riesca a memorizzare la vendita.
Una volta ripristinato il normale funzionamento della cassa basterà lanciare la funzione Registrazione Vendite.
Inserire la data delle vendite e il codice cassa, nel caso di più postazioni e nel caso in cui questa operazione venga effettuata dalla postazione ufficio
Se alcune vendite sono state fatte normalmente, qui avremo l'elenco di quelle correttamente registrate a sistema

 :  : FIG RegistrazioneVendite

Premere F6=Inserisci
Verranno richiesti : 
 * Data= data della vendita, che il sistema propone in automatico da quella che abbiamo impostato nella maschera precedente
 * Cassa= la cassa in cui è stata efettuata la vendita
 * Codice a Barre
 * Qta
 * Prezzo=si riferisce al prezzo di vendita, quindi, se su un articolo abbiamo applicato uno sconto, dovremo correggere il prezzo a mano perchè in automatico verrà proposto il prezzo di listino
 * Tipo Vendita=permette di attribuire il codice di un tipo vendita speciale, in modo da poterne tenere traccia in caso di interrogazioni future (es. la vendita ad enti pubblici)
I tasti : 
 * F9=Modifica Ultima Riga permette di correggere l'ultimo articolo appena inserito, che è quello che appare in alto nella schermata di inserimento
 * F11=Automatico/Manuale permette di selezionare la modalità di inserimento della vendita
 ** Automatico :  in caso di inserimento tramite lettore di barcode è consigliabile selezionare questa modalità in modo da poter bippare i codici a barre uno dopo l'altro, senza dover nemmeno confermare
 ** Manuale :  consigliato quando vanno applicate modifiche ai prezzi di vendita e alle quantità. Bisogna poi premere Invio per confermare

Una volta inserite tutte le vendite mancanti, premere Esc=Indietro e verificare che nella barra in alto la QUantità del Totale Venduto e il relativo Importo Totale si siano aggiornate correttamente
I tasti : 
 * F4=Elimina permette di eliminare solo le vendite inserite manualmente, che si contraddistingono da quelle provenienti dalla cassa perchè non hanno alcun codice sotto la colonna Provenienza, mentre le altre hanno il codice 025
 * F8=Tutti/Esclusa Provenienza premuto una volta riporterà solamente le vendite SENZA Provenienza (quindi quelle inserite manualmente tramite la Registrazione Vendite). Premuto di nuovo visualizzerà tutte le vendite del giorno
 * F9=Totale Provenienza propone una maschera riassuntiva del Totale Venduto per Tipo di Povenienza

Le vendite inserite manualmente, quindi non effettuate normalmente tramite il programma di cassa, non verranno visualizzate all'interno della Visualizzazione Incassi Casse (vedi capitolo Visualizzazione Incassi Casse), ma nella Visualizzazione Incassi (vedi capitolo Visualizzazione Incassi) perchè questa interrogazione tiene conto di tutti i movimenti di magazzino.
