## OBIETTIVO
Raccogliere in un archivio i dati di non conformità relativi ai lotti : 
- acquistati;
- in C.to lavori;
- di produzione;
- resi da clienti;
in modo da : 
- produrre per ogni lotto un documento riepilogativo delle non conformità rilevate;
- assegnare ad ogni non conformità, un difetto, una causa del difetto, ed un parametro di merito legato all'importanza del difetto rilevato;
- identificare, l'articolo, l'ente responsabile della non conformità;
- evidenziare il danno economico associato alla non conformità.
## FORMATI VIDEO
## (4.13.1) GENERALITA'
Il fornitore deve predisporre e mantenere attive procedure documentate per assicurare che non venga involontariamente utilizzato o installato un prodotto non conforme ai requisiti specificati. Tale controllo deve assicurare l'identificazione, la documentazione, la valutazione, la segregazione (ove applicabile),
funzioni interessate.
Quando si rileva che un prodotto o servizio intermedio o finale, non
è conforme alle specifiche tecniche (per esempio mediante prove, collaudi o controlli) si dovrebbe impedirne l'utilizzazione o l'installazione involontaria. Ciò vale per i prodotti che risultino non conformi durante la produzione del fornitore, sia per i prodotti non conformi in arrivo.
Il fornitore dovrebbe stabilire e mantenere procedure per gli scopi seguenti : 
-determinare quali unità sono coinvolte nelle non conformità, per esempio :  che periodo di produzione o quali macchine operatrici o lotti di prodotto sono interessati;
-identificare i prodotti non conformi, per assicurare che siano distinguibili da quelli conformi;
-documentare l'esistenza delle non conformità e, per esempio, quali unità di prodotto, macchine, lotti sono coinvolti;
-valutare la natura delle non conformità;
-considerare le alternative per il trattamento dei prodotti non conformi, decidere quale tipo di trattamento effetuare e registrarlo;
-tenere sotto controllo (per esempio mediante segregazione fisica) i movimenti, gli immagazzinamenti e le successive lavorazioni per le unità di prodotto non conformi, in modo coerente con le decisione prese;
-notificare la non conformità alle altre funzioni che possono essere interessate o influenzate, e, quando è il caso, al committente.
Il Q9000 mette a disposizione un modulo dedicato specificatamente alla gestione delle non conformità. Il modulo supporta, in modo flessibile, le varie esigenze che si presentano nella gestione delle non conformità, dalla registrazione alle misure di intervento alla gestione dei verbali.
A questo modulo si accede in modo diretto oppure tramite altri moduli ad esso collegati :  vedi ad esempio il caso della "Dichiarazione delle prove, controlli e collaudi" dove è possibile in caso di riscontro di non conformità collegarsi direttamente al modulo per effettuarne la registrazione (si rimanda per i particolari al capitolo 10, prove, controlli, collaudi).
Operativamente, quando vengono riscontrate non conformità, durante ad esempio, una fase di autocontrollo da parte di un operatore su un certo lotto ci si collega con il modulo di Gestione Non Conformità nella sezione omonima attivando la seguente schermata : 
Formato guida
Smeup                **    GESTIONE NON CONFORMITA'   **
Scelta
Codice Lotto Interno  :      T3NT00006
Numero Documento . .  :       86640010
contingenti : 
-il codice del lotto è un'informazione che lega il seguito delle fasi operative a quello specifico lotto; questo serve chiaramente quando esiste un lotto a cui la non conformità che si vuole dichiarare, appartiene. Può accadere invece che ciò su cui è stata riscontrata la non conformità non appartenga specificatamente ad un lotto; è giustamente lasciata la libertà di annullare il campo del codice lotto e inserire solo il nome/codice del documento di registrazione;
-il numero del documento è un codice che in presenza del lotto è automaticamente riportato (la sua utilità in questo caso è superflua); nel caso in cui non è specificato il lotto il numero del documento permette di identificare in modo inequivocabile la registrazione della non conformità.
Da questo punto ci si collega con tutte le non conformità riscontrate sul lotto, oppure per quel documento,
documentate fino a quel momento : 
--------------------------------------------------------------------
Smeup               **    GESTIONE NON CONFORMITA'   ** 2/03/95                     Lista Documenti
X=Scelta
S Documento  Data   Articolo    Tipo Nr Lotto Int.NrOrd.F.Lav.F.Col.
..86640010  280295 14915500161 DFO T3NT00006            100     100
..86640010  181193 14915500161 DFO T3NT00006            100     200
--------------------------------------------------------------------
-Qualsiasi non conformità riscontrata su quel lotto viene proposta con una serie di informazioni di riepilogo sul lotto stesso (il modulo è in collegamento con l'anagrafica dei lotti) e sulle caratteristiche delle non conformità (tipo, fase di lavorazione e collaudo, se esistono). Questo tipo di legame tra il lotto e le non conformità rilevate è di fondamentale importanza per il soddisfacimento della norma che richiede una chiara documentazione sui prodotti, macchine, lotti coinvolti dalle difettosità riscontrate.
E' possibile entrare in variazione nelle singole sezioni del documento per aggiornare o modificare i dati raccolti.
Nel caso in cui si debba registrare una nuova non conformità relativa ad un lotto, è richiesto di specificare la fase di lavorazione e collaudo nella quale si è riscontrata la difettosità.
E' previsto inoltre che ad un lotto per cui non sia esplicitamente collegata una fase di collaudo o lavoro (vedi il caso di lotti di acquisto o di prodotti finiti ai quali non è imputabile una singola fase) inserire un codice Jolly (**) che permetta di identificare univocamente la non conformità.
Questo è un chiaro esempio del grado di flessibilità ed adattabilità del Q9000, e che è richiesto ad un software che non sia di intralcio ma di supporto alle fasi operative.
Vediamo adesso come viene realizzata dal programma la registrazone della non conformità, che prescrive la norma.
2/03/95                     Immissione
Codice Articolo   :  14915500161     Articolo  00672
Classe Funzionale :  CF-2       Planner  :     Esp.Mod. :      Reparto : 
Fase Lavorazione  :  **        ....................
Fase Collaudo  .  :  **2       ....................
Codice Difetto .  :                                       Imp.Carat : 
Classe Difetto .  :                                       Gravita'  : 
Causa del Difetto :                                       Caus.Acc. : 
Tipo Non Conformi : 
Lotto Interno  .  :  T3NT00006       Ricorrenza difetto . :          -
Ente Rilevatore   :  FO / 004715     Fornitore  00044
Numero Ordine  .  :                  Operazione/Riga : 
Numero Commessa   : 
Ente Collaudatore :  DI / CAP        CAPPI CRISTIANO
Azioni su N.C :   Escl.Statist.  :   Escl.Vendor :   Stampa Oss.Col. : 
-------------------------------------------------------------------
Collegandosi con l'anagrafica dei lotti il programma è in grado di recuperare le informazioni relative all'articolo (decodifica, classe funzionale).
Viene richiesto di specificare il codice del difetto (per la ricerca ci si collega alla tabella relativa ai difetti).
Nel difetto si specifica in modo automatico la classe del difetto (importante o meno) e la sua gravità (è un parametro comunque modificabile). Si specifica poi la causa del difetto e l'accertamento della stessa.
L'importanza della caratteristica su cui si è rilevata la non conformità la si può immettere direttamente oppure, se è il caso, può essere specificata nella stesura della fasi di collaudo (vedi sezione relativa).
Chi rileva la difettosità deve indicare anche il tipo di non conformità che ha trovato (se è uno scarto o un reso o un'accettazione in deroga). Segue una serie di ulteriori informazioni sull'identità degli enti o operatori coinvolti sull'articolo interessato. Del difetto è possibile visitarne la
"storia", tramite il campo Ricorrenza del difetto; ci si collega con l'archivio dei difetti e si osserva la ricorrenza dei difetti su quell'articolo e per la combinazione articolo/ente (sul documento delle non conformità sono riportate in sintesi tali ricorrenze tramite due numeri separati da un tratto).
Vediamo in dettaglio i campi che sono riportati in basso : 
------------------------------------------------------------------
Azioni su N.C :   Escl.Statist.  :   Escl.Vendor :    Stampa Oss.Col. : 
------------------------------------------------------------------
1. Quantità_
Tramite il campo Quantità l'operatore può registrare il riassunto delle quantita che ha rilevato distinguendole nelle differenti classi (scarti, accettati in deroga...)
-------------------------------------------------------------------
......................................
.                                    .
. Controllata .  :       90,000 NR     .
. Ricor.Difetto  :       10,000 NR     .
.                                    .
.                                    .
. Selezionata .  :       90,000 NR     .
. Acc.in deroga  :        5,000 NR     .
. Scartata  . .  :        4,000 NR     .
. Rilavorata  .  :        1,000 NR     .
.                                    .
. F12=Annulla   F15=Riep.Lotto       .
.                                    .
.                                    .
......................................
-------------------------------------------------------------------
Automaticamente viene controllata l'esattezza dei dati introdotti ed
è proposto un riepilogo sull'intero lotto.
2. Costi_
Il campo dei Costi permette di specificare il costo complessivo che ha comportato la non conformità distinto secondo le voci proposte : 
-----------------------------------------------------------------
...........................................
.
.         TOTALE COSTI INTERVENTO
.
. Totale Materiale  .  :            1233333
. Totale Lav.Esterna   : 
. Totale Lav.Interna   : 
. Totale Macchina . .  :            10000000
.
.              COSTI UNITARI
. ----------------------------------------
. Costo Unitario  . .  :          1756,053
.
. F12=Ritorno
.
..........................................
---------------------------------------------------------------
E' messo in evidenza il costo unitario; quest'ultimo è ricavato in base al tipo di non conformità (costo primo, costo industriale...contenuti nell'archivio dei prezzi) e all'articolo.
Tale costo viene moltiplicato per il numero di pezzi che sono risultati non conformi ed il risultato sommato per le voci di costo specificate nella tabella soprariportata.
Questa finestra permette quindi di quantificare il costo della non conformità tenendo conto dell'entità del difetto, del valore del prodotto a quella fase della lavorazione e di tutte le spese sostenute per affrontare la non conformità in termini di tempo,
addebiti/accrediti del fornitore.
3. Dati per addebito/accredito_
Una finestra molto importante dal punto di vista della conformità del programma alla norma è la seguente : 
-----------------------------------------------------------------
.............................................................
.                     DATI  PER  ADDEBITO / ACCREDITO
.
. Articolo Respon. :  14917500309        Articolo  00681
. Lotto Responsan. :  P3N&00068
. Costo Non Conf.  :     111239712,159   Lire
. Codice Ente . .  :  RI /               INSACCHETTATRICE
. Tipo Add./Acc.   : 
. Totale Add./Acc. :                     Lire
. Stato Add./Acc.  : 
.
. Note Ente Addeb. : 
.............................................................
-------------------------------------------------------------------
Le prime due voci evidenziate portano di Default il codice dell'articolo e del lotto; tramite l'interrogazione (/) è possibile collegarsi con la distinta base del prodotto e scandire tutti i sui componenti ed individuare il responsabile della non conformità.
La seguente è la schermata che permette di collegarsi alla distinta base scegliendo il tipo opportuno di esplosione.
----------------------------------------------------------------
.......................................
. SCELTA DATI COLLEGAMENTO COMPONENTI .
.                                     .
. Scelte                              .
.                                     .
. Tipo Esplosione  :      1 = Livello   .
.                       2 = Scalare   .
. Esclusione Lotti :                    .
.                                     .
. Limiti                              .
.               Iniziale   Finale     .
. Tipo Lotto  :   .......    .......    .
. Data Lotto  :   .......    .......    .
.                                     .
. F12=Ritorno                         .
.                                     .
.                                     .
.......................................
--------------------------------------------------------------------
Se, ad esempio, accade che durante il collaudo finale venga riscontrato un difetto imputabile ad un particolare interno, tramite la connessione con la distinta del prodotto è possibile riportare in questo campo il codice dell'articolo e del lotto responsabile.
Qualora l'azienda fosse dotata di un sistema di rintracciabilità, si fornitore originario e quindi addebitargli la responsabilità ed i costi) che ha causato il difetto.
C'è da sottolineare che in questo caso il programma non permette di specificare che lo scarto riguarda solo il particolare e non il complessivo (la registrazione dello scarto è associata al codice dell'articolo complessivo); il fatto diventa spinoso quando si va a costificare l'entità dello scarto :  in genere infatti non si scarta l'intero prodotto ma si sostituisce semplicemente il componente; questa informazione non è specificabile dal programma.
Sempre se il fornitore ha una gestione di rintracciablità è possibile identificare tutti quei prodotti che sono coinvolti dalla non conformità riscontrata; il Q9000 non permette tale ricerca che è demandata al software gestionale.
Esempio
Per la realizzazione di 1000 caldaie viene impiegato un articolo prelevato dal magazzino in lotti differenti tra cui il lotto N°100. Il cliente che acquista la caldaia, riscontra una difettosità. Il Q9000 supporta la fase di registrazione della non conformità :  tramite il modulo riportato precedentemente si visualizza la distinta base e si risale al codice del pezzo difettoso; da qui poi se esiste la gestione di rintracciabilità è possibile risalire al lotto 100 a cui apparteneva l'articolo responsabile quindi individuare tutte le caldaie coinvolte dalla difettosità. E'comunque importante ribadire che la competenza della rintracciabilità non può far parte di un pacchetto di qualità.
Riprendiamo la spiegazione della finestra relativa agli addebiti/accrediti; si può notare la presenza del campo dei costi che riporta il totale che è stato calcolato come spiegato in precedenza. C'è la possibilità di modificare tale valore se l'ente competente lo ritiene inadeguato.
Si identifica poi l'ente di addebito/accredito al quale riferire la rilevazione della non conformità in termini di spesa.
Il tipo di addebito/accredito (se da addebitare, accreditare o altro) viene registrato nel campo omonimo collegandosi alla tabella relativa.
Un informazione molto importante ai fini del controllo dello stato di evoluzione della non conformità è contenuta nel campo specificato in fondo alla finestra; tale campo riporta lo stato in cui si trova l'addebito/accredito :  la registrazione dello stato è obbligatori e non si procede  fino a quando non è stato compilato il campo e quelli ad esso logicamente legati. Se ad esempio si conferma lo stato di accordo dell'addebito/accredito è obbligatorio inserire la cifra totale.
Qualsiasi altra informazione legata all'addebito/accredito che si desidera allegare, può essere inserita tramite il consueto sistema di gestione delle note libere.
4. Azioni sulle non conformità_
al tipo di difetto per quella causa specifica. Se supponiamo che un difetto si presenti frequentemente sotto quella causa l'ente responsabile (generalmente la Direzione Tecnica) ha la possibilità di descrivere una serie di operazioni correttive che permettono all'operatore di attivare opportune azioni di intervento per eliminare il problema. Questa informazione rimane legata in modo indissolubile all'articolo per quel difetto sotto quella causa cosicchè quando il problema si ripropone all'operatore compaiono automaticamente i tipi di intervento che può eseguire.
..............................................................
 :  Smeup            Lista Azioni Non Conformità                : 
 :                                                              : 
 :  Codice Articolo  :  14917500309     Articolo  00681           : 
 :  Esponente Mod.   :                                            : 
 :  Fase Lavoro . .  :  **                                        : 
 :  Codice Difetto   :  ARR-SE        ARROTONDATURA DENTE ERRATA  : 
 :                                                              : 
 :  Cd Causa   Ac Sq Azione                                     : 
 :  1CA-AC     SI 1  CORREZIONE RETTIFICA                       : 
 :  1CA-AC     SI 2  RILAVORAZIONE SUPERFICIALE                 : 
 :                                                              : 
 :                                                              : 
 :                                                              : 
 :                                                              : 
 :               F15=Immissione      F20=Azioni Correttive      : 
 : ............................................................ : 
L'immissione di queste operazioni segue una data sequenza che scandisce la priorità di esecuzione delle attività,
decisa dall'ente responsabile.
La finestra offre in più l'opportunità di vedere elencate (e naturalmente anche di consultarle) le azioni correttive
che sono state adottate per quella non conformità, su quel dato articolo, sotto quella specifica causa e per quella
fase di lavoro.
Una volta che si è introdotta tramite la finestra degli interventi l'azione correttiva (vedere seguito) e si è
terminata la sessione di lavoro, automaticamente viene registrato in questo campo.
E' da sottolineare il fatto che la  finestra mostra l'insieme di tutte le azioni intraprese e non solo per quella
sessione di lavoro.
E' una opzione comoda quando si desidera consultare velocemente lo stato dell'intervento per vedere se è stato evaso o
meno.
La forza, come sempre, dei collegamenti che realizza il Q9000 risiede nel fatto che questo tipo di collegamento è
dinamico cioè segue "run time" l'evoluzione delle attività dell'azienda. Questo è un requisito fondamentale per
un'efficiente gestione del sistema qualità, che richiede "in primis" un controllo efficace dello sviluppo dello stato
delle operazioni coinvolte.
5. Esclusione dalla statistica_
E' possibile decidere di escludere la registrazione della non conformità dal calcolo statistico che il programma
effettua per la determinazione dei piani di campionamento (livelli di qualità) che
piani di campionamento). Ciò può risultare importante quando si è in presenza di situazioni speciali o anomale per cui
si ritiene di non doverne tenere conto nel conteggio complessivo delle difettosità che riguardano un articolo. Il
programma quindi, in questo caso dimostra di non essere di ostacolo alla pratica operativa che presenta quasi sempre
gradi di libertà imprevedibili :  l'aspetto fondamentale di un software efficiente, al servizio dell'azienda, è
rappresentato dall'assenza di vincoli immodificabili.
6. Esclusione dal Vendor Rating_
E' possibile, anche in questo caso, decidere di escludere, per un qualsiasi motivo, la dichiarazione della non
conformità dal calcolo del Vendor Rating (Vedere la sezione specifica per i particolari sull'argomento).
7. Stampa osservazioni sui collaudi_
E' un campo di segnalazione della stampa di questo modulo (si rimanda alla sezione dedicata alla stampa).
8. Intervento_
Su questo campo si apre una finestra che, operativamente, è di fondamentale importanza.
-------------------------------------------------------------------
....................................................
.                                                  .
.                   INTERVENTO                     .
.                                                  .
. Richiesta di intervento . .  :  EDVT950019         .
. Analisi Richiesta Intervento : ..                  .
. Documento di Riferimento  .  : .........           .
. Centro di Lavoro Sel./Rec.   : .........           .
. Ore Intervento per Sel./Rec. : ..........          .
. Rifer. Impiego Non Conforme  : ..........          .
....................................................
--------------------------------------------------------------------
La norma prevede che all'accertamento della difettosità ed alla sua registrazione, deve attivarsi un pronto intervento
che permetta di provvedere alla non conformità.
Per le specificazioni sul trattamento della non conformità si rimanda al paragrafo successivo.
Direttamente da questo modulo, l'operatore che riscontra la non conformità (che può essere il collaudatore, oppure se
la difettosità avviene durante una fase di autocontrollo, l'addetto abilitato) attiva, quando lo ritiene necessario
un'azione di intervento.
Esempio
riscontra la presenza di non conformità che non permette un'azione risolutiva inequivocabile (la difettosità non è
grave al punto di indurre lo scarto completo del lotto). Identifica la non conformità tramite le procedure previste e
la documenta nel modulo di gestione dedicato. Non essendo abilitato a procedere (questo aspetto è estremamente
variabile da situazione a situazione) richiede l'intervento di un ente responsabile all'analisi del problema.
Tramite il modulo del Q9000 questa operazione di attivazione delle azioni di intervento si realizza semplicemente
entrando nella finestra di Intervento e collegandosi al modulo delle richieste di intervento. Grazie alle solite
tabelle decide il tipo di richiesta (in questo caso si tratta di un Deroga), la compila e la invia al l'ente designato
(per i particolari si rimanda al paragrafo successivo).
Nel seguito, lo stato di gestione della richiesta di deroga può essere controllato dall'operatore che ha innoltrato la
richiesta, attraverso l'interrogazione del medesimo campo (il collegamento tra la "gestione delle non conformità" e la
"richiesta di intervento" è sempre attivo ed indissolubile dal momento in cui è stato creato).
Ulteriori informazioni che si desidera allegare possono essere introdotte nei campi successivi : 
- Documento di Riferimento  .  : 0154D2...
- Centro di Lavoro Sel./Rec.   : SCO......
- Ore Intervento per Sel./Rec. : 1.........
- Rifer. Impiego Non Conforme  : ..........
Le informazioni che sono inserite in questi campi dipendono dalla specifica situazione in cui ci si trova ad operare.
Nel caso di selezione o recupero diretto da parte dell'operatore, quest'ultimo inserirà :  il centro di lavoro dove è
stata eseguita (tabellato) questa fase; il tempo speso per eseguire il recupero e l'??????????(tabellato). Oppure,
quando viene specificata una richiesta di intervento il campo Tipo di intervento permette di stabilire lo stato della
richiesta.
Ad ogni sviluppo della fase di intervento, viene aggiornato il campo (ad esempio :  da un'iniziale "da evadere" ad una
finale
"definitivamente evasa").
Ciò è in linea con quanto richiede la Norma al punto (4.12), ovvero che l'identificazione dello stato delle prove,
controlli e collaudi sia mantenuta durante tutte le fasi di produzione relative al prodotto per assicurare  che solo i
prodotti che abbiano superato positivamente le prove siano immagazzinati outilizzati. Si fa notare che, a nostro
parere, un intervento opportuno sarebbe quello di esigere l'immissione obbligatoria di questo campo per l'uscita dalla
finestra.
La registrazione delle non conformità continua con la seguente videata : 
-----------------------------------------------------------------
............................................................
.                                                          .
.                   VALORI IN ARCHIVIO                     .
. Articolo / Nr Lotto  :   00104700137     / A3N&00001       .
. Esito del Controllo  :   20 Deroga interna                 .
. Az.Prossima Consegna :   ...............                   .
.                                                          .
.         NUOVI VALORI PER MODIFICA/FORZATURA              .
.                                                          .
. Esito del Controllo  :   29 LOTTO IN ATTESA DI DEROGA      .
. Az.Prossima Consegna :   T  COLLAUDO COMPLETO ARTICOLO     .
.                                                          .
.                                                          .
........................................................... : 
-----------------------------------------------------------------
1. Esito del controllo_
Il primo campo evidenziato specifica la sintesi del controllo, prova o collaudo eseguito sul lotto; il campo è
tabellato e l'operatore collegandosi con la relativa tabella può decidere di aggiornare l'esito del controllo presente
in archivio. Per comprendere meglio questo aspetto ci si deve riferire all'esempio pratico in cui la sequenza di
collaudo comprende varie fasi, per ognuna delle quali può risultare necessario registrare delle non conformità.
Tramite questo campo si decide dinamicamente l'esito del controllo fino al termine dell'operazione.
1. Azione sulla prossima consegna_
Questo campo permette di specificare, a fronte del risultato ottenuto dalle prove sul prodotto, le azioni che si
intendono richiedere al fornitore o, più in generale, esercitare sulla successiva consegna per prevenire il ripetersi
delle non conformità riscontrate. Il dato viene inviato alla gestione degli acquisti che ne terrà conto quando
richiederà il prossimo lotto.
Un Sistema di Qualità supportato da strumenti come questo, dimostra sicuramente un livello di efficenza elevato. Se ad
esempio ad un fornitore viene richiesto il Certificato di Qualità, e all'atto della consegna della merce va persa
questa informazione, perchè non esiste un efficiente gestione di documentazione e di collegamento tra i vari enti
interni, il Sistema di Qualità è sicuramente da ritenersi scadente oltreché l'immagine dell'azienda poco seria.
La rispettabilità di un'azienda si misura anche nell'essere coerente con le decisioni che prende e le richieste che
fa.
Un campo come questo presuppone che l'azienda pratichi ciò che la
Norma specifica al punto (4.14.3) Azioni Preventive che chiede al fornitore di adottere e mantenere attive delle
procedure per prevenire il ripresentarsi di situazioni di non conformità. Questo collegamento che il Q9000 è in grado
di realizzare, rappresenta sicuramente un importante supporto alla filosofia della prevenzione.
Qui di seguito è riportata la videata conclusiva di riepilogo della dichiarazione delle non conformità.
Smeup            ** RIEPILOGO QTA' LOTTO-NON CONFORMI ** 3/03/95
S Cd Difetto Cl Causa Dif.Qtà Scart.Qtà NonCon.Qtà Selez.Qtà Rilav.
ARR-SE     MN BLO-ECC
CIL-IM     IM CON-DIF     20,000
DIM-LC     CR BLO-ECC
DIM-LC     CR BLO-ECC      4,000       5,000             1,000
DIM-LC     CR CAD-ACC
DIM-LC     CR BLO-ECC
-----------  -------  --------  ------
=================   RIEPILOGO QUANTITA' DEL LOTTO  ==============
Codice Lotto Interno . .  :  A3N&00001        Qtà Dichiarata  :  100,000
Articolo  00008
Qtà Contr.  Qtà Conf.  Qtà Scart.  Qtà NonCon. Qtà Selez.Qtà Rilav.
100,000    90,000        4,000       5,000             1,000 100,000    90,000        4,000       5,000
1,000
Questa schermata riassume tutte le non conformità che sono state dichiarate durante i controlli effettuati sul lotto.
Nella prima metà viene riportato in modo esteso, con la possibilità di ottenere altri dati, l'elenco di tutte le
difettosità distinte per tipo (scarto, rilavorato, selezionato, Accettato in deroga).
Naturalmente il sistema non è in grado di riconoscere le sovrapposizioni di difettosità, quindi può accadere che un
prodotto sia affetto da più di una non conformità; il totale dei rilievi non tiene conto di questo fatto ed è compito
dell'operatore indicare il numero reale di non conformità.
Operativamente ciò comporta che per la conclusione della sessione di lavoro è necessario immettere i valori
complessivi nell'ultima riga in fondo :  questo conteggio non comporta alcuna difficolta per l'operatore. In caso
comunque di errore il programma segnala l'incongruenza nel conteggio effettuato e non permette la prosecuzione del
lavoro.
Come sempre vi è poi la possibilità di allegare un insieme di in formazioni libere non strutturate tramite l'agile
strumento delle note libere. E' riportato un esempio  : 
------------------------------------------------------------------ 3/03/95                 NON CONFORMITA'
Lotto           A3N&00001
f.l.+f.c.       **    010                                 Liv.sup
CC=Copia  EE=Elim.  In=Inser  P =Prima  A = Dopo  G =Gest.
Op  NOTE LIBERE - NON CONFORMITA'                               F
=========================================================   *
RICHIESTA/E PER PROSSIMA FORNITURA                          *
----------------------------------                          * x -) Allegare il Certificato di Qualità e Conformità x
-) Allegare il Certificato di Origine della Materia Prima x -) Allegare Analisi Chimica e/o Analisi Metallurgica.
x -) Nessuna Richiesta
=========================================================   *
Termina qui il primo modulo dedicato alla gestione delle non conformità.
## (4.13.2) ESAME E TRATTAMENTO DEL PRODOTTO NON CONFORME
Devono essere definte le resonsabilità per l'esame del prodotto non conforme e l'autorità per le relative decisioni.
Il prodotto non conforme deve essere esaminato secondo procedure documentate. Esso può essere : 
a) rilavorato per soddisfare i requisiti specificati;
b) accettato con o senza riparazione mediante concessione;
c) declassato per applicazioni alternative o
d) rifiutato
o scartato.
Quando previsto dal contratto, la proposta di utilizzazione del prodotto non conforme (vedere 4.13.2 b) ai requisiti
specificati deve essere notificata al cliente o al suo rappresentante per ottenere concessione. La descrizione della
non conformità accettate e delle riparazoni, deve essere registrata per evidenziare l'effettivo stato del prodotto
(vedere 4.16).
Il prodotto riparato e/o rilavorato deve essere ricontrollato in accordo ai requisiti del piano della qualità e/o di
procedure documentate.
Q9000
In una realtà aziendale la gestione delle non conformità segue in genere un percorso simile alseguente : 
1. Grave non conformità accertata
In caso di grave difettosità riscontrata durante un fase di collaudo o di autocontrollo, l'operatore abilitato scarta
o rilavora (dipende dalle procedure adottate dall'azienda) il pezzo direttamente senza far seguire alcun tipo di
azione di intervento. Viene comunque notificata la non conformità perchè possa essere addebitata / accreditata
all'ente responsabile tramite il modulo spiegato nel paragrafo precedente. Questa non conformità, come già detto, va
ad incidere sulla statistica e sul Vendor Rating in quanto rimane documentata nell'archivio del sistema.   1.
Richiesta di intervento
In tutte le altre situazioni il rilevatore della non conformità è tenuto ad attivare tramite il modulo di "Gestione
delle non conformità" l'intervento di un ente competente perche analizzi la situazione e decida l'azione risolutiva.
Il pacchetto effettua il collegamento con il modulo delle richieste di intervento lasciando la massima libertà di
decidere quale tipo di azione attivare. In genere si richiede l'utilizzo della deroga di cui si riporta qui di seguito
un'esempio : 
Smeup             ** IMMISSIONE RICHIESTE D'INTERVENTO ** 3/03/95                        Immissione
Progressivo Richiesta  :  EDVT950022   Origine Richiesta  :  CQAM40
Ente Richiedente  . .  :  DI / 004655       Fornitore  00039
Obiettivo/Soluz.prop.  :  RISOLUZIONE DEL PROBLEMA
Procedura Riferimento  :  P13-01            Procedura nr  00048
Responsabile Evasione  :     /
Lista Distribuzione .  :               Quantità lotto  .  :  100,000
Data Evas.Programmata  :   3/03/95     Unità di misura .  :  NR
E' subito da notare che la traccia di questa richiesta rimane chiaramente presente nella registrazione delle non
conformità all'interno della finestra degli Interventi (vedi paragrafo precedente). La connessione è comunque
biunivoca; infatti sulla richiesta di deroga viene riportata la codifica del "documento sorgente". In immissione
questo particolare può risultare di scarsa importanza; si rivela invece fondamentale in fase di gestione come si vedrà
nel seguito.
In automatico viene riportato tutto ciò che è relativo all'identificazione della non conformità (articolo, fase di
lavorazione, di collaudo....) e del lotto. Viene richiesto di completare la stesura di alcuni campi che specificano,
come si legge dalla schermata precedente : 
_la problematica in questione;
-l'obiettivo della richiesta;
-la proposta di soluzione che può risultare utile per chi va ad analizzare il problema;
-la procedura di riferimento(il campo è controllato dalla tabella delle procedure);
-l'ente designato alla gestione della deroga;
-la data di evasione prevista;
In casi particolari si può forzare l'immissione dei campi di priorità e del responsabile di evasione che in genere
sono stabiliti dall'ente designato.
Si può come sempre allegare una serie di note non strutturate di questo tipo : 
3/03/95                 RICHIESTE D'INTERVENTO
Azione          EDVT950022
Liv.sup
CC=Copia  EE=Elim.  In=Inser  P =Prima  A = Dopo  G =Gest.
Op  NOTE LIBERE - RICHIESTE INTERVENTO                            F
===========================================================   *
Problematica / Richiesta                                      *
Durezza rilevata dopo rettifica su 30 ralle. Si propone la
fornitore il motivo del difetto rilevato.
===========================================================   *
Obiettivo / Proposta                                          *
===========================================================   *
Soluzione Adottata                                            *
Selezionare l'intero lotto oppure rieseguire  il trattamento di tempra in atmosfera controllata di carbonio.
Le ralle sotto i 61HRC non si possono assolutamente accettare.
===========================================================   *
Nei campi che registrano lo stato del prodotto non conforme viene segnalata la condizione di deroga.
A questo punto termina la fase di immissione della richiesta di intervento e inizia la gestione vera e propria da
parte dell'ente designato. Quest'ultimo, consultando l'insieme delle richieste a lui rivolte (vedi anche capitolo 4),
si collega con la deroga specifica tramite il modulo di Gestione delle richieste di intervento ed entra in variazione
per completare le informazioni che devono essere fornite al responsabile di evasione. Ecco cosa compare all'ente che
gestisce la richiesta di deroga : 
Smeup          **  GESTIONE RICHIESTE D'INTERVENTO  ** 3/03/95                    Variazione
Progressivo Richiesta  :  EDVT950022   Origine Richiesta  :  CQAM40 _
Ente Richiedente  . .  :  FO / 004655       Fornitore  00039
Priorità di evasione   :  A                 Priorità massima
Obiettivo/Soluz.prop.  :  RIS.PROB
Procedura Riferimento  :  P13-02      Procedura nr  00049
Responsabile evasione  :  DI / CAP    CAPPI CRISTIANO
Lista Distribuzione .  :              Data Evas.Program. : 3/03/95
Ore a Preventivo  . .  :   10,0000    Quantità lotto  .  : 100,000
Costo a Preventivo  .  : 1000000,0    Unità di misura .  :  NR
L'ente che gestisce la deroga può facilmente collegarsi in qualsiasi momento con il modulo di gestione delle non
conformità tramite il campo di collegamento riportato accanto al "Origine
Richiesta". Viene poi completato il documento indicando in modo obbligatorio la priorità che deve essere assegnata
alla deroga e il responsabile a cui viene affidata l'evasione; si indica la procedura
di preventivo relativi al tempo ed al costo per l'evasione (questi dati sono mascherati alla consultazione
dell'operatore che ha innoltrato la richiesta).
Nella successiva schermata (alla quale ha accesso esclusivo l'ente chegestisce la richiesta) viene inserità
un'ulteriore serie di dati : 
Smeup          **  GESTIONE RICHIESTE D'INTERVENTO  ** 3/03/95                  Variazione
Progressivo Richiesta  :  EDVT950022   Origine Richiesta  :  CQAM40
Obiettivo/Soluz.prop.  :  RIS.PROB
Richiesta Collegata .  :  .. RDLV950002   Ric.Evas.R.I. :   7/03/95
Rapporti di Prova . .  : ....................................
Ore a Consuntivo  . .  : .............. Altri Costi a Con. : 
Centro di Lavoro  . .  :                  Costo Totale Cons. : 
Ente di Addebito  . .  :  FO / 000460     Fornitore  00003
Soluzione Adottata  .  :  MODIFICA  DELLA GOLA DI SCARICO
Esito Soluz. Adottata  : 
Descrizione Esito Sol. : 
Data Effett. Evasione  : 
Approv. Rilascio Doc.  :              Modulo 4/5 stampato . .  :     /
Attraverso questo modulo l'ente responsabile deve indicare l'ente a cui addebitare la deroga (nel caso dell'esempio il
fornitore del prodatto sul quale è stata riscontrata la non conformità).
Il Tipo di Intervento permette di specificare lo stato della richiesta (nell'esempio giustamente compare "da
evadere").
L'ente di evasione ha la facoltà di indicare la soluzione adottata e di decidere l'accettazione o meno della deroga
(con le condizioni di accettazione della deroga).
Questo modulo deve venire completato dall'ente designato per l'evasione alla fine della gestione della deroga con i
valori a consuntivo : 
- Ore a Consuntivo;
- Costo Totale Cons.;
- Altri Costi a Con.;   - Esito Soluz. Adottata ;
- Descrizione Esito Sol.;
- Data Effett. Evasione ;
E' da notare che quando l'evasione è completata lo stato deve essere cambiato. Molte informazioni vengono fornite
anche all'operatore che ha inoltrato la richiesta; alcune rimangono invece nascoste come quelle relative al giudizio
sull'esecuzione della soluzione proposta e quelle relative ai costi.
Quando lo ritiene opportuno il responsabile, tramite questo modulo, ha la possibilità di attivare azioni di
intervento, quali ad esempio le sperimentazioni, per approfondire l'analisi della deroga.
si ricollega con il modulo delle Richieste di intervento e da qui poi è possibile emettere la Sperimentazione del caso
ed attivare, in generale, una catena che sviluppi tutti gli interventi necessari a sviluppare la deroga. Talvoltà,
infatti, quando la richiesta è di una certa importanza,è opportuno realizzare uno studio di affidabilità del prodotto
in deroga (FMEA,FMECA).
La deroga si chiude (lo stato dell'intervento passa ad "Evaso") solo alla conclusione di tutte le azioni attive.
Ad una deroga, in generale, fa seguito una emissione di documentazone per informare la parte interessata del rilievo
della non conformità.
Si parla in questo caso di "Osservazioni di Collaudo" che notificano, ad esempio, al Fornitore l'accettazione in
deroga del lotto oppure lo scarto e la relativa rottamazione del lotto stesso.
Il Q9000 dispone di una funzione che permette la compilazione e la stampa del documento collegandosi al modulo delle
non conformità.
CHIEDERE SE ALLEGARE UN ESEMPIO DI OSSERVAZONE COLLAUDO
