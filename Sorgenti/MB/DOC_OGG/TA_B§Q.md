# B§Q - Questionari
## OBIETTIVO
Raccoglie tutte le caratteristiche e le impostazioni che servono per avviare correttamente un questionario servendosi della struttura del LOA34.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso e rappresenta il nome del questionario.

 :  : FLD T$B§Q1 __Configuratore __
In questo campo deve essere indicato il nome del configuratore specifico che servirà per raccogliere i dati di input per poter caricare correttamente il questionario.
Esempio :  si indica
 - CQRICO/1 se si vogliono compilare tramite questionario le registrazioni di collaudo a partire    dal lotto
 - CQRICO/2 se si vogliono compilare tramite questionario le registrazioni di collaudo a partire    da una risorsa. Se la compilazione avviene tramite device, è possibile abbianare il    dispositivo a una risorsa precisa (dalla quale si ricava l'ordine di produzione e il lotto)    tramite la tabella B§M (l'elemnto della B§M è il nome del device e al suo interno viene    abbinata la risorsa).

 :  : FLD T$B§Q2 __Programma specifico __
In questo campo deve essere indicato il nome del programma specifico che servirà alla scrittura delle domande e delle potenziali risposte del questionario. In questo programma devono essere incluse tutte le logiche di caricamento delle domande e di memorizzazione delle risposte.
Questo programma viene chiamato più volte dal programma generico LOA34_SE : 
 - all'inizio per il caricamento delle domande (scritta del file di work)
 - all'uscita per la scrittura del file "definitivo" e per la cancellazione del file di work
 - all'abbandono senza conferma per la cancellazione del file di work

 :  : FLD T$B§Q3 __Controllo accessi?  __
Con questo flag si procede all'attivazione di un controllo che impedisce a due o più utenti di intervenire simultaneamente sulla stessa istanza. Il vincolo viene attivato dal programma di exit del configuratore specifico (indicato nel campo T$B§Q2 - Configuratore) e gestito poi all'interno del programma standard specifico (indicato invece in T$B§Q3 - Programma specifico).
Il vincolo può interessare uno o più oggetti richiesti dal configuratore.
Nei questionari standard proposti, i vincoli vengono per esempio attivati sul lotto, per evitare che lo stesso lotto venga dichiarato contemporaneamente da due utenti.

 :  : FLD T$B§Q4 __Impostazione livelli __
Attraverso questo flag è possibile impostare la modalità di visualizzazione del questionario.
* '1' = modalità fissa tale per cui il questionario viene caricato già aperto. Scegliendo quindi questo valore vengono visualizzati tutti i capitoli e tutti i relativi paragrafi in modalità fissa (non sensibili a dinamismi).
Esempio :   C/P/D fisso aperto
  CAPITOLO 1
   PARAGRAFO 1
   PARAGRAFO 2
  CAPITOLO 2
   PARAGRAFO 1
   PARAGRAFO 2

* '2' = modalità aperta, con possibilità di chiusura dei paragrafi. In questo modo il questionario viene caricato aperto (come nel primo caso), ma è possibile collassare i capitoli nascondendo i relativi paragrafi. Il questionario risultante è quindi sensibile a dinamismi di apertura/chiusura.
Esempio :  C/P/D aperto con possibilità di chiusura
  Caricamento iniziale :      Cliccando sul capitolo 2 :    Cliccando sul capitolo 1 : 
    CAPITOLO 1                CAPITOLO 1                  CAPITOLO 1
     PARAGRAFO 1               PARAGRAFO 1                CAPITOLO 2
     PARAGRAFO 2               PARAGRAFO 2
    CAPITOLO 2                CAPITOLO 2
     PARAGRAFO 1
     PARAGRAFO 2

* '3' = modalità chiusa, con possibilità di apertura dei paragrafi. In questo modo il questionario viene caricato chiuso ed è possibile aprire i capitoli che interessano  sempre con un clic : 
relativi paragrafi. Il questionario risultante è quindi sensibile a dinamismi di apertura/chiusura.
Esempio :  C/P/D chiuso con possibilità di apertura
  Caricamento iniziale :      Cliccando sul capitolo 1 :    Cliccando sul capitolo 2 : 
    CAPITOLO 1                CAPITOLO 1                  CAPITOLO 1
    CAPITOLO 2                 PARAGRAFO 1                 PARAGRAFO 1
                               PARAGRAFO 2                 PARAGRAFO 2
                              CAPITOLO 2                  CAPITOLO 2
                                                           PARAGRAFO 1
                                                           PARAGRAFO 2

* '4' = modalità con capitoli nascosti. Anche se presenti nel questionario, questa modalità permette di NON visualizzare i capitoli nel questionario, visualizzando così solo i paragrafi.
Il questionario risultante non risulta sensibile a dinamismi
Esempio :  C/P/D con capitoli nascosti
    PARAGRAFO 1
    PARAGRAFO 2
    PARAGRAFO 1
    PARAGRAFO 2
* '5' =  Questionario in cui vengono gestiti solo i paragrafi e le domande
P/D
* '6' = Nel questionario sono presenti solo le domande.
D

 :  : FLD T$B§Q5 __Note Generali __
Se impostato, questo flag abilita la gestione delle note a livello del questionario.
Questo è il livello di massima generalità dal momento che viene legato all'oggetto "questionario".
 :  : FLD T$B§Q6 __Note capitolo __
Se impostato, questo flag abilita la gestione delle note a livello di capitolo del questionario e permette quindi la gestione delle note per quei record del file di work che hanno  BTFL01="1".
 :  : FLD T$B§Q7 __Note paragrafo__
Se impostato, questo flag abilita la gestione delle note a livello di paragrafo del questionario e permette quindi la gestione delle note per quei record del file di work che hanno  BTFL01="2".
 :  : FLD T$B§Q8 __Note domanda__
Se impostato, questo flag abilita la gestione delle note a livello di domanda del questionario e permette quindi la gestione delle note per quei record del file di work che hanno  BTFL01="3".

 :  : FLD T$B§Q9 __Configurazione specifica __
Stringa di 20 caratteri che consente di influenzare la costruzione del questionario.
A seconda del questionario e del programma specifico che si intende utilizzare, i 20 caratteri possono assumere significati diversi.

 :  : FLD T$B§QC __Posizionamneto autoamtico capitolo __
Se impostato, il flag permette di avere un caricamento automatico della prima serie di domande alla quale si deve rispondere. Risposto a queste, il programma caricherà automaticamente la serie di domande relativa al paragrafo successivo.

 :  : FLD T$B§QA __Modello informativo__
Questo flag influenza la gamma di colori da utilizzare nel questionario. Quando infatti vengono fornite le risposte alle varie domande, il paragrafo corrispondente viene marcato da una icona che può essere : 
 * BLU :  se il flag in questiona vale "1" e se quindi non è possibile attribuire un  significato    positivo o negativo alle risposte date;
 * ROSSA o VERDE :  se questo flag è lasciato *blanks. In questo modo l'icona del paragrafo diventa    rossa se la risposta fornita è diversa da quella attesa, verde in caso di conformità.

 :  : FLD T$B§QD __B£H per personalizzazioni__
In questo campo deve essere indicato il nome dell'elemento di B£H che deve essere usato per accedere al sottosettore di B£J nel quale devono essere indicati eventuali bottoni personalizzati da aggiungere alla scheda standard del configuratore.

 :  : FLD T$B§QE __Suff.Pgm.Aggiustamento__
Suffisso del programma di aggiustamento chiamato dal servizio specifico per aggiungere dettagli e personalizzazioni. Il programma chiamato dal quello specifico si chiamerà :  PGMSPECIFICO_X se X è la lettera messa in questo campo.
Esempio :  se il pgm specifico è CQSER_25, allora il programma di aggiustamento si chiamerà CQSER_25_X
