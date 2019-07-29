# P5S - Tipo impegno risorse
 :  : DEC T(ST) K(P5S)
## OBIETTIVI
Descrivere le modalità di formazione e di scarico degli impegni di risorse di produzione (interni) e di lavorazione (esterni), sia attivi che passivi.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P5SA __Tipo origine__
Definisce l'oggetto a cui è assegnato l'impegno di risorse :  ordine di produzione, riga di ciclo esterno, articolo/magazzino, contenitore, ecc...
 :  : FLD T$P5SB __Tipo ciclo origine__
Definisce il tipo ciclo che si usa nella scansione delle operazioni di partenza.
È obbligatoriamente un tipo che ha come assiemi oggetti di tipo articolo.
**Attenzione** :  la mancanza di questo campo significa che non si vuol avere nessun ciclo origine. Non viene assunto nessun tipo di default.
 :  : FLD T$P5SC __Tipo ciclo memorizzazione__
Definisce il tipo ciclo in cui si memorizza il ciclo del documento.
È obbligatoriamente un tipo che ha come assiemi oggetti del tipo a cui si assegna l'impegno (ordini di produizione o righe di documento esterno).
**Attenzione** :  se non si imposta questo campo e il modo di costruzione degli impegni, prevede la scansione del ciclo del documento, la scansione stessa va subito a fine, con segnalazione di errore.
 :  : FLD T$P5SD __Tipo ciclo variazione__
Definisce il tipo ciclo in cui sono presenti le variazioni da applicare al ciclo origine per ottenere gli impegni effettivi.
 :  : FLD T$P5SE __Modo costruzione impegni risorse__
Definisce il modo in cui si compongono gli impegni (ad esempio il solo ciclo origine, quello del documento, e in assenza, il ciclo origine, se e come tener conto del ciclo di variazione).
 :  : FLD T$P5SF __Causale di attività__
Definisce la causale con cui vengono eseguiti gli avanzamenti relativi ad impegni di questo tipo.
 :  : FLD T$P5SG __Tipo/Parametro ciclo di variazione__
Il tipo e parametro del ciclo di variazione definiscono la natura dell'oggetto intestatario del ciclo di variazione.
 :  : FLD T$P5SH.T$P5SG
 :  : FLD T$P5SI __Scenario di schedulazione__
Questo campo è significativo SOLO nella gestione impegni risorse base (SM) :  è lo scenario da cui si reperiscono le informazioni per il completamento degli impegni risorse stessi.
Nella gestione degli impegni risorse avanzata (S2), lo scenario per la produzione è fisso a '**', e quindi questo campo non è significativo.
Gli eventuali altri scenari sono riservati per la simulazione.
 :  : FLD T$P5SL __Rifasatura impegni__
Definisce la modalità di rifasatura degli impegni di risorse dopo la manutenzione o l'annullamento del ciclo del documento.
-    Se impostato a 'A', gli impegni di risorse vengono rifasati automaticamente.
-    Se impostato un altro valore qualsiasi, gli impegni vengono rifasati, previa richiesta di conferma.
-    Se lasciato in bianco, non viene eseguita nessuna rifasatura.
 :  : FLD T$P5SM __Programma aggiustamento impegni__
È il suffusso x del programma P5FURIT_x (impegni risorse base) oppure S5FURIT_x (impegni risorse avanzati).
Se presente, viene eseguito prima della scrittura dell'impegno, con la  possibilità di modificare l'impegno stesso.
 :  : FLD T$P5SN __Programma ripresa valori precedenti__
_7_Impegni risorse base
Se impostato, e se presente il flag corrispondente in tabella P51, nella rifasatura degli impegni risorse, in modalità non rigenerativa, viene eseguito il programma P5FASIR_x, dove x è il suffisso qui impostato. Questo programma riceve sia il record prima della rifasatura (se presente) sia quello successivo.
È così possibile trasferire le informazioni che si vogliono conservare, dal primo al secondo.
Questo richiamo viene eseguito prima del programma di aggiustamento, che è sempre l'ultima operazione prima della scrittura.
_7_Impegni risorse avanzati
In questo caso viene sempre eseguita una ripresa 'standard' dei campi interessati alla schedulazione BCD, se è presente il flag di tabella P51.
Questo campo va impostato quando si vogliono riprendere altri campi, tramite il programma S5FASIR_x.
 :  : FLD T$P5SO __Residuo per impegni__
-    Se impostato ' ', nettifica nella costruzione degli impegni in base alle attività lavorative eseguite;
-    Se impostato '1', nettifica nella costruzione degli impegni in base alla quantità versata;
-    Se impostato '2',  come ' ' ma, in più, forza schedulazione su ultima risorsa consuntivata.
 :  : FLD T$P5SP __Programma Aggiustamento Ciclo Memorizzato__
È il suffusso x del programma P5FUCDC_x. Se presente, viene eseguito dopo la scrittura del ciclo memorizzato e prima della cancellazione, con la possibilità di leggere il record appena scritto per modifiche oppure per eseguire attività come la copia delle note dal ciclo articolo al ciclo memorizzato.
 :  : FLD T$P5SQ __SV riservato SMEUP__
Il campo è riservato per uso SMEUP
 :  : FLD T$P5SR __Tipo data scansione ciclo__
È la data di validità che viene assunta nella scansione del ciclo per la costruzione degli impegni di questo tipo : 
-     Se impostato ' ', per gli impegni di produzione si assume la data inizio richiesta, per gli impegni esterni la data di consegna confermata.
-     Se impostato 'O', si assume la data odierna in entrambi i casi.
-     Se impostato 'D', si assume la data dal documento.
-     Se impostato 'E', si assume la data di inizio validità dell'esponente di modifica
-     Se impostato 'L', si assume per gli impegni di produzione la data fine richiesta, per gli impegni esterni la data di consegna confermata, rettificata (anticipando) dal Lead Time dell'assieme.
-     Se impostato 'P', viene lanciato il programma B£DATS_x (Da valore impostato in suffisso programma)
 :  : FLD T$P5ST __Suffisso programma__
È il suffisso del programma B£DATS che viene lanciato se impostato P nel tipo data scansione ciclo
 :  : FLD T$P5SJ __Aggiorna ris.sec.__
Se impostato, viene eseguita la costruzione dell'archivio degli impegni di risorse secondarie, dei tipi risorse per cui tale funzione è prevista in tabella BRK.
 :  : FLD T$P5SK __T$P5SK  Modalità scarico__
Definisce la modalità di scarico degli impegni risorse.
' '  Dichiarazioni attività standard
        gli impegni risorse vengono scaricati dalle dichiarazioni di avanzamento effettuate
        sulle singole fasi (con le eventuali impostazioni di milestone definite a livello di ciclo).
'1'  Dichiarazione automatica Milestone standard
        L'ultima fase del ciclo verrà considerata milestone standard (tipo milestone 1) e tutte le fasi precedenti
        verranno considerate milestone Automatica precedente (milestone P). Questa impostazione dichioarerà
        automaticamente TUTTE le fasi del ciclo (con tempi standard) al momento della dichiarazione dell'ultima fase.
        Questo comportamento è analogo a quello che si otterrebbe impostando il flag Tipo Milestone nelle singole
        fasi del ciclo di lavorazione. In questo modo si evita di dover gestire tale flag su ogni fase del ciclo.
'2'  Dichiarazione automatica Milestone solo quantità
        Come il valore 1, ma l'ultima fase verrà considerata milestone solo qtà (tipo milestone 2)
