La codifica degli oggetti di smeup si basa sempre sulle applicazioni (tabella B£A), perciò i primi due caratteri dell'oggetto definisco l'applicazione di appartenenza.

 :  : DEC T(ST) K(B£A)

# Archivi (File)

| File Fisici | xxmmmm0F | dove _xx_ indica l'applicazione, _mmmm_ il modulo e _F_ ---|
| indica che si tratta di un fisico |
| File Logici | xxmmmmnL | dove _xx_ indica l'applicazione, _mmmm_ il modulo, _n _ è un numero progressivo e _L_ indica che si tratta di un logico |
| File Logici di Join | xxmmmmnJ | dove _xx_ indica l'applicazione, _mmmm_ il modulo, _n _ è un numero progressivo e _J_ indica che si tratta di un file di Join. I file di join sono piuttosto rari in SME.UP. Solitamente si preferisce ricavare i dati in join in runtime. |
| 


Nelle definizioni dei file fisici di SME.UP non viene indicata la chiave. Normalmente la chiave unica è indicata nel primo logico. Ogni logico dovrebbe avere come ultimo campo il campo chiave, ottenendo in questo modo un indice implicitamente univoco.
Per ottenere una ricerca case insensitive sugli indici per descrizione si usa l'istruzione

ALTSEQ(QTOCSSTBL)

Per determinare l'ordinamento dei record in base alla tabella di sequenza QTOCSSTBL, nella quale a ciascuna lettera maiuscola è associato il medesimo codice della minuscola corrispondente.
I nomi dei campi devono essere univoci in tutto SME.UP, secondo la codifica xxnnnn, dove i primi due caratteri identificano il file, mentre i quattro successivi identificano il campo.
Le modifiche apportate ai file di dati vengono indicate nel membro SMESTD/SRCDB/AAAFIL, separate per rilascio.
Le modifiche effettuate durante lo sviluppo vengono invece indicate nel membro SMEDEV/SRCDB/AAAFIL.

>     A*----------------------------------------------------------------                      .
     A* Anagrafico cespiti
     A*----------------------------------------------------------------                      .
     A                                      ALTSEQ(QTOCSSTBL)
     A          R A5CESPR                   PFILE(A5CESP0F)
     A*
     A          K TAAZIE
     A          K TADECE
     A*


## Il buon file
I nuovi file Sme.UP dovrebbero avere tutti questi campi : 
* Dati statistici di inserimento
** Origine
** Data (di sistema)
** Ora (di sistema)
** Utente
* Dati statistici di ultima modifica
** Origine
** Data (di sistema)
** Ora (di sistema)
** Utente
* 10 Campi alfanumerici liberi
* 10 Campi numerici liberi
* 10 Campi per date se pertinenti (di tipo alfanumerico)
* 40 Campi flag

# Programmi
I programmi riguardanti la gestione di un file vengono codificati nel seguente modo : 
>AAOOppx, dove : 
 * _1_AA = Applicazione - 2 caratteri (TAB£A).
 :  : DEC T(ST) K(B£A)

 * _1_OO = Oggetto - 2 caratteri (TA*CNTT).
 :  : DEC T(ST) K(*CNTT)

 * _1_pp = Progressivo numerico di due caratteri.

 * _1_x = ultimo carattere che varia in base alla funzione del pgm : 
 ** finiscono per L i pgm di lista
 ** finiscono per G i pgm di acquisizione parametri
 ** finiscono per P i pgm di parzializzazione (filtri)

Es. :  BRAR01G è il pgm di acquisizione parametri dell'oggetto AR (=Articoli).
Se un pgm è di test di una /COPY, si chiamerà TST+codice /COPY senza il carattere "£".
Per tutti gli altri programmi valo solo la regola dei primi due caratteri che devono corrispondere al codice dell'applicazione.

**I primi 4 caratteri della descrizione (il testo del membro) di un'applicazione devono essere il codice di un modulo_ (_altrimenti non vengono compilati dal comando CO_).
Es. :  BRAR01L ha come testo del membro _ARTI Lista articoli_

# File video
Normalmente seguono la stessa codifica del programma che li utilizza con l'aggiunta del carattere "V" finale.

# File dei messaggi
I messaggi (di errore, informativi, ecc.) sono archiviati in appositi file messaggi (*MSGF) per applicazione, il cui nome è codificato come MSGaa, dove _aa_ è il codice dell'applicazione (un'eccezione è il MSGBA corrispondente all'applicazione B£).

# File di Dizionario
Per ottenere la **tipizzazione di un campo** è necessario indicare _tipo e parametro dell'oggetto nelle definizioni dei campi nel TEXT() .
In questo modo il sitema può identificare il tipo del campo e associare ad esso attributi e funzioni dell'oggetto senza indicazioni specifiche nel file video.

Esempio di tipizzazione di un campo data : 
>  A            DTIA           8  0       TEXT('Data Inizio Ammortamento

 A                                      D8*YYMD')


# /COPY
La codifica delle /COPY di smeup si basa su un suffisso di 4 caratteri :  il primo carattere è sempre il carattere "£", mentre gli altri caratteri a seconda della funzione che la /COPY svolge può assumere differenti codifiche : 
 * se la /COPY svolge una funzione specifica di un'applicazione i successivi 3 caratteri corrisponderanno al codice dell'applicazione, seguita da una lettera o un numero
 * se la /COPY è la definizone di una tabella i caratterei successivi saranno "TAB" ed il codice settore tabella
 * se la /COPY svolge una funzione di interfaccia i caratteri successivi saranno "I" o "IF" seguiti da caratteri che identifichino l'oggetto dell'interfaccia
 * se la /COPY svolge una funzione di carattere generale i caratteri successivi saranno "G" seguito da un numero di due cifre o un codice di tre lettere che possa rimandare in qualche modo alla funzione della /COPY
Su codifica dei caratteri successivi si possono trovare delle eccezioni, ma non esistono eccezioni al carattere "£" iniziale.
Se la /COPY, oltre ai succitati caratteri, riporta come caratteri finali "DS", "D", "E", "I" significa che contiene le specifiche di definizione utilizzate dalla /COPY corrispondente che non presenta tali desinenze.
Tutte le variabili utilizzate da una /COPY sono codificate riportando come primi 4 caratteri gli stessi caratteri del codice della /COPY cui appartengono. Perciò in Sme.up se una variabile ha un codice che inizia per "£" si ha la certezza che sia contenuta in una /COPY, e che questa dovrebbe essere identificabile dai 3 caratteri successivi della variabile.

Creazione di un nuovo oggetto : 
- [Creare un nuovo oggetto](Sorgenti/MB/DOC/A£BASE_01I)
