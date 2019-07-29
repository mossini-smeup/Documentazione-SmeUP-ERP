## Obiettivo
TO DO
## Struttura
TO DO
## Statistiche
### Previsioni con metodo Holt Winter
Si eseguono i seguenti passi : 

- Si assume il verticale come esercizio (di norma anno) e l'orizzontale come periodo (di norma mese)
- Si determinano gli esercizi sensati nel modo seguente : 
-- Si individuano gli estremi (primo e ultimo valido)
-- Se si scostano dalla media degli altri periodi per oltre il 50% si escludono
-- Considerati i periodi validi rimanenti si determina la fine da considerare
-- In funzione del numero di periodi per esercizio di calcolano gli esercizi validi
-- Si determina l'inizio retrocedendo dall'ultimo periodo per gli esercizi validi
- La serie (che sarà un multiplo del numero di periodi) viene passata alla funzione di calcolo
- Si emette la serie di origine, il risultato (e la defferenza)
- Si emette il nuovo esercizio calcolato (si assume origine=calcolato per non emettere delta)


L'analisi grafica consente di verificare la bontà del calcolo

### Funzione di set'play (se autorizzate)
Emettiamo i valori per

- la determinazione degli esercizi come sopra esposto (con tutti i numeri del calcolo)
- la serie passata
- tutti i numeri ricevuti dalla COPY £G56

