## Obiettivo

Obiettivo di questa funzione è popolare l'archivio contenente il dettaglio dei dati da trasmettere per la Comunicazioni Art. 21 DL 78/2010 (poi modificato dall'articolo 2 comma 6 del Dl 16/2012) a partire dai dati presenti in contabilità.

## Parametri di Input

* Modalità Esecuzione : 
** Solo Stampa  :  Verranno solo prodotte le stampe di log dell'elaborazione eseguita
** Stampa ed Esecuzione  :  Verranno prodotte le stampe di log dell'elaborazione eseguita e verranno scritti i record elaborati correttamente
* Tipo Ripresa  : 
** Scrivi solo mancanti :  Verranno ripresi solo i record che non sono scritti all'interno del file dello spesometro
** Scrivi tutti :  verranno cancellati e riscritti anche i record già presenti nell'archivio
* Tipo Elaborazione  :  permette di filtrare le registrazioni elaborate in base al fatto che si tratti di movimenti di acquisto/vendita
* Anno  :  indica l'anno solare di riferimento, saranno elaborati i movimenti registrati all'interno di questo periodo
* Periodo  :  permette di filtrare le registrazioni elaborate all'interno dell'anno.

## Prerequisiti e Note di elaborazione
* Criteri di Inclusione Automatici dei movimenti iva : 
** Data registrazione inclusa nel periodo indicato.
** Movimento Fiscale e Attivo (quindi non simulato o sospeso)

* Criteri di Esclusione Automatica dei movimenti iva : 
** Movimento di Corrispettivo
** Movimento di Pura IVA
** Movimento su Registro IVA Fittizio
** Assoggettamento con indicazione in tabella di caratteristica di Fuori Campo IVA o di esclusione esplicita dagli elenchi clienti/fornitori
** Movimenti estratto tramite apposita elaborazione dei dati black list.
** Intestatario che presenta nell'estensione anagrafica £44 l'indicazione che i documenti del soggetto non vanno trasmessi
** Movimenti che risultano essere trasmessi nell'intra. NOTA BENE :  vengono esclusi i movimenti per cui viene trovata una corrispondenza per n° di registrazione sull'archivio dei movimenti intra. Se tale corrispondenza non viene riscontrata, ma il movimento era stato di facto trasmesso, l'omissione dovrà essere applicata intervenendo manualmente sull'archivio dei movimenti dello spesometro. In alternativa l'esclusione potrebbe essere operata tramite l'esclusione degli assoggettamenti a livello di tabella IVA.
** Assenza di dati anagrafici completi del soggetto intestatario

* Forzature Applicabili da anagrafica : 
** Tramite l'estensione £44 dell'anagrafica contatti è possibile forzare :  la modalità di pagamento da applicare a tutti i documenti del soggetto o l'esclusione di tutti i documenti del soggetto

* Controlli/Modifiche da applicare manualmente, o tramite pgm di exit, per le esclusioni previste : 
** Cessioni all'esportazione di cui all'art. 8, comma 1, lettere a) e b), D.P.R. n. 633/1972  :  impostare i flag di esclusione dagli elenchi clienti/fornitori sugli assoggettamenti pertinenti nella tabella IVA
** Operazioni fuori campo IVA :  è nativamente previsto che gli assoggettamenti che presentano tale indicazione nella tabella IVA vengano automaticamente escluse. Ma qualora per varie ragioni si sia scelto di non dare questa indicazione precisa, andrà almeno indicata indicazione dell'esclusione dagli elenchi clienti/fornitori
** Operazioni effettuate dai contribuenti minimi :  nelle anagrafiche di questi soggetti andrà indicata, tramite l'estensione anagrafica £44 l'esclusione di tali soggetti dalla trasmissione.
** Importazioni :  se necessario (a seconda di come vengono registrate queste operazioni) escludere gli assoggettamenti pertinenti, tenendo comunque conto che i movimenti non iva, su registri fittizzi e di pura iva sono già automaticamente esclusi.
** Operazioni già comunicate all'anagrafe tributaria di cui all'art. 7 del D.P.R. n. 605/1973 (ad es. :  contratti di assicurazioni, compravendite immobiliari, ecc.) :  per queste sarà necessario operare essenzialmente secondo tre modalità : 
*** Escludendo le operazioni degli enti intestatari tramite l'estensione £44
*** Escludendo dagli elenchi clienti/fornitori gli assoggettamenti se previsti di specifici
*** Escludendo manualmente le singole operazioni dopo averle estratte, entrando in gestione del movimento e togliendone la validità.
** Operazioni Effettutate nei confronti di contribuenti non soggetti passivi iva e pagate dagli stessi con carte di credito, di debito o prepagate emesse da operatori finanziari soggetti agli obblighi di cui all'art. 7 del D.P.R. n. 605/1973 :  se possibile si potrà escludere direttamente i soggetti intestatari tramite l'estensione £44, viceversa, sarà necessario escludere sui singoli movimenti tramite manutenzione.
** Operazioni Effettuate e Ricevute in Ambito comunitario per le quali vi è l'obbligo di presentazione degli elenchi INTRASTAT :  tenendo conto come citato in precedenza vengono esclusi solo i movimenti per cui viene trovata una corrispondenza precisa per n° di registrazione andrà valutata la presenza degli eventuali movimenti manuali che si collegano "di facto" a documenti che risultano da trasmettere. Tali movimenti andranno poi esclusi tramite intervento manuale sull'archivio dei movimenti dello spesometro.
** Passaggi interni di beni tra rami di azienda documentati con fattura :  se possibile anche per questo casi si potrà indicare l'esclusione dei soggetti intestatari tramite l'estensione £44, mentre vicersa sarà necessario intervenire sui singoli movimenti.

* Altri Controlli/Verifiche : 
** Note credito non residenti :  se si sceglie la trasmissione analitica verranno escluse, mentre se si usa la forma aggregata, il valore delle note credito decurta il valore delle fatture. In questo ultimo caso, potrebbe  esserci la possibilità che nel periodo di elaborazione le note credito abbiano un valore più alto delle fatture. Questa casistica non è risolta dal modello polivalente.
** Eventuali movimenti di corrispettivi rientranti nell'obbligo andranno imputati manualmente
** Se si sono operate rettifiche o variazioni agli importi monetari delle transazioni, senza passare da registrazioni di documenti (es. registrazioni pura iva e/o registrazioni di contabilità generale), tali rettifiche dovranno essere poi aggiustate direttamente nell'archivio dei movimenti dello spesometro. Tali movimenti potrebbero essere intercettati tramite la ricerca di movimenti su causali aventi tali scopi.
** Triangolazioni comunitarie di cui all'art. 58 del D.L. n. 331/1993  :  vanno incluse, va quindi verificato che per le modalità in cui vengono trattate nel sistema lo vengano effettivamente.

* Programmi di aggiustamento.
** A standard sono previsti due programmi di aggiustamento, che nel caso possano essere previste delle logiche di aggiustamento ripetitive per l'azienda si possa sopperire alle considerazioni sopracitate.
** E' prevista l'exit standard C5CI00B_X, tramite la quale è possibile intervenire sui dati costruiti dalla logica standard con logiche proprie.
** E' prevista l'exit standard C5CI00C_X, tramite la quale è possibile intervenire sui controlli effettuati dal pgm standard.

## Stampe di Log

Al termine dell'elaborazione verranno prodotte tre stampe di log : 
* Quadratura Movimenti IVA :  Verrà prodotto un riepilogo dei movimenti iva elaborati per Mese/Registro/Assoggettamento IVA (più una sintesi finale per Registro/Assoggettamento).
Ognuna di questa sintesi verrà a sua volta spezzata se per la combinazione di Mese/Registro/Assoggettamento risultano presenti movimenti scartati, con l'indicazione del motivo preciso di scarto. Questa motivazione sarà anteceduta da due caratteri fissi : 
** "I" :  per indicare che la segnalazione è solo informativa e che il movimento è stato escluso per uno dei criteri previsti
** "E" :  per indicare che la segnalazione indica la presenza di un errore sui dati
Il totale per registro di questa stampa corrisponde allo stesso totale della stampa dei registri IVA. NOTA BENE :  il fatto che un movimento venga scartato, non implica un errore, può anche essere corretto che il movimento sia scartato. In caso di dubbio è possibile poi effettuare i dovuti controlli tramite il prodotto della stampa successiva.
* Segnalazioni Movimenti IVA :  Verrà prodotta una stampa con il dettaglio dei movimenti scartati, con indicazione del motivo dello scarto. Tramite questa stampa è possibile vericare in modo preciso il dettaglio delle segnalazioni sintetiche indicate dalla precedente stampa.
* Controllo Movimenti IVA :  verrà prodotta una stampa con il dettaglio di tutti i movimenti IVA elaborati.
