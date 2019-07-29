# Gestione dati Magazzino / Articolo
Con questa gestione si impostano dei parametri tipici della gestione di un articolo gestito in un plant, quali :   tecnica di gestione, ubicazione, tipo contenitore, parametri di pianificazione (scorta minima, lotto economico, punto di riordino, consumo medio).

Il formato di partenza è il seguente : 

![GMBASE_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMARMG/GMBASE_01.png)
La gestione di questa tipologia di parametri è prevista sia a livello di dettaglio (articolo / plant) che a livelli mano a mano più generici, ed è previsto un programma di risalita dai livelli di massimo dettaglio ai livelli più generici per recuperare le informazioni necessarie.

In questa implementazione sono stati definiti 4 possibili livelli che sono selezionabili sul formato guida : 

![GMBASE_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMARMG/GMBASE_02.png)
il formato di dettaglio è il seguente che come modalità di gestione è comune a tutti i livelli : 

![GMBASE_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMARMG/GMBASE_03.png)
i campi significativi sono : 

- _2_Tecnica di gestione, identifica come viene trattato l'articolo dal punto di vista dei prelievi da magazzino e dello scarico componenti al versamento. I valori possibili e le loro caratteristiche sono nella tabella GMT.
- _2_Ubicazione assunta, serve per attribuire una ubicazione fissa al versamento di un articolo.
- _2_Famiglia contenitori, quantità per contenitore, serve per attribuire un contenitore all'articolo.
- Gli altri campi sono di utilizzo intuitivo.

