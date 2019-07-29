#  Generalità
L'obiettivo principale di questo modulo è quello di fornire situazioni valorizzate, di fine esercizio, della giacenza di magazzino (sintesi valorizzate). Una tipica applicazione è la "Giacenza Fiscale di Fine Anno".

In Sme.up sono possibili due metodi per ottenere queste sintesi : 

- Attraverso chiusure periodiche dei magazzini (tipicamente chiusure di fine mese).
- Attraverso la ricostruzione della giacenza alla data di fine esercizio partendo da una situazione di giacenza. A sua volta questo secondo metodo può usare come situazione di partenza la giacenza attuale oppure una foto della giacenza costruita alla data di chiusura.

Nel modulo sono fornite tutte le funzioni per : 

- creare le sintesi di magazzino
- valorizzare le sintesi memorizzate (utilizzando diversi tipi costi e con diverse modalità di valorizzazione)
- stampare le sintesi valorizzate (le stampe possono essere anche usate ai fini fiscali)
- aggiornare i costi nell'archivio dei costi
- stampare i movimenti di carico / scarico magazzino nel periodo
- gestire manualmente i valori e le quantità memorizzati nelle sintesi di magazzino

Con questo modulo si possono anche gestire delle simulazioni (es. utilizzando diversi tipi costo), ogni simulazione può essere memorizzata separatamente a fronte di uno specifico scenario.

Sono fornite anche funzioni di massa per la gestione degli scenari (modifica, copia, cancellazione).

_2_Nota con questo modulo è anche possibile ottenere la valorizzazione di giacenze di articoli dettagliata per configurazione o per uno qualsiasi degli altri oggetti applicativi di Sme.up con cui si può caratterizzare una giacenza (UB = Ubicazione, LO = Lotto, D8 = Data registrazione, MT = Matricola, OP/OO/FA = Fase di cliclo di lavoro, CM = Commessa, EM =  Esponente di modifica, CF = Configurazione, CL/FO/CN = Ente, CC = Centro di costo, TA_UMS = Unità di misura esterna).

La valorizzazione per oggetto di riferimento pretende che nella tabella di personalizzazione della gestione materiali (GM1) sia attivata la funzione degli scenari in valorizzazione fiscale e che nella tabella degli scenari (GM3) sia attivata la gestione per oggetto di riferimento.

# Sintesi da chiusura periodica di magazzino
Ogni movimento di carico e scarico del magazzino, se ha valenza fiscale, viene classificato secondo la sua tipologia (es. i movimenti di traferimento tra una ubicazione e l'altra non hanno valenza fiscale in quanto non modificano il saldo di magazzino, la tipologia di carico / scarico può essere :  versamento di acquisto, prelievo di produzione, rettifica inventariale, ecc.....).

Ad ogni chiusura di magazzino (es. chiusura mensile) tutti i movimenti effettuati successivi alla chiusura precedente vengono rilevati classificati e sommarizzati algebricamente nell'archivio degli indici storici.

Dopo l'analisi e la validazione degli indici storici un programma specifico costruisce la sintesi di magazzino relativa al nuovo esercizio, sommarizzando i dati raccolti nell'archivio indici storici nei periodi appartenenti all'esercizio in corso (cioè relativi alle chiusure periodiche successive all'ultimo esercizio chiuso).

![GM_FISC_01](http://localhost:3000/immagini/MBDOC_OPE-GMFISC01/GM_FISC_01.png)
# Sintesi da giacenza
Possiamo costruire delle sintesi_2_da giacenza corrente, la funzione costruisce la sintesi del nuovo periodo partendo dalla giacenza attuale ed elaborando a ritroso tutti i movimenti di magazzino relativi alle aree di giacenza con rilevanza fiscale fino alla data di fine esercizio. Se alla fine dell'esercizio la giacenza risulta superiore all'esercizio precedente la differenza viene riportata come carico del periodo, altrimenti viene riportata come scarico.

![GM_V001_02](http://localhost:3000/immagini/MBDOC_OPE-GMFISC01/GM_V001_02.png)