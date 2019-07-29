# P51 - Parametri gestione produzione
 :  : DEC T(ST) K(P51)
## OBIETTIVI
Contiene i parametri che permettono di ottenere particolari comportamenti nella  gestione della produzione.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P51A __Materiali solo a fasi logistiche__
Se impostato, gli impegni dei materiali saranno assegnati solo a fasi logistiche. In caso contrario saranno assegnati a tutte le fasi. Ricordiamo che una fase è logistica se è presente, nell'anagrafico cicli, l'opportuno flag.
 :  : FLD T$P51B __Modo calcolo scarti__
La determinazione dello scarto residuo previsto, che va a decrementare la disponibilità dell'ordine di produzione, viene eseguito secondo la modalità definita in questo campo : 
-     ' '  Non viene calcolato lo scarto residuo previsto
-     'A'  La quantità dell'ordine viene moltiplicata o divisa per la % di scarto previsto (in funzione del campo successivo) e si sottrae lo scarto rilevato :  il risultato, se positivo, è lo scarto residuo previsto. In questa modalità si assume che lo scarto si verifichi in modo casuale durante la produzione.
-     'B'  Si determina la quantità residua (ordinato - versato - scartato) e lo si moltiplica/divide (in funzione del campo successivo) per la % di scarto previsto :  il risultato è lo scarto residuo previsto. In questa modalità si assume, invece, che lo scarto si verifichi in modo costante durante la produzione.
La compilazione di questo campo è discriminante per il trattamento degli scarti in pianificazione :  infatti, solo se esso è valorizzato, gli impegni pianificati vengono maggiorati dello scarto dell'assieme, moltiplicato per il coefficiente di impiego.
La presenza dello scarto sull'assieme, da sola, non basta perchè esso sia considerato. Infatti, se non si intendono gestire gli scarti di assieme, è inutile, per motivi di prestazioni, leggere lo scarto.
 :  : FLD T$P51C __% Scarto su quantità buona__
Se impostato, la % di scarto previsto è intesa come % della quantità buona (B), se lasciato a blanks è intesa come % della quantità ordinata (O).
Nel primo caso, percentuale su versato buono, si dovrà produrre una quantità pari a : 
  O = B + %B  ->  O = B * (1 + %)
                                                                                        %
  O = B + %B  ->  O + %O = B + %B + %O ->  O * (1 + %) = B * (1 + %) + %O ->  O = B + -----O
                                                                                      1 + %
espressa rispetto all'ordinato
Nel secondo caso, percentuale su ordinato, si dovrà produrre una quantità pari a : 
                                                              1
  O = B + %O  ->  O - %O = B   ->  O * (1 - %) = B  ->  O = -----B
                                                            1 - %
dove % = Valore percentuale in T$P51C
 :  : FLD T$P51D __Scarto non arrotondato__
Se impostato, lo scarto viene calcolato senza arrotondamento, se lasciato a blanks viene eseguito l'arrotondamento all'unità più vicina.
 :  : FLD T$P51E __Numeratore dichiaraz.__
È il numeratore delle dichiarazioni di attività e costituisce la chiave univoca di questo archivio.
Deve essere definito numerico di 7 posizioni.
 :  : FLD T$P51F __Numeratore eventi__
È il numeratore degli eventi e costituisce la chiave univoca di questo archivio.
Deve essere definito numerico di 9 posizioni.
 :  : FLD T$P51G __Modo dichiaraz.scarti__
Identifica il modo di dichiarare gli scarti nelle attività produttive; il significato è il seguente : 
-     ' '    La quantità prodotta è al netto degli scarti
-     '1'    La quantità prodotta è al lordo degli scarti
-     '2'    Come ' ' e gli scarti vengono tolti dal residuo
-     '3'    Come '1' e gli scarti vengono tolti dal residuo
È necessario ricordare che questo campo è utilizzato unicamente all'atto della dichiarazione :  nell'archivio delle attività, e di conseguenza nelle sue visualizzazioni e stampe, sono sempre riportate separatamente le quantità di buoni e di scarti.
 :  : FLD T$P51H __Sovraproduzione__
Se impostato, l'eventuale sovraproduzione in un'operazione viene assunta come quantità da produrre per le operazioni successive. Se lasciato in bianco, la quantità da produrre non supererà la quantità originale dell'ordine.
 :  : FLD T$P51I __Variazione automatica risorsa__
Se impostato, viene assunta in automatico l'ultima risorsa su cui viene eseguita la dichiarazione.
Questa impostazione è da valutare con attenzione, in quanto i tempi standard sono comunque quelli della risorsa di partenza.
 :  : FLD T$P51L __Contenitore note attività__
Se impostato, è attivo il collegamento delle note alla dichiarazione delle attività.
 :  : FLD T$P51M __Contenitore note eventi__
Se non è impostato il campo T$P5DJ in tabella P5D risale al campo T$P51M per il collegamento delle note alla gestione degli eventi. Se non impostato nemmeno T$P51M assume contenitore EV.
 :  : FLD T$P51N __Ripresa impegni materiali__
Se impostato, e se nel tipo impegno materiali (P5I) è presente il suffisso del programma di ripresa, viene eseguita la ripresa. Riferirsi alla documentazione della tabella P5I per ulteriori informazioni.
 :  : FLD T$P51O __Ripresa impegni risorse__
_7_Impegni risorse base
Se impostato, e se nel tipo impegno risorse (P5S) è presente il suffisso del programma di ripresa, viene eseguita la ripresa. Riferirsi alla documentazione della tabella P5S per ulteriori informazioni.
_7_Impegni risorse avanzati
Questo campo va sempre impostato in presenza di schedulazione BCD. In essa verrà comunque eseguita la ripresa dei campi standard di  schedulazione (date inizio e fine, risorsa specifica, vincoli ...)
Il suffisso del programma di ripresa di tabella P5S va utilizzato per riprendere altri dati specifici.
 :  : FLD T$P51P __Tempo fittizi__
Se impostato, il tempo di approvvigionamento dei codici fittizi (o resi tali nel legame) si aggiunge a quello dell'assieme (o quello di rettifica del legame) per datare gli impegni rilasciati.
Viene assunto unicamente il tempo di approvvigionamento fisso di produzione.
Se presenti più fittizi in cascata, i tempi vengono sommati.
**NB** :  questa azione viene eseguita unicamente nella datazione degli impegni rilasciati. Per ottenere lo stesso risultato nella datazione degli impegni pianificati bisogna impostare il flag in tabella M51.
 :  : FLD T$P51Q __Attivazione scenari__
Se impostato, nelle funzioni di interrogazione e stampa, viene richiesto lo scenario.
Va ricordato che la costruzione degli impegni risorse a partire dal ciclo dell'ordine / documento nettificato dagli impegni risorse, nel caso di impegni avanzati (S2), viene sempre eseguita sullo scenario '**'.
 :  : FLD T$P51R __Numeratore impegni risorse__
È un elemento della tabella CRNS5.
È il numeratore del file S5IDIR0F che permette di recuperare la chiave univoca del file degli impegni risorse.
Questo numeratore viene utilizzato anche per reperire l'IDOJ degli impegni pianificati, derivati dai consigli di pianificazione (archivio M5CONS0F).
 :  : FLD T$P51S __Ultima operazione da ciclo__
Se impostato, nella funzione di lettura dell'ultima fase di un documento viene fatta la scansione del ciclo del documento attivo al momento della lettura.
Va ricordo che, se non impostato, la fase viene derivata dal maggiore tra impegni risorse residui ed attività consuntivate.
 :  : FLD T$P51T __Visualizz.su ord.produzione__
È un valore V2/SI/NO. Se impostato, viene attivata la gestione variabile 'a visualizzatori' degli ordini di produzione tramite la forma di presentazione specificata nella tabella del tipo ordine. Se lasciato bianco, resta attiva la gestione base 'fissa'.
 :  : FLD T$P51U __Forma presentazione__
È significativo se è stato impostato in questa tabella il flag di visualizzatore su ord.prod, e se è assente il campo corrispondente a livello di tipo ordine (tabella P5T).
È un elemento della tabella B£Q, in cui si indica il programma di visualizzazione utilizzato per gli ordini di produzione.
 :  : FLD T$P51V __Suff.Parz.Lista__
Il campo rappresenta il suffisso del programma P5OR01L_x  (dove x = al contenuto del campo della tabella).
Valorizzando il campo si abilita il lancio del programma in oggetto che consentono di effettuare parzializzazioni
specifiche nella lista delle testate ordini di produzione (P5OR01L)
 :  : FLD T$P51W __Numeratore MFP__
SV :  E' il numeratore utilizzato per i legami interni MFP.
Implicitamente la sua presenza ha il significato di MFP attivata :  in tal modo si evita di appesantire l'applicaizione con controlli inutili, in assenza di MFP.
 :  : FLD T$P51X __Tempi previsti da archivio dichiarazioni__
Impostando a '1', si ottiene che i tempi previsti (da £G35) di una attività su origine vengano letti dall'archivio attività (P5ATTI0F) e non ricalcolati a partire dal ciclo (ad esempio dell'ordine di produzione nel caso di tipo origine VP).
Il default è ' ', ovvero tempi previsti ricalcolati da ciclo.
 :  : FLD T$P51Z __Modo dichiarazione automatiche__
Normalmente per le operazioni automatiche che hanno il flag di rilevanza operazione a '1' (non riportare su S5IRIS) non viene scritta la dichiarazione di attività su P5ATTI, contestualmente alla dichiarazione della milestone.
Se si imposta il presente flag, viene scritta la dichiarazione automatica anche in questa situazione.
