# Reference regole

## Il linguaggio delle Regole
Questo linguaggio di regole non è case sensitive e non fa quindi differenza tra lettere minuscole e lettere maiuscole (quindi la funzione AddVal è la stessa sia se invocata come "ADDVAL" che come "addval"). Inoltre non è posizionale e non tiene conto degli eventuali spazi bianchi compresi nelle chiamate alle procedure

Tutte le regole sono espresse utilizzando i seguenti costrutti : 

- SE condizione ALLORA azione
- SE condizione ALLORA azione1 ALTRIMENTI azione2
- Azione
- Commento

Le prime due strutture permettono di controllare se una parte di codice deve essere eseguita in base al risultato di una condizione. Se la condizione è vera vengono eseguiti i comandi della parte ALLORA, in caso contrario quelli della parte ALTRIMENTI (se si utilizza il secondo costrutto).
La sintassi è la seguente : 

SE ((condizione booleana) [E/O (condizione booleana)] ) ALLORA [azione]

Oppure

SE ((condizione booleana) [E/O (condizione booleana)] )ALLORA [azione] ALTRIMENTI [azione]

Le parentesi quadre prima dell'istuzione ALLORA non fanno parte della sintassi. È una notazione che indica che il loro contenuto può essere ripetuto.

Le lettere "E" e "O" sono utilizzate per indicare due operatori booleani And e Or.

## La condizione booleana
La condizione booleana ha la seguente forma : 

(valore sinistro, operatore di confronto, valore destro).

Per decidere se la condizione è vera viene confrontato il valore sinistro con quello destro. Il tipo di confronto da fare viene determinato dalla scelta dell'operatore di confronto.
Nella tabella 5 sono elencati i tipi di operatori di confronto disponibili.

| **Valore sinistro** | **Operatore di confronto** | **Valore destro** |
| ---|----|----|
| Valore, Variabile, Proprietà di domanda, Proprietà di sezione, Attributo Sme.up oggetto risposta, Espressione | Codice Descrizione, == (uguale), < (minore), > (maggiore), <= (minore uguale), >= (maggiore uguale), <> (diverso) | Valore, Variabile, Proprietà di domanda, Proprietà di sezione, Attributo Sme.up oggetto risposta, Espressione |
|  | IN (compreso) | Range |
| 

Tabella 5 - I possibili operatori di confronto

_2_Valore :  identifica un valore costante, per esempio il numero 10 viene espresso con la stringa :  '10'.

_2_Variabile :  identifica la risposta fornita dall'utente.

_2_Proprietà di una domanda o della Sezione :  posso accedere alla definizione della struttura della domanda o della sezione ed eseguire controlli sulla struttura o cambiarne la visibilià.
Nell'esempio che segue controlliamo il tipo della domanda V02_01 e se il tipo è numerico assegnamoil valore della domanda V01_01 incrementato di 5.

_1_SE D.V02_01.TACFDC == 'NR' ALLORA V02_01 = V01_01 + '5'

_2_Attributo Sme.up oggetto risposta :  data una risposta ad una domanda viene identificato un oggetto Sme.up, identificato l'oggetto posso accedere ai suoi attributi.
Se per esempio richiedo un agente, posso poi testare la sua data di nascita, se è tra i suoi attributi.

_2_Espressione :  è una struttura del tipo operando1 operatore operando2. Operando 1 e Operando2

## Le Funzioni
Le funzioni che questo linguaggio delle regole può implementare sono le seguenti : 

### Le funzioni sui valori e di filtro

- _2_AddVal (cod_domanda; valore (o range)) :  aggiungo un valore o un gruppo di valori alla domanda selezionata.
- _2_RmvVal (cod_domanda; valore) :  rimuovo un valore o un gruppo di valori alla domanda selezionata.
- _2_AddAll (cod_domanda) :  abilito tutti i valori della domanda selezionata
- _2_RmvAll (cod_domanda) :  disabilito tutti i valori della domanda selezionata
- _2_AddFunVal() e RmvFunVal() : possono aggiungere o rimuovere una lista di valori letta da AS400 utilizzando un servizio che restituisca una griglia. I parametri ammessi sono i seguenti :  domanda a cui vanno aggiunti/rimossi i valori, funzione da invocare, codice colonna che contiene valori, codice colonna di filtro e valore filtro. Gli ultimi due valori sono opzionali. Per rendere dinamica la chiamata da fare all'AS400 si possono inserire le variabili del configuratore con la sintassi "aperta quadra" codice_domanda "chiusa quadra". Se la variabile è multipla vengono eseguite n chiamate, una per ogni valore. La funzione accetta fino a 3 variabili.
- _2_SetFiltro ( cod_domanda; cod_filtro; param1 filtro; ...; param N filtro) :  imposto un filtro sulle possibili risposte fornite. Se si desiderano utilizzare i filtri definiti nella JAC il codice del filtro deve diventare *JAC
- _2_ResetFiltro(cod_domanda) :  annullo il filtro


### Le funzioni sui messaggi

- _2_AddMsgT(testo) emette un messaggio bloccante :  la compilazione si arresta.
- _2_AddMsgW(testo) emette un messaggio di avviso.
- _2_AddMsgI(testo) emette un messaggio informativo.
- _2_ClrMsg ( ) rimuove tutti i messaggi della sezione alla quale la regola appartiene.


### Le funzioni matematiche
Operano tutte su parametri numerici.

- _2_abs(VAR) Restituisce il valore assoluto di VAR.
- _2_acos(VAR) Restituisce l'arcocoseno dell'angolo VAR in radianti da 0 a PI
- _2_asin(VAR) Restituisce l'arco seno dell'angolo VAR da -PI/2 a PI/2
- _2_atan(VAR) Restituisce l'arco tangente dell'angolo VAR da -PI/2 a PI/2
- _2_ceil(VAR) Approssima VAR all'intero successivo. Es. Ceil('12.23') = 13.
- _2_cos(VAR)  Restituisce il coseno di VAR.
- _2_exp(VAR)  Restituisce il numero di Eulero elevato alla potenza di VAR.
- _2_floor(VAR) Approssima VAR all'intero precedente. Es. Flor('12,77') = 12.
- _2_log(VAR) Restituisce il logaritmop naturale di VAR.
- _2_max(VAR_A, VAR_B) Restituisce massimo tra i due valori
- _2_min(VAR, VAR_B) Restituisce il minimo tra i due valori.
- _2_pow(VAR, VAR_B) Eleva VAR alla potenza di VAR_B
- _2_random() Genera un numero casuale compreso tra 0 e 1
- _2_sin(VAR) Restituisce seno di VAR
- _2_sqrt(VAR) Restituisce la radice quadrata di VAR
- _2_tan(VAR) Restituisce la tangente di VAR
- _2_toDegrees(angRad) Converte un angolo espresso in gradi in radianti
- _2_toRadians(angDeg) Converte un angolo espresso in radianti in gradi.


### Le funzioni sulle stringhe o di conversione

- _2_concat(String a, String b) restituisce la stringa formata dal concatenamento di a e b
- _2_substring(String A, Number B, Number C) restituisce la sottostringa di A che inizia dall'indice B e termina all'indice C escluso :  esempio substring('ABCDEF',0,3) = ABC; substring('ABCDEF',2,3) = C
- _2_substringFrom(String A, Number B) restituisce la sottostringa di A che inizia dall'indice B e va fino alla fine. Esempio substringFrom('ABCDE';2)=CDE
- _2_number2string(a[,b,c]) converte il numero a  in una stringa. Esempio number2string('12345.6789') restituisce '123456.6789'. Se vengono specificati anche i parametri b e c allora il numero viene convertito in una stringa lunga b con c decimali, senza uso della virgola come separatore dei decimali. Esempio number2string('12345.6789'; '7', '2') restituisce 1234567 mentre - _2_number2string('12345.6789'; '10','2') restituisce '0001234567'
- _2_string2number() converte una stringa formattata secondo lo standard AS400 in numero. Esempio string2number('1234567'; '5'; '2' ) restituisce 123,45


### Le funzioni di accesso alle risposte multiple e/o configurate

- _2_getResponseAtIndex(cod_domanda; indice) restituisce la risposta della domanda di dato indice :  si usa con le domande a risposta multipla.
- _2_getRespAt(cod_domanda; indice) forma abbreviata della precedente.
- _2_getNRRespAtIndex(cod_domanda; indice; lunghezza; decimali) restituisce la risposta di dato indice in formato numerico, restituendo una risposta di data lunghezza e dati decimali.
- _2_getNRRespAt(cod_domanda; indice; lunghezza; decimali) forma abbreviata della precedente.
- _2_getDescRespAt(cod_domanda; indice) restituisce la descrizione della risposta di dato indice.
- _2_getDescResp( cod_domanda) restituisce la descrizione della risposta (se la domanda è a risposta multipla restituisce la descrizione della prima risposta).
- _2_getObjDesc(tipo; parametro; codice) restituisce la decodifica dell'oggetto identificato dalla terna tipo-parametro-codice. Tipo parametro codice sono espressioni.
- _2_getAuxResp('nome domanda ausliaria senza asterisco') restituisce la risposta ausiliaria. Le domande ausiliarie sono le seguenti : 
-- *DE è la descrizione della configurazione
-- *QU è il codice del questionario
-- *UC è l'utente che ha creato la configurazione
-- *DC è la data di creazione
-- *IC l'ora di creazione
-- *DM è l'utente che ha modificato la configurazione
-- *IM l'ora di modifica
-- *UM è l'utente che ha modificato
Esempio getAuxResp('UM') restituisce il codice dell'utente che ha modificato la configurazione. Queste informazioni ausiliarie sono disponibili solo se nel questionario si specifica di aggiungere queste informazioni.
- _2_getLoocupVarValue('cod_LoocupVariable') restituisce il valore della variabile di ambiente di Loocup. Le variabili di ambiente includono i dati relativi all'applicazione (es. posizione icone), i dati relativi alla macchina e i dati della JVM utilizzata. Maggiori dettagli sono disponibili nella documentazione di LoocUp.


### Le funzioni di modifica delle risposte multiple e/o configurate

- _2_setNota(cod_domanda; testo_nota) aggiunge una nota ad una domanda. Sono ammesse le sole lettere e i numeri.
- _2_setRespAt(cod_domanda; nuova_risposta; indice_risposta) consente di variare una risposta di dato indice.


### Le funzioni di test
_2_IsEmpty(cod_domanda) restituisce vero se alla domanda identificata da cod_domanda non è stata fornita nessuna risposta.

## I Commenti
E' possibile inserire dei commenti alle regole. Queste porzioni di testo non vengono interpretate dal sistema, ma servono solo all'utente per documentare il lavoro fatto.
Per inserire dei commenti è sufficiente farli precedere dalla stringa '//' (doppia barra); tutto quello compreso tra tale stringa e la fine della riga è considerato commento.

## I Messaggi
Build.up permette la visualizzazione di messaggi di testo definibili dall'utente. Esistono tre tipi di messaggi :  bloccanti (identificati dalla lettera "T" ), di avviso ("W") e informativi ("I").

I primi, quando vengono emessi, bloccano l'esecuzione del questionario ed obbligano l'utente a correggere le risposte sbagliate date in precedenza. I messaggi di avviso, invece, comunicano all'utente che i valori immessi potrebbero non essere corretti, ma lasciano proseguire la compilazione del questionario. Infine il terzo tipo di messaggio (informativo) serve per comunicare all'utente informazioni aggiuntive di carattere generale.

I messaggi vengono emessi scrivendo, nelle regole, opportune funzioni. Ogni funzione richiede due parametri, un codice e una testo. Se il codice è vuoto significa che il messaggio è del questionario, altrimenti è della sezione o della domanda identificata.

La rimozione dei messaggi è eseguita con la funzione CLRMSG( ) :  elimina tutti i messaggi dati fino a questo punto della compilazione.

La funzione ADDMSGT visualizza un messaggio bloccante ( T sta per Terminale) nella sezione alla quale appartiene la regola che richiama questa funzione.
Ecco un esempio :  _2_ADDMSGT ( ' Hai inserito un valore fuori dal range consentito ' )
Mentre la altre due servono per emettere messaggi di avviso o informativo.
Ecco alcuni esempi del loro utilizzo : 

- _2_ADDMSGW ( ' Questo è un messaggio di avviso' )
- _2_ADDMSGI ( ' Questo è un messaggio di informativo ' )

La funzione CLRMSG ( ) rimuove tutti i messaggi della sezione alla quale la regola appartiene.

## L'editor delle regole
Per facilitare l'inserimento e la manutenzione delle regole del questionario è stato sviluppato un apposito editor ed il suo aspetto è mostrato in Figura 8 : 

![CFBASE_028](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_028.png)Figura 8 - L'editor delle regole

E' dotato di tutti gli strumenti di un classico editor di testo (funzioni di salvataggio, stampa, taglia, copia, incolla, help, etc') e facilita la lettura delle regole, evidenziando con colori differenti le parole riservate del linguaggio e i valori delle variabili.

Il tasto "Compila" manda in esecuzione il parser che abbiamo realizzato al fine di validare sintatticamente la regola digitata. Quando si preme il tasto "Salva" viene comunque eseguito questo controllo per garantire che qualsiasi regola inserita sul server AS400 sia almeno sintatticamente corretta.

l grande vantaggio di questo editor sta nella presenza del "Wizard", ossia di una procedura che guida l'utente nell'inserimento delle regole. Il Wizard, in base al punto in cui l'utente si trovacol cursore durante la scrittura della regola, suggerisce tutte le possibili opzioni valide tra le quali l'utente può selezionare quella desiderata. Ad esempio quando l'utente digita il "SE"il Wizard mostra la finestra riportata in figura 12, nella quale propone la scelta dell'oggetto (variabile) da testare nella condizione booleana, ed in seguito propone l'elenco dei possibili valori della parte destra dell'operazione di confronto, prendendo questa lista direttamente dalla tabella memorizzata su AS400 alla quale la domanda stessa è associata. Il processo guidato continua fino alla terminazione della regola.

![CFBASE_035](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_035.png)Figura 9 - Il wizard dell'editor delle regole con la finestra di selezione degli operatori

### La messa a punto delle regole

In LoocUp non esiste un debugger interattivo vi è però la possibilità di visualizzare tutte le operazioni compiute.
Durante la compilazione viene, di default, tenuta traccia delle azioni compiute dalle regole. Questa traccia è visibile dalla finestra di compilazione di LoocUp. I pulsanti preposti sono quelli che riportano una pergamena.
La storia di esecuzione si può disabilitare con l'apposito pulsante oppure mediante parametri :  se nella richiesta di configurazione si inserisce nel parametro P il valore DEBUG(0).
La storia di esecuzione può diventare molto grande. Se si desidera analizzare un particolare gruppo di regole si può cancellarla o tenerla disabilitata fino al momento opportuno.

Esistono due modi di visualizzarla :  in una tabella non riordinabile (molto veloce) oppure in una matrice. La seconda strada, se le regole eseguite sono molte è più lenta, ma permette inoltre di esportare la matrice in formato EXCELL e di eseguire ricerche più accurate.

L'esportazione in EXCEL risulta molto utile quanto non si capisce quale regole abbia agito su una determinata domanda.

## Correlazione tra oggetti e regole
Per creare un questionario occorre, oltre che definire sezioni e domande, scrivere le regole. E' attraverso di esse che si riesce a dare al configuratore un comportamento dinamico, attivando o disattivando la visualizzazione di sezioni e di domande, o svolgendo funzioni particolari. Le regole legano tra loro gli oggetti che costituiscono un configuratore (li correlano), confrontandoli o modificandone i valori.

Ad esempio, una regola potrebbe dover confrontare i valori di Oggetto1 e Oggetto2 e impostare il valore di un terzo oggetto chiamato Oggetto3. Al crescere della complessità del questionario aumenta, però, in proporzione, anche la possibilità che lo stesso oggetto compaia in più regole. E' facile quindi arrivare ad avere una struttura "ingarbugliata" del questionario, costituita da numerosissimi legami invisibili tra oggetti e regole. Il questionario, inoltre, non ha una struttura che, una volta realizzata, rimane tale per sempre. Viene sottoposto continuamente a modifiche e aggiornamenti perché il prodotto che viene configurato può avere nuove varianti, o certe sue parti possono finire fuori produzione ecc... Chi implementa questi cambiamenti ha quindila necessità di avere a disposizione strumenti che lo aiutino nell'apportare tali modifiche.

Solitamente la sua necessità è quella di poter sapere in quali regole compare un determinato oggetto o, viceversa, dato un oggetto poter risalire a conoscere in quali regole compare :  nella figura che segue vediamo lo strumento di analisi delle regole : 

![CFBASE_027](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_027.png)Figura 10 - La finestra Correlazione Regole

Questo strumento riceve dall'AS400 tutte le regole di un questionario. Per ognuna di esse estrae tutti gli oggetti che la compongono e li inserisce in una tabella bidimensionale. Ad ogni riga corrisponde un oggetto di una regola; se lo stesso oggetto compare in più regole ci saranno più righe con quell'oggetto ma associate a regole diverse. Le colonne sono 8 e ognuna identifica una caratteristica dell'oggetto o della regola che caratterizzano la riga.

In particolare sono : 

- Questionario :  è il nome del questionario a cui la regola appartiene;
- Tipo regola :  dice se la regola è una regola di domanda, di sezione o di questionario;
- Codice regola :  è il codice della sezione o della domanda alla quale la regola è associata;
- Significato :  è il testo della domanda se la regola è associata alla domanda, è invece il nome della sezione se la regola è associata alla sezione;
- Tipo oggetto :  è il tipo dell'oggetto che, assieme alla regola, identifica la riga;
- Oggetto :  è l'oggetto trovato nella regola, con la regola identifica univocamente la riga;
- Significato :  è la descrizione dell'oggetto. Ad esempio, se l'oggetto è una domanda, rappresenta il testo della domanda;
- Regola :  è la regola nella quale l'oggetto compare.

A questo punto è possibile operare su questa tabella per ottenere informazioni sui legami che esistono tra oggetti e regole (la loro correlazione).

L'idea è quella di poter "guardare" la tabella da diversi punti di vista, ognuno dei quali mette a fuoco determinati aspetti. Le righe della tabella possono essere riordinate secondo un ordine deciso dall'utente. Quest'ultimo si limita a scegliere quale ordinamento dare alle colonne.

Se per esempio si vuole sapere in quali regole compare l'oggetto XXXX basta scegliere nell'ordine le colonne "Oggetto" e "Regola". A questo punto compare l'elenco di tutti gli oggetti presenti nelle regole; se espandiamo la riga dell'oggetto XXXX troviamo tutte le righe della tabella originale che avevano tale oggetto nella propria regola, ordinate per regola.

## Integrazione col sistema gestionale
Quando si progetta un configuratore bisogna tenere presente che un suo prerequisito fondamentale deve essere la possibilità di interfacciarsi col sistema gestionale esistente nell'azienda. Interfacciarsi significa dare allo strumento la possibilità di estrarre, immettere, o elaborare informazioni significative per la gestione dell'azienda stessa. Uno strumento che raccoglie semplicemente informazioni (magari le risposte ad alcune domande) e le salva, per esempio, in un foglio Excel ha un'utilità relativa. Esso richiede comunque la presenza di un operatore che, leggendo tale documento, inserisce le informazioni nel posto giusto del sistema informativo. Questa fase del processo di introduzione dei dati (ad esempio un ordine di acquisto) può essere lunga e soprattutto non esente da errori. Un errore in questo punto vanifica tutto il lavoro compiuto per presentare una configurazione corretta. Anche l'impiego della configurazione nel gestionale dovrebbe dunque essere automatizzata.

A questo punto riteniamo doveroso fare una precisazione. Quando si costruisce uno strumento come il configuratore e si decidono quali funzionalità deve svolgere e quali problemi deve risolvere, bisogna considerare che i suoi utilizzatori finali possono essere di diversa natura e avere necessità differenti. Per questo motivo lo strumento che si realizza sarà composto sia da parti standard che da parti che dovranno essere soggette a personalizzazioni sulla base delle caratteristiche del cliente (o del suo sistema gestionale).

Riferendoci a Build.up questa separazione è abbastanza evidente soprattutto per quanto riguarda il livello di integrazione con l' E.R.P.

Quando si costruisce un questionario, infatti, si inserisce nel configuratore una serie di domande, alcune delle quali tipizzate. Ricordiamo che una domanda è tipizzata quando alla sua risposta è associato un Tipo di oggetto. Esempi di queste domande sono la richiesta di una data, che sulla base della risposta istanzia un oggetto applicativo di tipo Data, oppure la richiesta di un articolo che ha, tra le risposte possibili, l'elenco degli articoli (ognuno di essi è un oggetto applicativo) tra i quali l'utente può scegliere quello desiderato. In entrambi i casi viene stabilita una relazione tra l'oggetto che sto configurando e l'oggetto istanziato dalla risposta (la data) o l'oggetto scelto dall'elenco (l'articolo). Questo approccio produce una seriedi innegabili vantaggi. In primo luogo viene evitata la duplicazione dei dati perché decidendo, ad esempio, che una domanda è di tipo Articolo l'elenco di tutti gli articoli non deve essere copiato nel configuratore, ma il configuratore automaticamente si preoccupa di andare a leggere tale elenco nell'unico punto del gestionale in cui è presente. Evitare la duplicazione dei dati porta dei risparmi economici all'azienda, dovuti al risparmio delle spese di manutenzione e gestione dei dati stessi, nonché ad una limitazione dello spazio fisico occupato [13]. In secondo luogo la manutenzione dei questionari viene notevolmente ridotta, in quanto se inserisco un nuovo articolo nel sistema automaticamente questo sarà disponibile nell'elenco degli articoli associato alla domanda, senza dover compiere nessuna operazione particolare. Questa parte è standardizzata, in quanto i dati necessari al configuratore vengono letti direttamente nel database e passati in formato XML, indipendentemente dalla struttura gestionale sottostante.

La parte del configuratore, legata all'integrazione col gestionale, che non è standardizzabile è il processo che, partendo dalla raccolta delle risposte ad un questionario di configurazione di un prodotto porta, ad esempio, alla costruzione di una distinta base. Questo limite è dovuto al fatto che aziende differenti gestiscono la loro distinta base in modi differenti.

## Il Questionario visto da Looc.up
Anche il configuratore utilizza Looc.up come strumento di interfaccia verso l'utente.

Chi scrive questionari utilizzerà questo client grafico visibile in Figura 14.

Analizzando la Figura 14 possiamo vedere che sulla sinistra vengono elencate tutte le sezioni, mentre sulla destra si possono vedere le domande appartenenti alla sezione selezionata. Ad ogni domanda e sezione sono associate le regole PRE e POST; cliccando su queste regole si accede all'editor grafico preposto alla loro manutenzione (inserimento, modifica, salvataggio, compilazione).

Sempre sulla sinistra vengono mostrate tutte le funzioni necessarie alla gestione del configuratore, quali ad esempio "Nuova Domanda" e "Nuova Sezione" per inserire rispettivamente unadomanda ed una sezione, "Modifica definizione questionario" per reimpostare le caratteristiche del questionario (ad esempio come associargli le sezioni), "Elenco configurazioni" per visualizzare tutte le configurazioni (cioè i questionari compilati) e "Gestione configurazione" che lancia un browser Internet per utilizzare il configuratore e rispondere alle domande.

![CFBASE_029](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_029.png)Figura 11 - La gestione del questionario in Looc.up

### La Scheda del Configuratore
L'accesso alle funzioni del configuratore avviene mediante un'apposita scheda (CFBASE).

Questa scheda è accessibile dal menù delle applicazioni di Loocup con il seguente percorso :  Menù Ingresso utente, *AP :  Applicazioni, LOOC_Up Graphic Environment, Schede, configuratore.

Verrà visualizzata la seguente scheda (Figura 12) : 

![CFBASE_037](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_037.png)  Figura 12 - La scheda del configuratore (CFBASE)

Sulla sinistra si possono vedere cinque tab, quattro raggruppano i questionari in base al loro tipo.
Esistono quattro tipi di configuratori : 

- i questionari Q- sono quelli definiti dall'utente, hanno una struttura ad albero e sono quelli descritti in questo documento
- i questionari T-, sono questionari dedicati alla manutenzione tabelle
- i questionari L- sono i setup e i questionari dedicati a definire i wizard di script
- i questionari C- sono quelli ricavati dalle categorie parametri.


In questo documento analizzeremo solo quelli definiti dall'utente.

Per accedere alle funzioni disponibili sul questionario bisogna selezionarne uno dall'elenco di sinistra.
Sulla destra verrà caricata la scheda del questionario (RE) : 

### La scheda del questionario
E' composta da tre sotto schede :  una dedicata alla manutenzione della struttura del questionario (è la prima visibile e riporta la dicitura "Questionario"), una dedicata alla gestione delle configurazioni (riporta la dicitura "Configurazioni") e una dedicata alla manutenzione delle regole (riporta la dicitura "Regole").

In figura 13 possiamo vedere le 3 schede con in primo piano quella del questionario.

![CFBASE_036](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_036.png)Figura 13 - La scheda del questionario.

Analizziamo in dettaglio le 3 schede.
 :  :  La sottoscheda del questionario
La sottoscheda del questionario consente la navigazione e la manutenzione del questionario e di tutti i suoi componenti logici (sezioni, domande e valori).

Le prime informazioni che compaiono sono gli attributi del questionario (Figura 13).

Per ogni oggetto contenuto è attivo un menù di popup sensibile al contesto. In figura 13 si vede il popup di una sezione :  le ultime due voci consentono di aggiungere una pre o post regola.
Se queste sono già definite per la sezioni in questione si entrerà in manutenzione.

### La sottoscheda delle regole

Con un doppio click sul talloncino delle regole si ottiene che la scheda vada a pieno schermo : 

![regole](http://localhost:3000/immagini/LOCG30_RUL/regole.png)
 Figura 14 - La scheda delle regole

qui si possono vedere tutte le regole nella zona "Elenco regole" e selezionandone una si può vedere la scomposizione sulla sinistra e la sua traduzione in italiano sulla destra.

In basso un pulsante che consente la manutenzione.

Per aggiungere nuove regole su sezioni o domande ci si posiziona sulla scheda del questionario e con il tasto destro si accede a queste funzioni.

### La sottoscheda della configurazione

La sottoscheda elle configurazioni, visibile in figura 15, riporta sulla sinistra l'elenco delle configurazioni create, e sulla parte destra l'elenco delle risposte.

Posizionandosi su una configurazione e utilizzando il tasto destro, sotto la voce "Questionario" si hanno le azioni di Gestione, Visualizza o Elimina.

![CFBASE_026](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_026.png)Figura 15 - La sotto scheda della configurazione e il popup di gestione


### la compilazione di un questionario
Compilare un questionario porta alla creazione di una configurazione.

La creazione di una nuova configurazione avviene con il tasto F8 mentre la modifica di una precedentemente salvata avviene con la voce "Gestione questionario" e poi  "Gestione (Imm/Cop/Del)"  del popup della configurazione.

![CFBASE_024](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_024.png)Figura 16 -  La compilazione di un questionario in LoocUp


![CFBASE_039](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_039.png)precedente, alla sezione successiva, auto compilazione)
![CFBASE_022](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_022.png)storia di esecuzione, visualizza la storia di esecuzione in tabella non ordinabile, visualizza in tabella ordinabile e filtrabile)
![CFBASE_021](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_021.png)sintattico sulle regole, attiva ricerca all'interno delle regole, traduci le regole in italiano, esegui controllo su ricerca domande e/o sezioni duplicate)

## La compilazione su WEB
### Prerequisiti.
Buildup è integrato in WEB-Up e pertanto necessario avere un Web-Server con installato WEB-Up. Per le ulteriori informazioni si rimanda alla documentazione di WEB-Up.

### L'interfaccia WEB.
La compilazione su WEB è simile a quella che avviene in LoocUp. Visto l'ambiente nel quale ci si trova viene disattivata la traccia di esecuzione delle regole. Mancano anche i pulsanti relativi ai possibili controlli (duplicazione domande, controllo sintattico, rigenerazione motore regole).

Nella figura 17 si può vedere l'interfaccia della finestra di compilazione : 

![CFBASE_023](http://localhost:3000/immagini/LOCG30_RUL/CFBASE_023.png)Figura 17 -  La compilazione di un questionario mediante browser.

In questa versione l'albero delle sezioni è stato portato in alto. Le sezioni percorse appaiono n grigio chiaro, quella corrente ha il testo in grassetto mentre quelle ancora da percorrere sono con lo sfondo grigio scuro.

Le sezioni disabilitate non vengono mostrate.

L'interfaccia è facilmente personalizzabile attraverso la modifica di fogli di stile che definiscono colori e dimensioni dei principali componenti.

Si possono anche aggiungere o rimuovere pulsanti secondo specifiche esigenze.

## Glossario
_2_Application Server. È un server che riceve la richiesta di una pagina che deve ancora essere creata; esegue del codice coinvolgendo solitamente anche altri moduli, quali ad esempio un database server e scrive il risultato della richiesta in una pagina HTML (quindi statica) che restituisce al web server che l'ha richiesta.

_2_Colloquio di configurazione. Durante la fase iniziale del processo di configurazione si svolge la raccolta delle informazioni sulle caratteristiche del prodotto richieste dal cliente. Questa fase prevede un colloquio, denominato appunto "colloquio di configurazione", tra commerciale e cliente in cui il cliente risponde a domande che riguardano le diverse possibilità di scelta previste, le risposte date permettono la completa specificazione del prodotto.

_2_Configuratore. È lo strumento che serve per realizzare un questionario e per utilizzarlo. Permette quindi l'inserimento di domande e regole e gestisce il suo comportamento. Sulla base cioè delle risposte che l'utente fornisce e dell'interpretazione delle regole sceglie quali altre domande devono essere poste.

_2_Configurazione. È il risultato della compilazione di un questionario. Una configurazione è l'elenco delle risposte fornite alle domande del questionario e identifica una particolare variante di prodotto.

_2_Distinta base. È l'elenco di tutti gli articoli che costituiscono il prodotto finale, unitamente alla loro quantità.

_2_Looc.up. È il client grafico del gestionale. Fornisce un'interfaccia grafica al gestionale Sme.up.

_2_Mass Customization. È un nuovo modo di concepire la produzione dei beni, con il riconoscimento della centralità delle esigenze e dei desideri dei clienti, ma senza nessuna rinuncia all'efficienza, all'efficacia ed al contenimento dei costi.

_2_Oggetto applicativo. È l'entità su cui si basano le azioni di inserimento e di reperimento delle informazioni del sistema gestionale Sme.up. Ogni oggetto è individuato dalla classe di appartenenza (chiamata "tipo") e dall'identificativo che è univoco all'interno della classe stessa; per alcune classi si identifica anche la sottoclasse (chiamata "Parametro"). Ad ogni oggetto sono associate delle funzioni che determinano quali azioni possono essere eseguite sull'oggetto stesso.

_2_Pagina dinamica. È una normale pagina basata su codice HTML che però viene generata da un server, con parametri e metodologie diverse a seconda delle circostanze. Esempi di tecnologie che realizzano pagine dinamiche sono gli script CGI (Common Gateway Interface) e le JSP (Java Server Pages).

_2_Prodotto configurabile. È un tipo di prodotto offerto, non corrisponde ad un oggetto fisico ma ad una categoria di prodotti potenzialmente realizzabili.

_2_Prodotto configurato. È una singola variante del prodotto configurabile e corrisponde ad un oggetto fisico, costruito o da costruire. Il prodotto configurato si ottiene personalizzando (precisando la scelta delle caratteristiche configurabili) un prodotto configurabile.

_2_Questionario. È l'insieme di tutte e sole quelle domande che servono a definire univocamente un prodotto. La compilazione del questionario, cioè le risposte fornite alle domande, permettono di identificare la variante di prodotto desiderata.

_2_Variante di prodotto. È uno fra i possibili prodotti che si ottengono modificando i parametri e le caratteristiche di un prodotto configurabile.

_2_Web server. Viene detto anche HTTP Server, è un programma che, avendo ricevuto delle richieste da parte del browser, spedisce il documento richiesto (o un messaggio di errore) al browser stesso.

_2_Web.up. È un modulo aggiuntivo di Sme.up. E' pensato per fornire strumenti di aiuto all'inserimento di dati prelevati dal database aziendale in pagine HTML.

## Conclusioni
Questa breve presentazione del prodotto Build.up ha mostrato le principali caratteristiche del programma nella speranza di offrire una panoramica d'insieme che possa rendere giustizia alle effettive qualità del pacchetto proposto.

La versione attuale di Build.up rappresenta quanto di meglio è oggi ottenibile nel settore dei configuratori :  la struttura fortemente modulare di Build.up, tipica di tutti i prodotti della Smea, lascia comunque aperte molte strade di sviluppo e miglioramento e rende più agevole la manutenzione del pacchetto stesso anche in funzione delle nuove tecnologie che si renderanno disponibili in futuro.
