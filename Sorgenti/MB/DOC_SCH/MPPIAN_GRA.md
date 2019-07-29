# Rappresentazione grafica dati MPS
In questa scheda sono presenti le seguenti sottoschede : 
 * _2_Dati per "Oggetto 1" "Oggetto 2"
 * _2_Dati per periodo
 * _2_Riepilogo
 * _2_Analisi di un piano

## Dati per "Oggetto 1" "Oggetto 2"
La scheda presenta graficamente i valori contenuti nel piano / vista selezionati dalla scheda precedente.
Nella sezione in alto a sinistra è possibile selezionare uno tra i due possibili oggetti presenti nella vista / piano. Nella sezione in alto a destra sono mostrati gli oggetti 2 congruenti con l'oggetto 1 selezionato.

La sezione in basso è dedicata alla rappresentazione grafica, vengono presentati : 
 * i dati totali dell'oggetto 1 (se selezionato)
 * i dati totali dell'oggetto 2 (se selezionato)
 * i dati della coppia oggetto 1 / oggetto2

![MPPIAN_075](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_GRA/MPPIAN_075.png)
## Dati per Periodo
In questa scheda sono presenti i grafici riferiti ai singoli periodi.

Nella sezione in alto a sinistra è possibile selezionare il periodo tra quelli presenti nella vista / piano. Nella sezione in alto a destra sono mostrati gli oggetti visibili nel periodo selezionato.

La sezione in basso è dedicata alla rappresentazione grafica, vengono presentati : 
 * i dati totali, sommati per oggetto 1 nel periodo selezionato
 * i dati totali, sommati per oggetto 2 nel periodo selezionato
 * il dettaglio dei dati dell'oggetto 2 nel periodo selezionato
 * il dettaglio dei dati dell'oggetto 1 nel periodo selezionato

![MPPIAN_076](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_GRA/MPPIAN_076.png)
## Riepilogo
In questa scheda vengono presentate le matrici di riepilogo degli oggetti 1 e 2 selezionati tra quelli presenti nella vista / piano : 

![MPPIAN_077](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_GRA/MPPIAN_077.png)
La terza matrice presenta tutti i dati con possibilità di raggruppamento per oggetto 1 o oggetto 2.

![MPPIAN_078](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_GRA/MPPIAN_078.png)
## Analisi di un piano
La scheda mostra tutti i dati di un piano raggruppati e totalizzati per Oggetto.
All'apertura della scheda selezionare uno dei bottoni in basso che rappresentano gli oggetti presenti nel piano : 

![MPPIAN_079](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_GRA/MPPIAN_079.png)

# Help Tecnico
Input
-Parametri : 
 TPKY2 :    Tipo chiave2
 DECTKY1 :  Decodifica chiave2
 DECTKY2 :  Decodifica chiave1
 PIA :      Codice piano
 DECPIA :   Decodifica piano
 VIS :      Codice vista
 DECVIS :   Decodifica vista
 OGG :      K1      riferire i grafici alla chiave1 passata in oggetto1
          K2      riferire i grafici alla chiave2 passata in oggetto1
          *BLANKS non riferire i grafici ad un particolare oggetto in chiave
-Oggett1 :  tipo, parametro e codice dell'eventuale oggetto a cui riferire i grafici


