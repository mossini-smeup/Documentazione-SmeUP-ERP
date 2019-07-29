# Assegnazione suggerimento a fornitori
I suggerimenti di acquisto o conto/lavoro vengono assegnati dall'MRP a uno o più enti in funzione delle impostazioni presenti nella politica di riordino (tabella M5A) ed in particolare i campi : 

- T$M5AM    Modo assegnazione ente
- T$M5AN    Parametro assegnazione ente

Il modo di assegnazione ente diventa il metodo utilizzato dalla copy £V5U con funzione = "ASS".
Attualmente i metodi previsto dalla copy, per la funzione ASS  sono : 

- _2_CON = Contratto, il parametro di assegnazione in questo caso è il _3_tipo documento del contratto.
- _2_PRE = Ente preferenziale, , il parametro di assegnazione in questo caso è il _3_tipo ente.


La quarta posizione del "Parametro assegnazione ente", se compilata,  identifica un programma specifico di assegnazione enti che si deve chiamare V5V5U0_x, dove x è il carattere qui impostato, il programma rappresenta una exit che influenza le regole di assegnazione. Ci saranno exit appartenenti alla famiglia di assegnazione per contratto ed altre appartenenti alla famiglia di assegnazione per ente preferenziale da utilizzare in coerenza con il campo modo di assegnazione ente.
A standard sono formite 2 exit : 

- _2_V5V5U0_1 = Assegnazione da contratto;
- _2_V5V5U0_2 = Assegnazione da ente preferenziale.

Le posizioni successive del campo "Parametro assegnazione ente" possono contenere ulteriori valori di condizionamento che possono essere richiesti dai programmi di exit.

## Assegnazione da contratto
Il programma ricerca le righe valide (livello e data di validità), i campi Data consegna richiesta e Data cons. confermata del V5RDOC sono da intendersi come data inizio e fine validità, se la data è bianca si intende valido da sempre (data inizio) o per sempre (data fine).

In questo programma la quinta posizione del "Parametro assegnazione ente" rappresenta la _3_Strategia di assegnazione e il sesto viene utilizzato come filtro sul Flag 10 della riga (blank = Acquisto, 1 = Conto lavoro).

Sono previste le seguenti strategie di assegnazione : 

### Strategia ' ' - Rispetto completo della quantità residua
La quantità da assegnare viene attribuita ai vari contratti in funzione della qtà residua presente, se la qtà da assegnare è superiore alla qtà residua del contratto si assegna la qtà residua e si passa al contratto successivo con la qtà rimanente.

### Strategia '1' - Rispetto delle quantità residue arrotondate al lotto
Come la precedente con la differenza che la qtà attribuita è arrotondata secondo la lottizzazione eventualmente maggiorando la qtà proposta rispetto a quella residua del contratto

### Strategia '2' - Contratto senza limite di quantità
La quantità (arrotondata al lotto superiore) viene assegnata totalmente al primo contratto valido.

_2_Per una spegazione più dettagliata riferirsi alla documentazione tecnica del programma V5V5U0_1.

## Assegnazione da ente preferenziale
Questa regola di assegnazione cerca nei dati _3_Ente/Articolo il fornitore che ha "Codice priorità" maggiore.
A parità di codice di priorità : 

- se non ci sono exit viene scelto il fornitore con codice minore
- se è presente l'exit 2 (programma V5V5U0_2) ed esistono più fornitori viene eseguita la distribuzione in funzione della "% copertura fabbisogno" attribuita a ciascun fornitore tenendo conto delle regole di lottizzazione. _2_Per una spegazione più dettagliata riferirsi alla documentazione tecnica del programma V5V5U0_2.


### Lottizzazione
L'assegnazione per ente preferenziale è in grado di leggere i parametri di pianificazione differenziati per ente, qualora si stata attivata questa modalità.
Per attivarla si deve : 

- impostare in tabella M51 _3_Tipo e parametro di pianificazione per riferimento (tipo = E, Parametro = tipo ente)
- nella politica (tab. M5A) da abilitare alla lottizzazione differenziata ativare (porr = 1) il campo _3_Parametri di pianificazione per riferimento


## Riferimenti di documentazione
- [&-x2a; M5A - Politica di riordino                 (1)](Sorgenti/MB/DOC_OGG/TA_M5A)
 :  : DEC T(MB) P(QILEGEN) K(£V5U)
- [BRARES0F Dati articolo per esterno](Sorgenti/MB/DOC_OGG/F_BRARES0F)
 :  : DEC T(MB) P(QILEGEN) K(£G26)
- [M51 - Pianificazione materiali](Sorgenti/MB/DOC_OGG/TA_M51)
