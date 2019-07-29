# Prerequisiti e Controlli preliminari
Si raccomanda di controllare prima del lancio della funzioni che la tabella delle causali delle prestazioni (tabella C5P) sia compilata con i codici standard revisti dalla normativa del modello 770 e della certificazione unica.

Se i codici utilizzati non corrispondono a quelli indicati dall'Agenzia delle Entrate è necessario allineare i dati delle ritenute rilevate con tali codici.

# Obiettivo
Tramite questa funzione verrà prodotto il file da trasmettere all'agenzia delle entrate per il 770 semplificato, relativo al lavoro autonomo.

Verranno elaborati tutti i movimenti presenti nell'archivio delle ritenute per il periodo di elaborazione selezionato.

Prima di procedere è necessario controllare i dati anagrafici aziendali : 
 * Ragione sociale
 * Partita Iva
 * Codice Fiscale
 * Indirizzo Mail

# Richiesta Parametri

* Periodo di competenza :  indicare l'anno di competenza dell'invio

* Data :  da compilare nel caso in cui si voglia selezionare un periodo diverso da inizio e fine dell'anno indicato nel punto precedente

* Percipiente :  da compilare nel caso in cui si voglia selezionare un range o singolo percipiente

* Trasferimento :  mettendo una carattere qualsiasi si accede alla finestra di impostazione del percorso di salvataggio del file. In questa finestra impostare il tipo di trasmissione (si consiglia di utilizzare il 5), il nome del file (può essere utilizzato qualsiasi nome e qualsiasi estensione), e il percorso della cartella IFS (preceduta e seguita dal carattere "/") in cui verrà collegato il file da trasmettere all'agenzia. La cartella deve essere creata : 
![C5C070_005](http://localhost:3000/immagini/MBDOC_OGG-P_C5DC03A/C5C070_005.png)Nel caso in cui in fase di installazione vi sia già stato impostato il percorso di trasferimento potrete sceglierlo indicando un '!' nel campo 'Memorizzazione Dati Video' in alto a sinistra : 
![C5C070_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5DC03A/C5C070_006.png)
## Casi particolari

* Per gestire i casi delle causali G/H/I per le quali risulta necessario indicare l'anno di cui è sorto il diritto alla percezione delle indennità, è stato previsto che debbano essere specificatamente create delle causali C5P al cui interno venga indicato lo specifico anno di riferimento. Va verificato se sussistono casi del genere e nel caso vanno codificate le specifiche causali. Tali causali andranno poi imputate ai documenti di pertinenza.

* Per gestire i casi in cui la quota non imponibile va indicata in "altre somme non soggette" anche per i soggetti esteri (invece di somme non soggette a ritenuta per regime convenzionale) andrà previsto per le relative causali l'indicazione del campo "Forza altre somme".

* Per gestire i casi in cui la ritenuta va indicata in "a titolo di imposta" e non "di acconto" andrà previsto per le relative causali l'indicazione del campo "A titolo di imposta".

* Per gestire i casi di "categorie particolari" andrà previsto per le relative causali l'indicazione del campo corrispondente.

* Per i soggetti esteri il codice fiscale italiano dovrà essere inserito tramite l'apposita estensione anagrafica £24.

