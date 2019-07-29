## GM_RS     -  RISALITA SCORTA MINIMA
Nell'archivio DATI ARTICOLO/MAGAZZINO, si inserisce il valore della scorta minima. E' possibile inoltre impostare, nello stesso archivio, un criterio calcolo scorta/lotti, la cui presenza fa sì che si attivi una funzione di calcolo della scorta minima. Il presente V2 definisce la priorità e la risalita nel calcolo della scorta minima.
Si ricorda che la risalita viene eseguita in modo totale :  si arresta al record di maggior dettaglio inserito, indipentemente dal fatto che contenga valori significativi (non a zero).
Ad esempio, se si impostano i dati a livello di famiglia articolo, e per essa si inserisce sia la scorta sia il criterio di calcolo, si può presentare la necessità di inserire un'eccezione a livello di articolo.
In questo caso si devono inserire, a livello di articolo, sia il valore della scorta sia sia il criterio di calcolo. Inserendo solo il valore della scorta si ha l'effetto che, per questo articolo, non verrà utilizzato il criterio di calcolo (anche se presente a livello superiore).

## Valori possibili
 * **' ' Scorta inserita con risalita a scorta calcolata**; se presente viene ritornata la scorta inserita. Se a zero, e se presente il criterio, viene ritornata la scorta calcolata
 * **'A' Scorta calcolata con risalita a scorta inserita**; se presente il criterio di calcolo, viene ritornata la scorta calcolata. Se assente il criterio o scorta calcolata pari a zero, viene ritornata la scorta inserita
 * **'B' Solo scorta inserita**; viene ritornata la scorta inserita
 * **'C' Solo scorta calcolata**; se presente il criterio, viene ritornata la scorta calcolata. Se assente il criterio, viene ritornato zero
 * **'D' Solo scorta calcolata se presente criterio**; se presente il criterio, viene ritornata la scorta calcolata. Se assente il criterio, viene ritornata la scorta inserita; si differenzia dal caso 'A' in quanto, se presente il criterio e scorta calcolata a zero, ritorna zero (mentre nel caso 'A' verrebbe ritornata la scorta inserita); si differenzia inotre dal caso 'C' in quanto, se assente il criterio e scorta calcolata a zero, ritorna la scorta inserita (mentre nel caso 'C' verrebbe ritornato zero).
