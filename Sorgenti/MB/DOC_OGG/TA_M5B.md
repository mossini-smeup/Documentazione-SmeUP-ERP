# M5B - Scenari M5
## OBIETTIVI
Impostare le caratteristiche di uno scenario di pianificazione.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$M5BA __Tipo oggetto di riferimento__
E' il codice di selezione che appare quando si consultano i suggerimenti dell'MRP che aiuta a trovare ciò che si vuole vedere.E' praticamente la "rubrica" che si vuole vedere
Si può impostare : 
_7_TA se l'oggetto di riferimento è una classificazione dell'articolo.
_7_OA se l'oggetto di riferimento è un OAV dell'articolo.
 :  : FLD T$M5BB __Parametro oggetto di riferimento__
Se il tipo oggetto è 'TA' si può impostare : 
_7_CLS     classe articolo;
_7_BRO       ,,   programmazione;
_7_BRH       ,,   gestione;
_7_BRV       ,,   valore;
_7_BRB       ,,   contabile;
_7_BRF       ,,   fiscale;
_7_BRP       ,,   tipo parte;
_7_BRA       ,,   articolo;
Se il tipo oggetto è 'OA', si imposta il codice di un OAV dell'articolo (NB :  vengono considerati solo gli OAV generali, non quelli a livello di articolo/tipo articolo).
 :  : FLD T$M5BC __Intestazione oggetto di riferimento__
Se impostata, viene assunta questa intestazione per l'oggetto di riferimento.
 :  : FLD T$M5BD __Scenario di rilascio__
Se impostato, e se non è lo scenario '**', si può eseguire il rilascio dei suggerimenti da  da questo scenario.
Per quanto riuarda lo scenario '**', il rilascio è naturalmente ammesso, a meno che sia espressamente impedito in tabella M51.
Riassumendo : 
Scenario ** :  normalmente rilasciabile
. Se impostato flag in tabella M51, è impedito rilascio
. Il flag in tabelle M5B non è significativo
Altri scenari :  normalmente non rilasciabili
. Impostare il flag in tabelle M5B per permettere il rliascio
 :  : FLD T$M5BE __No lotti in ordini di produzione__
Se impostato, in questo scenario non verrà eseguita la lottizzazione sui suggerimenti di  produzione
 :  : FLD T$M5BF __No lotti in ordini di acquisto__
Se impostato, in questo scenario non verrà eseguita la lottizzazione sui suggerimenti  di acquisto
 :  : FLD T$M5BG __No lotti in ordini di lavorazione esterna__
Se impostato, in questo scenario non verrà eseguita la lottizzazione sui suggerimneti dii lavorazione esterna
 :  : FLD T$M5BH __No tempi in ordini di produzione__
Se impostato, in questo scenario non verranno considerati i tempi di approvvigionamento negli ordini di produzione
 :  : FLD T$M5BI __No tempi in ordini di acquisto__
Se impostato, in questo scenario non verranno considerati i tempi di approvvigionamento negli ordini di acquisto
 :  : FLD T$M5BJ __No tempi in ordini di lavorazione esterna__
Se impostato, in questo scenario non verranno considerati i tempi di approvvigionamento negli ordini di lavorazione esterna.
 :  : FLD T$M5BR __No gr.fonti politica__
Se impostato, in questo scenario non verranno considerati i gruppi fonti definiti a livello di politica, ma verrà mantenuto quello di lancio.
In questo modo, ad esempio, se si lancia la pianificazione in uno scenario alternativo, con un gruppo fonti che esclude gli ordini in corso, si evita l'effetto che essi possano essere reintrodotti, perchè presenti in un gruppo fonti definito a livello di politica.
 :  : FLD T$M5B7 __No oggetto rottura SV__
Se impostato, in questo scenario sarà trascurata, per tutti i codici, la pianificazione a oggetto di rottura impostata in tabella M51.
Questo comportamento è simile ad aver impostato in tabella M51 l'oggetto di rottura ma non il flag  (sempre in M51) che tutti gli oggetti sono pianificati ad oggetto di rottura, e non aver impostato l'analogo flag in nessuna tabella delle politiche (M5A).
 :  : FLD T$M5BK __Scenario impegni risorse__
È significativo solo se è attiva (in tabella B£1) la gestione avanzata degli impegni risorse.
Se impostato, agli ordini pianificati di produzione, vengono costruiti gli impegni risorse del tipo impostato nel campo di questa stessa tabella.
Essi vengono schedulati a capacità infinita secondo quanto impostato nello scenario.
 :  : FLD T$M5BL __Tipo impegni risorse__
Va compilato insieme allo scenario di impegni risorse. Deve essere di tipo origine 'M5'; il modo di costruzione del tipo impegno risorse deve essere 'CO'.
 :  : FLD T$M5BM __Costruzione impegni risorse differito__
Se impostata la costruzione impegni risorse, normalmente viene eseguita contestualmente alla creazione degli ordini pianificati. Se invece si imposta questo campo, essa non viene eseguita automaticamente, ma lanciando la funzione specifica di ricostruzione totale impegni risorse pianificate. Ciò può essere utile quando tale funzione risulta particolarmente gravosa, e non si vuol appesantire la normale esecuzione della pianificazione.
Anche l'aggiornamento/eliminazione degi impegni risorse pianificati, all'atto del rilascio dei relativi ordini, viene eseguito se questo campo non è impostato, in quanto solo in questo caso si è certi di operare sul medesimo oggetto (l'IDOJ viene riassegnato ad ogni pianificazione).
 :  : FLD T$M5BN __Politica DRP__
Se si imposta questo campo, nella pianificazione su questo scenario, verrà utilizzato per tutti gli articoli il bilanciamento DRP pre-pianificazione con questa politica.
 :  : FLD T$M5BO __Tipo costo__
Se impostato, nelle valorizzazioni della pianficazione di questo scenario, verrà assunto questo tipo costo.
Se assente, verrè assunto il campo omonimo di tabella D01.
NB. questa risalita è indipendente dalla corrispondente sul livello di costo.
 :  : FLD T$M5BP __Livello costo__
Se impostato, nelle valorizzazioni della pianficazione di questo scenario, verrà assunto questo livello di costo .
Se assente, verrè assunto il campo omonimo di tabella D01.
NB. questa risalita è indipendente dalla corrispondente sul tipo costo.
 :  : FLD T$M5BQ __Costruz.Indici__
Se impostato, al termine di ogni pianificazione completa, verranno calcolati e memorizzati gli indici dell'MRP, definiti nel contesto "Scenario" (TAM5B) e nel tema £I2.
 :  : FLD T$M5BS __Classif.coperture__
Se impostato, nella pianificazione si classificano i fabbisogni in base alla loro copertura più "rischiosa" (giacenza, ordini in corso, ecc...).
Viene inoltre ritornata l'informazione (nell'OAV J/I03) di come sono coperti gli ordini di produzione e di conto lavoro
(sia rilasciati sia pianificati) e, in particolare, il valore di copertura dell'impegno più rischioso.
 :  : FLD T$M5BT __Filtro impegni__
E' il suffisso della exit M5OAV01_X che, se presente, permette di escludere alcuni impegni, nella determinazione del livello di copertura degli ordini (OAV J/I03).
Ad esempio, si possono trascurare i materiali di consumo, oppure considerare soltanto materiali critici.
 :  : FLD T$M5BU __Tipo distinta__
Se impostato, la scansione della distinta base per costruire gli impegni pianificati, avverrà con questo tipo distinta, indipendentemente dal valore presente nel campo della tabella della politica.
Ricordo che l'ordine di selezione del tipo distinta è il seguente : 
- valore dello scenario
- valore generale (in tabella M51)
- valore fisso "ART"
Per far sì che il tipo distinta qui impostato sia utilizzato anche per il calcolo e il reperimento del LLC, impostare, nella presente tabella, anche il campo "Distinta per LLC"
 :  : FLD T$M5BV __Autopulente__
Se impostato, prima di qualsiasi elaborazione di MRP eseguita su questo scenario, comprese quelle parziali (per singolo articolo, per gruppi di articoli e per singola commessa), lo scenario stesso viene cancellato completamente. In questo modo è possibile quindi, elaborare un MRP "pulito", vale a dire non influenzato da fonti esterne a quelle che sono frutto dell'elaborazione.
Questa impostazione ha inoltre l'effetto che, in caso di MRP parziale, nella consultazione sono visibili solo i codici elaborati.
NB :  questo flag NON è impostabile sullo scenario **, e quindi, implicitamente, non può essere eseguita in ambienti monoscenario.
 :  : FLD T$M5BW __SV Distinta per LLC__
Se valorizzato, in questo scenario, il tipo distinta, impostando anche il presente campo, il tipo distinta verrè utilizzato, oltre alla scansione per determianre gli impegni pianifcati, anche per : 
- calcolare il LLC (se previsto in tabella M51)
- scandire l'archivio dati tecnici articolo (BRARDT) per determinare la sequenza di   pianificazione degli articoli
 :  : FLD T$M5BX __Escluso da pianificazione__
Se impostato, non è possibile eseguire la pianificazione su questo scenario.
Questa impostazione può essere utile se si vuol sfruttare il presente scenario solo come rilascio (e vi si copiano le informazioni da uno scenario di pianficazione), e non si vuole correre il rischio che una pianificazione, lanciata erroneamente su di esso, vada a sovrapporsi alle informazioni in corso di elaborazione.
Questa impostazione NON è significativa per lo scenario **.
 :  : FLD T$M5BY __SV Forzatura raggruppamenti__
E' possibile impostare in questo campo un valore che viene utilizzato come raggruppamento fabbisogni, indipendentemente dal valore impostato nella politica.
Esso può assumenre i seguenti valori : 
'A' - raggruppamento nel giorno (corrispondente al tipo raggruppamento ' ')
'B' - non raggruppa (corrispondente al tipo raggruppamento '1')
NB :  NON è possibile impostare questo campo se lo scenario  è di rilascio, oppure se è lo scenario base (**) indipendentemente dal fatto che sia di rialscio o meno.
 :  : FLD T$M5B1 __SV Anticipi e ritardi minimi__
Si imposta il numero di giorni al di sotto dei quali viene emesso un suggerimento di
spostamento :  nella prima riga l'anticipo, nella seconda il ritardo, nella prima riga
per gli ordini di produzione, nella seconda per quelli di acquisto, e nella terza per gli
ordini di lavorazione.
Si considerano i giorni solari o di calendario in base a quanto impostato in tabella M51 e, nel
caso di calendario, si utilizza, se impostato sempre in tabella M51, il calendario dell'ente.
NB :  si imposta il numero di giorni al di sotto dei quali viene emesso un suggerimento. Se si vuol
eliminare il suggerimento di spostamento di zero giorni (possibile in caso di utilizzo di calendario
lavorativo, e con i fabbisogni datati in un giorno di chiusura) bisogna impostareil valore '1'.
Se ciò non può avvienire, e non si vuole escludere nessun suggerimento, si lasciano i valori
a '0', per non appesantire le prestazioni, in quanto, in questo caso, non viene eseguito
nessun controllo.
 :  : FLD T$M5B2.T$M5B1
 :  : FLD T$M5B3.T$M5B1
 :  : FLD T$M5B4.T$M5B1
 :  : FLD T$M5B5.T$M5B1
 :  : FLD T$M5B6.T$M5B1

 :  : FLD T$M5B8 __Exit fine livello__
E' il suffisso della exit M5MRP0A_X, che viene eseguita, se presente questo campo, alla fine dell'elaborazione di ogni livello dell'MRP.

Con questa exit è possibile eseguire delle azioni che coinvolgono più di un articolo dello stesso livello.

