# NSI - NOTE-Informazioni
## CONTENUTO DEI CAMPI
 :  : FLD T$INTE __Intestazione/percorso__
Descrive l'intestazione che apparirà a video, per descrivere il significato della nota e fornire una guida per
l'immissione dei dati.
Se il tipo di informazione è collegata ad un documento OFFICE, questa intestazione contiene il percorso (CARTELLA) che,
unito con quanto specificato nella tabella NSC, indica dove si trova il documento richiesto.
Se il tipo informazione è invece legato alla gestione con
Windows, allora il campo PERCORSO ha lo stesso significato di quello della gestione Office/400, ossia è il percorso
dove si trova il file.
 :  : FLD T$NSIA __Vista editor note__
Definisce la modalità con cui viene aperto l'editor di immissione/modifica delle note.
Se non impostato viene utilizzato l'editor 5250 vista 24x80 caratteri.
Se impostato il valore 1, viene utilizzato l'editor 5250 vista 27x132 caratteri.
Se impostato il valore 2, e la sessione in esecuzione è dal client Loocup, viene aperta una finestra grafica con la gestione delle note (Scheda OGBASE)
Se impostato il valore 3, e la sessione in esecuzione è dal client Loocup, viene aperta una finestra grafica con l'editor di testo (componente EDT).**Sconsigliata e obsoleta**
 :  : FLD T$NSID __Numero caratteri massimi visualizzabili__
Se impostato, imposta visivamente un limite di digitazione di caratteri per riga, in modo da dare indicazione
all'operatore di quanti caratteri sono ammessi per il tipo nota. I caratteri digitati oltre tale limite vengono
evidenziati con un attributo colorato lampeggiante, anche se comunque memorizzati.
In base all'impostazione scelta nel campo "Vista a 132 caratteri", il limite massimo di caratteri visualizzabili viene
gestito nei seguenti range : 
- visualizzazione standard :  da 1 a 70 caratteri.
- visualizzazione estesa :  da 1 a 100 caratteri.
 :  : FLD T$NSIE __Suffisso pgm exit di gestione commenti__
Questo campo dovrebbe normalmente essere usato in alternativa al "Numero caratteri max".
Se impostato, la manutenzione delle note viene demandata al pgm esterno B£AMC1_a (dove "a" è il contenuto di
questo campo), che utilizza un formato video con lunghezza righe diversa dallo standard.
Il prototipo del pgm è B£AMC1_X, a cui si rimanda per ulteriori informazioni.
 :  : FLD T$TACO __Tabella di controllo__
Utilizzata per i controlli se manca il nome del programma nel parametro successivo. Ciò indica che il contenuto della
riga di nota dovrà essere controllato secondo le caratteristiche della tabella indicata.
**NB** :  Funzione prevista ma non attiva
 :  : FLD T$PGCO __Programma di controllo__
È un programma strutturalmente "SEMPLICE" che gestisce una stringa di dati per dei controlli specifici. Il programma
può essere scritto e/o modificato successivamente.
 :  : FLD T$LNLS __Lettura note di livello superiore__
Quando si immettono nuove note, è possibile riprendere da un codice di livello superiore. Vengono rimossi di seguito i
codici non bianchi, fino a che si trovano delle note.
 :  : FLD T$PROT __Livello di protezione__
Tre caratteri che permettono di presentare il formato video con le tre colonne
 :  : FLD T$NSIB __Gestione avanzata flag__
Se impostato a '1', quando scelgo l'opzione 'GR' o 'G' nella gestione delle note, ci si aspetta che il "flag nota"
dell'archivio NTSTRU0F venga restiuito dal programma di controllo (T$PGCO) in un campo aggiuntivo della PARM.
Se impostato a *blanks, viene mantenuta la compatibilità con il passato, cioè questo flag viene passato nel
centesimo byte (l'ultimo) della riga di nota.
 :  : FLD T$NSIC __Conferma abbandono__
Se impostato a '1', in caso di uscita dall'editazione con il tasto F12 o F03, verrà presentata una finestra
di conferma di uscita senza memorizzazione. Il medesimo campo è presente nella tabella NSC Contenitore Note.
L'eventuale impostazione a '1' nella tabella NSC verrà ereditata da tutti gli elementi della tabella NSI gestiti
per quel capitolo
