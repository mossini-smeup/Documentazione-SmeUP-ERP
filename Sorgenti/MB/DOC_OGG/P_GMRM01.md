# Generalità
Le richieste di movimentazione sono gli strumenti utilizzati da Sme.up nelle applicazioni di Logistica Avanzata in cui si vuole spingere la movimentazione non solo allo spostamento tra aree di magazzino ma anche fino all'utilizzo delle ubicazioni multiple per articolo o alla gestione delle prenotazioni di materiale.
Le richieste di movimentazione possono venire anche utilizzate per la pianificazione delle missioni di movimentazione all'interno dei magazzini oppure l'ottimizzazione dei percorsi o come supporto per l'interfaccia con sistemi di magazzino automatico.
Nella richiesta di movimentazione vengono registrate le domande che l'ambiente logistico esterno porta al magazzino in termini di articoli, quantità da prelevare e distribuire o da immagazzinare e data richiesta.
Le richieste di movimentazione sono il supporto informatico su cui appoggiare i programmi di applicazione delle regole di ottimizzazione dei versamenti e prelievi ed il supporto operativo per la gestione delle risorse interne al magazzino.
Nella configurazione pi- estesa le richieste di movimentazione sono costituite di :  una testata, che riporta i dati logistici della richiesta (ordini di vendita, ordine di produzione, cliente, ) tante righe, una per ogni articolo, quantità, data richiesta.


# Testate Richieste Movimentazione
La testata delle richieste di movimentazione contiene le informazioni di carattere generale della lista a cui è associata.
Il tipo di informazioni contenute nella testata viene definito dal "Tipo Documento di Movimentazione" che è tabellato nella tabella GMO, in questa tabella si definiscono i 3 oggetti caratteristici della richiesta di movimentazione : 

- _2_oggetto di generazione, da cui la richiesta di movimentazione è stata generata
- _2_oggetto di origine, da cui la richiesta di movimentazione trae origine
- _2_oggetto di destinazione, a cui la richiesta di movimentazione è destinata


Nella tabella GMO si definiscono anche il numeratore e il tipo riga assunto.
La gestione delle testate richieste di movimentazione ricalca gli standard Sme.up (formati guida, lista, parzializzazioni, dettaglio).

## Formato dettaglio

![GM_02_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMRM01/GM_02_01.png)
# Righe Richieste Movimentazione
Nelle righe richieste di movimentazione sono gestite le quantità di articoli da movimentare, le date richieste e le informazioni di origine e destinazione.
Alle righe delle richieste di movimentazione vengono abbinate, sia per la parte di origine che per la parte di destinazione, le relative causale e chiavi di giacenza, cosicché quando la richiesta viene applicata, automaticamente vengono lanciati i due movimenti di scarico e carico.

![GM_02_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMRM01/GM_02_02.png)
Nella normalità quando la riga viene creata i dati chiave dell'origine e della destinazione non sono completamente compilati, altri programmi di elaborazione successiva (cfr. paragrafo Azioni su Richieste Movimentazione) si occupano del trattamento delle righe, compreso il completamento dei dati origine e destinazione.
Se la riga richiesta di movimentazione proviene da un documento gestionale (ordine produzione o documento ciclo attivo/passivo) nella riga vengono riportati i riferimenti al documento origine.

![GM_02_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMRM01/GM_02_03.png)
Per l'esecuzione di particolari attività (es. attribuzione ubicazione e versamento a magazzino) sono previste richieste di movimentazione di sole righe.
La ragione è essenzialmente pratica, in questi casi esistono richieste di movimentazione create temporaneamente (per permettere l'esecuzione dell'attività, dopo vengono cancellate automaticamente) e con una sola riga, è inutile quindi creare contestualmente anche la testata.

# Azioni su Richieste Movimentazione
Sulle richieste di movimentazione possono essere eseguite diverse attività, una parte di queste sono di carattere generale e interessano tutti i clienti dove sono implementati processi di logistica avanzata, una seconda parte riguarda applicazioni specifiche del cliente e vengono realizzate con programmi specifici.
Le attività più significative connesse alle richieste di movimentazione sono : 

- _2_assegnazione, collegata al versamento o al prelievo, attraverso l'attivazione di regole specifiche definisce in quale ubicazione versare il materiale oppure da quale ubicazione eseguire il prelievo
- _2_esecuzione, è l'applicazione della richiesta di movimentazione :  vengono lanciati i movimenti connessi allo scarico dalla giacenza origine e al carico nella giacenza destinazione

Le azioni sulle richieste di movimentazione  possono essere lanciate di massa, su tutte le righe appartenenti ad una testata : 

![GM_02_06](http://localhost:3000/immagini/MBDOC_OGG-P_GMRM01/GM_02_06.png)
oppure ad una singola riga : 

![GM_02_07](http://localhost:3000/immagini/MBDOC_OGG-P_GMRM01/GM_02_07.png)
_3_Nota; allo stesso formato video di gestione attività di picking sulle righe si arriva anche dal formato guida con l'opzione EZ

Per applicare l'azione ad una riga si utilizza il campo Opzione, i valori possibili sono condizionati allo stato della riga (es. se la riga è già assegnata una delle opzioni possibili sarà la disassegnazione, mentre l'assegnazione non sarà ammessa).

Sono previsti dei comandi funzione che possono agire sui campi opzione e quantità di ciascuna riga : 

- _2_Tasto F15 = Ripetizione; serve per ripetere un'opzione su tutte le righe sottostanti,
- _2_Tasto F17 = Residuo; trasporta il valore presentato nel campo di lista Residuo nel corrispondente campo Qtà fisica.
- _2_Tasto F20 = Esecuzione + residuo; forza l'opzione ES su tutte le righe e contemporaneamente trasporta il valore presentato nel campo di lista Residuo nel corrispondente campo Qtà fisica


## Assegnazione (AS)
Con il termine di "assegnazione" si intende assegnare, nel senso più ampio, una ubicazione ad una richiesta di movimentazione.

Abbiamo i 2 casi : 

- _2_assegnazione al versamento, l'attività principale è la scelta dell'ubicazione, nella richiesta di movimentazione settore destinazione vengono modificati o confermati  Causale, Area, Tipo giacenza, Codice 1,2,3,4 con i dati chiave in base alla giacenza di destinazione.
Nel versamento il sistema crea in automatico delle richieste di movimentazione per guidare il versamento stesso, sulla richiesta di movimentazione c'è il riferimento all'attività collegata (Tabella GMH) che indirizza verso le azioni dell'opportuno sottosettore della tabella GMK dove sono descritte le regole del motore inferenziale per la scelta ubicazione di versamento.

- _2_assegnazione al prelievo, (detta anche allocazione) l'attività principale è determinare se esiste giacenza disponibile, prenotare la quantità disponibile splittare la richiesta in caso di quantità insufficiente e ripetere la ricerca per la quantità residua. Vengono modificati o confermati  Causale, Area, Tipo giacenza, Codice 1,2,3,4 con i dati chiave in base alla giacenza di origine.

Nel prelievo attraverso il meccanismo dell'attività collegata e del motore inferenziale il sistema ricerca le ubicazioni da cui eseguire il prelievo, se trova quantità disponibile prenota (alloca) la quantità voluta, se la quantità della richiesta è superiore allora splitta un 2 la richiesta originale (una richiesta corrispondente alla quantità allocata, la seconda per la quantità residua) e ripete la ricerca per la quantità residua.
Sia nel caso del versamento che in quello del prelievo, se esistono le informazioni di destinazione nella richiesta di movimentazione viene incrementata anche la quantità attesa nella destinazione.
Se, dopo l'assegnazione di prelievo, rimangono delle richieste di movimentazione non soddisfatte queste si definiscono "mancanti", si può attivare così un processo di urgenza e destinazione veloce dei materiali mancanti quando questi diventano disponibili.
## Elimina assegnazione (DS)
Riporta indietro la situazione a prima dell'assegnazione.
## Esecuzione (ES)
É l'attività di applicazione di una richiesta di movimentazione, con la quale si eseguono i movimenti associati alla richiesta cioè si scarica l'origine e si carica la destinazione.
## Elimina esecuzione (EE)
Riporta indietro la situazione a prima dell'esecuzione.
