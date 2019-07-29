# G.SEZ Sezione
Le sezioni sono il punto di partenza nella composizione delle schede, esse infatti definiscono
le finestre di cui la scheda è composta.

# Parametri
 * uno
 * due

Questa specifica si parametrizza nel seguente modo : 

## Pos :  Posizione
E' un parametro obbligatorio che definisce la posizione in cui la finestra verrà visualizzata.
La codifica del suo valore segue una struttura ben specifica :  essa può essere infatti costitutita
da una serie di uno o più caratteri alfanumerici :  i caratteri alfabetici determinano l'ordine
della suddivisione verticale della scheda, mentre i caratteri numerici definiscono l'ordine della
suddivisione orizzontale.

Obbligatorio = SI
Default = Nullo

## Dim :  Dimensione
La dimensione di una sezione è automaticamente adattata al numero di sezioni presenti nella
scheda (es. se metto due sezioni ognuna delle sezioni occuperà il 50% della scheda). Tramite
questo parametro è possibile forzare la % di copertura della sezione. Il valore da immettere
deve essere un numero di due cifre seguito dalla segno %.

Obbligatorio = NO
Default = Nullo

## Aut :  Autorizzazione
Tramite questo parametro è possibile indicare un livello di autorizzazione necessario ad un utente
per poter visualizzare la sezione.

Obbligatorio = NO
Default = Nullo

## Rem :  Commento
Tramite questo parametro è possibile indicare un breve commento riguardante la sezione.

Obbligatorio = NO
Default = Nullo
