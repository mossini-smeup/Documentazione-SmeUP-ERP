# Struttura delle Ricerche in Finestra

La struttura delle ricerche in finestra costituisce il principale esempio di impiego dei componenti forniti dalla struttura delle query.

# Struttura di Risoluzione di una ricerca

## 1) Ricerca Grafica o Ricerca in Emulazione?

* Tutto parte dal client, che in un campo di input, intercetta la richiesta di risoluzione di una ricerca (primo carattere corrisponde ai caratteri "!", "?", "+" o " : ")
* A questo punto viene lanciata la funzione di risoluzione della ricerca, corrispondente al valore della variabile *SEAMODE (Oggetto J1/VAR/SEAMODE). Si, possono avere i valori :  "ADVANCED" che lancia la funzione di query java, "5250" che lancia il pgm funizzato B£RICE01 e "SCH" che lancia una scheda attraverso il servizio B£EQRY_SE. A seguire ci si sofferma esclusivamente sul flusso che viene eseguito quando nella variabile è presente il valore "SCH", da scheda.
* Innanzitutto il client verifica se la ricerca non debba essere svolta dal client stesso e nel caso si occupa direttamente della risoluzione senza richiamare il server (si vedano le ricerche sugli oggetti D8*YYMD e J1PATHFILE)
* Viene lanciata una chiamata F(TRE;B£EQRY_SE;CTR.SEA). Questi i parametri ricevuti : 
** Nell'oggetto 1 è riportata la classe di riferimento della ricerca. Vengono riempiti i campi tipo e parametro corrispondenti
** Str :  contiene la stringa di ricerca
** Solo se la ricerca viene lanciata da emulazione : 
*** Pgm :  contiene il pgm da cui è partita la ricerca
*** Fld :  contiene il nome del campo video da cui è partita la ricerca
*** Dspf :  contiene il nome del file video da cui è partita la ricerca
*** Fmt :  contiene il nome del formato del file video da cui è partita la ricerca
* Tramite questo servizio viene determinata quale funzione lanciare per la risoluzione della ricerca con queste alternative : 
** Lanciare la ricerca in emulazione 5250
*** La prima casistica viene applicata qualora siano state utilizzati i caratteri speciali di ricerca parametrica previsti dal vecchio standard (in linea generale rientrano in questa categoria tutti i caratteri di ricerca "+" seguiti da un carattere non alfabetico che erano stati previsti in passato)
*** In alternativa questa scelta può essere effettuata se a standard o tramite exit della /COPY £K04 per una certa classe è stata, per vari motivi forzata la risoluzione tramite emulazione
** Lanciare la scheda di ricerca grafica
** Quando la ricerca è partita dall'emulazione può inoltre porsi la seguente casistica :  se dalle informazioni ricevute non si è in grado di determinare la classe da ricercare non viene ritornata alcuna funzione. Il che si traduce per la funzione in emulazione nella ripresa dell'elaborazione che a questo punto risolverà per suo conto la ricerca.

## 2) Se la ricerca è grafica la stringa ricevuta viene interpretata e rielaborata prima del lancio della scheda vera e propria

* Se viene dalla succitata funzione viene ritornata la ricerca tramite scheda viene lanciata questa funzione F(EXD;B£EQRY_SE;LAN.QRY), con i medesimi parametri della funzione CTR.SEA. Questa funzione pur essendo con componente EXD serve in realtà solo per capire come comporre la funzione di ricerca effettiva. A partire infatti dal contenuto della stringa viene determinato : 
** Quale query di ricerca deve essere lanciata (es. se arriva il ? viene riconosciuto che va lanciata la scheda ordinata per descrizione, mentre verrà lanciata per codice se arriva il !)
** Se alla query devono essere passati dei parametri (es. riprendendo l'esempio del ? se mi arriva ?BER, alla query verrà passato il parametro di posizionamento valorizzato a BER)
** Identificata la query a partire dal risultato della richiamo della funzione "FUN" della /COPY £IQ1 della query verrà determinata quale funzione lanciare.
* A questo punto la vera funzione di ricerca viene lanciata attraverso una risposta di tipo RFunction alla precedente chiamata

## 3) Elaborazione della query

* Salvo particolari eccezioni la funzione di ricerca viene svolta nel seguente modo : 
** Con una sezione di richiesta parametri
** Con una sezione di esecuzione
* La sezione di richiesta parametri si baserà o su un particolare configuratore o sulle richieste parametri che risultano correlate alla query (si veda la funzione LIS.RIC della £IQ1)
* La sezione di esecuzione si baserà sul richiamo del servizio LOA10_SE. Questo a sua volta si appoggerà alle funzioni della £IQR ed in particolare a quelle svolte dal pgm B£IQRM che risponde alle funzioni SEL
* Questo pgm si svolge in questo modo : 
** Vengono analizzate i dati dei componenti della query (fonte, filtro, schema, ordinamento)
** Queste componenti potranno restituire i seguenti risultati : 
*** Tutti i componenti possono essere risolti da SQL, quindi l'intera query viene così risolta tramite una SELECT SQL (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"C"** nel campo "Tipo Risoluzione")
*** Solo alcuni componenti della query sono risolvibili tramite SQL. In questo caso, quello che è possibile verrà risolto tramite SQL, mentre il resto tramite elaborazione rpg. Questa casistica si declina a sua volta in queste varianti : 
**** Con lo schema completamente risolto dalla SELECT SQL (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"S"** nel campo "Tipo Risoluzione")
**** Con lo schema parzialmente risolto dalla SELECT SQL, allo schema nel caso fossero assenti vengono automaticamente attributi come campi nascosti i campi che servono per la risoluzione dei valori non SQL (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"Z"** nel campo "Tipo Risoluzione")
**** Con lo schema totalmente irrisolto dall'SQL, in questo caso nell'sql verrà ritornato l'intera DS del record al fine di essere poi al pgm di risoluzione dello schema. (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"P"** nel campo "Tipo Risoluzione")
**** Con il filtro completamente risolto da una WHERE SQL (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"P"** nel campo "Tipo Risoluzione")
**** Con il filtro parzialmente risolto da una WHERE SQL (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **"P"** nel campo "Tipo Risoluzione")
**** Con il filtro totalmente irrisolto dall'SQL (sia per questo caso che per il precedente, allo schema nel caso fossero assenti vengono automaticamente attributi come campi nascosti i campi che servono per la risoluzione dei filtri, in modo che questi possano poi essere verificati).
*** E' importante che se i campi non risolvibili da SQL sono il risultati dell'applicazione di funzioni RPG (es. Decodifiche, OAV), questi verranno risolti, sia per i filtri che per gli schemi, attraverso il pgm B£IQRC tramite funzione VAL della £IQR (a meno che queste funzioni non siano state risolte tramite colonne aggiuntive, in questo caso è il servizio LOSER_25 a risolvere le funzioni)
*** Se invece nessuno componente risulta essere compatibile con estrazioni sql, la query viene risolta dal pgm B£IQRG, attraverso le chiamate con funzioni INZ/SLC e in ciclo SCN/POS/LET. Queste al suo interno prevedono già le chiamate implicite al pgm B£IQRC tramite la funzione VAL della £IQR dei campi funzione (dall'analisi cache richiamabile dal tasto F22 della matrice, si vede il valore **" "** nel campo "Tipo Risoluzione")
** In questo modo le righe risultanti vengono quindi inviate al client.


## 4) Gestione della paginazione e riposizionamento

* A questo punto si riporta infine come viene risolta la paginazione : 
** Quando la query è anche solo parzialmente risolta da SQL, nell'SQL viene sempre aggiunto come primo campo della SELECT esattamente la stringa che dovrà essere utilizzata come WHERE aggiuntiva per la paginazione successiva. In questo modo prendendo il valore del campo per l'ultima riga sarà possibile inviare al client, l'informazione che ricevuta dalla successiva paginazione permetterà di applicare il corretto posizionamento.
** Viceversa ci sia aspetta che sia il pgm di risoluzione della query a fornire tale informazione. In merito a questo sussistono eccezioni ma normalmente quando si ricade in questo caso, il pgm di risoluzione di tratta del pgm B£IQR_01 che a sua volta si basa sulla £G60 che a sua volta si basa sulla risoluzione tramite B£DEC4 (per lo meno per gli oggetti che hanno portato a questa risoluzione nelle ricerche) la quale fornisce queste funzionalità attraverso l'indicazione del prossimo codice da leggere.

 :  : DEC T(OJ) P(*PGM) K(B£EQRY_SE)
 :  : DEC T(OJ) P(*PGM) K(LOA10_SE)
 :  : DEC T(OJ) P(*PGM) K(B£IQRM)
 :  : DEC T(MB) P(QILEGEN) K(£K04)
 :  : DEC T(MB) P(QILEGEN) K(£IQR)





