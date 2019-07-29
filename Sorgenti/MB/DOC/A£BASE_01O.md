## Valori possibili
In base alla tipologia di "lavoro Sme.up" (emulazione Looc.up, schede, emulazione 5250, ecc...) in cui un programma viene eseguito, alcuni campi assumono un valore particolare.
I campi in questione sono il £INZJT e il £G61JT (dopo aver richiamato la £G61 sia con funzione BAS che JOB) e i valori che possono assumere sono : 

| _1_Lavoro | _1_£INZJT | _1_£G61JT |
| ---|----|----|
| LO_Sxxx | L | B |
| LO_Exxx | B | B |
| LO_Txxx | B | B |
| batch lanciato da interattvo | B | B |
| batch lanciato da emulazione loocup | B | B |
| 


## Metodo di determinazione £INZJT : 
Viene eseguita la £G61 sul lavoro corrente (funzione BAS), se il lavoro risulta essere batch (ossia se £G61JT='B') viene eseguita la £G61 sul lavoro che l'ha sottomesso (quindi £G61 con funzione JOB); se il subtype risulta essere P(o D?) o J allora è considerato un lavoro di loocup; a questo punto viene fatta la £CRI su JAJAS0. Se il risultato è positivo allora £INZJT='L'.

## Nota sul £G61JT
La £G61 non fa tutto il "giro" del £INZJT; inoltre sulla funzione JOB (dati di un lavoro specifico) non sarebbe nemmeno in grado di farlo, perché bisognerebbe fare la £CRI non sul lavoro corrente (da cui viene eseguita la £G61) ma su un altro.

## Problemi derivati
 * Non ho modo di sapere se un lavoro batch è stato lanciato da un 5250 interattivo o da una emulazione loocup. In questo modo non siamo in grado (ad esempio) di reindirizzare i messaggi di completamento lavoro verso loocup piuttosto che la console.
 * Dal punto di vista del £INZJT, LO_Exxx e LO_Txxx non vengono riconosciuti come lavori loocup.
 * La G61 non distingue un lavoro batch da un lavoro loocup.

## Possibili soluzioni (sviluppi futuri)
Si potrebbero introdurre due nuovi campi simili (oppure modificare i valori assunti dai campi in questione) : 

| _1_Lavoro | _1_$INZJT | _1_$G61JT |
| ---|----|----|
| LO_Sxxx | L | _1_L |
| LO_Exxx | _2_L | _1_L |
| LO_Txxx | _3_L | _1_L |
| batch lanciato da interattvo | B | B |
| batch lanciato da emulazione loocup |__C__ |__C__ |
| 

Volendo, si potrebbero distinguere le "prime tre L", facendo assumere al campo valori diversi.
Ho indicato i campi con $ iniziale (e non £), perché forse la soluzione migliore è non modificare il valore assunto dai campi esistenti, ma crearne due nuovi. Questo è da valutare.
In questo modo si avrebbe sempre sotto controllo il lavoro in analisi.
La modifica _2_blu è semplicissima :  basta fare la CRI anche sul JAJAS1 invece che solo sul JAJAS0.
La modifica _3_verde non lo è altrettanto, perché i lavori LO_T vengono lanciati dal lavoro LO_E (che non credo abbia subtype J o P).
Le modifiche _1_rosse, sono particolarmente complesse (nel caso di funzione JOB) perché avrei bisogno di fare la CRI su un altro lavoro.
Le modifiche __sottolineate__ sono banali una volta fatte le altre, infatti mi basta eseguire la G61 sul lavoro che ha effettuato la sottomissione.

### Proposta di modifica del metodo di determinazione del tipo
Le modifiche da fare mi sembrano particolarmente complesse, quindi perché non  cambiare il modo di determinazione del tipo lavoro?
Ad esempio potremmo dire che tutti i lavori batch il cui nome inizia con LO_ e che sono stati immessi nella coda lavori specificata nella tab. UI1, sono lavori loocup. A questo punto non avremmo più il problema della £CRI su altri lavori.
Ci leghiamo in questo caso al nome lavoro invece che al nome del pgm lanciato alla sottomissione del lavoro

### Vantaggi di questo metodo
La determinazione del tipo lavoro nel caso di LO_S, LO_E e LO_T diventa banale (sia per il £INZJT che il £G61JT). Di conseguenza diventa banale anche per gli altri casi.
