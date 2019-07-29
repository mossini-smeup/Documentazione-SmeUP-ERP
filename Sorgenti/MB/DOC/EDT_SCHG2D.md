# G.SUB.CHA :  Grafico

All'interno di una sezione è possibile definire la visualizzazione di un grafico che permetta
di dare una veste grafica ad un certo fenomeno.

# Dati

Supporta le funzioni dati relative alle matrici con prerequisito di gestire la definizione
delle colonne ASSE e SERIE.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.CHA

## Typ :  Tipo
Seleziona l'apparenza del grafico. I valori possibili sono HBAR/VBAR/LINE/PIE/POINT rispettivamente per grafico a Barre Orizzontali, a Barre Verticali, a Linee, a Torta e a Punti. Il valore di default è VBAR.
## Inv :  Inverti serie colonne
Inverte le righe con le colonne in modo da visualizzare il trasposto del grafico di origine. I valori possibili sono Yes/No. Il valore di default è No.
## Leg :  Visualizza legenda
Visualizza la legenda associata alle serie del grafico. I valori possibili sono Yes/No. Il valore di default è No.
## Asp :  Aspetto
Specifica se l'aspetto del grafico è piatto o tridimensionale. I valori possibili sono 2D/3D. Il valore di default è 2D.
## Cmd :  Mostra comandi
Visualizza la barra dei pulsanti associata al grafico. I valori possibili sono Yes/No. Il valore di default è No.
## Dta :  Mostra dati
Visualizza i dati del grafico in una tabella a lato del grafico. I valori possibili sono Yes/No. Il valore di default è No.
## Ser :  Mostra serie
Visualizza un pannello con le serie associate al grafico. I valori possibili sono Yes/No. Il valore di default è No.
## Axe :  Imposta come asse
In questo attributo è possibile specificare il nome (del campo, non la descrizione) di una colonna della matrice dei dati che verrà usata come asse.
## Series :  Imposta le Serie Fld1|Fld2
In questo attributo è possibile specificare i nomi (dei campi, non le descrizioni) delle colonne della matrice dei dati da usare come serie divise da un carattere "|".
## Stack :  Stack della serie
Imposta come le serie devono essere visualizzate nei grafici a barre. I valori possibili sono NONE/SIDE/STACKED/STACKED100/SIDEALL. Il valore di default è SIDE.
## FitAll :  Visualizza tutto in sola pagina
Visualizza tutte le serie del grafico in una sola pagina riscalando le dimensioni di assi e serie. I valori possibili sono Yes/No. Il valore di default è Yes.
## PointsPerPage :  Numero punti per pagina
Definisce il numero di valori di una serie da mostrare in una singola pagina se è disabilitato l'attributo FitAll. I valori possibili sono numeri interi. Il valore di default è 0.
