
# Obiettivo

Tramite questa funzione è possibile registrare le ricevute di accettazione, associandole al file XML inviato.
Per ricevuta di accettazione si intende l'identificativo dato dall'Agenzia Delle Entrate ove si comunica che il file è stato accettato senza errori o accettato con segnalazioni.


# Richiesta Parametri

* Tipo Elaborazione : 
**   - Acquisti e Vendite  - Verranno elencati i file relativi ad acquisti e vendite
** A - Acquisti            - Verranno elencati i file relativi agli acquisti
** V - Vendite             - Verranno elencati i file relativi alle vendite

* Data Iniziale :  Data iniziale dei file che si vogliono gestire

* Data Finale   :  Data finale dei file che si vogliono gestire

* Esito : 
** N - Non Ricevute        - Verranno elencati i file senza ricevute di accettazione
** R - Ricevute            - Verranno elencati solo i file con ricevute di accettazione
**   - Tutti               - Verranno elencati tutti i file

# ASSEGNAZIONE FILE XML E RICEVUTA DI ACCETTAZIONE
In fase di trasmissione ordinaria viene dato un nome al file XML. Questo file verrà evidenziato nell'elenco. Quando l'Agenzia Delle Entrate comunica che il file è stato accettato senza errori o accettato con segnalazioni allora usare l'opzione 02 (Modifica dati), inserire il nome file XML  e l'identificativo file presente nella ricevuta. Inserendo la ricevuta di accettazione i record interessati verranno identificati come definitivi. (i dati inclusi in questa ricevuta assumeranno nel campo "Stato Trasmissione" il valore  "2 - In definitiva").
Una volta inserita la ricevuta di accettazione non è possibile toglierla in questa gestione, ma è necessario fare l'annullamento in fase di trasmissione indicando "Idfile per annullamento intera comunicazione".
Qualora siano stati inviati più file e solo alcuni sono stati scartati, allora devono essere inserite le ricevute dei file accettati, modificare i dati errati, e fare la trasmissione. In fase di trasmissione vengono generati i file XML ove non è presente la ricevuta di accettazione.
