## Costo Medio - Definizione
Il costo >MEDIO di un >ARTICOLO è la media ponderata del costo degli eventi, presenti sui >movimenti di magazzino, che concorrono alla sua
determinazione in quel periodo

Questo processo NON è effettivamente un calcolo di un costo ma : 
* Una selezione degli eventi con possibilità di determinare quale tipo e per quale oggetto scatenare il calcolo (exit >D0CO10_01x)
* Un sistema di generazione, di uno o più calcoli, rispetto ad un evento relativamente ad un oggetto (Passi> B£J/D0)
* La valorizzazione di ogni singolo evento per un suo costo totale, a valore e quantità (Calcolo base> D0CO01A)
* La sommatoria dei valori e quantità degli eventi, per determinare la media ponderata dell'articolo

## Costo Medio - Logiche di Calcolo
Con >Logiche di calcolo si intende evidenziare i metodi di applicazione del costo medio, al fine di comprenderne l'utilizzo ed il tipo di impostazione.
A completamento di queste informazioni si può verificare anche le impostazioni del modello in SmeUP. Le logiche di Calcolo dovrebbero permette all'installatore ed all'utente di comprendere qual'è il modello rispondente alle proprie esigenze.

Le ipotesi >Logiche sviluppate in questo calcolo si possono sintetizzare nei seguenti tipo di costo medio : 
- [Logiche di Calcolo](Sorgenti/MB/DOC/D0CCMC_14A)

## Costo Medio - Impostazioni
- [Impostazione Costo Medio Articolo](Sorgenti/MB/DOC_OGG/P_D0CO10A)

## Costo Medio - Controllo dei risultati
_7_Documentazione in fase di sviluppo

### Costo Medio - Errori
- [Analisi errori](Sorgenti/MB/DOC_OGG/P_D0CO03A)

### Costo Medio - Documentazione
- [Documentazione del calcolo costo](Sorgenti/MB/DOC_OGG/P_D0CO02A)




