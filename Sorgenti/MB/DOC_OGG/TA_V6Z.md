# V6Z - Piano Anticipi
 :  : DEC T(ST) K(V6Z)
## OBIETTIVO
Definisce le modalità di calcolo degli anticipi automatici da corrispondere agli agenti.
## CONTENUTO DEI CAMPI
 :  : FLD T$V6ZA **Tipo Valore Anticipo**
Indica la modalità di calcolo dell'anticipo, a meno che non sia stato specificato un piano di liquidazione.
Esso può assumere i seguenti valori : 
- "1"= _Importo Fisso_ :  viene corrisposto un anticipo per l'importo fisso stabilito contrattualmente, indicato nel campo **Valore Anticipo**;
- "2"= _% su Pagato_ :  viene corrisposta una % (indicata nel campo valore anticipo) su quanto pagato dal cliente nel dato periodo;
- "3"= _% su Fatturato_ :  viene corrisposta una % (indicata nel campo valore anticipo) su quanto fatturato nel dato periodo.
 :  : FLD T$V6ZB **Valore Anticipo**
Vedi T$V6ZA

 :  : FLD T$V6ZC **Tipo Provvigioni**
Indica il tipo provvigione da attribuire all'anticipo.
**NOTA BENE** :  questo campo è fondamentale per identificare, attraverso il campo tipo imponibile, indicabile nella tabella del tipo, se l'anticipo rappresenta : 
* un minimo garantito (l'anticipo verrà conguagliato solo per l'importo delle provvigioni l'importo in eccesso non verrà mai conguagliato).
* un importo fisso (l'anticipo non verrà in assoluto, mai conguagliato)
* un anticipo (l'anticipo verrà sempre conguagliato e l'eccesso rispetto all'importo delle provvigioni viene riportato al periodo di conguaglio successivo).
Tale indicazione si traduce nella valorizzazione del flag 12 della provvigione a valore 3, 4 o 1.

**NOTA BENE 2** :  questo campo è inoltre fondamentale per comprendere se in un dato periodo l'anticipo è già stato calcolato o meno. In caso di esecuzioni multiple della liquidazione, solo la presenza di una provvigione con il tipo qui indicato disattiva il ricalcolo dell'anticipo. E' quindi opportuno che ogni tipo anticipo abbia un suo tipo provvigione specifico.

 :  : FLD T$V6ZD **Suff. exit pgm calc.**
Permette di indicare i pgm di exit "V5PR04C_" attraverso cui viene determinato l'importo dell'anticipo.

 :  : FLD T$V6ZE **Periodicità Calcolo**
Indica la cadenza in base a cui vengono calcolati gli anticipi. Può assumere i seguenti valori : 
- " "= Nel caso in cui all'agente vengano liquidate le provvigioni con periodicità maggiore al mese, gli anticipi vengono liquidati per i mesi in cui l'agente non percepisce alcun compenso e stornati nel mese di liquidazione;
- "1"= Le provvigioni vengono erogate nello stesso periodo in cui avviene la liquidazione e stornate nel periodo successivo (es. anticipo in base al fatturato e poi liquido in base all'incassato).
- "2"= Nel caso in cui all'agente vengano liquidate le provvigioni con periodicità maggiore al mese, gli anticipi vengono liquidati per tutti i mesi anche nel mese in cui l'agente percepisce il compenso. Nota bene :  con questo metodo non viene fatto alcun conguaglio con la liquidazione periodica.

 :  : FLD T$V6ZF **Inclusione Note**
Solo se questo campo viene valorizzato, quando è previsto che il calcolo dell'anticipo sia fatto su una base del fatturato o dato dell'incassato, in tale base di calcolo vengono incluse anche le eventuali note di accredito del periodo.

