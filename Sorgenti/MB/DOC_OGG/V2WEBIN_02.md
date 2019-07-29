## Obiettivo
Permettere di identificare la posizione geografica su una mappa di uno o più indirizzi.
Abilitare la possibilità di associare alla posizione alcune caratteristiche come colore, forma, nota al fine di meglio rappresentare il dato

## Esempi applicativi
- Dove si trovano i clienti di un agente
- Dove è andata una persona nell'ultimo mese
- Dove abitano le persone che lavorano per l'azienda evidenziando con colori diversi i dipendenti dai collaboratori esterni
- Dove sono le persone della mia azienda oggi a lavorare
- Da dove mi sono arrivati gli ordini di ieri
- Dove sono le banche con cui lavoriamo
- Distribuzione per fatturato dei miei clienti nella provincia di Milano (come evidenziare almeno A/B/C usando colore e lettera)
- Dove devo consegnare i materiali collegati a questo viaggio

### Idea di generalizzazione

1.   Definisco un Costruttore (Diciamo A28 ad esempio)

2.   Definirei un modello (Diciamo SE;SUB_A28;xxxxxxxxxxxx)
Nel modello ci sono tutte le condizioni di setup e di trattamento della fonte

3.   Definisco una fonte mediante Tipo e parametri del tipo. Ad esempio
3.1   Tipo=SQL Parametro=Strinag SQL che ha fisso come risultato un oggetto (quindi Tipo+parametro, Codice)
3.2   Tipo=LIS Parametro = identificazione della lista
3.3   Tipo=FUN Parametro= Funzione

4.   Cablo l'associazione dell'indirizzo dato un oggetto

5.   Gestisco due forma di output
5.1   Matrice (di setup e/o di dati)
5.2   URL risultante
