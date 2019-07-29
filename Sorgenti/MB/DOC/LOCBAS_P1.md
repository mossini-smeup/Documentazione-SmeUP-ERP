# Sviluppi modulo base (J1-GRA-BAS)
Il modulo comprende : 
- Il modulo di comunicazione con As/400
- Il modulo grafico di base che gestisce
  . utenti
  . le finestre, il loro richiamo e la comunicazione tra i vari moduli Java e non.
- Gli oggetti grafici di base come
  . la finestra di selezione di un oggetto
  . il preview di funzione
  . il carrello
  . il setup ecc.

## Versione 1 (04 ottobre 2004)

- Introdotto il meccanismo fi funzioni multiple su oggetti multipli.
  Casi possibili : 
  . Lista di funzioni da applicare sequenzialmente ad un singolo oggetto.
  . Funzione singola da applicare sequenzialmente ad una lista di oggetti.
  . Lista di funzioni da applicare sequenzialmente ad ognuno degli oggetti di una lista di oggetti.

## Versione 2 (13 ottobre 2004)

- Modificata la finestra di ricerca nell'esecuzione del funzioni con campo aperto (-). Ora viene richiesto il solo oggetto da immettere.

- Nuova gestione oggetti operativi As/400 attestata su IBM operation navigator. E' ora possibile gestire stampanti, spool di stampa,lista lavori e messaggi utente
attraverso l'integrazione in LoocUp di alcuni moduli operativi del programma
Operation Navigator. Per fruire di queste utilità è necessario installare sul proprio
PC il prodotto IBM Operation Navigator for iSeries, fornito gratuitamente con
il sistema operativo OS400.

- Corretto errore su passaggio da tabella in scheda a foglio Excell o a tabella esterna.

- Modificata la gestione dell'emulatore 5250 all'interno di LoocUp. Il tasto ESC che
prima avviava il modulo di emulazione telnet 5250 è stato disabilitato ed è stata
aggiunta una nuova voce sotto il menù "servizi-servizi AS400". All'avvio, l''emulazione
5250 si ferma alla pagina di signon e preimposta l'utente e la password agli stessi valori
di quelli usati per collegarsi con Looc.Up. In fase di signon non viene più eseguito alcun
programma RPG.

## Versione 3  (14 ottobre 2004)

- Corretto errore su richiesta esterna di funzioni di tipo EDT. Prima venivano accettate
solo richieste di tipo *EDTLET e rifiutate tutte le altre.

- Corretta gestione delle funzioni e oggetti preferiti. La lettura del XML viene ripetuta ad
ogni apertura del carrello per garantire che l'utente veda sempre la situazione aggiornata.
Evita problemi nel caso utenti diversi operino contemporaneamente sullo stesso carrello
condiviso.

## Versione 4 (10 dicembre 2004)

- Nella finestra principale, all'interno dei tab delle funzioni e degli oggetti preferiti è stata
inserita una icona che attiva direttamente la finestra di gestione dei preferiti. L'attivazione
avviene con un singlo click sull'icona (o è meglio un doppio click?)
- Corretto il meccanismo del cambio dell'ambiente. In precedenza il cambio dell'ambiente
operava correttamente solo su code estese (e processi correlati) ma non funzionava
sulle code di emulazione 5250. Ora il cambio ambiente funziona correttamente ma
richiede una SMEDEV aggiornata almeno al 26 novembre 2004. In conseguenza delle
modifiche effettuate, il numero massimo di emulazioni 5250 attivabili contemporaneamente
è passato da 30 a 25.
- Eliminata dalla parte di comunizazione tutta la parte di cancellazione/creazione
di code. Il Client di LoocUp non crea o cancella mai code, ma si limita a richiedere
all'AS/400 questo tipo di operazioni e registrarne il risultato.

## Versione 5 (17 dicembre 2004)

- Modificata attivazione menù di gestione dei preferiti da tabbedpanel.
Ora l'attivazione avviene per doppio click sulla icona posta nella
linguetta del tabbed pane.

## Versione 6 (10 gennaio2005)

- Modificata la gestione del popup. Se viene richiesto per oggetti di
tipo J1-PATHFILE, J1-PATHDIR o J1-PCCMD viene inserita in testa al
popup una voce che consente l'apertura dell'oggetto puntato. Quindi,
nel caso J1-PATHFILE verrà aperto il file (con il programma di gestione
registrato sul sistema operativo), nel caso J1-PATHDIR verrà aperta
la directory con explorer e nel caso J1-PCCMD verrà eseguito il
comando DOS associato all'oggetto.

## Versione 7 (20 gennaio 2005)

- Inserita la possibilità di avviare Loocup con un modulo diverso
dal modulo "albero dei menù". Il modulo da avviare come primo
modulo è determinato dal contenuto del XML letto in fase di avvio
del sistema. Nel caso il primo modulo sia un modulo esterno Delphi
la terminazione di Loocup si ottiene con la pressione del tasto F12
sulla prima finestra. Verrà attivato anche in questo caso la gestione
del tasto F23 per la chiusura.

- Gestione del campo NOTIFY nella stringa di funzione. Se la
funzione contiene un campo NOTIFY(xyz), il modulo ad essa
associato viene avviato in modo che sia in grado di notificare al
chiamante la sua chiusura. In pratica, quando il modulo chiamato
dalla esecuzione della funzione ha terminato il suo lavoro notifica
al chiamante la fine della transizione passando la stringa xyz nella
notifica di UNDO. Attraverso questo meccanismo è possibile
avviare un modulo funzione e fare in modo che il modulo chiamante
senta la fine del modulo chiamato e reagisca di conseguenza. Il
caso tipico è il refresh di un modulo alla fine di una operazione di
modifica eseguita da un altro modulo.

## Versione 8 (25 gennaio 2005)

- Inserito nel menù "Servizi" la voce "Scheda del programma sorgente"
che rilancia la scheda relativa al programma RPG che ha
generato il file XML passato al modulo grafico corrente. Per
ora la funzone è attiva per i soli moduli Java, andrà estesa
anche ai moduli esterni.

## Versione 9 (28 gennaio 2005)

- Spostato il menù di "Scheda del programma sorgente" dal menù
servizi al menù di help. La voce di menù ha assunto la nuova descrizione
"Scheda servizio" ed è stata collegata alla scheda dell'oggetto OJ-*PGM
definito nel campo "Servizio" presente nella sezione "Service" del file
XML del modulo.

- Inserito nel programma principale la nuova gestione messaggi.
Il gestore dei messaggi filtra le chiamate XML su coda e visualizza i messaggi
definiti all'interno del file XML letto. Nel menù "Servizi" della finestra principale
è invece possibile aprire il gestore dei messaggi e gestire in grafica i messaggi
attuali e precedenti.

- Gestione messaggi di vario tipo :  informativi, di conferma, di scelta tra opzioni e di tipo G30.

## Versione 10 (1 febbraio 2005)

- Corretto preview di funzione per eliminare il problema nel salvataggio nei
preferiti di una funzione. In precedenza veniva perso ogni riferimento all'oggetto
di riferimento, che veniva sempre impostato a **. Corretto anche il malfunzionamento
sulla modifica di una voce già preesistente.

## Versione 11 (10 febbraio 2005)

- Inserito la gestione dei nuovi oggetti "Funzione di Loocup" (oggetti di
tipo J1-FUNA, J1-FUNF, J1-FUNM).
- Modificata la finestra di ricerca degli oggetti per gestire i nuovi tipi di oggetto
- Modificata la finestra di Preview di funzione. La logica di questa finestra è stata
modificata da semplice preview a cruscotto di controllo per la costruzione sintattica e
semantica di una funzione. Per ora è gestito solo il controllo sintattico e il controllo
semantico di base (esistenza degli oggetti immessi nei singoli campi ma nessun
controllo sulle loro dipendenze).
- Esteso ObjectField per gestione nuovi oggetti e corretto alcuni errori presenti
sul controllo di esistenza dell'oggetto immesso.
- Estesa la classe UIFunctionDecoder per gestire i nuovi tipi di oggetti. Inserita
una nuova funzionalità per la decodifica e il controllo di una stringa intesa come
funzione di LoocUp.

## Versione 11 (15 febbraio 2005)

- Modificata la gestione del carrello delle funzioni per consentire la creazione
di una nuova funzione direttamente dal manager delle funzioni preferite.
- Completamento della gestione dei nuovi oggetti funzione.
- Corretto errore di visualizzazione del FunctionPreview quando veniva richiamato
da un oggetto UIObjectField. Esisteva un conflitto tra la finestra di ricerca di una
funzione e la finestrella gialla che mostra la storia delle chiamate associata al campo
di immissione.

## Versione 11.1 (16 febbraio 2005)

- Unificati i parametri dell'oggetto funzione in uno solo. I tipi oggetto J1-FUNF,
J1-FUNA e J1-FUNM sono stati unificati in J1-FUN
- Modificato il pannello di immissione di funzione (UIFunctionPreview) :  il campo
funzione è ora di tipo V3-ASE, sono state modificate le posizioni e le dimensioni dei
campi di immissione (ingranditi a sfavore dei campi di decodifica) per evitare il
taglio dei codici immessi.

## Versione 12 (5 marzo 2005)

- Inserito nuovo parametro SERVE£() nella struttura di funzione. Consente di
deviare la richiesta di XML da AS400 ad un server esterno. Il server esterno deve
essere interpellato come web service sotto protocollo HTTP.
- Prima implementazazione del nuovo motore di ricerca. Attivabile su tutti gli
ObjectField attraverso la pressione del tasto F5. Supporto di base degli schemi di
ricerca attraverso query.

## Versione 13 (25 Marzo 2005)

- Nuova gestione delle finestre modali di dialogo. Ora le finestre di dialogo non
sono bloccanti per tutto il sistema ma solo per la finestra padre che li ha generati.
Migliorata la gestione dei dialoghi richiesti direttamente dai moduli esterni Delphi : 
permangono però alcuni problemi con la gestione dei fuochi (non sempre il passaggio
del fuoco da finestra esterna Delphi a finestra Java funziona correttamente). La nuova
gestione delle finestre ha richiesto la modifica di un gran numero di programi e potrebbe
portare a qualche instabilità (per lo meno nella fase immediatamente successiva al
rilascio).

## Versione 14 (22 aprile 2005)

- Corretta la gestione dei fuochi delle finestre e introdotto nuovo meccanismo di gestione
 finalizzato al contenimento dei problemi di perdita del fuoco. Introdotta nuova libreria di
 gestione nativa DelphiFunctions.dll
- Unificato il meccanismo di gestione delle voci di menù. Ora il modulo base controlla il contenuto
dei menù sia della parte Java che della parte Delphi. L'esecuzione delle azioni associate al singolo
menù è stata centralizzata e sono state gestite tutte le eccezioni relative ad azioni per loro natura non
centralizzabili.

## Versione 15 (2 maggio 2005)

- (DF)Nuovo meccanismo di ricerca associato ai campi di immissione di oggetti Smeup. Il nuovo
 meccanismo è ancora in fase beta ed è attivabile sul campo di immissione attraverso la
 pressione del tasto F5. Non è ancora stato integrato nella parte di emulazione 5250.
- (DF)Nuova codifica degli oggetti di tipo colore. Il codice colore è ora del tipo J1-COL-RrrrGggBbbb
 con rrr, ggg e bbb un numero compreso tra 000 e 255. Sono stati definiti dei colori predefiniti
 che vengono identificatoi con un codice dinamico che inizia per D. (ad esempio D.WIN per indicare
 il colore di default per lo sfondo delle finestre di Windows).
- (DF)Migliorata la gestione della memoria per eliminare il fastidioso problema di memoria esaurita che si
 verificava con il richiamo multiplo dei componenti grafici più complessi. Inserito un meccanismo di
 rilascio della memoria non più necessaria e del suo riutilizzo per nuovi componenti.

## Versione 16 (9 maggio 2005)

- (DF) Corretta gestione della voce menù "Scheda servizio" che non funzionava quando richiamata dalla
parte Delphi.
- (DF) Inserito nello stack la registrazione alle chiamte ad un modulo esterno come istanza di un oggetto di
tipo NullActionPanel. La registrazione riporta sia la FunInputStructure che il file XML associato alla
funzione.

## Versione 17 (11 maggio 2005)

- (DF) Inserita a menu la possibilità di visualizzare il log di comunicazione java-Delphi

## Versione 18 (18 maggio 2005)

- (DF) Modificata la procedura di selezione degli ambienti disponibili per ovviare al
problema legato al tasto Annulla. In precedenza la selezione del tasto "annulla"
provocava l'uscita non controllata dal programma e la perdita di tutte le impostazioni
non salvate.
- (DF) Inserita la nuova funzione di cambio password su AS/400. E' disponibile come
voce del menù Servizi-Servizi AS400-Cambio password

## Versione 19 (19 maggio 2005)

- (DF) Corretto gestione dei colori di sistema. Sono stati allineati i colori disponibili a
quelli disponibili nei componenti Delphi in modo da unificare il significato dei colori.
- (DF) Migliorata la procedura di selezione dei colori di sistema. Il pannello di selezione
è stato migliorato e sono stati risolti i problemi di mantenimento della selezione che si
erano verificati nella versione precedente.

## Versione 20 (26 maggio 2005)


- (DF) Corretto errore di undo su preview di funzione. Se si attivava un preview di funzione da
un modulo Java non visibile, il client grafico andava in crash in occasione del primo F12.
- (DF) Inserito tasto di editazione dello script della query all'interno del nuovo dialogo per ricerca
oggetti.

## Versione 21 (7 giugno 2005)


- (DF) Inserito nel menù file la possibilità di avviare una nuova sessione di Loocup identica alla
attuale o diversa. E' inoltre possibile avviare una nuova sessione con un ambiente diverso da
quello attualelmente in uso (a patto che ci siano più ambienti a disposizione)
