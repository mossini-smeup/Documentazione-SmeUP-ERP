# GESTIONE AREA DATI LOCALE ESTESA (SMELDA)

  Tramite questa /COPY permette la gestione di un'area dati locale estesa, accessibile
  a qualsiasi pgm di una sessione di lavoro (5250 o Loocup) ed ereditabile dai lavori sottomessi
  dalla sessione stessa.

# FUNZIONE BASE

  La funzione base della £G00 è quella di "programma mongolfiera".
  La £G00 permette, infatti, di passare una quantità arbitraria di
  dati da un programma a un altro. Questo è possibile perchè questa Copy
  è capace di scrivere e leggere il B£MEDE0F  utilizzando il suo campo
  di 30'000 byte per memorizzare i dati.

  ESEMPIO : 
        1)scrittura di un record di B£MEDE
     C                   EVAL      £G00FU='OUT'
     C                   EVAL      £G00ME=*BLANKS
     C                   EVAL      £G00TS='CHIAVE'
     C                   EVAL      £G00RE='DATI DA TRAFERIRE 30'000 BYTE'
     C                   EXSR      £G00

  La lettura dei dati salvati può essere effettuata in un qualsiasi momento da qualsiasi programma
  dello stesso JOB. Per recuperare le informazioni salvate si deve utilizzare lo stesso valore del
  campo £G00TS che rappresenta quindi la CHIAVE.

        2)lettura di un record di B£MEDE
     C                   EVAL      £G00FU='IN'
     C                   EVAL      £G00ME=*BLANKS
     C                   EVAL      £G00TS='CHIAVE'
     C                   EXSR      £G00
     C
     C                   EVAL      <DATI LETTI> = £G00RE

  N.B. : La lettura dei dati non cancella il record del B£MEDE, il record si cancella automaticamente quando
  l'utente si scollega.

  L'archiviazione di dati che fa la G00 è quindi volatile perchè legata alla sessione, se si vuole un archiviazione
  permanent come l'MDV guardare la £MDE
# FUNZIONI ESTESE

  Le varie funzioni possono essere raggruppate nelle seguenti categorie : 
  - Job
  - Ambiente
  - Servizio
  - Navigazione contabile

## FUNZIONI DI JOB

  Tramite queste funzioni è possibile scrivere/leggere/cancellare dati nella SMELDA del lavoro.
  Ogni gruppo di dati che viene scritto deve essere riconscibile da un tipo record. Il tipo record
  ** contiene le variabili d'ambiente fisse.

  Variabili di input :  £G00TS -> tipo record
  Variabili di input/output :  £G00RE -> record di dati (fino a 30000 caratteri)

  **SLR** :  dato un tipo record si posiziona sui record del tipo record.
  **RDE** :  dopo aver eseguito il posizionamento permette da la scansione degli eventuali
             record successivi del tipo record
  **UPD** :  dopo una lettura permette di aggiornare i dati contenuti in un record
  **DEL** :  dopo una lettura permette di cancellare un record dall'area
  **WRI** :  permette di scrivere dei dati nell'area dati

## FUNZIONI DI AMBIENTE

  Variabili di input/output :  £G00ST (e relativi sottocampi)

  Queste funzioni rappresentano una semplificazione della lettura/aggiornamento delle informazioni
  standard della SMELDA (tipo record = **).

  **SET** :  permette di gestire interattivamente il setup delle informazioni standard della SMELDA
  **IN**  :  permette di leggere la DS delle informazioni standard della SMELDA (questa funzione non si
             limita a leggere il fisicamente i dati ma attua anche delle risalite automatiche es. l'ambiente
             e la lista delle librerie le ricava dall'LDA, l'azienda dall B£2 ecc.)
  **OUT** :  permette di scrivere la DS delle informazioni standard della SMELDA

  Volendo è anche possibile utilizzare queste funzioni anche per semplificare l'aggiornamento letture di tipi record
  specifici, in questo caso è necessario passare nel campo £G00TS il tipo record, mentre come campo di input/output
  verrà utilizzato il campo £G00RE.

## FUNZIONI DI SERVIZIO

  Sono funzioni di manutenzione dell'area dati. Dovrebbero essere utilizzate esclusivamente dei
  pgm di login/logout ed eventualmente dal TST della /COPY stessa.

  **LDA** :  forza la rilettura della dtaara LDA nel pgm di gestione della £G00
  **CPY** :  permette di copiare la SMELDA del lavoro corrente su un'altro lavoro (es. per la sottomissione lavori batch)
  **CLO** :  viene pulita l'area dati corrente ed il tipo record ** viene memorizzato per essere riutilizzato
             al prossimo login dell'utente corrente sull'ambiente corrente
  **RGZ** :  riorganizzazione delle aree; tramite questa funzione vengono cancellate le aree dati collegate
             a lavori non più attivi (es. perchè la sessione è caduta prima che sia stata lanciata la funzione CLO)

## FUNZIONI DI NAVIGAZIONE CONTABILE

  Sono le funzioni originali della £G00, nate per gestione le variabili di riferimento necessarie
  per la navigazione all'interno dei dati contabili.
  Nella versione attuale queste funzioni svolgono le stesse funzioni della categoria di delle funzioni di
  ambiente, ma mirata esclusivamente ai dati rilevanti contabilimente (azienda/esercizio), cui si aggiungono
  alcune funzioni di decodifica e di gestione dei campi a video

  Variabili di input/output :  £G00DS (e relativi sottocampi)

  **VER** :  verifica dati correnti
  **DEC** :  decodifica dati correnti
  **IMP** :  impostazione scelta
  **GES** :  gestione
  **RIT** :  ritorna valori correnti

# DOCUMENTAZIONE TECNICA


## GESTIONE GENERALE

  Al login vengono caricate una serie di variabili che vengono associate al lavoro
  Le variabili vengono caricate secondo due fonti :  default per ambiente/utente (cioè la memorizzazione dell'ultima
  configurazione dell'utente in quell'ambiente) e le assunzioni cioè quei dati che vengono forzati (azienda da B£2) o
  derivati (es. Esercizio da data corrente).
  Queste variabili potranno essere modificate in modo cieco dai pgm oppure in modo interattivo tramite apposita funzione
  di gestione interattiva.
  La sottomissione di nuovi lavori da parte del lavoro corrente comporta la copia del suo setup come setup dei lavori
  sottomessi.
  Al logout la configurazione corrente del setup viene memorizzata come default ambiente/utente (per poi essere ripresa
  al successivo login).

## GESTIONE IN LOOCUP

  In loocup a differenza della normale gestione interattiva ad una "sessione" possiamo avere associati più lavori
  paralleli. Per ottenere lo stesso effetto della gestione interattiva normale, le variabili non vengono associate ad
  ognuno dei lavori interattivi ma vengono tutte ricondotte all'unico lavoro che crea tutti i lavori di gestione di una
  sessione, cioè quello che li sottomette.
  In questo modo la modifica del setup in uno qualsiasi dei lavori di sessione comporta automaticamente l'aggiornamento
  dei riferimenti di tutti i lavori di loocup di una sessione.

## DATABASE

  La SMELDA di un lavoro viene fisicamente memorizzata nel file B£MEDE0F con le seguenti chiavi : 
  - METIPA="REM-£G00JB"
  - MECODI=Tipo record ("**" per £G00ST)
  - MECOD1=Nome Utente
  - MECOD2=Nome Lavoro
  - MECOD3=N° Lavoro

  Il default delle variabili per utente/ambiente viene memorizzato sempre nel B£MEDE0F con le seguenti
  chiavi : 
  - METIPA="REM-£G00AU"
  - MECODI=Nome Utente
  - MECOD1=Ambiente (elemento B£B)
  - MECOD2=" "
  - MECOD3=" "

