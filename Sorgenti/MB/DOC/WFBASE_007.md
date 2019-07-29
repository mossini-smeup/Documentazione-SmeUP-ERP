# INTRODUZIONE GENERALE

La struttura di un ordine xxx, istanza di un processo yyy (tabella WFA), viene specificata in uno script, individuato con le seguenti regole : 

- Lo script viene inizialmente cercato come membro xxx  del file sorgente SCP_WFA_F1 (questa funzione è da approfondire, per ora non è utilizzata).
- Se assente si risale al membro yyy nel file sorgente SCP_WFA.
- Se assente si risale al membro zzz nel file sorgente SCP_WFA, dove zzz è il gruppo processo definito nella tabella del processo yyy.


# STRUTTURA DELLA RETE

La definizione del processo è centrata sulla dichiarazione delle sue transizioni, che saranno convertite in impegni da eseguire e in attività nel corso dell'esecuzione.
Per ogni transizione (TRA) vanno definiti : 

- I luoghi in ingresso alla transizione (tag FROM).
- I luoghi in uscita alla transizione (tag TO).
- (opzionale) Il programma di dichiarazione / presa in carico dell'esecuzione della transizione (tag DIC, PRC).
- (opzionali) Le azioni esterne eseguibili dall'utente contestualmente all'esecuzione della transizione (tag EXT).
- (opzionali) Le conseguenze automatiche dell'esecuzione della transizione (tag CSG.EXT).


# CONSIDERAZIONI SULLE ISTRUZIONI

Per una spiegazione dettagliata degli attributi consultare il wizard nell'editor grafico ed i relativi help di campo.

## LUOGHI

I luoghi sono definiti all'interno del tag FROM se sono in ingresso alla transizione, TO se in uscita.
Deve essere definito almeno (ma non necessariamente uno) luogo iniziale; la presenza di luoghi finali non è indispensabile (lo è per chiudere gli ordini di workflow :  un ordine viene chiuso quando TUTTI i luoghi finali hanno il token).

## REQUISITI

Una transizione è pronta se sono soddisfatti sia i requisiti sui luoghi sia i requisiti esterni.

### Requisiti sui luoghi

Se non impostato si assume implicitamente un and-join (tutti i luoghi precedenti devono avere il token).
Può essere specificata, nel tag FROM, una di queste modalità alternative : 

- Requisiti sui luoghi in OR (Tip="O") :  basta che un luogo precedente abbia il token.
- Requisiti sui luoghi in X-OR (Tip="X") :  solo un luogo precedente deve avere il token
- Programma (Tip="P", Pgm="NomePgm) :  si passa la schiera dei luoghi con i rispettivi token :  il programma decide se rendere pronta la transizione. Può implementare exclusive-or, oppure requisiti particolari (ad esempio a maggioranza :  se ci sono cinque luoghi precedenti, basta che tre abbiano il token).


### Requisiti esterni

I requisiti esterni rendono pronta una transizione in base alla situazione del mondo esterno.

Si può impostare uno dei seguenti requisiti : 

- Programma :  si esegue un programma, a cui si passa la transizione, che ritorna se essa è attivabile.
- Condizione :  si controlla una condizione :  se è verificata la transizione è attivabile.

Per l'esposizione delle variabili utilizzabili in una condizione riferirsi all'opportuna sezione.

## CONSEGUENZE

Dopo l'esecuzione di una transizione (attività) vengono eseguite le conseguenze associate alla transizione.

### Conseguenze sui luoghi

Definiscono i luoghi in cui si mette il token dopo che una transizione è stata eseguita.
Se non impostata la modalità di assegnazione dei token si assume implicitamente l'and-split (TUTTI i luoghi successivi ricevono il token).
Si può, in alternativa, impostare una delle due seguenti modalità nel tag TO : 

- Programma (Tip="P") :  si esegue un programma, in cui si impostano i luoghi in cui mettere il token. E' cura di chi realizza il programma di assicurarsi che venga scritto almeno un token, per non mandare in stallo il processo.
- Condizioni (Tip="C") :  il luogo o i luoghi in cui mettere il token vengono scelti in base a delle condizioni specificate nel seguito.


Nel caso di conseguenza con condizioni, essa può essere automatica (eseguita dal motore di workflow all'avanzamento) oppure manuale (ogni condizione rappresenta un'opzione per l'utente, che ne sceglie da 1 a n).
Esempio di selezione automatica di condizioni : 
   ;;TO Tip="C"
   ;;WHN Con="Condizione 1 ........"
     ;;LUO Val="CodiceLuogo 1"
     ;;LUO Val="CodiceLuogo 2"
   ;;WHN Con="Condizione 2 ........"
     ;;LUO Val="CodiceLuogo 3"
   ;;OTH
     ;;LUO Val="CodiceLuogo 2"
     ;;LUO Val="CodiceLuogo 4"
Si imposta una struttura di selezione :  TUTTE le condizioni WHN che sono verificate vengono selezionate; in assenza di condizioni valide si prende la strada dell'OTH, obbligatorio.
Un luogo può essere presente più di una volta, in diverse condizioni.
Nell'esempio il luogo 2 è attivato dalla condizione 1 e dall'OTH.

Le conseguenze sui luoghi vengono valutate dopo aver eseguito le conseguenze esterne, quindi è possibile utilizzare nelle loro condizioni valori di OAV che sono stati modificati da queste ultime.

Per quanto riguarda la selezione manuale, bisogna impostare la keyword Sst nell'istruzione TRA. A questo punto si enumerano le scelte possibili da parte dell'utente con la WHN, impostando nel campo Con soltanto un'enumerazione di valori (1, 2, ...).

### Conseguenze esterne

Le conseguenze esterne (facoltative) permettono di codificare le azioni "cieche" sul mondo esterno che vengono eseguite all' esecuzione di un'attività o di un passaggio di stato signifcativo.
Si possono assimilare al flusso di inserimento dell'attività stessa; a differenza di quest'ultimo, la selezione delle azioni è più flessibile, in quanto è possibile condizionare in modo strutturato le azioni da eseguire.

Deve essere presente inzialmente il tag che definisce che la parte sottostante è una conseguenza esterna (;;CSG.EXT), con il relativo parametro che indica il tipo di conseguenza (ATT/PRC/DIC...). Questo va seguito da un blocco di flusso, per specificare le funzioni da eseguire (si veda più avanti).

## DICHIARAZIONE/PRESA IN CARICO/DISTRIBUZIONE/ASSEGNAZIONE

È possibile impostare il programma che esegue la dichiarazione dell'attività che esegue la transizione, con la sintassi ;;yyy.xxx, dove yyy vale DIC nel caso di dichiarazione di esecuzione, PRC nel caso di presa in carico, e dove xxx rappresenta il tipo di azione da eseguire (attualmente è implementato il valore FUN, per lanciare programmi funizzati o servizi)
Esempio :  ;;DIC.FUN Fun="A(Programma;Funzione;Metodo) P(Parametri)

Nel caso di programmi funizzati viene passato in chiave 1 l'impegno che si sta trattando (Oggetto di tipo F2), mentre in chiave 2 il tipo di azione (dichiarazione o presa in carico).
Nel caso di chiamate a funzioni di Looc.up viene passato in chiave 1 l'impegno che si sta trattando, mentre lo specificare il tipo di azione è lasciato alla funzione / metodo di chiamata del servizio.

Se non è stata impostato questo tag, si assume come default il programma WFATT_01 a struttura funizzata, a cui viene passato in modo automatico, nella funzione, il tipo di dichiarazione (es. ;;DIC.FUN Fun="A(WFATT_01;DIC))
Ovviamente è possibile definire un tag di presa in carico e non uno di esecuzione, o viceversa.
In questi casi viene assunto il default per il tag mancante.

## AZIONI ESTERNE

Le azioni esterne permettono di codificare le azioni sul mondo esterno che possono essere eseguite contemporaneamente allo svolgimento di un'attività.
Deve essere presente il tag che definisce che la parte sottostante è una serie di azioni esterne (;;EXT), seguito da un blocco di flusso, per specificare le funzioni da eseguire (si veda più avanti).

NB :  le azioni esterne POSSONO essere eseguite dall'utente DURANTE un'attività, le conseguenze esterne VENGONO eseguite automaticamente AL TERMINE dell'attività!

## BLOCCHI DI FLUSSO
Un blocco di flusso descrive un insieme di funzioni, che il motore di workflow lancia (nel caso di conseguenze esterne) o presenta all'utente (nel caso di azioni esterne).
Sono previsti sia tag di definizione funzioni sia tag di selezione.

### Tag di definizione funzioni.
Si utilizzano per descrivere le azioni che verranno eseguite (;;AZI.xxx), dove xxx rappresenta il tipo di azione da eseguire; attualmente è implementato il valore FUN, per lanciare sia programmi funizzati che funzioni Looc.up.
In questo caso la sintassi completa è ;;AZI.FUN Fun="A(Programma;Funzione;Metodo) 1(...) ... 6(...) P(Parametri)" Cls="zzz",
dove zzz è la classe di esecuzione, utilizzata solo nel caso di azioni esterne (serve alla scheda di impegno per decidere rappresentare un'azione come scheda o pulsante).

In chiave 1 viene passato, di default : 

- l'impegno (F2), se l'azione è esterna o di dichiarazione (sotto i tag EXT o xxx.FUN).
- l'attività (F4), se l'azione è una conseguenza esterna (sotto il tag CSG.EXT).

Nel codice 2 viene passato, di default : 

- Il tipo di azione (ASS, PRC, DIS, DIC), se l'azione è di dichiarazione.
- Il tipo di conseguenza esterna, intesa come stato (ASG, PRO) o attività (ATT, ASS, PRC, DIC, DIS), nel caso di conseguenza esterna.
- niente, nel caso di azioni esterne.

Se nella definizione delle azioni nello script viene definito qualcosa di diverso negli oggetti 1 e 2 questo ha la precedenza rispetto alle informazioni sopra descritte.

Il parametro P e gli oggetti da 3 a 6 sono sempre lasciati a disposizione dell'utilizzatore per passare parametri liberi.

### Tag di condizione
Si utilizzano per impostare condizioni sull'eseguibilità su insiemi di azioni (condizioni IF, le azioni tra l'IF e l'ENDIF solo eseguite solo se la condizione è valida).
Il modo di passare le informazioni dall'istanza di workflow alla condizione sono gli OAV dell'attività o dell'impegno, che possono essere aggiornati (ad esempio come parametri) dalla dichiarazione dell'attività stessa.

Nel caso di conseguenze esterne le azioni vengono eseguite nella sequenza in cui sono codificate :  in tal modo è possibile condizionare le azioni successive. Nel caso di azioni esterne è l'utente che sceglie quali azioni eseguire e in che ordine.

Se un'azione richiede un'informazione a video che viene poi memorizzata, e se essa è raggiungibile tramite OAV di variabili, la si può inserire in una condizione di selezione di un IF successivo all'azione eseguita.
A questo proposito gli OAV utilizzati nelle condizoni, vengono 'rinfrescati' ad ogni lettura, dato che è stata utilizzata la modalità di rilettura forzata degli attributi ad ogni nuovo richiamo (anche se relativi all'ultimo oggetto trattato).
