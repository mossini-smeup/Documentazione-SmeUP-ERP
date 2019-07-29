# Prerequisiti e Controlli preliminari
Si raccomanda di controllare prima del lancio della funzioni che la tabella delle causali delle prestazioni (tabella C5P) sia compilata con i codici standard revisti dalla normativa del modello 770 e della certificazione unica.

Se i codici utilizzati non corrispondono a quelli indicati dall'Agenzia delle Entrate è necessario allineare i dati delle ritenute rilevate con tali codici.

# Obiettivo

Tramite questa funzione verrà prodotto il file da trasmettere all'agenzia delle entrate per la certificazione unica.
Oltre a generare il file verranno prodotte le stampe di controllo ed i modelli.

Si ricorda che vengono gestiti solo i seguenti tipi record : 
* A :  record di testa della fornitura e contiene i dati identificativi della fornitura e del soggetto responsabile dell'invio telematico (fornitore).
* B :  record contenente i dati anagrafici del sostituto d'imposta tenuto alla presentazione delle C.U.
* D :  record contenente i dati anagrafici del percipiente della singola C.U.
* H :  record contenente i dati relativi alle comunicazioni dati delle certificazioni lavoro autonomo, provvigioni e redditi diversi.
* Z :  record di coda della fornitura e contiene alcuni dati riepilogativi della stessa

Verranno elaborati tutti i movimenti presenti nell'archivio delle ritenute per il periodo di elaborazione selezionato.

Prima di procedere è necessario controllare i dati anagrafici aziendali : 
 * Ragione sociale
 * Partita Iva
 * Codice Fiscale
 * Indirizzo Mail

# Richiesta Parametri

![C5C070_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5CU14A/C5C070_004.png)
* Tipologia di invio. Selezionare : 
**   - Invio ordinario - Normale Trasmissione dei Dati prima della scadenza
** S - Invio sostitutivo - Trasmissione che sostituisce una precedente certificazione inviata
** A - Annullamento - Trasmissione che annulla una precedente certificazione inviata, senza che vengano inviati nuovi dati sostitutivi

* Periodo di competenza :  indicare l'anno di competenza dell'invio

* Data :  da compilare nel caso in cui si voglia selezionare un periodo diverso da inizio e fine dell'anno indicato nel punto precedente

* Percipiente :  da compilare nel caso in cui si voglia selezionare un range o singolo percipiente

* Trasferimento :  mettendo una carattere qualsiasi si accede alla finestra di impostazione del percorso di salvataggio del file. In questa finestra impostare il tipo di trasmissione (si consiglia di utilizzare il 5), il nome del file (può essere utilizzato qualsiasi nome e qualsiasi estensione), e il percorso della cartella IFS (preceduta e seguita dal carattere "/") in cui verrà collegato il file da trasmettere all'agenzia. La cartella deve essere creata : 
![C5C070_005](http://localhost:3000/immagini/MBDOC_OGG-P_C5CU14A/C5C070_005.png)Nel caso in cui in fase di installazione vi sia già stato impostato il percorso di trasferimento potrete sceglierlo indicando un '!' nel campo 'Memorizzazione Dati Video' in alto a sinistra : 
![C5C070_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5CU14A/C5C070_006.png)
* Codice Attività :  indicare il codice dell attività svolta in via prevalente (con riferimento al volume d affari) desunto dalla classificazione delle attività economiche, vigente al momento del rilascio della Certificazione Unica. Si precisa che la tabella dei codici attività è consultabile presso gli uffici dell Agenzia delle Entrate ed è reperibile sul sito Internet del Ministero dell Economia e delle Finanze www.finanze.gov.it e dell'Agenzia dell Entrate www.agenziaentrate.gov.it.

* Codice Sede :  è un dato facoltativo che può essere utilizzato per identificare diverse sedi, ovvero gestire separatamente gruppi di dipendenti. Per fare ciò è possibile indicare per ciascuna gestione un codice identificativo. Tale codice,autonomamente determinato dal sostituto è costituito esclusivamente da valori numerici compresi tra xl valore 001 ed il valore 999. Il predetto codice, riportato nel 730-4 messo a disposizione del sostituto, costituisce elemento identificativo della gestione di appartenenza del dipendente al fine dello svolgimento delle operazioni di conguaglio.

* Data Firma :  inserire la data della firma della certificazione unica

* Dati Rappresentante firmatario della comunicazione
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto che firmerà la certificazione (in genere si tratta del rappresentante legale)
** Codice Carica :  codice carica del soggetto
** Società :  qualora il vero rappresentante sia una società, qui dovranno essere indicati il tipo ed il codice contatto dell'anagrafica enti utilizzato per il soggetto che firmerà la certificazione. Viceversa come rappresentante dovrà essere indicato l'ente rappresentante di tale società.

Ad esempio se il rappresentante legale è il fornitore 123456 dovrò compilare i campi in questo modo : 
![C5C070_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5CU14A/C5C070_007.png)
* Dati Soggetto Intermediario :  questi campi vanno indicati solo nel caso in cui l'invio tramite Entratel dei dati non venga effettuato dall'azienda stessa ma da un intermediario
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** Data Impegno :  data impegno intermediario
Ad esempio se il mio intermediario è il fornitore 111111 e si è impegnato a trasmettere per me in data 01/01/15 dovrò compilare i campi in questo modo : 
![C5C070_008](http://localhost:3000/immagini/MBDOC_OGG-P_C5CU14A/C5C070_008.png)
* Dati Responsabile Trasmissione :  questi campi vanno indicati solo nel caso in cui l'invio tramite Entratel dei dati non venga effettuato dall'azienda stessa ma da un intermediario. In questi campi va indicato il soggetto a cui è intestata la firma digitale Entratel. Nella quasi totalità dei casi in questo campo va indicato lo stesso codice impostato nel campo Intermediario
** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto in questione
** Tipo Fornitore :  indicare 10 se si tratta di intermediario

* Protocollo Telematico (compare ed è da compilare solo in caso di annullamento o reinvio sostitutivo) :  protocollo della trasmissione, da sostituire/annullare
* Protocollo Documento (compare ed è da compilare solo se annullamento o reinvio sostitutivo) :  protocollo documento della trasmissione, da sostituire/annullare

* Stampa Modelli :  se impostato con 1 produce la stampa cartacea dei modelli della certificazione

## Casi particolari

* Per gestire i casi delle causali G/H/I per le quali risulta necessario indicare l'anno di cui è sorto il diritto alla percezione delle indennità, è stato previsto che debbano essere specificatamente create delle causali C5P al cui interno venga indicato lo specifico anno di riferimento. Va verificato se sussistono casi del genere e nel caso vanno codificate le specifiche causali. Tali causali andranno poi imputate ai documenti di pertinenza.

* Per gestire i casi in cui la quota non imponibile va indicata in "altre somme non soggette" anche per i soggetti esteri (invece di somme non soggette a ritenuta per regime convenzionale) andrà previsto per le relative causali l'indicazione del campo "Forza altre somme".

* Per gestire i casi in cui la ritenuta va indicata in "a titolo di imposta" e non "di acconto" andrà previsto per le relative causali l'indicazione del campo "A titolo di imposta".

* Per gestire i casi di "categorie particolari" andrà previsto per le relative causali l'indicazione del campo corrispondente.

* Per i soggetti esteri il codice fiscale italiano dovrà essere inserito tramite l'apposita estensione anagrafica £24.

