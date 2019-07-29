# Funzioni generali
Il modulo V5STAT utilizza anche delle funzioni generali : 
 * l'interrogazione di dettaglio delle righe scelte, che sfrutta le funzioni fornite dalla scheda LOA13 per presentare una estrazione SQL dei dati.
 * il filtro generalizzato sui record di un archivio, che sfrutta le funzioni fornite dalla scheda Q3 a cui si rimanda per la documentazione di dettaglio

# Filtro Q3
## Generalità
Il filtro è uno strumento che dà la possibilità di scegliere un determinato insieme di record relativamente ad un archivio. Mentre i parzializzatori classici prevedevano la necessità di creare un diverso programma per ogni archivio, il filtro è una funzione generica che può essere applicata a qualsiasi archivio od oggetto applicativo che faccia riferimento ad un archivio. Inoltre è da sottolineare come il filtro non abbia una validità limitata alla singola schermata, ma una valenza a livello di sessione utente. Questo significa che se si imposta un filtro sull'archivio degli articoli, tale filtro non è limitato alla singola schermata (ad esempio alla singola matrice), ma resta valido anche per altre schermate che utilizzino il filtro sullo stesso oggetto.

L'oggetto filtro è anche presente nella nuova scheda dell'oggetto file.

![B£BASE_023](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_023.png)
# Scheda filtro Q3
La scheda del filtro si presenta come segue : 
![B£BASE_024](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_024.png)
La scheda è divisa i 3 sottoschede : 
 * La sezione "**E/*JOB**" , è relativa al filtro attivo per il lavoro in corso (*JOB). In questa sezione abbiamo la __forma normale__, che presenta i campi maggiormente utilizzati nei filtri (per impostare questi campi è necessario intervenire nei file di configurazione della navigazione - SCP_NAV), la __forma tecnica__, che presenta tutti i campi possibili del file
 * La sezione "**Gestione memorizzazioni**" , è relativa alla gestione delle memorizzazioni multiple di diverse impostazioni di filtro (rifarsi alle memorizzazioni multiple dei parzializzatori)
 * La sezione "**Analisi**" , è dedicata alla presentazione delle istruzioni SQL impostate nel filtro

## Sezione *JOB
La sezione è relativa al filtro attivo per il lavoro in corso (*JOB), per semplicità di esposizione faremo riferimento alla forma normale :  la forma completa segue le stesse regole di compilazione : 
![B£BASE_025](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_025.png)
* Nella prima colonna viene presentata la lista dei campi del file
* La seconda e la terza colonna sono i "Da" a "A" delle vecchie parzializzazioni e rappresentano il limite inferiore e il limite superiore del filtro. Valgono le regole consuete : 
** valore "Da" = blank e valore "A" = * (asterisco) si assumono i limiti massimi (es. da zero a infinito)
** valore "Da" è compilato e valore "A" = blank si assume il valore "A" uguale al valore "Da"
** valore "Da" = blank e valore "A" compilato si assume il valore "Da" uguale al minimo possibile (es. zero)
** nei campi da / a sono attive le ricerche "!", "?", "/"
* Nella colonna "Lista inclusi" si può indicare una lista di oggetti da includere nel filtro. Le ricerche "!" o "?" permettono di vedere e selezionare una delle liste esistenti (per la gestione delle liste vedere paragrafo specifico :  Gestione Liste Inclusi / Esclusi)
* Nella colonna "Lista esclusi" si può inserire una lista di oggetti da escludere nel filtro
* La colonna "Operatore" permette di attribuire un operatore SQL al filtro. Sono attive le ricerche "!" o "?" per la scelta dell'operatore
* La colonna "Condizione" associa una condizione all'operatore inserito nella colonna precedente (es. GT  12345). Sono attive le ricerche "!" o "?" o "/" per la scelta della condizione. Nel caso l'operatore sia "LS" o "LN" (lista di inclusione e lista di esclusione) nella condizione si indicano N. valori separati dal punto-e-virgola  ";" (nota bene, gli N. valori devono essere separati solo dal punto-e-virgola,  non ci devono essere spazi bianchi)

Tutte le selezioni possibili con le varie colonne vengono elaborate in "AND".

Quando viene eseguita una selezione su una riga, questa assume uno sfondo di colore diverso nella prima colonna : 

![B£BASE_026](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_026.png)Sul basso della scheda sono presenti dei bottoni la maggior parte dei quali con utilizzo intuitivo o aderente allo standard Looc.UP. Una menzione particolare per : 
 * **F6 =Conferma**, conferma le selezioni eseguite e le attribuisce al lavoro corrente dell'utente (*JOB)
 * **F16=Pulisci filtro**, sbianca tutte le impostazioni di selezione precedentemente eseguite
 * **F19=Pulisci campo**, sbianca tutte impostazioni della riga selezionata

### Gestione liste inclusi / esclusi
Con questa funzione si possono costruire o modificare liste di oggetti da utilizzare nei filtri come "inclusi" o "esclusi". Le liste possono essere "statiche" (es. lista di codici ente) oppure "dinamiche" (es. tutti i clienti della provincia di Brescia).
Per attivare la gestione liste mettere un carattere di ricerca ("!" o "?") nel campo inclusi o esclusi : 
![B£BASE_031](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_031.png)viene presentato l'elenco delle liste attualmente presenti : 
![B£BASE_033](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_033.png)per creare una nuova lista, usare l'opzione 01, viene presentato un formato di selezione del tipo lista : 
![B£BASE_034](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_034.png)selezionato il tipo lista (es. per attributi del cliente) viene mostrato un formato dove inserire il nome e la descrizione della nuova lista : 
![B£BASE_035](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_035.png)inserire nome e descrizione e premere F6 per selezionare gli attributi da utilizzare, esce il secuente formato dove inserire gli attribuiti ed i codici di filtro : 
![B£BASE_036](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_036.png)confermare con F6 e selezionare la lista appena creata

## Sezione Gestione memorizzazioni
![B£BASE_027](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_027.png)Attraverso le "Azioni" permette di lavorare sulle memorizzazioni dei filtri
 * Creare un nuovo filtro
 * Salvare con un nome il filtro selezionato
 * Eliminare il filtro attivo
 * Attivare un filtro
 * Sbiancare il filtro selezionato
 * Eseguire il filtro attivo e visualizzare il risultato in matrice

![B£BASE_028](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_028.png)
Se viene selezionato il "Salva con nome" compare la seguente scheda di impostazione del salvataggio : 

![B£BASE_030](http://localhost:3000/immagini/MBDOC_SCH-Q3/BXBASE_030.png)**Filtro personale**, di default è attivo e se selezionato salva il filtro solo ad uso esclusivo dell'utente, mentre se non è selezionato salva il filtro ad uso di tutti gli utenti.

Le azioni di "**Documentazione**" mostrano le selezioni del filtro in forma di matrice o di stringa SQL.

Il **set'n play - scheda con navigazione** apre la scheda del filtro nella versione precedente
Il **set'n play - 5250** apre la gestione in lista del filtro in modalità emulazione
