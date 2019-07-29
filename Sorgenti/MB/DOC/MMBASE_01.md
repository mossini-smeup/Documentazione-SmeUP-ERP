# Anagrafici e dati di base
Sono tutte le informazioni necessarie ad una corretta pianificazione degli interventi programmati.

## Anagrafico impianti
Permette la manutenzione dei dati caratteristici di una macchina o impianto soggetto a manutenzione, ad ogni apparecchiatura gestita in questo anagrafico è associato un tipo (tabella MMT) che ne definisce la caratteristiche i riferimenti e le eventuali informazioni aggiuntive non contenute nell'anagrafico impianti.

![MMAM10D](http://localhost:3000/immagini/MMBASE_01/MMAM10D.png)Per un impianto l'applicazione può visualizzare un cruscotto riepilogativo con le informazioni che ciascun cliente ritiene più significative, un esempio è il seguente : 

![SK_IM](http://localhost:3000/immagini/MMBASE_01/SK_IM.png)
## Distinta componenti di un impianto
Un impianto può essere a sua volta costituito di altre apparecchiature di cui si vuole gestire la manutenzione (ciascuna di queste apparecchiature potrà essere codificata nell'anagrafico impianti).

In funzione della definizione del tipo impianto possiamo avere una gestione canonica di distinta base oppure una gestione particolare, appositamente dedicata alla manutenzione impianti.

![BRDI01L](http://localhost:3000/immagini/MMBASE_01/BRDI01L.png)Nel caso si voglia costruire una distinta di oggetti eterogenei (articoli, impianti, oggetti non codificati, ...) si deve utilizzare la gestione specifica della manutenzione.

## Tipo intervento
È una classificazione degli interventi contenuta nella tabella MMI, rappresenta la regola da utilizzare per calcolare la successiva data di intervento.
Nella tabella è contenuto il codice "Cadenza intervento" a cui è associata la regola da richiamare.
_7_Nota bene, la regola può essere una di quelle predefinite in Sme.up oppure può essere una regola specifica eseguita da un programma cliente.

![TA_MMI_MMF](http://localhost:3000/immagini/MMBASE_01/TA_MMI_MMF.png)
## Codice intervento
È la descrizione standard dell'intervento nella tabella MMO, contiene dei parametri che condizionano l'attività di attribuzione di un intervento ad un impianto : 

![TA_MMO](http://localhost:3000/immagini/MMBASE_01/TA_MMO.png)
## Attribuzione interventi ad un impianto
Con questa funzionei è possibile impostare le varie tipologie di interventi che vengono effettuate sugli impianti, nonchè i dati tramite i quali estrarre le previsioni degli interventi futuri : 

![MMA12G](http://localhost:3000/immagini/MMBASE_01/MMA12G.png)
il processo parte da un impianto, poi richiede di selezionare prima il tipo intervento, poi il codice intervento, quindi si presenta il formato di dettaglio dove si compilano le informazioni caratteristiche del gruppo di interventi per lo specifico impianto : 

![MMA12D](http://localhost:3000/immagini/MMBASE_01/MMA12D.png)
_7_Nota :  ad un intervento può essere associata una procedura. La procedura può essere un documento della Qualità gestito in Q9000 (modulo DOCU :  documentazione) oppure un commento associato direttamente attraverso la funzione "GC" delle note strutturate.

## Attribuzione materiali ad un gruppo di interventi
Per ogni intervento codificato è possibile associare l'elenco dei materiali che verranno impiegati nell'intervento. L'associazione può essere fatta direttamente dal formato guida attraverso l'opzione  "MA", oppure dal formato di lista, sempre con l'opzione "MA" : 

![MMA12L](http://localhost:3000/immagini/MMBASE_01/MMA12L.png)Con l'opzione 01 si aggiungono nuovi materiali che, in funzione della tipologia materiali scelta (tab MMM), possono essere sia codificati che non codificati, nella mappa di dettaglio si inserisce la qtà prevista e si possono inserire i dati del fornitore preferenziale : 

![MMA13D](http://localhost:3000/immagini/MMBASE_01/MMA13D.png)