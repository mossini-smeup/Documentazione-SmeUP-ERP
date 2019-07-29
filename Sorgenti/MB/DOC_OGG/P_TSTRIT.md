# Gestione tabelle
## Controllo e lettura tabelle
La lettura ed il controllo delle tabelle vengono eseguiti tramite routines esterne, per i vari ambienti applicativi in
cui può essere inserito il programma. Per l'ambiente SMEUP, esistono inoltre routines adibite alla ricerca alfabetica
dei settori e dei subsettori.
## Controllo tabelle
Qualora sia sufficiente controllare l'esistenza di un elemento di tabella, eseguire la ricerca alfabetica, ed
ottenerne la decodifica, si usano le routines £RITxx, dove xx è il prefisso dell'ambiente (AC : Acg, SM : Smeup, SG :  San
Giorgio, SE : Seltering).
In input si passa :  il settore £RITST (5) e l'elemento £RITEL (15), e, nel caso di ambiente SMEUP, il campo £RITMA (1)
diverso da blanks se non è abilitato il passaggio dalla ricerca alfabetica alla manutenzione, ed il campo £ITRS (1),
che, se diverso da blanks, fa eseguire la ricerca dei settori.
In output si ottiene, oltre a £RITEL riempito dalla ricerca alfabetica, la descrizione dell'elemento £RITDS, (30 :  nel
caso in cui l'ambiente non preveda un campo esplicito di descrizione, vengono considerati tali i primi 30 caratteri
del contenuto della tabella) l'indicatore 35 acceso per elemento non trovato ed il 36 acceso per effettuata ricerca
alfabetica.
## Lettura tabelle
Nel caso in cui è necessario acquisire il contenuto di un elemento di tabella, si usano le routines £LETxx, dove xx è
il prefisso dell'ambiente (AC : Acg, SM : Smeup, SG :  San Giorgio,
SE : Seltering).
In input si passa :  il settore £RITST (5) e l'elemento £RITEL (15).
caratteri del contenuto della tabella) e l'indicatore 35
In output si ottiene la descrizione dell'elemento in £RITDS (30 :  nel caso in cui l'ambiente non preveda un campo
esplicito di descrizione, vengono considerati tali i primi
acceso per elemento non trovato.
Per ogni ambiente è inoltre necessario definire il file tabelle interessato e la struttura del tracciato della
tabella.
Lettura tabelle ACG
Si deve definire il File ANTAB01L, e la DS esterna del settore da leggere. Dopo il richiamo con esito positivo della
routine, si deve inoltre muovere il campo di data base
XDTAB nella DS esterna per riempirne i sottocampi.
Lettura tabelle Selternig
Si deve definire il File TABFA03L (descritto internamente) e, nelle specifiche 'I', la /COPY QCPYSRC,£TABxxx del
settore xxx da leggere.
Lettura tabelle S.Giorgio
Si deve definire il File GENTB01L, e la DS esterna del settore da leggere. Dopo li richiamo con esito positivo della
routine, si deve inoltre muovere il campo di data base
TDTAB nella DS esterna per riempirne i sottocampi.
Lettura tabelle SMEUP
Si deve definire il File TABEL01L (descritto internamente) e, nelle specifiche 'I', la /COPY SRC,£TABxxx del settore
xxx da leggere.
## Ricerca alfabetica settori SMEUP
La routine £RISET esegue la ricerca alfabetica dei settori : 
si imposta in £COSET (3) il codice del settore :  di ritorno si riceve, sempre in £COSET, il settore selezionato, in
£DESET (30) la relativa descrizione, l'indicatore 35 acceso per elemento non trovato ed il 36 acceso per effettuata
ricerca alfabetica.
## Ricerca alfabetica subsettori SMEUP
La routine £RITSS esegue la ricerca alfabetica dei subsettori :  si imposta in £COSET (3) il codice del settore ed in
£COSBS (2) il codice del subsettore :  di ritorno si riceve, sempre in £COSBS, il subsettore selezionato, in £DESBS (30)
la relativa descrizione, l'indicatore 35 acceso per elemento non trovato ed il 36 acceso per effettuata ricerca
alfabetica.
# Controllo specifico settori tabelle
Qualora i controlli formali previsti nella gestione tabelle parametriche non fossero sufficienti (ad esempio si
volessero attivate controlli incrociati), oppure si presentasse la necessità di riempire un campo di tabella in
funzione di altri (ad esempio :  si digita un ordine cliente e si vuol acquisire in tabella il codice del cliente), è
possibile relizzare un programma di controlli che viene eseguito in cascata ai controlli formali della manutenzione
tabelle. Tale programma va specificato nella definizione del settore.
Per realizzarlo, bisogna partire dallo scheletro B£T000, contenuto in SMESRC/SRC.
Il suo nome dovrà essere B£Txxx, dove xxx è il nome del settore interessato. Deve essere stata costruita la /COPY
della DS della tabella.
Si devono specificare gli eventuali files interessati e sostituire xxx con il nome del settore.
I campi della tabella sono presenti in questo programma con lo stesso nome che hanno nella /COPY della tabella.
I controlli sull'elemento si inseriscono nella routine
CTRELE, in cui si tolgono gli asterischi alla parte di controllo errore.
I controlli sui rimanenti campi si inseriscono nella routine
CTRALT, in cui si tolgono gli asterischi alla parte di controllo errore. L'indice nella schiera errori di ogni campo
(ERC,XX), è riportato nella /COPY delle specifiche 'I' della tabella.
E' possibile anche modificare i campi :  ad esempio la descrizione dell'elemento può essere formata da un insieme di
altri campi, oppure un campo è la decodifica o un attributo di un altro ( ad esempio, il codice articolo e la sua
classe). Va tenuto presente che essi non passano più per i controlli formali predefiniti e quindi si potrebbero
introdurre anomalie nei dati.
nel qual caso viene riemesso il formato di manutenzione
C'è inoltre la possibilità di restituire acceso l'indicatore
tabelle :  può servire quando viene fatta per la prima volta una decodifica (nell'esempio precedente, se la classe
dell'articolo non era presente o era diversa da quella che si sta inserendo).
