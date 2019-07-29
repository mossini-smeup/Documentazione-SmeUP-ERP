# Setup Utente per Looc.up V3R1 e V3R2.

A partire dalla versione V3R1 di Looc.up è stata introdotta la nuova gestione dei Setup Utente sulle sezioni della scheda.
La gestione nuova è stata pensata per esaurire le seguenti due esigenze : 
- Univocità delle chiavi di salvataggio dei setup in base ad un valore fornito nei dati da servizi generici. Questo valore si chiama Contesto (attributo Context nell'XML dei dati).
- Miglioramento delle performance di caricamento delle schede e dei setup.

Le differenze tra la gestione vecchia e la gestione nuova non si limitano solo a differenze tecniche, ma anche pratiche ed applicative.

Con la nuova gestione, non sono più visibili i bottoni di salvataggio e dei setup stessi, ma è visibile il solo bottone di gestione che mostra un popup per la selezione del setup ed altre funzioni.
Inoltre è stata rimossa l'applicazione automatica del setup utente di Default. Nelle future release sarà implementata la possibilità di attivare questa caratteristica nelle sezioni dove si ritiene utile o necessaria.

E' stata mantenuta, per compatibilità, la possibilità di disattivare la nuova gestione in favore della vecchia, ben sapendo che questa genera un decadimento delle performace di circa il 25-30% rispetto alla gestione nuova.
E' possibile attivare/disattivare la nuova gestione dei setup tramite una variabile (ENABLENEWSETUP) presente in SCP_CLO/DEFAULT (o più specifici per gruppo, ambiente, utente etc.).

Per usufruire appieno dei vantaggi in termini di performance della nuova gestione è anche necessario impostare il valore "Disabilita Invio Setup" presente nella tabella B£5. In questo modo si eviterà al sistema di inviare informazioni non più utili (i setup utente con le chiavi della vecchia gestione) a Looc.up.

Infine a partire dal 17/11/2010 è stata introdotta nel JACFG1 la variabile dinamica SMEUP.VER, utile a Looc.up per sapere che versione di Sme.UP è in uso. Questo può influire nel funzionamento della vecchia gestione dei setup. A seguire uno schema riassuntivo del funzionamento dei setup rispetto alle chiavi : 

## Vecchia gestione attiva : 

- Versione SMEDEV precedente al 17/11/2010
-- Salvataggio :  Come in precedenza viene utilizzata la chiave relativa alla scheda e alla sezione.
-- Caricamento :  Come in precedenza viene utilizzata le chiave relativa alla scheda e alla sezione.
-- Note :  Questo caso garantisce la perfetta retro-compatibilità con versioni SMEDEV più datate.

- Versione SMEDEV successiva al 17/11/2010
-- Salvataggio :  Se è presente l'informazione di contesto viene utilizzata come chiave, altrimenti viene utilizzata la chiave relativa alla scheda e alla sezione.
-- Caricamento :  Se è presente l'informazione di contesto viene utilizzata come chiave. In OGNI CASO vengono caricati anche i setup con le chiavi relative alla scheda e alla sezione.
-- Note :  I setup salvati in presenza di contesto non sono più caricabili da Looc.up o in SMEDEV più datati. Il sistema è comunque in grado di mostrare i setup salvati per la sezione in precedenza.

## Nuova gestione attiva : 

- Qualsiasi SMEDEV V3R1 o superiore
-- Salvataggio :  Se è presente l'informazione di contesto viene utilizzata come chiave, altrimenti viene utilizzata la chiave relativa alla scheda e alla sezione.
-- Caricamento :  Se è presente l'informazione di contesto viene utilizzata come chiave, altrimenti viene utilizzata la chiave relativa alla scheda e alla sezione.
-- Note :  I setup salvati in presenza di contesto non sono più visibili da Looc.up o in SMEDEV più datati. Inoltre in presenza di contesto i setup salvati precedentemente all'attivazione della gestione nuova non sono più visibili.




