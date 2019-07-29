# Scopo
 * introdurre e gestire i rilievi analitici dei controlli e collaudi operati sui lotti
 * stampare la documentazione interna ed esterna (certificati di Qualità)
 * introdurre e gestire gli effettivi tempi e costi di controllo

# Definizioni
## Rilievi di Lotto
Sono i parametri sintetici (devianza, valore massimo rilevato, media, ...), specificati a fronte di una misura del ciclo di collaudo. La definizione dei parametri caratterizzanti della misura viene realizzata attraverso la tabella CQT. La gestione e memorizzazione, viene operata attraverso le funzioni di questo modulo. È importante sottolineare che i rilievi di Lotto, possono essere determinati in modo automatico, qualora vengano introdotte le singole misurazioni di campioni, attraverso un tasto funzionale (F08).

## Rilievi analitici (su campioni)
Rappresentano le singole misure eseguite sui campioni a fronte di valori di riferimento specificati sulla fase di collaudo. La definizione dei valori di riferimento della misura è realizzata attraverso la tabella CQT.

# Tabelle utilizzate dal modulo : 
Questo modulo non ha specifiche tabelle da attivare, ma utilizza la base dati costruita all' interno della definizione dei cicli di collaudo.

# Processo di avviamento ed utilizzo
Non esiste uno specifico processo di avviamento ed utilizzo, ma una integrazione delle funzioni di questo modulo nelle attività di Gestione Benestare di Collaudo dei Lotti.

# Menù funzioni Gestione Rilievi e Collaudi
![CQ_RICO_01](http://localhost:3000/immagini/CQRICO_01/CQ_RICO_01.png)
La funzione 1701 permette la gestione (inserimento/variazione/interrogazione) dei Rilievi di Lotto e delle misurazioni analitiche di campioni
La funzione 1702 permette attraverso una funzione semplificata, di gestire esiti delle singole fasi di collaudo ed il collegamento alla gestione dei rilievi di lotto e di misurazione.
Le funzioni 1703/1704  permettono di produrre liste di sintesi e dettaglio dei rilievi eseguiti.
La funzione 1705 permette di produrre i certificati di qualità sui lotti controllati.
