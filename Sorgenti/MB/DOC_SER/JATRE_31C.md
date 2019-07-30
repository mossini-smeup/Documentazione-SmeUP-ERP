# OBIETTIVO
Questo servizio implementa le funzionalità necessarie ad operare con i barratori di SME.up.
I barratori forniscono un modo di accedere ai dati di un determinato file secondo i suoi logici
 (NB :  non tutti, per ora!) :  si fissano le prime chiavi di un logico e si possono vedere i record che
 scelta di chiavi, secondo l'ordinamento imposto dal logico.


# FUNZIONI/METODI (DA RISTRUTTURARE)
## *BLANKS
È l'unica funzione prevista dal servizio, restituisce risultati diversi a seconda dei parametri passati
del componente scelto.
Nel primo oggetto va passato il nome del programma barratore (es. V5TDOC_B, BRARTI_B, ...) oppure un
 oggetto senza chiave oppure un elemento di TAB§O (negli ultimi due casi il barratore viene ricavato
Nel secondo oggetto si indica il numero di logico da usare (0L, 1L)
Nei parametri si indicano le chiavi del logico da utilizzare.

Se il componente scelto è TRE viene restituito un albero con le scelte possibili per la prima chiave
analizzando i record del file che soddisfano le altre chiavi imposte.
Se il componente scelto è EXB viene restituita una matrice (le colonne sono cablate nel barratore) con i
record del file che soddisfano le chiavi imposte.

