Il componente **LaTeX/PDF** permette di generare un file PDF partendo da un membro di documentazione attiva. Lo scopo di questo documento è illustrare tutte le potenzialità del componente per la creazione di presentazioni e documenti di elevata qualità.

# Cosa è LaTeX?
E' un linguaggio di markup usato per la preparazione di testi basato sul programma di composizione tipografica **TEX**.
E' principalmente utilizzato in ambito scientifico / matematico.

# Perchè LaTeX?
Perchè LaTeX separa il contenuto dalla formattazione, e consente di ottenere documenti di elevata qualità.
Un documento LaTeX sarà costituito pertanto dal testo e da direttive che specificano la formattazione.
Le specifiche di formattazione sono raggruppate in classi e ne sono state sviluppate di vario tipo in funzione della destinazione.
Ci sono così classi per : 
 * realizzare libri
 * articoli, soprattutto scientifici
 * lettere
 * report
 * creare presentazioni (con Beamer si raggiunge una elevata qualità)

# Come lo usiamo in SmeUp
Con l'avvento di LoocUp grossa parte della documentazione è stata scritta impiegando una sintassi definita ad HOC, basata in parte su quella della documentazione attiva.
La sintassi della documentazione attiva è diversa da quella impiegata in LaTeX. Per non dover riscrivere tutti i documenti si è scelto pertanto la strada della estensione e conversione.
Estensione perchè la sintassi della documentazione attiva è stata arricchita di istruzioni appositamente pensate per produrre presentazioni (tag P).
Conversione perché tutta la documentazione scritta viene convertita in formato LaTeX in modo trasparente all'utente mediante un apposito servizio.

Questo approccio consente di


- riutilizzare quanto già scritto;
- standardizzare la produzione della documentazione;
- mantenere un repository comune su AS400.
- non obbliga l'utente ad imparare nuove sintassi


# Il componente LaTeX/PDF
La generazione del file PDF si applica in due diversi contesti : 

- la generazione delle presentazioni;
- la generazione della documentazione.


Nel caso delle presentazioni, la sintassi di ogni elemento inizia con il tag ** : **** : P.** (dove P specifica l'appartenenza dell'elemento al gruppo "presentazione").
Nel caso della documentazione, la sintassi è quella standard di Sme.up.
