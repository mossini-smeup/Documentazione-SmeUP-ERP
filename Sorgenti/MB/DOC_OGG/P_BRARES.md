# Gestione Dati Ente/Articolo
## Generalità
Nella gestione dei rapporti commerciali con enti esterni quali fornitori o clienti capita molto spesso che per lo stesso articolo esistano delle diversità tra le informazioni di anagrafico proprie dell'azienda e quelle legate alla sua interazione con l'ente esterno (es. il codice materiale usato internamente all'azienda generalmente non è lo stesso codice che il fornitore assegna allo stesso articolo). In più è da considerare che le informazioni di un articolo variano da ente a ente (es. lo stesso articolo per un fornitore assume un numero di codice, per un altro ne assume uno diverso).
In Sme.up queste informazioni diverse e specifiche da ente a ente sono gestite nell'anagrafico ente / articoli.

## Tipi di enti
Un ente esterno è caratterizzato da un tipo ente che ne descrive la categoria. Avremo ad esempio fornitori, clienti, agenti, trasportatori, ecc.
Il tipo ente è definito nella tabella BRE (tipo contatto).
Un esempio dei vari tipi ente che potrebbero essere gestiti è il seguente : 

- AGE = Agente
- CLI = Cliente
- PRO = Produttore (Casa produttrice di un articlo di acquisto che puo venire fornito da un fornitore generico ma di cui si vuole tenere traccia del costruttore originale)
- FOR = Fornitore
- DES = Indirizzo di destinazione (usato per gestire diversi indirizzi da utilizzare nella creazione delle bolle di spedizione)


## Gestione dati ente / articolo
La gestione di questi dati è la stessa sia che si tratti di un fornitore che di un cliente. Le particolarità esistono legate alle caratteristiche aggiuntive che sono definite a livello di specifica implementazione Sme.up. Per comodità di esposizione presenteremo la gestione dei dati Fornitore / Articolo, perché è quella più completa, da questa sarà possibile estrapolare il parallelo con quella dei dati Cliente / Articolo.

Per attivare la gestione si parte dal seguente formato guida : 

![B£_11_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRARES/BX_11_01.png)
Utilizzando le opzioni si accede alla videata di dettaglio dove sono presentati tutti i campi propri : 

![B£_11_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRARES/BX_11_02.png)
### Descrizione dei campi

- _2_Articolo /  Fornitore, codice materiale e descrizione che vengono assegnati da fornitore all'articolo in questione. Questi dati possono essere usati nella stampa dell'ordine di acquisto in alternativa o in aggiunta al codice / descrizione interno aziendale.

- _2_Unità di misura di acquisto / Fattore di conversione, rappresenta l'unità di misura con cui il fornitore gestisce il materiale ed il fattore di conversione tra l'unità di misura interna e quella del fornitore (es. un fornitore di vernici può vendere a chilogrammi mentre internamente all'azienda la vernice può essere gestita a litri). Nel caso il fattore di conversione non sia compilato si assume il fattore di conversione standard inserito nella tabella delle unità di misura (tab. UMS).
- _2_Priorità di selezione, utile nel caso che lo stesso articolo possa essere fornito da più fornitori :  il programma di determinazione del fornitore preferenziale, usato ad esempio dall'MRP per suggerire il fornitore, suggerisce come fornitore preferenziale quello che ha il valore più alto in questo campo.


_3_F10 Completo
Con F10 si apre la possibilità di aprire il formato completo su cui è possibile gestire informazioni ulteriori da utilizzare per gestioni particolari : 

![B£_11_03](http://localhost:3000/immagini/MBDOC_OGG-P_BRARES/BX_11_03.png)
premendo di nuovo F10 si torna al formato ridotto.

_3_F15 Parametri aggiuntivi
Con questo tasto si apre la gestione dei parametri della categoria £P6.

![B£_11_04](http://localhost:3000/immagini/MBDOC_OGG-P_BRARES/BX_11_04.png)
In questa categoria, oltre ai parametri iniziali forniti nell'avviamento si possono aggiungere anche altri parametri specifici per ogni azienda.
