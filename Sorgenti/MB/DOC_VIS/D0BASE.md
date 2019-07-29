# Visione Costi Avanzati Base
## Panoramica costi avanzati base
Questa applicazione calcola il costo articolo in diversi modi : 
* Costo standard di massa
* Costo standard interattivo
* Costo consuntivo (per lotto)

## Composizione del costo di un articolo
Con questo modulo viene superata la visione classica che scomponeva il costo secondo elementi predefiniti, in favore di una struttura più flessibile dove la scomposizione viene studiata in funzione delle esigenze specifiche del cliente.
Così potremo ad esempio vedere il costo di un articolo scomposto in quote quali : 
* acciaio
* lavorazione
* energia elettrica
* ......

La composizione di questi elementi viene guidata dalla customizzazione, possiamo arrivare ad avere fino a 99 elementi del costo.

## Calcolo costo standard
Essenziamente è un calcolo che valorizza un articolo attraverso la valorizzazione del suo ciclo e della sua distinta. Fatto salvo che in customizzazione possiamo definire a piacere la struttura del costo di un articolo in funzione delle esigenze di controllo aziendali, con Sme.UP forniamo la seguente struttura di esempio : 
![D0BASE_00](http://localhost:3000/immagini/MBDOC_VIS-D0BASE/D0BASE_00.png)
### Impostazioni del calcolo
* tipo costo / tema dove memorizzare il costo articolo
* tipo costo / tema dove memorizzare il costo alla fase
* tipo costo per lettura aliquote orarie
* tipo costo per lettura lavorazioni esterne
* tipo costo per lettura acquisto
* metodo di memorizzazione costi (solo senza errori, tutti, nessuno)
* filtro articoli da estrarre (parzializzazioni interne / esterne

### Flessibilità
Durante il calcolo vengono di volta in volta chiamati programmi specializzati per un tipo di azione : 
* tipo di calcolo
* dettaglio oggetti di calcolo
* calcolo ricariche
* caratteristiche articolo
* calcolo ciclo
* calcolo distinta
* aggiustamento finale
* controllo errori
* stampa
* aggiustamento schiere
ciascuno di questi programmi permette l'adozione di exit per il condizionamento.
