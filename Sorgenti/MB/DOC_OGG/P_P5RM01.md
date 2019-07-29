# Creazione R. M. da Impegni P5
Questa funzione serve per la creazione delle R.M. da impegni che possono essere : 

- _2_interni, da ordini di produzione
- _2_esterni, da ordini di conto/lavoro (in questo caso viene richiesto il tipo ordine)


![GM_02_04](http://localhost:3000/immagini/MBDOC_OGG-P_P5RM01/GM_02_04.png)
Con il tipo di ordinamento si sceglie se creare una testata di richiesta di movimentazione per ogni estrazione, oppure per ogni ordine o di accodare le righe estratte ad un lista esistente (in questo caso viene richiesto il  numero documento).
Se selezionata l'assegnazione il sistema, in coda alla creazione della lista, ne lancerà direttamente l'assegnazione (cfr. paragrafo Azioni su Richieste Movimentazione)
Attraverso le parzializzazioni si possono filtrare gli oggetti da cui estrarre le righe della lista da creare. Le parzializzazioni sono contestuali al tipo di estrazione richiesta (filtro su ordini di produzione o su righe documenti esterni).

_3_NOTA :  attraverso le tabelle P55 e V55 si definisce quale tipo di Richiesta Movimentazione sarà generata in base
al documento di partenza.
