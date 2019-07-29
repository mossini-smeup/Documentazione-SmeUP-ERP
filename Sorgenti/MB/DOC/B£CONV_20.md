# LIBRERIA
I pgm di tutte le conversioni sono contenuti nella libreria**SMECON** (la versione aggiornata di pgm è disponibile sull'SRVAMM.SMEUP.COM); per ogni conversione è predisposto un file sorgente apposito il cui codice è dato da : 
"codice ambiente partenza" + "_" + "codice ambiente arrivo" .
I codici degli ambienti sono fissi e sono codificati dalla tabella *CNAA, perciò ad esempio il file sorgente delle conversioni da ACG a SMEUP è denominato A7_SM.

 :  : DEC T(ST) P() K(*CNAA)
   In tale file è possibile trovare i seguenti tipi di sorgenti : 
   - Programmi
   - File
   - Testo
# PROGRAMMI
## Codifica
I pgm di conversione sono orientati alla conversione di un file o di una tabella, per evidenziarne la funzione ne è stata assunta una precisa codifica : 

   a) pgm di conversione di un file
      Ambiente partenza + primi 6 caratteri del file di arrivo + Ambiente arrivo
      es. il BRARTI0F da ACG a SMEUP ==> A7BRARTISM

   b) pgm di conversione di una tabella
      Ambiente partenza + "TA_" + Codice Settore + Ambiente arrivo
      es. la C5B da ACG a SMEUP ==> A7TA_C5BSM

E' da tenere comunque presente che tali regole non sono assolutamente rigide per quel che riguarda la codifica centrale del pgm, in quanto per convertire un file possono essere necessari più programmi, oppure per convenienza più file vengono convertiti contemporaneamente nello stesso pgm o ancora la conversione viene orientata ad oggetti che non sono nè file, nè tabelle.

## Assunzioni
Questi pgm, ad esclusione forse di quelli della contabilità, per poter avere comunque una valenza generale, sono costretti a fare determinate assunzioni che potranno poi essere modificate per coprire le specificità del cliente (vedi es. nel caso di una conversione a Smeup il concetto di tipo articolo non sempre è presente dall'ambiente di partenza).

Tali assunzioni vengono fissate nel modello nella tabella B§VCV nella tabella B§VCV. Queste assumono la seguente codifica : 
 - "_&_"+XX+"_"+3 caratteri numerici progressivi
Dove al posto di XX ci va o ££ per indicare una variabile che può avere una valenza generale per tutte le conversioni (es. codice azienda) o il codice di un ambiente origine per indicare una variabile che ha valenza per una conversione specifica. Es._&_££_001 è una variabile generale _&_A7_001 è una variabile che viene utilizzata solamente per la conversione da ACG.
 :  : DEC T(ST) P() K(B§VCV) I(_9_ B§VCV - Variabili Conversioni    >>)

Queste variabili vanno utilizzate all'interno dei pgm tramite la la /COPY £P001 che ha la doppia funzionalità di renderne semplice l'utilizzo nonchè di renderne visibile lo stesso nelle schede d'analisi di Loocup.
 :  : INI  _9_Help Tecnico £P001  >>
 :  : CMD CALL B£VED0 PARM('£P001' 'QPROGEN' '' 'H' '0')
 :  : FIN

## Documentazione
La descrizione delle assunzioni, e di ogni qualsiasi altra nota rilevante in merito allo svolgimento del pgm viene scritta all'inizio del programma utilizzando delle righe di commento precedute dalle lettere **"HD"** tali lettere permettono infatti di riconoscere le specifiche commentate come note tecniche.

Di seguito un esempio di utilizzo della documentazione tecnica nel pgm di conversione dei cespiti da ACG a SMEUP

 :  : INI _9_ Visualizza documentazione tecnica 
 :  : CMD CALL B£VED0 PARM('A7A5CESPSM' 'A7_SM' 'SMECON' 'H' '0')
 :  : FIN

## Alias
Con la conversione si presenta a volte anche l'opportunità di poter attuare la ricodificazione di alcuni codici. Tale ricodificazione è attuabile a standard tramite l'utilizzo degli alias.

Per attivare tale funzione è necessario seguire i seguenti passi : 

**1.**Inserire l'elemento della C£K che definisce la struttura degli alias (è consigliabile riprendere il contesto apposito previsto dal modello).
 :  : DEC T(ST) P() K(C£K) I(_9_     C£K - Contesti Alias  >>)

**3.**Applicare nei pgm di conversione, per tutti i codici per i quali abbia senso poter attuare una trascodifica, l'utilizzo della procedura £P002 che permette di servirsi degli alias in una sola istruzione nella valorizzazione dei campi di destinazione.
 :  : INI   _9_   Help Tecnico £P002  >>
 :  : CMD CALL B£VED0 PARM('£P002' 'QPROGEN' '' 'H' '0')
 :  : FIN

**4.**Al di là che si sia utilizzata la funzione di popolamento o meno degli alias da parte dell'apposita funzionalià £P002 sarà necessario inserire manualmente i vari alias nel relativo data entry.
 :  : INI _9_     Richiamo data entry Alias      >>
 :  : CMD CALL C£AL01G
 :  : FIN

NOTA BENE :  l'utilizzo della /COPY £P002 è un prerequisito per il funzionamento delle relative schede d'analisi di loocup.

## Conversione Tabelle
Per quel che riguarda la conversione delle tabelle viene spesso utilizzata come appoggio la tabella **B§W**, tramite questa tabella che ha come elementi i settori di tabella da convertire è possibile pilotare la conversione degli stessi. In particolare risulta rilevante la possibilità di utilizzo degli alias :  questi sono la funzionalità tramite la quale possono essere ricodificati gli elementi di tabella.

**2.**Inserire l'elemento della B§W utilizzando come codice il tipo oggetto del codice che si vuole ricodificare (es. sugli articoli AR per i clienti CNCLI), indicando nel campo "Usare ALIAS" l'elemento della C£K del punto 1.
 :  : DEC T(ST) P() K(B§W) I(_9_     B§W - Condizioni Conversione  >>)

## Parametrizzazione
 I pgm possono ricevere due tipi di parametri entrambi passati tramite l'LDA : 
 * Parametri di impostazione specifici :  in questi parametri viene impostata la £FUNPS dell'elemento della B£J che lancia il programma. Le posizioni dell'LDA che vengono occupate partono dalla posizione 151 per 200 caretteri.

 * Parametri di impostazione generale :  sono un lascito della vecchia gestione delle conversioni che per motivi di compatibilità con il passato sono rimaste attivate :  praticamente in questi parametri vengono impostate le variabili di ambiente _&_££ a partire dalla 1 alla 9. Questi sono memorizzati nella posizioni dell'LDA dalla posizione 300 per 66 caratteri.

# FILE
Sono file logici creati appositamente per la conversione, questi vengono infatti solitamente compilati e cancellati run-time durante l'esecuzione della conversione stessa (vengono creati nella QTEMP del lavoro).
A volte è possibile trovare anche la definizione di file fisici che vengono creati per il salvataggio di determinati dati, questi, svolta la loro funzione (cioè dopo che la conversione ha girato in via definitiva), vanno cancellati.

# TESTO
Sono sorgenti di documentazione richiamabili dalla documentazione attiva. Fra questi assume particolare rilevanza il sorgente denominato "DOC" che fa da gancio fra gli altri documenti specifici della conversione ed il resto della documentazione.
