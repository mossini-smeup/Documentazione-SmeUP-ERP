# P5C - Causali attività produttive
 :  : DEC T(ST) K(P5C)
## OBIETTIVI
Descrive le causali con cui si eseguono le dichiarazioni di attività di produzione
## SOTTOSETTORI
Non gestiti
## DEFINIZIONE TIPO ATTIVITÀ
L'attività di produzione può essere di tre tipi, in funzione della composizione dei campi della tabella : 
1)   Attività su origine :  è una dichiarazione a fronte di un impegno risorse relativo ad un ordine di produzione o ad  una riga di documento esterno. La si individua impostando il tipo origine.
2)   Attività su ciclo :  è una dichiarazione a fronte di una fase di ciclo relativo ad un oggetto. La si individua impostando il tipo ciclo e non il tipo origine.
3)   Attività estemporanea :  è una dichiarazione libera di tempi e/o quantità. La si individua lasciando vuoti sia il tipo origine sia il tipo ciclo.
## CONTENUTO DEI CAMPI
 :  : FLD T$P5CA __Sottocausale attività__
È un elemento della tabella P5B. Se impostato, è un campo proposto all'atto dell'inserimento dell'attività, ed è modificabile se previsto nel formato del visualizzatore.
 :  : FLD T$P5CB __Forma di presentazione__
È un elemento della tabella B£Q. È un campo obbligatorio :  individua il programma (visualizzatore) che guida l'inserimento delle attività di questa causale.
 :  : FLD T$P5CC __Gruppo flag__
È un elemento della tabella B£Y. Se valorizzato, alle dichiarazioni di attività vengono assegnati i flag di questo elemento.
 :  : FLD T$P5CD __Parametri impliciti__
È un elemento della tabella C£I. Definisce la natura dei campi liberi (5 numerici e 5 alfanuerici) dell'attività.
 :  : FLD T$P5CE __Tipo origine__
È un elemento fisso V2/P5TOS :  la sua presenza individua un'attività su origine.
Può assumere i seguenti valori : 
 :  : PAR F(04)
-     'VP'   definisce un impegno su un ordine di produzione.
-     'DO'   definisce un impegno di riga di documento esterno.
-     'CZ'   definisce un impegno su contenitore.
-     'AR'   definisce un impegno su un articolo.

 :  : FLD T$P5CF __Tipo documento__
È un elemento della tabella V5D. È significativo in caso di tipo origine 'DO' :  in questo caso viene proposto all'atto dell'inserimento dell'attività ed è modificabile se previsto nel formato del visualizzatore.
 :  : FLD T$P5CG __Tipo ciclo__
È un elemento della tabella BRT. Se è presente, il tipo origine non è significativo; altrimenti individua il ciclo a cui assegnare la dichiarazione. Non è modificabile nella dichiarazione dell'attività. Deve obbligatoriamente prevedere come oggetto tipo risorsa un oggetto di tipo 'RI'.
 :  : FLD T$P5CH __Tipo/parametro oggetto intestazione__
Il tipo e il parametro dell'oggetto intestazione individuano la natura dell'oggetto intestatario dell'attività.
Sono significativi in caso di attività estemporanea :  vengono proposti all'atto dell'inserimento dell'attività, e sono modificabili se previsto nel formato del visualizzatore.
In caso di attività su origine, il tipo, il parametro e l'oggetto sono fissati dall'origine stessa.
In caso di attività su ciclo, il tipo e il parametro sono fissati da quanto contenuto nel tipo ciclo.
In questi due ultimi casi non sono modificabili, anche se previsto dal visualizzatore :  vengono riportati ai valori originali.
 :  : FLD T$P5CI.T$P5CH
 :  : FLD T$P5CQ __Ripresa tempi__
È un campo libero, in cui si può stabilire in quali tempi verranno trasferiti i valori di input.
Il suo utilizzo naturale è in una ripresa batch : 
_9_Esempio :  una transazione contiene il tempo di lavoro ed un'altra il tempo di attrezzaggio, ad esse si assegneranno due causali diverse, nelle quali questo campo verrà impostato nel seguente modo (nell'ipotesi che il tipo tempo sia '1')  : 
 :  : PAR F(04)
- Posizione                '1...5....0'.
- Tempo lavoro :             'X         '.
- Tempo attrezzaggio :   :     '  X       '.

 :  : FLD T$P5CJ __Tipo Ente__
È un elemento della tabella BRE. In caso di attività su origine non è significativo :  il tipo e l'ente sono fissati da quanto contenuto nell'origine, e non sono modificabili, anche se previsto dal visualizzatore. Vengono riportati ai valori originali.
Negli altri casi viene proposto all'atto dell'inserimento dell'attività, ed è modificabile se previsto nel formato del visualizzatore.
 :  : FLD T$P5CK __Tipo Risorsa effettiva__
È un elemento della tabella BRR. È significativo in caso di attività estemporanea :  viene proposto all'atto dell'inserimento dell'attività. In caso di attività su origine o su ciclo, vengono proposti il tipo e la risorsa della fase inserita.
È in tutti i casi un campo modificabile se previsto nel formato del visualizzatore.
 :  : FLD T$P5CL __Tipo Risorsa specifica__
È un elemento della tabella BRR. Se impostato, è un campo proposto all'atto dell'inserimento dell'attività, ed è modificabile se previsto nel formato del visualizzatore.
 :  : FLD T$P5CM __Unità di misura dei tempi__
È un elemento della tabella UMS. Se impostato, è un campo proposto all'atto dell'inserimento dell'attività.
Se non impostato e l'attività è su origine o su ciclo, viene proposto il valore della fase inserita.
È in tutti i casi un campo modificabile, se previsto nel formato del visualizzatore.
 :  : FLD T$P5CN __Propone data odierna__
È un elemento fisso V2/SI/NO :  se impostato, all'atto della dichiarazione propone la data odierna, se non impostata.
 :  : FLD T$P5CO __Scarico impegni__
È significativo se l'attività è a fronte di ordine di produzione.
Se impostato, all'atto della dichiarazione : 
- se vale '1', esegue il prelievo dei componenti legati alla fase che si sta avanzando, per la quantità corrispondente, secondo il coefficiente di impiego, moltiplicata per la somma della quantità buona e della quantità scartata.
- se vale '2', invece di eseguire il prelievo in modo cieco, presenta la lista dei prelievi da eseguire (con la quantità proposta), con la possibilità di modificarli.
In questo secondo caso bisogna impostare, nel flusso di inserimento dell'attività, il passo di scarico. Ciò è necessario in quanto si può caratterizzare la modalità di presentazione, tramite i parametri del passo del flusso.
 :  : FLD T$P5CP __Carico assieme__
È un elemento fisso V2/SI/NO :  se impostato, all'atto della dichiarazione, e a fronte di ordine di produzione, esegue il versamento dell'assieme per la quantità buona, nel caso in cui sia l'ultima fase dell'ordine.
 :  : FLD T$P5CR __Risorsa effettiva assunta__
È un oggetto 'RI' del tipo impostato nel tipo risorsa assunta.
È a disposizione dell'utente per inserirvi, in programmi di caricamento personali (in un caricamento batch, ad esempio) la risorsa effettiva che verrà assunta dalla transazione.
 :  : FLD T$P5CS __Controllo Giacenza Materiale__
Se impostato 1 o 2, all'atto della dichiarazione, controlla che il materiale da prelevare alla fase sia disponibile in base al gruppo Fonti, specificato nella tabella P5I.
- Se vale '1', esegue il controllo di disponibilità e restituisce un eventuale messaggio di errore.
- Se vale '2', esegue il controllo come al punto '1' ma, in più, presenta un elenco dei materiali con le quantità disponibili, evidenziando la causa di indisponibilità
- Se impostato  'x', esegue il controllo lanciando un programma B£G35G3_x.
Si noti che il controllo è significativo solo nel caso di Modalità di prelievo alla fase.
 :  : FLD T$P5CT __Controllo Esistenza alla fase__
Se impostato 1 all'atto della dichiarazione, controlla che la quantità avanzata sia minore o uguale all'esistenza della fase precedente.
Se impostato 'x', esegue il controllo lanciando un programma B£G35G3_x
 :  : FLD T$P5CU __Emualzione / Input panel__
Se impostato, le dichiarazioni di attività con questa causale saranno eseguite in input panel, se
invece lasciato in bianco, saranno eseguite in emulazione.
In dettaglio : 
Se impostato (esempio programma P5SUP_02)
- in 5250 Client Access - NON Ammesso
- in Loocup - Ammesso
  se presente il video xxxxxxxV (dove xxxx è il programma) viene assunto per posizionamento dei
  campi, se assente si assume l'input panel incolonnato
- in Mobile - Ammesso
  si assume sempre l'input panel incolonnato
Se non impostato (esempio programma P5AT10G_XX)
- in 5250 Client Access - Ammesso in emulazione video
- in Loocup - Ammesso in emulazione video
- in Mobile - NON ammesso
Questo comportamento viene assunto ovunque si tratti la dichiarazione di attività con questa causale
sia in inserimento sia in varazione.
