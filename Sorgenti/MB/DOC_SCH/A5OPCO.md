## Obiettivo
Obiettivo di questa scheda è analizzare i saldi di contabilità generale e i saldi cespiti civilistici evidenziando le differenze

![A5OPCO_01](http://localhost:3000/immagini/MBDOC_SCH-A5OPCO/A5OPCO_01.png)
## Parametri di lancio

* Periodo :  è l'esercizio per il quale si voglia controllare la quadratura
* Data Situazione :  è la data a cui effettuare il calcolo dei saldi. Se lasciata vuota viene considerato tutto l'esercizio
* Divisione :  permette di analizzare i cespiti di una specifica divisione

## Dettaglio informazioni

All'interno della matrice vengono visualizzati i conti utilizzati per la contabilizzazione dei cespiti.
Per ogni conto sono riportati : 
 * Saldo contabile :  è il saldo delle scritture civilistiche (quindi con pertinenza 2 e condizione 6)
 * Saldo cespiti :  è il saldo della linea identificata come linea civilistica all'interno della tabella A51
 * Differenza tra i due valori

La determinazione dei conti utilizzati per la contabilizzazione viene fatta con questa risalita : 
 * Vengono analizzati i parametri di collegamento categorie/conti
 * Se i parametri di collegamento categorie/conti non sono impostati viene analizzata la tabella A5A

Per maggiori dettagli sull'impostazione dei collegamenti Cespiti/Contabilità si veda il seguente : 

- [Impostazione Conti Collegamento](Sorgenti/MB/DOC/A5OPCO_03)

## Opzioni

Digitando la lente d'ingrandimento posta nella prima colonna è possibile visualizzare il dettaglio dei cespiti totalizzati nella colonna _Saldo Cespiti_





