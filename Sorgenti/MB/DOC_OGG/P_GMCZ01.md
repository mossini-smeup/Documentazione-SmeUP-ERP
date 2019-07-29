# Gestione Colli
## Generalità
In Sme.up il collo viene utilizzato principalmente per : 
 * la movimentazione di magazzino (per unità di carico)
 * la movimentazione in produzione (per unità di movimentazione)
 * la gestione delle spedizioni e delle packing list (gestione degli imballi)

La gestione dei colli permette di creare modificare visualizzare e cancellare un contenitore (collo).

## Formato guida
![GMCZ_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMCZ01/GMCZ_01.png)Le opzioni sono quelle tipiche dei formati guida di gestione.

## Formato lista
![GMCZ_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMCZ01/GMCZ_02.png)
## Formato dettaglio
![GMCZ_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMCZ01/GMCZ_03.png)
### Campi significativi
 * _2_Tipo contenitore, identifica il tipo contenitore a cui il collo appartiene (es. pallet, scatola cartone, cassone ferro, ecc...) l'informazione è codificata nella tabella GMB
 * _2_Contenitore padre, si possono gestire contenitori che contengono articoli e che a loro volta sono contenuti in altri contenitori (es. scatole contenute in pallet o cassoni), in questo campo si può indicare il contenitore che contiene quello in gestione
 * _2_Peso netto, Peso lordo, Dimensioni, Volume, raggruppano le caratteristiche fisiche del contenitore
 * _2_altri dati, negli altri campi son o contenute informazioni specifiche proprie di gestioni particolari  per le quali si utilizza il contenitore (es. avanzamento produzione, spedizioni, logistica di magazzino)

Con F10 si lanciano le funzioni oggetto del contenitore, tra cui l'interrogazione generalizzata "Sintesi collo" (cfr. doc. P_GMSI02).
![GMCZ_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMCZ01/GMCZ_04.png)