# Obiettivo
La funzione consente la pianificazione dell'audit legando ad un codice di progressivo audit i codici di progressivo griglia che costituiscono i punti di verifica dell'audit

## Formato di richiesta

![CQ_AUDT_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM60/CQ_AUDT_10.png)
Inserire : 
 - il tipo di griglia;
 - il settore, l'ente a cui è destinato l'audit che in generale nella fase di immissione della lista di riferimento viene lasciato vuoto dato che può essere rivolta a più enti dell'azienda, a più fornitori, ecc..

## Formato di dettaglio

![CQ_AUDT_11](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM60/CQ_AUDT_11.png)
Si definiscono : 
 * la data pianificata per fare l'audit;
 * l'ente richiedente l'audit;
 * I campi "Costi" ed "Azioni correttive" permettono all'operatore di interrogare i costi e le azioni correttive che audit effettuati in precedenza hanno fatto emergere per tutti i progressivi griglia del tipo griglia e del settore selezionato. Facendo riferimento all'esempio fino ad ora analizzato interrogando questi campi si sarebbe potuto selezionare i progressivi griglia del tipo griglia PRO relativi al settore L02.
 * Il campo "Stato" specifica se l'audit è già stato gestito o meno.
 * Il campo "Legami"  specifica per l'audit con numero progressivo PRO200800001 quali sono le righe che costituiscono la griglia.
 * Il campo "Risultati" è disponibile in fase di Gestione dello scadenzario e serve per interrogare i risultati della verifica ispettiva

Il Q9000 per la scelta della lista di riferimento permette di : 
 - collegarsi con gli audit precedenti per copiarne la griglia;
 - collegarsi con l'archivio delle liste di riferimento;

Nelle figure seguenti è illustrata la scelta dei punti della griglia accedendo all'archivio delle liste di riferimento : 
![CQAUDT_017](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM60/CQAUDT_017.png)
Il Q9000 per identificare la lista di riferimento da aggiungere riporta : 
 * il codice del progressivo griglia
 * il livello di modifica
 * il codice delle tre chiavi selezionate in fase di immissione (codice 1, codice 2, codice3) della lista di riferimento e specifica con "nuovo" se lo quel punto non è  già presente sulla griglia (inizialmente quando la griglia è vuota saranno tutti in questo stato), e con "attivo" se già presente.

![CQAUDT_018](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM60/CQAUDT_018.png)
Con l'opzione 1 si selezionano le 'n' liste di riferimento che costituiscono i punti dell'audit, alla fina della selezione F6 per aggiungere i punti audit : 

![CQAUDT_019](http://localhost:3000/immagini/MBDOC_OGG-P_CQUM60/CQAUDT_019.png)