# D5E - Causale movimento di dettaglio
 :  : DEC T(ST) K(D5E)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
Codice di 6 caratteri identificativo del passo.
È possibile creare degli elementi xxxxxx.n (dove xxxxxx è il codice di un altro elemento ed n è un codice progressivo) nei quali specificare solo il metodo origine e destinazione.
Per questi elementi, la ricerca del contesto/tema e delle chiavi del record non viene eseguita e viene assunta quella dell'elemento xxxxxx. In questo modo viene velocizzata la ripresa e non bisogna replicare eventuali elementi della tabella D5M, nel caso in cui il record sia il medesimo.
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$D5EA **Contesto**
Contesto del D5COSO (tabella D5S) nel quale scrivere il valore.
Nel caso in cui venga specificato ** , viene utilizzato il contesto immesso nell'elemento della tabella D5R
 :  : FLD T$D5EB **Tema**
Tema del D5COSO (tabella D5O, SS dipendente dal contesto) nel quale scrivere il valore.
Nel caso in cui venga specificato ** , viene utilizzato il tema immesso nell'elemento della tabella D5R
 :  : FLD T$D5EC **Metodo determinazione origine**
Indica quale valore, riportato dal programma di ripresa dei sistemi conferenti, deve essere utilizzato nel passo.
*VAL :  uno dei dieci valori riportati dalla ripresa.
QTA :  quantità riportata dalla ripresa.

 :  : FLD T$D5ED **Parametro determinazione origine**
Indica quale dei dieci valori deve essere considerato.
Leggere gli help relativi ai vari programmi di ripresa, per vedere quali valori sono riportati e in che posizione.
Nel caso della quantità va lasciato in bianco.
 :  : FLD T$D5EE **Metodo determinazione destinazione**
Permette di individuare in quale dei 99 valori del D5COSO bisogna scrivere il dato.
*BLANKS :  numero dell'indice.
*IND    :  sottosettore ed elemento della tabella IGI
*VDS    :  indice specificato in un parametro di una voce di spesa (elemento della D5V)
*OAV    :  indice specificato in un OAV dell'oggetto contesto
*PAR    :  indice specificato in un parametro di un oggetto della chiave del record
*PA2    :  indice specificato in un parametro di uno dei dieci oggetti riportati dal programma di ripresa
*CAT    :  indice specificato in un campo di un elemento della tabella D5U. L'elemento è specificato in un parametro di uno dei dieci oggetti riportati dal programma di ripresa.

*CA2    :  Sviluppo
*CAO    :  indice specificato in un parametro di un oggetto derivato applicando l'algoritmo di ricerca specificato nell'elemento della tabella D5M (sottosettore uguale a quello della D5E) con codice cosi composto : 
>codice elemento D5E + '_' + *CAO (per esempio BOF001_*CAO).
Questo metodo è utile nel caso in cui l'indice sia legato ad una caratteristica di uno degli oggetti passati e non al singolo oggetto.

*D5MOVI :  indice passato dal programma di ripresa. Uno degli oggetti sarà quindi di tipo TAIGIxx, dove xx è il sottosettore specificato nel tema, a meno che la posizione dell'oggetto non venga specificata esplicitamente nel parametro.
 :  : FLD T$D5EF **Parametro determinazione destinazione**
_Metodo_
*BLANKS :  numero dell'indice
*IND    :  pos. 1-2 :  SS della IGI pos. 3-4 :  Elemento della IGI

È equivalente al metodo *BLANKS tranne che permette di utilizzare la ricerca degli elementi della IGI e risulta più esplicativo in quanto viene specificato anche il sottosettore.
*VDS    :  pos. 1-3 :  C£E del parametro dove è contenuta la voce di spesa; pos. 4-6 :  B£N del parametro; pos. 7-9 :  B£N della voce di spesa dove è contenuto l'indice della tabella IGI.
_7_N.B. :  La categoria della voce di spesa deve essere D5V.

*OAV    :  OAV
*PAR    :  pos. 1-3 :  C£E del parametro; pos. 4-6 :  B£N del parametro
*PA2    :  pos. 1-3 :  C£E del parametro; pos. 4-6 :  B£N del parametro
*CAT    :  pos. 1-3 :  C£E del parametro; contenente la categoria; pos. 4-5 :  SS della D5U; pos. 6-7 :  Numero del campo dell'elemento della D5U
_7_N.B. :  La categoria di un oggetto ha B£N = £01 fissa.
*CAO    :  pos. 1-3 :  C£E del parametro; pos. 4-6 :  B£N del parametro
*D5MOVI :  Indice da 01 a 10. Specifica in quale dei 10 oggetti del D5MOVI è presente l'indice da aggiornare.

L'oggetto deve essere un numero o una stringa numerica con valore compreso fra 01 e 99.
In questo caso non viene effettuato alcun controllo sul tipo e sul parametro dell'oggetto, ma solo la trasformazione del codice in un valore numerico lungo 2 con 0 decimali. Al contrario, nel caso in cui il parametro sia lasciato in bianco il programma cercherà nel D5MOVI un oggetto di tipo TAIGIxx dove xx è il sottosettore della IGI specificato nel tema.
 :  : FLD T$D5EG **Conserva relazione**
Se impostato a '1' salva le informazioni riguardanti la ripresa ed il valore nel file D5RECO0F. Sarà poi possibile effettuare l'esplosione e l'implosione dei valori nella visualizzazione dei record del D5COSO.
_7_N.B. :  nel salvare le relazioni possono venire creati moltissimi record e quindi creare problemi di spazio.
 :  : FLD T$D5EH **Pre-cancellazione ?**
Se impostato a '1' viene eseguita una cancellazione di tutti i dati pre-esistenti per il contesto e per il tema, specificati (o ereditati dalla D5R) per il periodo in cui viene lanciato il flusso.
_2_Questa opzione va messa esclusivamente sulla prima azione che scrive un contesto e tema.
## NOTE
Per reperire i codici degli oggetti, nei quali salvare i dati, esistono 2 possibilità : 
1. se non esiste nella tabella D5M (algoritmi di validazione) un elemento associato all'elemento della D5E (l'associazione viene fatta grazie alla codifica dell'elemento della D5M, vedere l'help di questa tabella per ulteriori informazioni), l'oggetto viene cercato in uno degli oggetti riportati dal programma di ripresa sistema conferente, confrontando i tipi/parametri. Nel caso esistano più oggetti validi viene utilizzato il primo.
2. utilizzare un algoritmo di ricerca (elemento della tabella D5M).
## ESEMPIO
Scrittura dei valori riportati da una ripresa da MPS di budget per voce di spesa, in uno schema dei costi per centro di costo.
Il contesto del D5COSO sarà CC, il tema, supponiamo, COS.
Il programma di ripresa da MPS pone il valore nel primo valore del D5MOVI. Il metodo di determinazione origine sarà, quindi, *VAL con parametro 01.
Supponendo che l'indice della IGI, nel quale scrivere il valore, sia dipendente dalla voce di spesa e che, quindi, sia specificato in un suo parametro (per esempio D5V D5A), il metodo di determinazione della destinazione sarà *PA2 con parametro D5VD5A.
Nel caso in cui la vista del piano del budget si sviluppi per voce di spesa e centro di costo, non sarà necessario utilizzare un algoritmo di ricerca (elemento della D5M) perchè la ripresa da  MPS riporterà come oggetti sia la voce di spesa sia il centro di costo (cioè gli oggetti indicati nella vista) e quest'ultimo verrà utilizzato come codice dell'oggetto contesto.
Se, invece, la vista si sviluppa solo per voce di spesa, per individuare in che centro di costo scrivere il valore, sarà necessario utilizzare un algoritmo.

_9_Esempio :  l'algoritmo legge un parametro della voce di spesa che ne indica i centri di costo di appartenenza, con relativa distribuzione.
