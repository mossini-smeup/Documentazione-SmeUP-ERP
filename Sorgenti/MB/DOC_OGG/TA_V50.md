# V50 - Fatturazione Elettronica
 :  : DEC T(ST) K(V50)
## OBIETTIVO
Definisce i parametri generali relativi alla fatturazione elettronica PA e B2B.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$DESC Note
 :  : FLD T$V50B
Se impostato, il provider indicato viene usato per le funzionalità di invio della fatturazione
elettronica al SdI per mezzo dell'intermediario, così come per l'inclusione degli allegati tramite
£H80 e per il download dei codici ufficio PA.
Se non impostato i programmi risalgono sulla tabella LOB, rispettivamente sul contesto K11 e
successivamente ** per l'invio e sul contesto H80 e successivamente ** per allegati e download
codici ufficio PA.
 :  : FLD T$V50H
Se impostato attiva il controllo di validità del codice univoco ufficio PA durante l'inserimento
dell'estensione £51 del cliente.
 :  : FLD T$V50I
Indica a quale ente sulla testata appartengono i riferimenti di fatturazione elettronica (£51)
da utilizzare nella generazione dell'xml del documento. Il programma risale sull'ente di
fatturazione se i riferimenti non sono reperiti sull'ente indicato in questo campo.
 :  : FLD T$V50T
Se impostato attiva il controllo di congruenza tra i dati della fattura su V5 e quelli estratti
in EDSEND durante la fase di generazione dell'xml. Gli errori vengono segnalati in una stampa
e in un record di edsend con il tracciato EDFEIT08
 :  : FLD T$V50M
Indica il progressivo di invio dell'ultimo file xml generato. È un campo alfanumerico di 5 caratteri
che viene generato durante la creazione dell'edsend e viene impostato sulla tabella dal programma
che lo calcola (V5ED04B). Se vuoto (primo invio) il primo progressivo è 'AAAAA'. Non esiste nessuna
tabella CRN per la gestione perchè non è un numeratore ma un progressivo alfanumerico di 5 caratteri
che deve essere indicato nel file xml.
 :  : FLD T$V50N
Indica la exit V5ED04B_xx (xx è il suffisso indicato nel campo) attivabile nella generazione del
file edsend a partire dal documento V5.
Tramite la exit è possibile modificare il record di edsend prima che venga scritto, impedirne la
scrittura e aggiungere record di edsend. Fare riferimento alla documentazione della exit per
ulteriori informazioni sul funzionamento

 :  : FLD T$V50O
Indica il suffisso del programma (V5_061A_xx dove xx è il suffisso) utilizzato per la trasmissione
del file xml a SdI. Impostare 01 per l'invio tramite intermediario Abletech.

Questa indicazione attiva anche : 
* la scheda avente medesimo nome dell'exit (V5_061A_xx), atta a visualizzare gli eventuali log di dettaglio relativi all'invio di una particolare fattura.
* il servizio V5_082A_xx atto ad elaborare l'aggiornamento degli esiti per tramite dell'intermediario specifico. Se non si ha Abletech si può guardare il V5_082A_01 come esempio.
* il programma V5_082B_xx atto ad controllare l'avanzamento degli esiti dell'intermediario specifico. Se non si ha Abletech si può guardare il V5_082B_01 come esempio.
* il programma e la scheda V5_082C_xx atte a mostrare il dettaglio delle informazioni di esito ritornate dall'intermediario specifico. Se non si ha Abletech si possono guardare i sorgenti V5_082C_xx.

 :  : FLD T$V50P
Indica se e in che condizioni scrivere il blocco <DatiOrdineAcquisto> nell'xml.
NB. Non è possibile non indicare uno fra ordine di acquisto o contratto, perchè obbligatori
per la trasmissione di CIG e CUP nel file xml.
 :  : FLD T$V50L
Indica come (da dove sul documento V5) reperire le informazioni relativa all'ordine di acquisto.
NB. Non è possibile non indicare uno fra ordine di acquisto o contratto, perchè almeno uno
dei due blocchi è necessario per la trasmissione di CIG e CUP nel file xml.
 :  : FLD T$V50Q
Indica se e in che condizioni scrivere il blocco <DatiContratto> nell'xml.
NB. Non è possibile non indicare uno fra ordine di acquisto o contratto, perchè obbligatori
per la trasmissione di CIG e CUP nel file xml.
 :  : FLD T$V50R
Indica come (da dove sul documento V5) reperire le informazioni relative al contratto.
NB. Non è possibile non indicare uno fra ordine di acquisto o contratto, perchè almeno uno
dei due blocchi è necessario per la trasmissione di CIG e CUP nel file xml.
 :  : FLD T$V50X
Forza la scrittura della commessa in caso non sia stato reperito ordine di acquisto o contratto
 :  : FLD T$V50U **Capit.Note Fatt.DODR**
Inserire un capitolo note specifico da esportare su EDSEND in fase di fatturazione elettronica.
Usare ** per prendere tutti i capitoli note relativi alla fattura.
 :  : FLD T$V50V
Inserire un capitolo note specifico da esportare su EDSEND in fase di fatturazione elettronica.
Usare ** per prendere tutti i capitoli note. L'ente del documento è l'ente di fatturazione
 :  : FLD T$V50Z
Permette di decidere la data indicata come "Data documento" sulla fattura elettronica.
Se impostato il valore '1' viene usata la data dell'ultima bolla presente nella fattura.
Altrimenti viene usata la data di protocollazione della fattura (campo T§DFAT).
