# Obiettivo
La funzione raggruppa tutti i programmi che permetto di interrogare o impostare i parametri logistici utilizzati nella produzione : 
 * parametri di produzione (Tipo ordine, Contenitore assunto / Qtà per contenitore, Lotto, Scorta minima, ecc..)
 * parametri di prelievo, utilizzati per lo scarico materiali alla fase, (Causale di scarico, Ubicazione, Causale di scarto, Causale di recupero)
 * parametri di alimentazione, che regolano il ripristino delle giacenze bordo macchina (Livello scorta, Qtà riordino, Modalità di ripristino)
 * parametri di versamento (Causale, Ubicazione, Causale versamento a scarto)
 * ciclo logistico, interrogazione congiunta del ciclo di produzione e dei materiali alla fase

I parametri possono essere impostati al dettaglio massimo oppure si possono utilizzare dei sistemi di risalita attraverso i quali i parametri possono essere impostati a livello di sintesi o di massima generalità, il programma andrà a ricercare prima il massimo dettaglio risalendo poi al primo o al secondo livello di generalizzazione in caso il dato sia mancante.

# Formato di richiesta
![P5SI01_01](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_01.png)
Attraverso la scelta si determina su quale tipologia di parametri logistici agire.

Se il campo "Valori assunti" è diverso da blank il sistema visualizza i valori assunti (a livello di dettaglio o ad un livello di risalita in funzione delle condizioni associate).

Se il campo "Livello risalita" è impostato con 1 o 2 il sistema apre la manutenzione del corrispondente livello, se questo campo è blank ed è blank anche il campo Valori assunti il sistema lancia la manutenzione dei parametri al livello di dettaglio.

Valori assunti e Livello di risalita sono in alternativa.

## Scelta 1 - Parametri ordine
Questi parametri sono gestiti con le seguenti categorie parametri : 
 * _2_£P3, parametri a livello magazzino (plant) / articolo
 * _2_1P3, parametri a livello magazzino (plant) / tipo articolo (Tabella BRA)
 * _2_2P3, parametri a livello magazzino (plant) / valore generico (_3_Nota bene :  il valore generico deve essere = "**")

### Interrogazione valori assunti
![P5SI01_02](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_02.png)
### Gestione parametri a livello 2
![P5SI01_03](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_03.png)
## Scelta 2 - Parametri di prelievo
Questi parametri sono gestiti con le seguenti categorie parametri : 
 * _2_£P1, parametri a livello risorsa / articolo
 * _2_1P1, parametri a livello tipo ordine di produzione (Tabella P5T) / tipo articolo (Tabella BRA)
 * _2_2P1, parametri a livello valore generico  / valore generico (_3_Nota bene :  il valore generico deve essere = "**")

### Interrogazione valori assunti
![P5SI01_04](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_04.png)
### Gestione parametri a livello 2
![P5SI01_05](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_05.png)
## Scelta 3 - Parametri di alimentazione
Questi parametri sono gestiti con la categoria parametri _2_£P4, parametri a livello ubicazione / articolo, e non prevede livelli di risalita

### Gestione parametri a livello di dettaglio
![P5SI01_06](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_06.png)
## Scelta 4 - Parametri di versamento
Questi parametri sono gestiti con le seguenti categorie parametri : 
 * _2_£P2, parametri a livello tipo ordine di produzione (Tabella P5T) / articolo
 * _2_1P2, parametri a livello tipo ordine di produzione (Tabella P5T) / tipo articolo (Tabella BRA)
 * _2_2P2, parametri a livello valore generico  / valore generico (_3_Nota bene :  il valore generico deve essere = "**")

### Interrogazione valori assunti
![P5SI01_07](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_07.png)
### Gestione parametri a livello 2
![P5SI01_08](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_08.png)
## Scelta 5 - Ciclo logistico
Selezionando : 
 * _2_Fasi non logistiche, vengono visualizzate anche le fasi non logistiche (se il campo è blank sono visualizzate solo le fasi con il flag di stato logistico impostato)
 * _2_Materiali, mostra i materiali previsti alle fasi di cui sopra

![P5SI01_09](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI01/P5SI01_09.png)