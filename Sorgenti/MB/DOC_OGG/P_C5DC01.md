# Obiettivo

Manutenere manualmente i record estratti e da includere all'interno del modello 770.

# Parametri
 * Anno :  inserire l'anno a cui si riferiscono i dati da manutenere
 * Sezione :  è possibile filtrare i quadri visualizzati nella successiva videata
* Campo filtro _ n _  :  nel caso in cui sia stata specificata una sezione è possibile effettuare tre filtri sui valori dei righi del quadro stesso. Ad esempio nel caso in cui si sia scelta la sezione ST, sarà possibile filtrare per codice tributo e/o per data versamento, ecc.

# Dettaglio
Confermando la videata di lancio verrà presentato il dettaglio dei record estratti all'interno del modello 770.
All'interno della videata sarà possibile gestire i record estratti e inserirne di nuovi.
Entrando all'interno del dettaglio di un record i valori estratti dal programma avranno un colore diverso rispetto ai dati da inserire manualmente : 
![C5C070_009](http://localhost:3000/immagini/MBDOC_OGG-P_C5DC01/C5C070_009.png)Tra i campi di dettaglio è possibile visualizzare anche lo stato della trasmissione che potrà essere : 
 * _Da trasmettere_ se il record non è ancora stato trasmesso e non si tratta di un record da inserire in una dichiarazione integrativa
 * _TRA Trasmessa_ se il record è già stato trasmesso in definitivo
 * _DIN DA integrare_ :  questo valore verrà impostato a mano nel caso in cui il record vada trasmesso in una dichiarazione di tipo 'Integrativo'
 * _NNN da non trasmettere : _ questo valore verrà impostato a mano nel caso in cui il record non vada trasmesso

Si sottolinea che i quadri estratti dal programma sono : 
 * Frontespizio
 * Quadro ST
 * Quadro SY sezione IV (percipienti esteri privi di codice fiscale)

Le altre sezioni del quadro IV andranno eventuamente inserite manualmente.

Per gestire gli altri quadri è invece necessario importare il file prodotto nel software di compilazione dell'agenzia delle entrare e completare i dati da li.

# Specificità per ravvedimenti

Nel caso in cui sia necessario inserire un record relativo a un ravvedimento digitare l'opzione 01 di inserimento. Nella prima videata indicare : 
 * Protocollo :  è un identificativo del record. E' possibile utilizzare il protocollo telematico del modello F24 per facilitare le ricerche/controlli futuri ma è anche possibile inserire una stringa alfanumerica libera
 * Periodo di Riferimento (quello indicato all'interno del F24 relativo al ravvedimento) dovrà essere compilato come MMAAAA dove MM è il mese di riferimento e AAAA l'anno
 * Ravvedimento :  impostare 1
 * Codice Tributo :  indicare il codice tributo a cui si riferisce il ravvedimento
Confermando lo specchietto comparirà il dettaglio del record in cui è necessario indicare : 
 * Ritenute operate :  inserire l'importo relativo alle ritenute ravvedute (_non_ l'importo relativo agli interessi versati, ovvero ai codici 8906)
 * Importo versato :  inserire l'importo totale versato (ritenute +  interessi)
 * Interessi :  inserire l'ammontare degli interessi versati per il ravvedimento in questione (quindi l'importo riportato sulla riga 8906)
 * Data versamento :  indicare la data in cui è stato effettuato il versamento del ravvedimento

Confermare quindi il record con F06

## Esempi

**Esempio 1 :   ravvedimento all'interno di uno stesso F24 di più periodi.**
In data 20/03/2015 è stato effettuato un ravvedimento operoso per 1000¤ di ritenute riferite a maggio 2014 sul codice tributo 1040 e per 400¤ di ritenute riferite a giugno 2014 sul codice tributo 1040.
Le sanzioni relative al primo ravvedimento sono 35¤ mentre quelle riferite al secondo ravvedimento sono 10¤ per un totale in F24 di 1445¤.
In questo caso sarà necessario inserire manualmente due righe : 
* Nella prima riga inseriremo : 
 ** Periodo di Riferimento :  052014
 ** Ravvedimento :  1
 ** Codice Tributo :  1040
 ** Data versamento :  20/03/15
 ** Ritenute operate :  1000
 ** Importo versato :  1035
 ** Interessi :  35
* Nella seconda riga inseriremo : 
 ** Periodo di Riferimento :  062014
 ** Ravvedimento :  1
 ** Codice Tributo :  1040
 ** Data versamento :  20/03/15
 ** Ritenute operate :  400
 ** Importo versato :  410
 ** Interessi :  10
**Esempio 2 :   presenza all'interno del F24 di versamenti corretti e di ravvedimenti**
In data 16/03/2015  sono state versate 1000¤ di ritenute riferite a febbraio 2015 sul codice tributo 1040 ed è stato effettuato un ravvedimento per 400¤ di ritenute riferite a gennaio 2015 sul codice tributo 1040. Le sanzioni relative al ravvedimento sono 10¤ per un totale in F24 di 1410¤.
In questo caso sarà prima di tutto necessario rettificare il record estratto e relativo alle ritenute riferite a gennaio 2015. Questo perchè il sistema avrà incluso la ritenuta di 400¤ nel record relativo alle ritenute di gennaio. Dal valore delle ritenute di questo record, quindi, andranno sottratti 400¤.
Successivamente sarà necessario inserire manualmente la riga del ravvedimento in cui inseriremo : 
 ** Periodo di Riferimento :  012015
 ** Ravvedimento :  1
 ** Codice Tributo :  1040
 ** Data versamento :  16/03/15
 ** Ritenute operate :  400
 ** Importo versato :  410
 ** Interessi :  10
