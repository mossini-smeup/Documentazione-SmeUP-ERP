# Installazione Richieste di movimentazione
Per attivare le richieste di movimentazione è necessario : 
 * _2_definire il numeratore delle Richieste
 :  : DEC T(ST) K(CRNGM)
 * _2_caratterizzare il tipo di testata delle Richieste
 :  : DEC T(ST) K(GMO)
 * _2_caratterizzare il tipo di riga delle Richieste
 :  : DEC T(ST) K(GMZ)
 * _2_definire le causali di movimentazione utilizzate dalle Richieste, affinchè agiscano , a seconda dell'utilizzo, sia sulla quantità _7_ATTESA che sulla quantità _7_ALLOCATA
 :  : DEC T(ST) K(GMC)

Se si attiva il motore inferenziale
 * _2_definire il flusso del motore inferenziale
 :  : DEC T(ST) K(GMH)
 * _2_definire i passi di esecuzione del motore inferenziale
 :  : DEC T(ST) K(GMK)

## Tabelle generazione R.M.
Utilizzate per creare le R.M. da impegni ordine di produzione o da impegni documenti ciclo esterno : 
 :  : DEC T(ST) K(P55)
 :  : DEC T(ST) K(V55)

# Motore inferenziale
Il motore inferenziale serve per determinare, attraverso iterazioni successive di regole utente, l'ubicazione di versamento oppure l'ubicazione di prelievo

Il motore di basa su 2 tabelle principali : 
 * Tabella GMH (flussi di esecuzione del motore)
 * Sottosettori della tabella GMK (azioni del motore)
 :  : DEC T(ST) K(GMH)
 :  : DEC T(ST) K(GMK)

_4_NOTA BENE
Se il motore inferenziale viene usato per determinare l'ubicazione di versamento in genere questo viene associato alla generazione/assegnazione/esecuzione/cancellazione di una richiesta di movimentazione (GMRRIM) e non è difficile che questo venga collegato al trattamento di un collo (CZ).
In questi casi si usa il deviatore standard dei colli (progr. GMGMB0X) con funzione metodo : 
> GES / APR - per creare la RRIM
 GES / ASS - per assegnare la RRIM (usa l'azione collegata
.            e il motore inferenziale)
 GES / ESE - per eseguire la RRIM (lancia i movimenti e
.            cancella la RRIM se flag 4 = 1)


Se si usa il GMGMB0X per creare la RRIM deve esistere oltre al tipo riga RRIM
 :  : DEC T(ST) K(GMZ)
anche il tipo testata TRIM
 :  : DEC T(ST) K(GMO)
