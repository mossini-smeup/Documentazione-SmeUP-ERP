# Connessioni Sme.Up
Una connessione è definita come l'insieme dei parametri necessari per l'avvio di Looc.Up :  comprende principalmente informazioni sul sistema a cui connettersi, l'utente da utilizzare, la password di autenticazione e l'ambiente operativo da selezionare. Oltre a queste informazioni, necessarie per stabilire un collegamento, ci sono tutta una serie di parametri aggiuntivi, di tipo facoltativo, che attivano particolari funzionalità o modalità di esecuzione del programma.

Storicamente l'unico modo per fornire a Looc.Up le informazioni necessarie al collegamento era quello di passarle a linea di comando in fase di chiamata al programma. Oppure non passare alcuna informazione e compilare ogni volta la finestra di connessione visualizzata alla partenza del programma.

 :  : PAR
Il gestore delle connessioni di Sme.Up ha lo scopo di superare i limiti di un tale sistema, fornendo all'utente un sistema grafico per la selezione, gestione e avvio delle connessioni.
L'idea di base è quella di replicare all'interno di Looc.Up un sistema simile a quello dell'Operation Navigator for iSeries di IBM.


![LOSMEG_014](http://localhost:3000/immagini/LOSMEG_02/LOSMEG_014.png)
 T(La gestione delle connessioni utilizza le seguenti aree : )
- Gruppi di connessioni condivise
- Gruppi di connessioni personali
- Connessioni disponibili nel gruppo selezionato
- Gestione gruppi e connessioni
- Comandi generali (avvio Looc.Up in modo classico, chiusura ecc ecc)

 T(Le connessioni vengono visualizzate secondo la seguente logica : )
- Ogni singola connessione è identificata da un oggetto che contiene tutte le informazioni necessarie alla creazione del collegamento
- Le connessioni possono essere raggruppate secondo una logica di aggregazione scelta a piacere dall'utente o dall'amministratore del sistema
- La finestra iniziale consente la visualizzazione, la selezione ed eventualmente la modifica delle connessioni.


## Avvio di Looc.Up
 T(L'avvio di Looc.Up può avvenire in due modalità diverse : )
- Attraverso il pulsante "Avvio Sme.up" dal riquadro "Generali" nel pannello a sinistra
- Attraverso un pulsante di una connessione configurata

Nel primo caso  Looc.Up si avvia mostrando la finestra di connessione.

Nel secondo caso Looc.Up viene attivato direttamente con i parametri definiti nella connessione configurata.
Se nella connessione non vengono inseriti tutti i dati necessari Looc.Up si avvia mostrando la finestra di connessioni.

![LOSMEG_009](http://localhost:3000/immagini/LOSMEG_02/LOSMEG_009.png)
Se non è specificato l'ambiente, viene mostrata una finestra di scelta ambiente.

## Gestione gruppi
Il riquadro "Gestione gruppi" presente nel pannello a sinistra permette di creare, modificare o eliminare un gruppo di connessioni.

![LOSMEG_015](http://localhost:3000/immagini/LOSMEG_02/LOSMEG_015.png)
## Gestione connessioni
Il riquadro "Gestione connessioni" presente nel pannello a sinistra permette di creare una nuova connessione, modificare o eliminare una connessione presente e verificarne la compatibilità con Looc.up.
Le stesse operazioni sono richiamabili premendo il tasto destro del mouse sull'icona di una singola connessione.

![LOSMEG_010](http://localhost:3000/immagini/LOSMEG_02/LOSMEG_010.png)
La finestra di creazione/modifica di una connessione consente di specificare i dati per eseguire un collegamento e una serie di parametri aggiuntivi.
Un parametro importante è il flag "Avvio automatico" che, se selezionato, permette di far eseguire direttamente la connessione di Looc.up automaticamente all'avvio di Sme.Up GO.

![LOSMEG_011](http://localhost:3000/immagini/LOSMEG_02/LOSMEG_011.png)
## Connessioni personali e condivise
Ci sono due tipologie di gruppi di connessioni : 
- personali :  gestibili in prima persona da ogni utente
- condivisi :  gestiti dall'amministratore di sistema per fare in modo che l'utente finale si ritrovi con un pannello di connessione già popolato con le connessioni a cui è autorizzato.

L'utilizzo delle connessioni condivise permette di semplificare e centralizzare in un solo punto la gestione delle connessioni per tutti gli utenti.
Per la loro gestione è sufficiente che l'amministratore si imposti come percorso personale la directory sul server su cui ha permessi di scrittura e non di sola lettura come tutti gli altri utenti.

### Dove vengono salvate le connessioni
I percorsi delle connessioni personali e condivise sono salvati nei file di configurazione di Sme.Up GO, gestibili in _Funzioni Avanzate -> Sistema --> Gestione Configurazione_

Il default per le connessioni personali è la cartella _%appdata%/SmeupGo/groups_
_7_Non deve essere impostato come percorso delle connessioni personali una sottocartella all'interno della cartella di installazione di Looc.Up :  aggiornamenti successivi potrebbero eliminare tali sottocartelle.

