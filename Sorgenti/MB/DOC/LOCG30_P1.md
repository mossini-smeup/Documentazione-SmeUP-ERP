# Funzioni comuni
# Funzioni versione WEB
    dal 25 febb 2005 sono stati aggiornati i siti demo.smeup.com e buildup.smeup.com.
    il primo riporta esempi di questionari generici, il secondo esempi di questionari di demo per clienti o di prova.
    E' presente un filtro che mostra SOLO i questionari attivi.
# Funzioni versione LOOC.up
## Versione 1

- Salva con nome :  corretta gestione codice di configurazione. Dopo il primo salvataggio il codice veniva sbiancato.
- E' possibile assegnare una nota anche a domande a cui non è stata fornita la risposta.
- BuildUp WEB-  I pulsanti di salva e salva con nome sono attivi solo sulla sezione del riepilogo
- BuildUp Loocup - Dopo il salvataggio di una configurazione viene aggiornata il pannello con il titolo e gli oggetti
- G30 :  sono attive le regole. Vengono valutate al momento del salvataggio.
- Buildup è possibile utilizzare all'interno espressioni matematiche avanzate (trigonometriche dirette e inverse, logaritmiche, esponenziali, di approssimazione).
 - Sono disponibili anche funzioni di conversione da numero a stringa in formato SmeUp e viceversa e operazioni sulle stringhe (concatenazione, troncamenti)
- BuildUp - Loocup - Dalla finestra di compilazione di una questionario sono presenti le seguenti funzionalità : 
- A. traduzuione di tutte le regola in italiano (disponibile anche nella finestra per la scrittura delle regole).
- B. controllo sintattico di tutte le regole del questionario.
- C. ri-generazione del motore delle regole.
- D. analisi delle regole :  ogni regola viene spezzata negli elementi che la compongono (domande, valori, operazioni eseguite) e viene costruita una matrice con le informazioni su dove usata.
- Buildup WEB - attiva la cache sui questionari (dentro il file di configurazione, nella sezione Buildup, ci sono i parametri che attivano la cache e ne stabiliscono la durata)
- Buildup WEB - attivato il pre-caricamento dei fogli di stile per aumentare le performance. Maggiorni informazioni nell note per gli sviluppatori.


### note sul motore delle regole
La nuova versione di LoocUp genera il motore delle regole nella cartella di installazione di LoocUp, cartella LOOCUP_WRK, cartella ambiente (DEFAULT) se non è definito, cartella utente, cartella _form.

La cartella contiene, per ogni questionario 3 file : 

nome questionario.java   ---> le regole tradotte in java
nome questionario.class ---> l'eseguibile delle regole
nome questionario.txt     ---> un file che contiene l'istante di creazione delle regole del questionario

Di default le regole rimangono valide per 1 giorno, dopo di che la prima compilazione provoca la rigenerazione del motore delle regole.
Per ora non è possibile modificare la durata di validità della cache.

In ogni momento è possibile richiedere la rigenerazione del motore :  è sufficiente andare sulla finestra di compilazione del questionario e utilizzare il tasto con il punto esclamativo rosso posto in alto.
La rigenerazione impiegherà alcuni secondi, dopo di che è necessario chiudere la finestra di compilazione e riaprirla.

Per verificare la corretta generazione basta verificare la data di creazione del .class.
Nel caso di malfunzionamenti  del processo di generazione è possibile forzare la generazione cancellando tutti i file  che iniziano per "nome questionario".

Se nel questionario esistono regole che fanno riferimento a oggetti non esistenti la generazione del motore non avviene (viene mostrata una dialog che elenca gli errori trovati).
Per maggiori dettagli sugli errori, si può chiedere il controllo sintattico di tutte le regole utilizzando il pulsante con le righe rosse, posto alla sinistra di quello per la generazione delle regole.

Purtroppo il componente matrice, quello utilizzato ad esempio per elencare le risposte date, se chiamato due volte di seguito rimane invisibile e blocca LoocUp.

## Versione 2

- Le icone in alto hanno associato CTRL C ed S che non funzionano e sono diversi da quelli in basso
- Implementata gestione note su domande a cui non è stata fornita risposta


## Versione 3

- Modificata icona di lista configurazioni.
- Ripristinata gestione nota su domanda
- Corretta struttura questionario GRUFASME :  il parametro CF1 faceva riferimento a sezioni inesistenti
- Aggiunti oggetti nella matrice del riepilogo e dell'analisi delle regole.
- Sistemata traduzione delle regole non andava a capo.
- Aumenata la dimensione della finestra del wizard delle regole
- Oggetto J1FUN gestito come oggetto SmeUp normale.
- I pulsanti relativi alle regole, nella header bar del questionario, sono mostrati solo se sono definite regole.
- I pulsanti della domanda di tipo aggiunta in lista non configurata sono stati tradotti in italiano
- Se si opera su una dialog del G30 non sono più necessari 2 click per confermare, annullare o cancellare.
- Oggettizzati i testi delle domande del questionario e del G30.


## Versione 4

- Corretto check forzatura domande (presente nei questionari e nei setup)
- Modificata la gestione della posizione e della larghezza dei campi nelle tabelle e nei form
- Standardizzati i nomi dei pulsanti
- Estesa la gestione delle dipendenze alle domande configurate multiple (uso della [] nell'oggetto)
- Tolti oggetti della key dalla barra degli oggetti
- aggiornati i siti


## Versione 5

- Corretta auto compilazione :  se una sezione spariva la compilazione procedeva fino al riepilogo.
- Corretta gestione posizioni nella manutenzione tabelle.
- Rimosso il parametro MainGuiFrame dal Runtime per rendere le dialog del G30 indipendenti dal MainGuiFrame.


## Versione 6

- Reso dipendente da parametri il tipo di XML di ingresso e di uscita delle risposte e della struttura del questionario
- Aggiunta la possibilità di ripetere le sezioni e di includere questionari in questionari (vedi tabella CFQ)
- Aggiunti attributi all'XML delle risposte : 
     Lev che specifica il livello della domanda (1 indica che è dentro una sezione ripetibile o in un form incluso non ripetibile) 2 che è in un form incluso ripetibile e così via
    NRS è il numero di ripetizione della sezione, se non definito significa che la sezione non è ripetibile
    NRD è il numero di ripetizione della domanda, se non definito significa che la domanda è a risposta singola
- Aggiunta la possibilità di nascondere come default le domande del questionario vedi tabella CFD campo T$CFDL posizione 14
- Aggiunta la possibilità di abilitare l'esecuzione delle regole alla risposta e non al cambio di sezione (tabella CFQ)


## Versione 7

- I check box al caricamento adesso prendono il fuoco
- Eseguito controllo sulle domande obbligatorie all'interno delle dialog
- modificate chiamate all'AS400 utilizzando il servizio CFSER_02 (per i dettagli dei metodi vedi le note di sviluppo)
- modificata grafica domande configurate
- completata la nuova gestione delle domande con livelli aggiungendo anche il numero di ripetizione del form e il codice del form


## Versione 8

- Aggiunta una struttura dell'XML delle risposte :  se il salvataggio è esteso e il tipo di XML in output delle risposte è di tipo RIS allora l'xml delle risposte è diviso in sezioni. Per maggiori dettagli vedi il documento LOCG30_SVI - Note di sviluppo.
- rimosse i pulsanti per la gestione di note, forzatura regole e/o risposte se in una sezione nessuna domanda le utilizza. Questo consente di recuperare spazio nella finestra
- Object Field che mantenga i caratteri se mi posizioni a metà (inserimento e non sovrascrittura)
- Messa in linea scheda nuova delle configurazioni
- Resa dipendente dal tag Setup l'aggiunta delle risposte ausiliarie
- Gestite le domande di tipo 02 multiple
- Scelta in lista multiple viene sentito l'oggetto sul tasto dx
- Domande configurate, gestito il popup sulla label con il testo della domanda
- Gestite le domande di tipo 02 configurate
- Gestita correttamente l'history delle domande multiple configurate
- Scheda Questionario :  corretto loop
- Gestione fuoco quando cambio sezione :  se ho una domanda a scelta in lista prende il fuoco
- Modificata gestione larghezza campi di input di tipo ObjectField :  la larghezza del campo è determinata dal numero di caratteri e dalla larghezza massima della finestra
- Modificata gestione forzatura regole, risposta e nota.
- rimossa l'history dagli oggetti di tipo **
- gestito il tasto enter sugli object field :  se all'interno della manutenzione tabelle provocano il salvataggio, negli altri casi provoca il cambio di sezione


## Versione 9

- Gestito l'attributo Extend che indica se il salvataggio delle risposte è standard cioè va nel CFVARI o esteso va cioè nel B£MEDE.
- migliorata grafica dell'oggetto J1TEXT e completata gestione dei cartteri speciali
- corretta gestione fuoco delle domande con CheckBox e delle domande configurate multiple
- possibile navigazione con i soli pulsanti
- unificata gestione Xml in ingresso e uscita :  è stata eliminata la versione "stile emulatore"
- i questionari derivati dagli script delle schede restituiscono solo le risposte fornite.


## Versione 10

- Corretta gestione passaggio record precedente / successivo
- Corretta gestione icone sulla barra del titolo :  non venivano aggiornate quando si utilizzavano i pulsanti per il cambio di configurazione e riportavano *NEW all'inserimento di un nuovo elemento
- wizard di script :  nel caso il formato sia "(" vengono gestite le parentesi annidate
- Corretta gestione XML delle risposte :  se veniva specificato il formato RIS per l'input non veniva caricato l'XML delle risposte.
- Corretta gestione unlock delle configurazioni dei questionari di tipo RE Q-
- manutenzione tabelle :  corretta la gestione del tasto enter
- manutenzione tabelle :  forzato in maiuscolo i campi di input nel caso di oggetti tipizzati o non di descrizione


## Versione 11

- Nella gestione tabelle :  corretto il comportamento dei pulsanti per l'esecuzione del roll
- corretta la gestione dei tasti funzione nelle dialog del G30 :  capitava che ad esempio l'F12 in una dialog del G30 provocava anche la chiusura della finestra sottostante. E' stato anche corretto e aggiornato il legame tra i pulsanti della tastiera e le azioni disponibili.
- manutenzione tabella :  corretta la gestione del lock nel caso di creazione di nuove configurazioni, sia se l'azione è richiesta da emulatore, sia se richiesta dalla scheda dell'elemento sia dalla finestra di selezione oggetto se è stato utilizzato l'F6
- corretta la gestione dei parent  tra le finestre SectionSelector (dialgo di selezione tag) e UIG30TagDialog (la dialog con le domande della sezione selezionata)
- aggiunta la decodifica sulla prima domanda nelle domande configurate a risposta singola
- domande configurate multiple :  corretta la gestione dei numeri senza decimali in cui il numero di cifre era superiore a 10
- corretta la gestione delle domande configurate multiple :  non era possibile modificare una riga della tabella una volta inserita
- gestito il caso in cui un campo di input fosse aperto
- bloccato salvataggio se un campo contiene un valore non valido
- nel caso del G30 Module (le dialog sono escluse) i campi di input risultano non modificabili se mancano i tasti salva o salva con nome
- manutenzione tabelle :  rimosse icone dalle label debli oggetti
- manutenzione tabelle :  rimosse icone dagli object field nel caso di oggetti di tipo ** o di tipo non specificato


## Versione 12

- Rimossi tutti gli errori riscontrati nella manutenzione tabelle
- Nella manutenzione tabelle è stata Implementata la gestione del tasto F15
- corretta la gestione delle immagini associate alle risposte nella compilazione di questionari
- incrementate le performance avendo ridotto le decodifiche e la verifica dell'esistenza degli oggetti
- corretta la gestione dell'unlock delle configurazione a seguito di copia o di salvataggio con nome diverso
- modifcata la gestione dei lock delle configurazioni :  viene eseguita solo se la configurazione è valida e non sono in copia
- corretta la gestione delle domande configurate multiple di tipo scelta in lista
- Modificato parser regole per corregere mancato riconoscimento di errori nei segni di espressione :  ad esempio la presenza di un === al posto di un == in un'operazione di confronto bloccava il parser
- Modificata la dialog delle regole che verifica la modifica di una regola dopo il controllo sintattico.
- corretta gestione fuoco dialog G30 quando veniva chiamata dalla finestra di definizione filtro ricerca oggetti
- nelle domande con valori associati è stata corretta la gestione delle decodifiche :  comparivano solo dopo selezione diretta e non dopo l'azione di una regola


## Versione 13

- ottimizzato l'uso delle decodifiche degli object field nel G30
- corretto errore gestione fuoco tra dialog G30 e dialog selezione oggetti
- corretto un'errore nell'object field :  se richiesto l'oggetto e non il valore nel caso di numeri veniva restituito il codice formato da zeri e non a blank
- corretta la gestione delle decodifiche nel caso di domande con un elenco di valori associati
- risolto problema dell'editor delle regole :  ora non si blocca più se vengono usati operatori non validi (es. === )
- manutenzione tabelle :   corretto un errore nella gestione di campi non tipizzati nel caso l'utente immetta un - corretta gestione eliminazione configurazioni da popup scheda questionari
- corretta gestione immagini associate alle risposte dei questionari
- corretta gestione modifica domande configurate di tipo scelta in lista
- manutenzione tabelle :  corretta gestione pulsante F6 nel caso si invocasse su un'oggetto non esistente
- corretta la dialog che gestisce gli script :  se un oggetto era dipendente da un'altro non veniva recuperato il valore
- corretta gestione fuoco tra editor e wizard
- modifica del parser, del wizard e del motore delle regole per consentire ricoscimento, costruzione guidata e interpretazione dei nuovi operatori di confronto. I nuovi operatori, disponibili nel wizard consentono di verificare che una data risposta appartenga a o non appartenga a un range o a una lista di oggetti dedotta da un OAV di SmeUp
- manutenzione tabelle :  corretta la gestione dell' F12 dopo l'esecuzione di una ricerca
- risolto problema campi di intestazione passati senza posizione
- corretta gestione messaggi di errore dopo l'esecuzione delle regole :  veniva riproposto l'ultimo messaggio emesso
- corretta gestione immagini se inserito codice non valido
- manutenzione tabelle :  corretto errore su copia elementi di tabella
- corretto errore salvataggio setup
- corretto errore su salvataggio oggetti J1TXT
- corretto wizard regole funzione SETFILTRO
- corretta gestione fuoco tra finestre wizard regole
- aggiunta la possibilità di visualizzare le immagini della prima domanda delle configurate multiple
- aggiunta la possibilità di scegliere per immagini quando una domanda ha associato valori
- aggiunto scroll su oggetto J1TXT


## Versione 14

- Aggiunte le regole ADDFUNVAL e RMVFUNVAL :  possono aggiungere o rimuovere una lista di valori letta da AS400 utilizzando un servizio che restituisca una griglia.
I parametri ammessi sono i seguenti :  domanda a cui vanno aggiunti/rimossi i valori, funzione da invocare, codice colonna che contiene valori, codice colonna di filtro e valore filtro.
Gli ultimi due valori sono opzionali.
Per rendere dinamica la chiamata da fare all'AS400 si possono inserire le variabili del configuratore con la sintassi "aperta quadra" codice_domanda "chiusa quadra"
Se la variabile è multipla vengono eseguite n chiamate, una per ogni valore.
La funzione accetta fino a 3 variabili multiple/singole
- Aggiunta la possibilità di emettere messaggi con parametri :  esempio ADDMSGT('attento il valore '; DOMANDA; ' non è valido')
- modificato wizard per la gestione delle funzioni ADDFUNVAL e RMVFUNVAL per avere l'inserimento guidato della funzione da chiamare
- aggiunta la possibilità di accedere a valori associati alle domande con la sintassi V.DOMANDA
- aggiunta la possibilità di accesso alle risposte multiple o agli oav multipli
- il motore regole è ora in grado di assegnare una risposta, a una domanda con valori associati obbligatoria, se è rimasta una e una sola risposta possibile da regole
- Manutenzione tabelle :  gestiti i campi /V
- Modificata gestione domande con valori associati.
 nel parametro di presentazione, campo tipo compilazione, è possibile specificare come mostrare l'elenco di valori associati :  come gruppo di check su 1/2/3 colonne oppure su liste di 10 o 15 valori.
Il comportamento di default è che la lista è mostrata quando ho più di 5 valori e i check quando ne ho meno.


## Versione 15

- Aggiunte le regole ADDMSGW e ADDMSGI :  vengono emessi dei messaggi di avviso o di informazione. non sono bloccanti. Se emessi una volta non vengono più emessi.
- aggiunto il controllo sulla lunghezza massima nel caso di risposte la cui lunghezza è di 35 caratteri.
- aggiunto il controllo sulla duplicazione di sezioni e domande
- aggiunta la possibilità di visualizzare le azioni compiute dalle regole anche nel motore statico.
- aggiunta la possibilità di attivare / disattivare il tracciamento delle regole
- implementata la possibilità di visualizzare le informazioni di esecuzione delle regole anche dentro la matrice
- corretto la gestione delle domande configurate singole nel caso in cui la prima domanda non era un object field
- compattato il formato dell'XML delle risposte scritte su AS400 :  vengono rimossi gli attributi non signifcativi
- aggiunta la possibilità di modificare la descrizione per i questionari con chiave automatica sul salva
- aggiunta la funzione GETDESCRESP(-variabile-) che recupera la descrizione della risposta contenuta in -variabile-.
- aggiunta la funzione GETDESCRESPAT(-variabile-; -indice-) che recupera la descrizione della risposta contenuta in -variabile- di dato indice (per domande multiple).
- aggiunta la funzione GETOBJDESC(-tipo-;-parametro-;-codice-) che recupera la descrizione del'oggetto identificato dalla terna -tipo-;-parametro-;-codice-
- corretto il comportamento dell'object field quando si eseguiva una selezione con la tendina aperta :  era necessaria una seconda selezione perchè la prima andava persa
- aggiunta la possibilità, nel caso di messaggi lunghi di copiarli nel clipboard.
- corretto il comportamento del motore delle regole nel caso di applicazione ad ogni risposta :  procedere all'indietro causava la non esecuzione delle regole delle domande.


## Versione 16

- Aggiunta la domanda di servizio *K1 :  consente di definire tramite regole il codice della configurazione. Questa variabile è disponibile solo per i questionari che fanno uso delle domande ausiliarie
- Corretta la gestione dei numeri espressi in forma scientifica.


## Versione 17

- Motore Regole BuildUp - Rimossa la domanda *K1 (vedi Versione 16). Aggiunta in sua vece la domanda di servizio CFG_K1. Aggiunte inoltre le domande ausiliarie CFG_K2 e CFG_K3 per consentire di modificare tramite regole i codici delle chiavi 2 e 3 della configurazione. Se le chiavi di configurazione sono automatiche le regole che modificano le chiavi non hanno effetto.
- Motore Regole BuildUp - Aggiunta la funzione setCfgDesc(espressione) che consente di impostare la descrizione associata alla configurazione. Come parametro ammette una qualunque espressione che restituisca un testo.
- Motore Regole BuildUp - Aggiunta funzione getAuxResp(apice codice_domanda_ausiliaria_senza_asterisco apice) che restituisce il valore delle domande ausiliarie definite in BuildUp. Ad esempio per sapere il nome dell'utente che ha creato la configurazione si utilizza la regola getAuxResp('UC') :  il codice della domanda ausiliaria è *UC. Per conoscere tutte le domande ausiliarie consultare la documentazione.
- Motore Regole BuildUp - Aggiunta la funzione ISEMPTY(codice_comanda) che restituisce VERO se alla domanda codice_domanda non è stata fornita una risposta.
- Wizard Script - Aggiunta la gestione per subsezioni :  se nello script di definizione del questionario all'interno di una sezione si trovano delle righe che iniziano con " : XXXX" indico che la sezione è composta da subsezioni. Il wizard mostrerà una finestra con n tab, uno per ogni subsezione.
- Wizard Script -  Gestire anche le domande configurate a risposta singola. Il formato dell'output è identico a quello delle domande non configurate. A differenza dell'uso in BuildUp, dove il formato della risposta cambia, l'utilizzo delle domande configurate a risposta singola negli script è solo un modo di organizzare graficamente la disposizione delle domande.

