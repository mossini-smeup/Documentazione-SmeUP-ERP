# FUNZIONI E METODI

## '   ' Ricerca / decodifica / lettura
 Dati i riferimenti di una configurazione, ne ritorna il relativo record (£ICFRP=Record)

## 'CTR' Controllo
 Data una configurazione controlla la validità delle sue risposte. Il record non può essere
 passato in input, ma viene ritornato in output.

 Se previsto nelle caratteristiche del tracciato per il controllo verrà eseguito
 anche il relativo programma specificato. Questo deve avere la stessa entry dei pgm
 della £ICF.

## 'GES' Gestione
 Permette di eseguire le azioni di gestione relative ad una configurazione

 '01'=Inserimento
 '02'=Modifica
 '03'=Copia
 '04'=Cancellazione
 '05'=Interroga

## 'STR' Funzioni su Stringa
 Permette di eseguire funzione di modifica/visualizzazione/controllo su una stringa
 di caratteri passata nella variabile £ICFRP rispetto al tipo configurazione passato
 nella variabile £ICFTC.

 In caso di modifica il risultato delle operazioni attuate viene ritornato nella
 stessa variabile.

## Metodi 'POS_PAR' e 'PAR_POS' della funzione 'STR'
Questi due metodi gestiscono la conversione di una stringa dati da una struttura posizionale : 
- XXYYYYZ
ad una struttura a parentesi : 
- A(XX)B(YYYY)C(Z)
di una configurazione.
Dove A, B e C sono i campi gestiti nella configurazine

Campi input : 
£ICFTC = Tipo configurazione (Esempio F-BRARTI0F, S-BRARTI/A)
£ICFRP = Stringa dati

Dalla £IR1 sono deternimanti i nomi dei campi con relativa posizione iniziale e lunghezza utilizzati
 nella trasformazione delle stringhe.

## 'MDE' Funzioni su Memorizzazioni Video
 Simile alla funzione STR con la differenza che la stringa viene ripresa da una memorizzazione
 video estesa, determinata dal contesto passato nella variabile £ICFCX.

 La funzione di modifica comporta l'aggiornamento della stessa. In questo caso viene inoltre
 sempre aggiornata anche la corrispondente area dati locale (SMELDA - £G00).

## 'ATT' Attiva
 Dati i riferimenti di una configurazione, questa viene copiata nella configurazione *JOB

## 'RID' Deriva IDOJ
 Data un record di configurazione, ne ritorna il relativo IDOJ (£ICFRP=Record)

## 'OPR' Operazioni su Risposte
 Dati i riferimenti di una configurazione, permette di eseguire operazioni sulle risposte
 (£ICFRP=Xml delle risposte)

 'RIT_ALL'= Ritorna tutte le risposte in output
 'AGG_ALL'= Aggiorna tutte le risposte a partire da quanto passato in input

