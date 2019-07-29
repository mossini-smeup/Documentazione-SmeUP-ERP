# Come usare un messaggio di tipo informativo
- UIMessageInfo vMsg = new UIMessageInfo (40, "Sorgente", "Descrizione breve", "Descrizione ampia");
- vMsg.showMessage(null);
- UIMessageController.getMsgManager().addMessage(vMsg); 
 F(02)
- Creo il messaggio chiamando il costruttore al quale passo i parametri adeguati 
- Mostro a video il messaggio tramite un JOptionPane 
- Aggiungo il messaggio al gestore dei messaggi 

# Classi principali del componente messaggi : 
## UIMessageController
dal quale parte l'analisi dell'xml di Loocup alla ricerca di messaggi.
Il metodo _3_ findMessage()  analizza l'xml e ne ricava le informazioni relative ai messaggi da
visualizzare (nessuno, uno o più messaggi per ogni xml). I messaggi vengono _2_ SEMPRE aggiunti  al gestore dei messaggi e visualizzati in un JOptionPane _2_ SOLO SE HANNO PRIORITA' >= 30. 

### Devo modificare questa classe se
- voglio modificare la _7_ soglia di priorità per la visualizzazione 
- voglio modificare ciò che è relativo al fatto che un msg con _7_ livello=99 sia bloccante 
- voglio modificare l'analisi dell'xml
- ho modificato/aggiunto/rimosso qualche attributo di un UIMessageObject (e derivati)


-------------------------------------------------------------------------------------


## UIMessageViewerPanel
che contiene le caratteristiche di visualizzazione del pannello riassuntivo con lo storico di tutti i messaggi archiviati.

### Devo modificare questa classe se
- voglio modificare il layout del visualizzatore di messaggi (es :  le caratteristiche della tabella che li contiene).


-------------------------------------------------------------------------------------



## UIMessageManager
che contiene/gestisce l'array di tutti i messaggi e avvia il visualizzatore con lo storico dei messaggi. Carica la console (contenitore della toolbar) e il pannello centrale (contenitore della tabella). Contiene i metodi add e remove per aggiungere o eliminare messaggi (singoli o a blocchi) dallo storico.

### Devo modificare questa classe se
- Voglio modificare la gestione logica dei messaggi (aggiunta/eliminazione/ricerca)


-------------------------------------------------------------------------------------



## UIMessageToolbar
che gestisce la barra ai piedi della tabella nel pannello di visualizzazione messaggi.
Contiene i bottoni per l'eliminazione dei messaggi e per il passaggio tra gli stati Visualizza tutti/Visualizza ultimi

### Devo modificare questa classe se
- Voglio modificare l'aspetto della barra


-------------------------------------------------------------------------------------



## UIMessageLabelRenderer
che gestisce il disegno(testo/sfondo/carattere..) di ogni singola cella che non appartenga alla colonna Livello (trattata diversamente dalle altre).

### Devo modificare questa classe se
- Voglio modificare la visualizzazione grafica (disegno) delle celle della tabella


-------------------------------------------------------------------------------------



## UIMessageTableLevelRenderer
che gestisce il disegno(testo/sfondo/carattere..) di ogni singola cella appartenente alla colonna Livello. Tale colonna è trattata diversamente dalle altrepoiché contiene un colore di sfondo diverso a seconda della gravità del livello di errore

### Devo modificare questa classe se
- Voglio modificare la visualizzazione grafica (disegno) delle celle della colonna Livello -es. voglio modificare i _7_ range  che stabiliscono la differenza di colore.


-------------------------------------------------------------------------------------



## UIMessageDefaultTableModel
che gestisce le caratteristiche grafiche della tabella che contiene i messaggi

### Devo modificare questa classe se
- Voglio modificare le caratteristiche grafiche della tabella (aggiungere/spostare righe/colonne)


-------------------------------------------------------------------------------------



## UIMessageObject
che gestisce le caratteristiche di qualsiasi oggetto di tipo messaggio

### Devo modificare questa classe se
- Voglio modificare le caratteristiche (attributi e metodi) comuni a tutti i messaggi


-------------------------------------------------------------------------------------



## UIMessageInfo
che gestisce le caratteristiche dei messaggi di tipo informativo (Risposta può solo essere OK)

### Devo modificare questa classe se
- Voglio modificare le caratteristiche (attributi e metodi) relative ai messaggi di tipo informativo. Es. se voglio modificare le _7_ soglie di gravità  che distinguono un messaggio INFO, WARNING o ERROR

UIMessageQuest, UIMessageRequestObj, UIMessageConf sono altre tipologie di messaggio; le classi rimanenti sono piuttosto semplici (Sorter o Comparer) e comunque il codice è commentato

