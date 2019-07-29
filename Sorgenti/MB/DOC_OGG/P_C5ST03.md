## Obiettivo
Attraverso questa funzione è possibile ottenere la stampa del prospetto relativo alla liquidazione periodica dell'IVA. La stampa può essere eseguita sia in modalità provvisoria che definitiva.

## Formato guida
La schermata del formato guida si presenta nel seguente modo : 

![C5C020_025](http://localhost:3000/immagini/MBDOC_OGG-P_C5ST03/C5C020_025.png)
Vediamo in dettaglio le voci che compaiono al suo interno : 

- Ultima stampa registri. Presenta la data di ultima stampa definitiva dei registri IVA.
- Ultima stampa liquidazione. Presenta la data di ultima stampa definitva della liquidazione IVA.
- Periodo liquidazione. Indica se la liquidazione è di tipo mensile o trimestrale (è un'informazione riportata tra i parametri fissi aziendali).
- Elaborazione mensile. In questo campo è necessario indicare il periodo da elaborare (mese o trimestre).
- Tipo stampa. Indica la modalità con cui verrà eseguita la stampa; le opzioni disponibili sono : 
-- P, Provvisoria :  è l'opzione presentata di default e può essere eseguita n volte
-- D, Definitiva :  può essere eseguita una sola volta per ogni periodo. Questa modalità aggiorna la data di Ultima stampa liquidazione ed esegue il calcolo definitivo del credito/debito da riportare nel periodo successivo.
-- R, Ristampa :  è utlizzata nel caso in cui si voglia stampare la liquidazione di un periodo già stampato in modo definitivo, può essere eseguita n volte.
- Formato di stampa. Permette di definire il tipo di output desiderato. Le opzioni disponibili sono spool di stampa e file PDF.
- Intestazione. Permette di inserire un'intestazione all'interno della stampa che riporta o meno i dati societari completi (partita IVA e sede legale).
- Stampa per settore. Vista la possibilità di codificare registri IVA per settore di attività, la stampa liquidazione può essere ottenuta, se richiesto, separando i registri per questo parametro.
- Registro di riferimento.  Normalmente, la liquidazione IVA viene stampata numerando i fogli da 1 ogni periodo. Se si desidera, invece, accodare la stampa a  uno dei registri esistenti, è sufficiente specificarne il codice in questo campo :  la numerazione della liquidazione partirà dalla pagina n+1 a cui era terminato il registro prescelto dopo l'ultima stampa definitiva, e lo aggiornerà a sua volta. Ad esempio, se vogliamo accodare la stampa della liquidazione alla stampa del registro riepilogativo che ha codice R compileremo questo campo con R; in questo modo il numero pagina della liquidazione andrà in sequenza con il registro riepilogativo.
- Esecuzione registrazione giroconto.  Eseguendo la stampa definitiva, è possibile ottenere anche la scrittura contabile di giroconto, previa impostazione dei parametri necessari nella tabella delle registrazioni automatiche (C5U). Nel caso in cui si esegua invece la stampa provvisoria della liquidazione verrà prodotta una stampa con l'indicazione della registrazione che verrebbe generata al lancio definitivo.
E' possibile eseguire il giroconto senza effettuare controlli di quadratura (opzione 1),
oppure eseguendo prima i controlli di quadratura (opzione 2).
Con questa ultima opzione verrà stampato il dettaglio dei movimenti presi in considerazione per effettuare il giroconto e verrà calcolata la differenza tra i conti di acquisti e vendite definiti nella tabella delle registrazioni automatiche (C5U).
- Data. In questo campo è necessario inserire la data registrazione alla quale si desidera effettuare il movimento di giroconto di cui sopra, se richiesto.
- Variazioni di imposta :  Debiti. Consente di immettere un importo che il programma utilizzerà per aumentare il totale dell'IVA a debito calcolata nel periodo, e quindi intervenendo sull'importo da versare o da riportare nel periodo. Questo campo andrà, quindi, compilato solo nel caso in cui siano presenti debiti da riportare sulla stampa della liquidazione (dovrebbe capitare solo in caso di acquisizioni/incorporazioni di aziende oppure nel caso in cui vi venga riconosciuto un ulteriore debito IVA in seguito ad un accertamento dell'Agenzia delle Entrate).
- Variazioni di imposta :  Crediti. Consente di immettere un importo che il programma utilizzerà per diminuire il totale dell'IVA a debito calcolata nel periodo, e quindi intervenendo sull'importo da versare o da riportare nel periodo. Questo campo andrà, quindi, compilato solo nel caso in cui siano presenti dei crediti da riportare sulla stampa della liquidazione (dovrebbe capitare solo in caso di acquisizioni/incorporazioni di aziende oppure nel caso in cui vi venga riconosciuto un ulteriore credito IVA in seguito ad un accertamento dell'Agenzia delle Entrate).
- IVA non versata.  Si utilizza nel caso in cui, a seguito della liquidazione automatizzata, risultino dovute e non versate delle somme. Il campo consente di immettere un importo che il programma utilizzerà per aumentare il totale dell'IVA calcolata nel periodo, e quindi intervenendo sull'importo da versare nel periodo.
- Acconto IVA.  In questo campo è possibile riportare l'importo versato come acconto IVA. Il programma utilizzerà questo importo per diminuire il totale dell'IVA calcolata nel periodo, e quindi intervenendo sull'importo da versare o da riportare nel periodo.
- Credito IVA anni precedenti portato in detrazione. Nel caso in cui nel mese in elaborazione l'azienda sia a debito IVA e voglia utilizzare parte del credito residuo degli anni precedenti dovrà inserire in questo campo l'importo da utilizzare. Si sottolinea che in questo campo va inserito solo il credito IVA dell'anno precedente, mentre quello dell'anno corrente viene automaticamente compensato nella liquidazione periodica.
- Credito anno corrente chiesto a rimborso. Permette di indicare la quota di credito IVA maturata nell'anno corrente che si vuole chiedere a rimborso.
- Credito anno precedente chiesto a rimborso. Permette di indicare la quota di credito IVA maturata nell'anno precedente che si vuole chiedere a rimborso. Questo importo non avrà alcun effetto sulla liquidazione attuale ma verrà considerato nella liquidazione del periodo successivo andando a diminuire il 'Credito riportato da anno precedente'.
- Compensazione esterna (F24) su credito anno corrente. Identifica quella quota di credito IVA maturata nell'anno corrente che viene portata in detrazione all'interno dell'F24.
- Compensazione esterna (F24) su credito anno precedente. Identifica quella quota di credito  IVA maturata nell'anno precedente che viene portata in detrazione all'interno dell'F24.
- Estremi del versamento. Sono la data e le coordinate ABI-CAB mediante le quali si effettua il versamento nel caso di debito IVA per il periodo in chiusura.


### Tasti funzionali

- F06 Conferma. Permette di confermare la stampa della liquidazione
- F11 Parametri esecuzione. Permette di definire le impostazioni della stampa liquidazione (nel caso di PDF consente anche di definire il percorso di salvataggio del file e il nome del file stesso).


## Output di stampa
Vediamo ora nel dettaglio la stampa prodotta con la liquidazione IVA : 
![C5C020_026](http://localhost:3000/immagini/MBDOC_OGG-P_C5ST03/C5C020_026.png)![C5C020_027](http://localhost:3000/immagini/MBDOC_OGG-P_C5ST03/C5C020_027.png)
 La stampa si compone dei seguenti campi : 

- IVA acquisti. E' l'ammontare dell'IVA derivante da tutti i registri di tipo acquisto, fatta eccezione per quelli relativi agli acquisti Intracee e agli acquisti reverse charge.
- IVA acquisti CEE. E' l'ammontare dell'IVA derivante da tutti i registri di tipo acquisto IntraCee.
- IVA acquisti reverse. E' l'ammontare dell'IVA derivante da tutti i registri di tipo reverse charge.
- IVA non detraibile. E' l'ammontare dell'IVA acquisti indetraibile presente su tutti i registri.
- IVA acquisti per cassa da liquidare. E' l'ammontare dell'IVA per cassa da liquidare nel periodo.
- Totale IVA acquisti. E' l'ammontare totale dell'IVA derivante da acquisti del periodo in liquidazione.
- % Pro-rata. Viene reperita dai dati aggiuntivi Azienda.
- IVa detratta per il periodo. E' l'ammontare totale dell'IVA da detrarre per il periodo considerando la percentuale prorata impostata.

- IVA vendite. E' l'ammontare dell'IVA derivante da tutti i registri di tipo vendita, fatta eccezione per quelli derivati dai registri di acquisto Intracee o reverse charge.
- IVA debito su acquisti Cee. E' l'ammontare dell'IVA derivante da tutti i registri di debito ottenuti in copia da quelli di acquisto Intracee.
- IVA debito su acquisti reverse. E' l'ammontare dell'IVA derivante da tutti i registri di debito ottenuti in copia da quelli di acquisto reverse charge.
- IVA vendite per cassa da liquidare. E' l'ammontare dell'IVA relativa a fatture incassate nel periodo e quindi con IVA da liquidare.
- Totale IVA vendite. E' l'ammontare totale dell'IVA derivante da vendite del periodo in liquidazione.

- IVA corrispettivi. E' l'ammontare dell'IVA derivante da tutti i registri di corrispettivi (IVA a debito).
- IVA esigibile del periodo. E' il totale dell'IVA a debito, ovvero la somma di IVA vendite e IVA corrispettivi.

- IVA a debito o credito del periodo. E' il saldo IVA del periodo in liquidazione, differenza tra IVA detratta e IVA esigibile.

- Variazioni di imposta Debiti/Crediti. Riportano quanto immesso nei parametri di lancio della liquidazione, andando ad incrementare/decrementare l'importo da versare o da riportare a credito del periodo.
- IVA non versata. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a incrementare/decrementare l'importo da versare o da riportare a credito del periodo.
- Credito riportato da periodo precedente. Viene riportato l'eventuale credito scaturito dalla precedente liquidazione. Si sottolinea che in questo campo viene riportato solo il credito maturato nell'anno in corso.
- Acconto IVA. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a decrementare l'importo da versare o da riportare a credito del periodo.
- IVA a credito per il periodo. Viene riportato, se si verifica la condizione, l'importo del credito del periodo.
- Importo da versare per il periodo. Viene riportato, se si verifica la condizione, l'importo a debito del periodo.

- Interessi liquidazione. E' l'importo degli interessi da corrispondere in funzione di una liquidazione trimestrale/annuale.
- Totale con interessi. E' la somma dei due valori precedenti, nel caso di debito per il periodo.

- Credito anno precedente portato in detrazione. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a decrementare l'importo da versare o da riportare a credito del periodo.

- Importo da versare/a credito. E' il risultato finale della liquidazione.

- Estremi del versamento. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso si debba effettuare un versamento dovuto per debito IVA tramite banca.
- Credito anno corrente chiesto a rimborso. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato richiesto un rimborso (che verrà riportato come credito nel periodo successivo).
- Compensazione esterna (F24) su credito anno corrente. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato utilizzato il credito IVA dell'anno corrente per compensare altri creiditi (l'importo diminuirà il credito nel periodo successivo).


Nella seconda pagina della liquidazione è riportata la sintesi dei crediti precedenti e delle compensazioni : 

- Credito IVA dell'anno precedente : 
-- Credito IVA dell'anno precedente. Riporta il credito totale derivante da anni precedenti e utilizzabile in compensazione.
--- Compensazione interna già effettuata. Riporta l'importo totale utilizzato in compensazione interna nei periodi precedenti.
--- Compensazione esterna (F24) già effettuata. Riporta l'importo totale utilizzato nei periodi precedenti in compensazione esterna del credito IVA accumulato in anni precedenti.
--- Compensazione interna del periodo. Riporta l'importo totale utilizzato in compensazione interna nel periodo in elaborazione.
--- Compensazione esterna (F24) nel periodo. Riporta l'importo totale utilizzato in compensazione esterna nel periodo in elaborazione del credito IVA accumulato in anni precedenti.
--- Credito già chiesto a rimborso. Riporta il credito IVA chiesto a rimborso nei periodi precedenti.
--- Credito chiesto a rimborso nel periodo. Riporta il credito IVA chiesto a rimborso nel periodo corrente.
-- Credito IVA dell'anno precedente residuo. Riporta il credito IVA derivante da anni precedenti ancora da compensare.
- Utilizzo compensazione esterna in F24
-- Importo limite. Riporta l'importo massimo utlizzabile in compensazione in F24
-- Già effettuato. Riporta l'utilizzo effettuato nei periodi precedenti.
-- Utilizzo nel periodo. Riporta l'utilizzo nel periodo corrente.
-- Residuo. Riporta il valore residuo compensabile tramite F24.

