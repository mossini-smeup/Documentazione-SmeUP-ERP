# Obiettivo
Permettere la manutenzione dell'archivio che definisce le caratteristiche della risorsa, ed in particolare la sua disponibilità per ciascun giorno della settimana e per i 5 tipi di giorni particolari (che corrispondono ai codici 1-5 nell'archivio calendario annuale). Non è necessario descrivere le condizioni di ogni risorsa poichè in mancanza di tale definizione, l'applicazione passa a leggere le condizioni generiche legate alla risorsa '**'

# Dettaglio formati
## Formato guida

![B£DIR2_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR2/BXDIR2_01.png)
### Tipo risorsa
Codice controllato sulla tabella TRG. Si rinvia a tale tabella per ulteriori chiarimenti.
### Codice risorsa
Viene controllato sull'anagrafico opportuno, in funzione dell'oggetto definito per il tipo di risorsa scelto.

## Formato gestione

![B£DIR2_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR2/BXDIR2_02.png)
### Risorsa collegata
Codice del gruppo di risorse cui appartiene la risorsa che si sta definendo. E' anch'esso un codice risorsa. E' un dato facoltativo. Se presente, tutti gli altri dati della risorsa verranno reperiti da tale codice. Questo permette di definire una sola volta le caratteristiche di risorse 'simili'.
### Codici orario
Codici controllati sulla tabella OLG.

Abbiamo due gruppi di codici : 

- Codici standard per giorno della settimana. Definiscono il codice orario valido per la risorsa nel giorno quando non esistono eccezioni specifiche per data.
- Giorni speciali 1/5 Definiscono i codici orario da utilizzare quando nel calendario base sono definite le condizioni 1/5 per una data. I codici devono essere immessi tutti. Possono essere lasciati vuoti solo se si immette il codice risorsa collegata e se tutti gli altri campi sono vuoti.


## Numero risorse
Indica il numero di risorse disponibili. Si intende che le risorse sono uguali tra loro ed operano in parallelo (un esempio può essere il numero di operai addetti al montaggio) :  in questo modo si riduce il tempo richiesto per svolgere un'operazione. Se non si immette, viene assunto 1.

## Percentuale utilizzo
La percentuale definita per la risorsa in un giorno della settimana o per eccezione, viene trattata come una percentuale di efficienza. Potrebbe essere usata per descrivere una riduzione di produzione al lunedì perchè le macchine devono essere accese.

# TABELLE COLLEGATE

- TRG  =    Tipo risorsa gestita
- OLG  =    Orari lavorativi

