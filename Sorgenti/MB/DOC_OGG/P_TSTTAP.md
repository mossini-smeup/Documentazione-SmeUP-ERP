# TRACE'N PLAY
Scopo di questa /COPY è di gestire una Trace sui programmi : 
Inserita all'interno del codice dei programmi, in zone 'significative' essa 'lascia una traccia' sul file B£TAPL0F multimembro e consente quindi controlli di prestazione dei programmi.
Esiste poi un servizio di loocUp che ne consente la visualizzazione e interrogazione (CTRL+F9 , scheda _Trace'n play_).

## STRUTTURA
### Il file B£TAPL0F

Si tratta di un file multimembro in cui ogni membro assume il nome del codice utente. Questo significa che ogni utente alimenta e gestisce una propria sezione del file.
Il file viene generato nella libreria SMEUPUIDQ, temporanea... essa viene svuotata giornalmente da un processo schedulato che garantisce il contenimento dei dati.
Ogni record del file viene identificato da tre elementi (chiave del file) : 


- Nome della trace               (£TAPNom)
- Ora della trace                  (£TAPTim)
- Progressivo automatico


Il nome della trace è una semplice stringa descrittiva.
L'ora se non impostata è quella all'atto di creazione della trace. Può essere forzata dall'esterno e può non essere un time, questo consente di sovrapporre ogni volta la trace alla sua precedente e di tenere su file solo l'ultima trace generata.
Se nell'inizializzazione indico nella variabile £LOGTra il valore LOG attivo la stampa forzando per tale trace la condizione della tabella PGM per l'attivazione del log.

### Variabili
La £TAPD definisce la lista di variabili per la Trace


-  DS di input...
-- £TAPDI          	DS         	 2500
-- £TAPFU                       	10          Funzione
-- £TAPME                       	10          Metodo
-- £TAPNom                    	30          Nome stampa
-- £TAPTim                      	10          Tempo/Ora
-- £TAPLiv                      	30          Livello
-- £TAPTri                      	30          Tipo riga
-- £TAPTra                      	30          info extra!
-- £TAPPar                     	256          Attributi
-- £TAPStr                    	2048          Contenuto
- DS di output...
-- £TAPDO     	 DS            12
-- £TAP35                		1          Indicatori
-- £TAP36                        	1	"


Le variabili livello/tipo riga e parametri specificano la tipologia della trace.

Il livello consente di disporre le informazioni in maniera gerarchica.
Le informazioni a livelli di profondità maggiore specificano le info dei livelli inferiori.
Sono disponibili 6 livelli in tutto.
E' previsto il livello '0' per reinizializzare la memoria... va usato alla prima chiamata di aggiunta riga di trace.

Si esemplifica ora come viene generato l'albero dei livelli.
I nodi vengono agganciati al nodo precedente di livello superiore.
Si ponga di aver creato la seguente sequenza di livelli : 


- aggiunta nodo di Livello 1
- aggiunta nodo di Livello 2
- aggiunta nodo di Livello 2
- aggiunta nodo di Livello 2
- aggiunta nodo di Livello 1
- aggiunta nodo di Livello 2
- aggiunta nodo di Livello 3
- aggiunta nodo di Livello 3
- aggiunta nodo di Livello 1
- aggiunta nodo di Livello 2


 Si otterrà quindi : 

>         1                     2                  3      Liv. 1
   ______|_______              |                  |
  /      |       \             |                  |
 1.1    1.2     1.3           2.1                3.1     Liv. 2
                          _____|______
                         /            \
                       2.1.1         2.1.2               Liv. 3


**La struttura dell'albero** generato non **dipende** quindi da proprietà di tipo dinamico, ma semplicemente **dall'ordine di sequenza con cui vengono aggiunti i livelli.**


  Il tipo riga serve a qualificare la tipologia di informazione.

  Gli attributi assegnano a ciascuna riga una proprietà in base alla quale è possibile eseguire dei filtri sui record.
  La sintassi per l'assegnazione di un attributo è la seguente : 

EVAL      £TAPPar='NomeAttributo'.TpParam=' "Valore" '
	
>     C                   EVAL      £TAPPar='Scadenza.D8*YYMD="'                        .
     C                             +%TRIM(%EDITW(S5SCAD : '    /  /  '))+'" '                 .
     C                             +'Pagamento.TAPAG="'+%TRIM(S5COPA)+'" '


 :  : PAR L(TAB)
- 'NomeAttributo' | stringa che indica il nome a piacere per l'attributo che verrà visualizzato nella scheda del Trace'n play
- TpParam | Tipo ed eventuale parametro di un oggetto SMEUP corrispondente all'attributo
- ' "Valore" ' | Stringa racchiusa tra " che contiene il valore dell'attributo associato alla riga



E' possibile **specificare più attributi per record** (come da esempio) accodando gli attributi separati da spazio.

Si indica il
  Livelli, tipo riga e attributi sono poi usati come filtri nel servizio di analisi della trace su LoocUp.


## FUNZIONI e METODI

Di seguito l'elenco dei metodi e delle funzioni previste dalla Trace : 


- LOG       	Gestione Log
-- INI       	Inizializzazione
-- CLO       	Chiusura
-- ADD       	Aggiunta riga di log
- DEL       	Cancellazione
-- ALL       	Tutto
-- NAM       	Per nome stampa
-- TIM       	Per ora

Prima di poter eseguire l'aggiunta di riga di trace bisogna richiamare metodo di inizializzazione che serve a svuotare memoria e reimpostare il puntatore del file.
Il metodo ADD serve ad aggiungere riga di trace, CLO a chiudere l'emissione della trace.
I metodi DEL di cancellazione cancellano rispettivamente tutto il contenuto del membro a proprio nome utente, i record con nome stampa indicato e con ora (o valore forzato) impostata!

E chiaro che la visibilità delle azioni suddette sul file è relativa solo al proprio sottomembro utente di accesso.

_1_Esempi di chiamata : 

**Creazione/Chiusura/Eliminazione log**
>     C                   EVAL      £TAPFU='INI'		
     C                   EVAL      £TAPME='NAM'
     C                   EVAL      £TAPNom=<'DescrizioneLog'>
     C                   EXSR      £TAP


**Aggiunta righe log**
>     C                   EVAL      £TAPFU='LOG'
     C                   EVAL      £TAPME='ADD'
     C                   EVAL      £TAPLiv=<'numerolivello'>
     C                   EVAL      £TAPTRi=<'TipoRiga'>
     C                   EVAL      £TAPTra=*BLANKS
     C                   EVAL      £TAPPar=<'NomeAttributo'.TpParam=' "Valore" '>
     C                   EVAL      £TAPSTr=<'StringaLog'>
     C                   EXSR      £TAP

