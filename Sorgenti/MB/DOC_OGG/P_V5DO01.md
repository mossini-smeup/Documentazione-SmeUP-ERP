# Obiettivo
Descrivere la gestione e la struttura generale di un documento, illustrare le caratterizzazioni principali (tipo documento, modello documento, tipo riga), spiegare le funzioni standard associate alle testate e quelle associate alle righe di un documento.

# Struttura di un documento
In Sme.up ogni documento, sia esso un ordine di vendita, un ordine di acquisto, una bolla di vendita, una bolla entrata merci, un contratto, una previsione, ecc. è costituito da una testata e da una o più righe.

Nella testata sono presenti i dati complessivi del documento (es. l'ente intestatario, quello di destinazione, quello di fatturazione e quello di conferma, i riferimenti commerciali, ecc..).

Nella figura seguente si vede un esempio di testata di un ordine di vendita : 

![V5_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_01.png)Nella riga sono presenti i dati caratteristici dell'oggetto e della transazione (es. articolo, quantità, data, prezzo, ecc.).


Nella figura seguente si vede un esempio di riga dello stesso ordine di vendita : 

![V5_01_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_02.png)Ogni testata è caratterizzata da : 

- _2_Tipo documento, identifica il documento come un ordine oppure una bolla, di acquisto o di vendita, ecc.
- _2_Modello documento, all'interno del tipo documento il modello rappresenta una ulteriore sottoclassificazione, ad esempio, all'interno degli ordini di vendita potremmo avere vendite Italia e vendite Estero, oppure negli ordini fornitori potremmo avere ordini di acquisto e ordini di conto lavoro. Non è obbligatorio definire modelli documento diversi, dipende dall'azienda e dal tipo di impostazione che si vuole dare.
- _2_Numero interno documento, è il numero che lo identifica (nel sistema la chiave è rappresentata da :  tipo documento + numero documento)
- _2_Numero Bolla / Numero Fattura, se il documento in questione è una bolla allora potremo avere anche il numero bolla (o numero DDT) che viene inserito in fase di registrazione entrata merci (bolle in entrata) o di stampa bolla (bolle uscita) se la bolla è fatturabile allora potremmo avere anche il numero di fattura inserito dalla fatturazione (bolle del ciclo attivo) o dal controllo fatture (bolle del ciclo passivo).

Ogni riga è caratterizzata da : 

- _2_Tipo / numero documento, quelli della testata a cui la riga appartiene
- _2_Numero riga, un  progressivo numerico che identifica univocamente la riga all'interno del documento
- _2_Tipo riga, definisce le caratteristiche della riga (se contiene articoli o se si tratta di una riga a valore, se è fatturabile o meno, se è di conto lavoro o di acquisto, se di entrata o di uscita, ecc.)

# Funzioni di testata documento
Tutte le testate documento hanno delle funzioni che sono proprie dell'oggetto testata e si possono attivare dal formato di dettaglio della testata con il tasto F10 : 

![V5_01_03](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_03.png)
## Lista campi
Presenta tutti i campi del record come sono memorizzati sul file : 

![V5_01_04](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_04.png)
di default vengono presentati solo i campi compilati, è possibile vedere anche i campi vuoti.

## Tabelle collegate
Presenta gli elementi di tabella collegati alla creazione del record : 

![V5_01_05](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_05.png)
## Sintesi documenti
Questa opzione premette di accedere ad un cruscotto dove sono compattate una serie delle principali visualizzazioni del documento, molte di queste visualizzazioni sono anche accessibili da altre opzioni richiamabili dalle funzioni di testata o dalle funzioni estese (vedi) : 

![V5_01_06](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_06.png)
## Sintesi conti spese tasse
Presenta, in funzione dell'opzione scelta, varie informazioni di carattere contabile e finanziarioassociate al documento, l'opzione ALL presenta in successione tutte le precedenti : 

![V5_01_07](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_07.png)
Di seguito un esempio di visualizzazione dell'opzione IMP - Importi totali : 

![V5_01_08](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_08.png)
## Dettaglio date
Presenta le date significative della testata del documento : 

![V5_01_09](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_09.png)
## Parametri per tipo
Se alla testata documento, attraverso la customizzazione, è  stata attribuita la facoltà di gestire dei parametri aggiuntivi, questa opzione rimanda alla loro gestione (cfr C£PARA Parametri).
## Attributi
Presenta, in modo simile alla lista campi, tutte le informazioni associate all'oggetto in questione, ma oltre ai dati del record mostra anche altri attributi associati al record in manieradinamica (cfr B£OGAT Oggetto Attributo) : 

![V5_01_10](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_10.png)
## Numeri
Presenta i numeri (quantità, importi, misure, ecc..) che sono associati al documento : 

![V5_01_11](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_11.png)
# Funzioni aggiuntive di testata documento
Dalla testata, premendo il tasto F14, si apre una finestra di selezione di altre funzioni (aggiuntive) associate alla testata : 

![V5_01_12](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_12.png)
## Gestione date
Presenta la stessa visualizzazione vista nel 'Dettaglio date' precedente, in questo caso c'è anche la possibilità della modifica.
## Gestione righe
Presenta la lista delle righe del documento. La stessa cosa si ottiene con il tasto F7 dal formato di gestione della testata.
## Gestione commenti
Ai documenti è possibile associare delle note o commenti (cfr B£NOTE Gestione note), con questa funzione, se in fase di customizzazione al documento sono state associate delle note, si accede alla manutenzione : 

![V5_01_13](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_13.png)
## Interrogazione commenti
Vedi gestione commenti.
## Aggiornamento data consegna righe
Presenta una finestra contenente le date significative del documento; spuntando il campo apposito è possibile aggiornare tutte le righe come da testata.
## Riempio campi vuoti con dati anagrafici enti
Il documento ha una serie di campi che in fase di creazione vengono copiati dall'anagrafico enti, se successivamente cambia il documento o l'anagrafico, questa funzione aggiorna i campi vuoti del documento recuperandoli dall'anagrafico.
## Sostituisco campi con dati anagrafici enti
Vedi precedente.
## Confronto campi con dati anagrafici enti
Vedi precedenti, vengono presentati i campi diversi tra documento e anagrafico enti : 

![V5_01_14](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_14.png)
## Visualizzazione formato standard
Il numero di dati contenuti in una testata documento supera la possibilità di visualizzazione di un formato; normalmente si utilizzano formati ridotti di una o due finestre contenenti solo i dati più significativi per l'attività in questione.
Questa funzione serve per passare alla visualizzazione completa, dove le informazioni sono raggruppate per tipologia in quattro finestre.
Un caso particolare di utilità è quando si ha un messaggio di errore del tipo 'Errore nel campo non visualizzato' in questo caso si passa al formato standard e si scorrono (con INVIO) tutte le finestre fino a quando il campo in errore non viene evidenziato : 

![V5_01_15](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_15.png)
## Stampa / Prestampa / Ristampa documento
Permette di lanciare le funzioni di stampa del documento.
## Elenco informazioni
Vedi visualizzazione attributi.
## Funzioni ente
Passa alla gestione delle funzioni dell'ente intestatario (uguale alla pressione del tasto F10 dal formato di gestione enti).
## Gestione parametri impliciti
In un record di testata documento si hanno cinque campi alfanumerici e cinque campi numerici, liberi da utilizzare per la gestione di informazioni aggiuntive, questi campi sono definiti parametri impliciti perché la loro impostazione ricalca quella dei parametri esterni mentre sono fisicamente presenti sul record.
Se alla testata documento, attraverso la customizzazione, è  stata attribuita la facoltà di gestire i parametri impliciti, con questa opzione si attiva la loro gestione : 

![V5_01_16](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_16.png)
## Gestione flag testata
La testata documento prevede una serie di flag che ne determinano il comportamento oppure lo stato di avanzamento; alcuni di questi flag hanno un significato preciso e stabilito in fase di sviluppo del modulo, altri flag sono liberi a disposizione utente per gestioni specifiche.
Questa opzione permette la visualizzazione ed eventuale modifica : 

![V5_01_17](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_17.png)# F18 Destinazione estemporanea
In un documento c'è la possibilità di identificare un indirizzo di destinazione diverso dall'indirizzo del codice intestatario, normalmente questi indirizzi sono a loro volta codificati (potrebbe essere, ma non è obbligatorio, che abbiano anche un tipo ente specifico), in casi particolari invece è necessario spedire ad un indirizzo estemporaneo che allora non è codificato come un ente canonico.
Per coprire anche questi casi, dalla manutenzione testata, con il comando funzione **F18** si apre il seguente formato dove inserire l'indirizzo estemporaneo : 

![V5_01_17A](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_17A.png)
in questo formato, con  F8 si possono riprendere dall'anagrafico dell'ente interstatario alcune informazioni (es. zona, comune, regione, ....), si completano i dati della destinazione e relativo indirizzo e si salva con INVIO. Il sistema salva, con i dati inseriti in input, un codice (tipo documento + numero documento) nell'archivio BRENTI0F con il tipo ente specificato in tabella V51 al campo "Tipo ente spedizione documenti".
**Nota**, se in tab. V51 il tipo ente spedizione documenti è vuoto questa funzione non è attiva (esce un messaggio di errore).

# Funzioni di riga documento
Tutte le righe documento hanno delle funzioni che sono proprie dell'oggetto riga e si possono attivare dal formato di dettaglio riga con il tasto F10 : 

![V5_01_18](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_18.png)
## Lista campi
Analoga alla funzione di testata.

## Dettaglio quantità
Presenta le quantità significative della riga : 

![V5_01_19](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_19.png)
## Dettaglio date
Analoga alla funzione di testata.
## Tabelle collegate
Analoga alla funzione di testata.
## Sintesi documenti
Analoga alla funzione di testata, in questo caso si aggiungono delle funzioni tipiche della riga tra le quali quelle di conto lavoro, valide solo quando la riga è di un ordine oppure di una bolla di conto lavoro : 

![V5_01_20](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_20.png)
## Sintesi conti spese tasse
Analoga alla funzione di testata.
## Funzioni testata
Passa alla gestione delle funzioni della testata documento (uguale alla pressione del tasto F10 dal formato di gestione testata).
## Funzioni oggetto
Passa alla gestione delle funzioni dell'oggetto intestatario della riga, generalmente l'articolo, (uguale alla pressione del tasto F10 dal formato di gestione articoli).
## Ordine produzione origine
Se la riga è di conto lavoro può trattarsi di conto lavoro di fase (esternamente viene eseguita solo una operazione tra quelle previste dal ciclo di lavorazione, le altre sono eseguite internamente oppure presso altri terzisti).
Nel caso di conto lavoro di fase molto probabilmente esiste anche un ordine di produzione interna,in cui una delle fasi di lavorazione viene eseguita con la riga in questione.
Questa funzione permette di andare alla testata dell'ordine di produzione originale.
## Parametri per tipo
Analoga alla funzione di testata.
## Funzioni spedizioni riga
Si applica principalmente quando la movimentazione per le spedizioni viene eseguita utilizzando le richieste di movimentazione. Viene presentato uno stato avanzamento della riga : 

![V5_01_21](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_21.png)
## Righe derivate
Da un documento si possono derivare altri documenti, ad esempio se il documento è un ordine, da questo si possono derivare N. bolle di spedizione, oppure se il documento è un contratto quadro daquesto si possono derivare N. ordini di consegna da cui possono derivare N. bolle di spedizione, ecc.La funzione mostra le eventuali righe derivate dalla riga in esame.
## Dettaglio riga origine
Come la precedente con la differenza che si visualizza il dettaglio della riga origine.
## Risalita origini
Visualizza tutta la catena delle righe da cui questa è stata originata (es. dalla riga bolla, a quella dell'ordine, al contratto quadro).
## Attributi
Analoga alla funzione di testata.
## Numeri
Analoga alla funzione di testata.

# Funzioni aggiuntive di riga documento
Dal formato di dettaglio riga, premendo il tasto F14, si apre una finestra di selezione di altre funzioni (aggiuntive) associate alla riga : 

![V5_01_22](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_22.png)
## Gestione quantità
Presenta la stessa visualizzazione vista nel 'Dettaglio quantità' precedente, in questo caso c'è anche la possibilità della modifica.
## Gestione prezzo
Premette di controllare la differenza tra il prezzo (e relativa scontistica) applicato sulla riga e quello previsto dal listino ufficiale, eventualmente adeguando la riga al listino : 

![V5_01_23](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO01/V5_01_23.png)
## Gestione date
Analoga alla funzione di testata.
## Gestione commenti
Analoga alla funzione di testata.
## Interrogazione commenti
Analoga alla funzione di testata.
## Visualizzazione formato standard
Analoga alla funzione di testata.
## Elenco informazioni testata
Analoga alla funzione di testata (si presentano i dati della testata).
## Elenco informazioni riga
Analoga alla funzione di testata (si presentano i dati della riga).
## Gestione parametri impliciti
Analoga alla funzione di testata.
## Gestione flag riga
Analoga alla funzione di testata.
