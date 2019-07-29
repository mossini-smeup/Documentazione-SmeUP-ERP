# Generazione PDF		
Per vedere qualche esempio sul componente FRM basta semplicemente andare su MyLoocup > Per lo sviluppatore > Esempi > 'Capire LoocUp' > 'I componenti' > CMP.FRM COPERTINA

## Copertina
E' stata introdotta la possibilità di generare i PDF con una copertina introduttiva davanti al documento. Questa copertina puo' essere anche completata e modificata con loghi, titoli, sfondi e quant'altro.
![03COMFRM01](http://localhost:3000/immagini/LOCFRM_PDG/03COMFRM01.png)Attraverso la G53, E' anche possibile, quindi, lanciare la generazione del PDF.

- E' stata anche aggiunta direttamente sulla scheda la presenza o meno della copertina. Un esempio pratico sulla scheda del LOA15, nella matrice relativa alla parte delle statistiche standard.


Come si puO' notare in alto sulla linguetta della sezione contenente la matrice, vi e' un'icona rossa che sta ad indicare la presenza della copertina per quella matrice, che arriva direttamente dal servizio che porta i dati nella sezione.
![LOCFRM_040](http://localhost:3000/immagini/LOCFRM_PDG/LOCFRM_040.png)
Un esempio della copertina che si pue produrre da questa sezione e' : 
![LOCFRM_041](http://localhost:3000/immagini/LOCFRM_PDG/LOCFRM_041.png)
Titolo, logo e dati reportistici vengono gestiti tramite delle variabili istanziate nei membri presenti in SCP_CLO.
 Per esempio il logo e lo sfondo sono gestiti con le variabili SFO.001 e LGO.001. Possono essere quindi gestiti (sostituiti) dal cliente.

<Cover _7_Img=[SFO.001] _7_Logo>=[LGO.001] _7_T01>=Statistiche standard _7_T02>=Divisione/Regione/Classe/Responsabile/Provincia/Cl _7_T03>=Responsabile/Regione/Cliente con incidenze>

Questo e' un esempio di XML di matrice che riguarda la configurazione della copertina. Per un esempio di copertina base fare riferimento a SMA_FRM_C1 definito in SCP_SET/SMEDEV, per uno complesso fare invece riferimento a SMA_FRM_C2.

## Volume
Il Volume non e' altro che l'insieme di piu' pdf. Come concetto e' simile ai book, che quindi hanno una copertina, un testo che deriva da un membro di documentazione, un report da matrice, ecc.
![03COMFRM02](http://localhost:3000/immagini/LOCFRM_PDG/03COMFRM02.png)Per crearlo viene lanciata una F specifica che esegue una serie di azioni di tipo report. Il volume ha un setup personalizzato descritto dal tag di scheda FRM.VOL. Per gestire i setup e' stato creato un nuovo oggetto J3 (vedi immagine sopra). Per maggiori dettagli si veda il documento di spiegazione dell'oggetto J3.

## Setup standardizzati mediante servizio standard B£GPE3
Il B£GPE3 permette l'aggiunta e l'override dei setup di schede e servizi. E' stato attivato solo per ora sui report (verra' esteso poi a tutti gli altri componenti) un meccanismo secondo il quale il setup che viene preso dalla scheda o tramite programma puo' essere completato o sovrascritto da altri livelli di risalita che possono aggiungere la configurazione definitiva del setup con il quale eseguire la funzione.
Ad esempio :  definisco in un solo punto la directory base in cui finiscono i report a prescindere dal singolo report in modo da non doverlo ridefinire per ogni report.
Esempio di risalita : 

- viene letto la SME.LDA se presente e leggo il nome del setup standard se richiesto
- viene quindi recuperato lo standard se presente (se non c'e' prende come assunto il modello A01)
- viene fatto un merge con il contesto
- verrà fatto dunque un altro merge tra lo standard e i parametri ricevuti
- se sono presenti i parametri di override allora faro' un merge con essi altrimenti con LDA.
- infine verra' ricostruita la stringa XML La scheda J3 mi aiuta a ricostruire le risalite


## Riorganizzazione della struttura dei Setup (INC, etc.)
Nella definizione dei tag di scheda (il membro EDT_SCH presente nel file SCP_CFG / SMEDEV), e' stata migliorata l'organizzazione dei vari setup dei componenti. Ecco una parte di script dove si vedono le impostazioni specifiche per ogni tipo di setup.
![03COMFRM03](http://localhost:3000/immagini/LOCFRM_PDG/03COMFRM03.png)Successivamente per utilizzare queste parti di setup comuni, e' stato necessario includerli all'interno dei vari componenti : 
![LOCFRM_042](http://localhost:3000/immagini/LOCFRM_PDG/LOCFRM_042.png)Per ogni tipologia di impostazione si avra' quindi : 

- la parte INC dove c'e' il setup comune a tutti
- la parte specifica dove ci sono i campi del componente in questione.

