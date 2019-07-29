# Generalità
L'inventario fisico è un processo che si compone di diverse fasi : 

- pianificazione
- preparazione dell'inventario
- esecuzione della conta fisica
- confronto con giacenza teorica e calcolo differenze
- analisi delle differenze e lancio delle rettifiche di giacenza
- reporting e analisi dei risultati dell'inventario


![GMINVE_01](http://localhost:3000/immagini/GMINVE_INT/GMINVE_01.png)
## Descrizione del modulo
La gestione dell'inventario fisico di Sme.up permette di supportare tutte le attività di inventario fisico : 

- identificazione delle conte da eseguire, determinabile secondo varie modalità stabilite dall'utente, e produzione di liste o cartellini di conta
- inserimento delle quantità contate, confronto con la giacenza di riferimento e determinazione delle differenze
- generazione delle rettifiche inventariali
- statistiche inventariali

Per l'inventario fisico possono essere usati dei supporti : 

- _2_liste di conta, contengono i dati di dettaglio della giacenza da controllare, possono essere stampate con o senza le quantità teoricamente giacenti
- _2_cartellini di conta, generalmente sono cartellini prenumerati che possono essere divisi in lotti di conta che vengono distribuiti agli addetti. Per ogni materiale inventariato si scrivono su un cartellino i dati di giacenza (articolo, lotto, area, tipo giacenza, ubicazione, ...) e la quantità trovata. I cartellini possono essere acquistati o stampati vuoti oppure generati partendo dalle liste di conta.


# Archivi utilizzati
 :  : DEC T(OJ) P(*FILE) K(GMDAIN0F)
 :  : DEC T(OJ) P(*FILE) K(GMRIIN0F)

# Tabelle utilizzate
 :  : DEC T(ST) K(GMI)
 :  : DEC T(ST) K(GML)
