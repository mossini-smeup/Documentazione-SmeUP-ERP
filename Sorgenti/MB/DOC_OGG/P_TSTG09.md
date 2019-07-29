# GESTIONE UNITA' DI MISURA
Questa funzione si propone di unificare tutti gli aspetti connessi alla gestione delle unità di misura.
Si veda anche la documentazione della tabella UMS.
# FUNZIONI / METODI
CO - Converte la quantità da u.m. origine a u.m. destinazione
IN - Presenta tutte le unità di misura coerenti con u.m. origine, ossia che hanno la stessa u.m. di riferimento
VE - Verifica se u.m. destinazione è coerente con u.m. origine, ossia se ha la stessa u.m. di riferimento :  se si,
restituisce la decodifica, altrimenti il comportamento dipende dal metodo : 
BT - segnala l'errore
IR - presenta la lista delle u.m. valide, e consente la scelta
# UNITÀ DI MISURA DI ORIGINE
E' obbligatoria per tutte le funzioni. Verificata in tab UMS.
# QUANTITÀ
E' il valore, espresso in u.m. origine, che deve essere convertito in u.m. destinazione.
# UNITÀ DI MISURA DI DESTINAZIONE
Funzione VE :  verifica che sia coerente con u.m. origine.
Funzione CO :  verifica che esista in tab UMS.
Se vuota, assume l'u.m. di origine.
# FATTORE DI CONVERSIONE
Deve essere immesso se le due u.m. non sono coerenti, altrimenti viene calcolato dalle tabelle e poi azzerato
all'uscita.
Se non viene immesso e le u.m. non sono coerenti, la funzione lo legge dalla tabella di correlazione tra le due u.m.
(= tab UMS che ha come codice 'u.m. origine + u.m. destinazione'), e se non lo trova segnala l'errore.
# DIVISORE/MOLTIPLICATORE
Indica se la quantità origine deve essere moltiplicata (se = '*') o divisa (se = '/') per il fattore di conversione.
Viene dedotto dalle tabelle.
Se le u.m. non sono coerenti, la funzione lo legge dalla tabella di correlazione tra le due u.m..
# METODO DI ARROTONDAMENTO
E' utilizzato dalla funzione di conversione solo se è stato impostato anche il fattore di arrotondamento.
Può assumere i valori : 
'-'    :  arrotondamento per difetto
'+'    :  arrotondamento per eccesso altro  :  arrotondamento standard (H)
# FATTORE DI ARROTONDAMENTO
Se non viene immesso, la funzione assume fattore e metodo della tab u.m. destinazione oppure, se è anch'esso zero,
legge fattore e metodo dalla tabella di correlazione tra le due u.m.
Se a questo punto il fattore è zero ma il metodo di arrotondamento non è vuoto, assume 1.
Normalmente il risultato della conversione viene arrotondato alla terza cifra decimale; impostando questo parametro è
possibile arrotondare il risultato nel modo voluto.
Esempi :  se il fattore è 1 si arrotonda all'intero; se è 0,01 si arrotonda al centesimo; se è 12 si arrotonda alla
dozzina.
