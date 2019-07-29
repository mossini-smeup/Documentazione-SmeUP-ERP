
# Obiettivo

Manutenere manualmente i record estratti e da includere nella comunicazione liquidazione iva
periodica.

# Parametri
 * Anno :  inserire l'anno a cui si riferiscono i dati da manutenere
 * Trimestre :  inserire il trimestre a cui si riferiscono i dati da manutenere
 * Liquidazione Gruppo :  settare il campo qualora si vogliano manutenere i dati relativi alla    liquidazione del gruppo
 * Sezione :  è possibile filtrare i quadri visualizzati nella successiva videata
* Campo filtro _ n _  :  nel caso in cui sia stata specificata una sezione è possibile effettuare tre filtri sui valori dei righi del quadro stesso. Ad esempio nel caso in cui si sia scelta la sezione VP, sarà possibile filtrare per mese/trimestre, ecc.

# Dettaglio
Confermando la videata di lancio verrà presentato il dettaglio dei record estratti per la
comunicazione liquidazione iva periodica.
All'interno della videata sarà possibile gestire i record estratti e inserirne di nuovi.
Entrando all'interno del dettaglio di un record i valori estratti dal programma avranno un colore diverso rispetto ai dati da inserire manualmente : 
Tra i campi di dettaglio è possibile visualizzare anche lo stato della trasmissione che potrà essere : 
 * _Da trasmettere_ se il record non è ancora stato trasmesso e non si tratta di un record da inserire in una dichiarazione integrativa
 * _TRA Trasmessa_ se il record è già stato trasmesso in definitivo
 * _DIN DA integrare_ :  questo valore verrà impostato a mano nel caso in cui il record vada trasmesso in una dichiarazione di tipo 'Integrativo'
 * _NNN da non trasmettere : _ questo valore verrà impostato a mano nel caso in cui il record non vada trasmesso.

Si sottolinea che i quadri estratti dal programma sono : 
 * Frontespizio :  1 record per comunicazione
 * Quadro VP  :  1 record se liquidazione trimestrale e 3 record (uno per mese) se liquidazione    mensile
