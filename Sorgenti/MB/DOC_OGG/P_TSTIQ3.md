# OBIETTIVO
Gestire le operazioni base sull'oggetto Q3 Filtro.

# FUNZIONI E METODI

## DAT - Ritorno dati
Viene ritornta in £IQ3OU la DS £IQ3D contenente le proprietà del filtro.

>   £IQ3DCD Codice
   £IQ3DDE Descrizione
   £IQ3DTT Tipo tracciato
   £IQ3DOT Oggetto tracciato
   £IQ3DFP Filtro privato
   £IQ3DDI Campi dinamici
   £IQ3DCF Id configurazione
   £IQ3DCN Nome configurazione
   £IQ3DCT Desc configurazione
   £IQ3DUS User configurazione
   £IQ3DFN Fonte
   £IQ3DSC Schema Associato


## LIS - Lista filtri
Viene ritornata la sequenza dei filtri pubblici disponibili per l'oggetto.
I filtri disponibili sono delle seuenti tipologie : 

>
  - S/xx - Schemi dello script.
     Definiti nello script, possono essere pubblici o privati.



## CAR : FLT - Caricamento campi
Vengono valorizzate le schiere £IQR3I e £IQR3D contenenti la definizione dei campi del filtro.
Definizione della £IQR3D dipende dalla DS £IQ3C
>  £IQ3CCD Nome
  £IQ3CIN Intestazione
  £IQ3COG Oggetto
  £IQ3CLU Lunghezza
  £IQ3CND Decimali
  £IQ3CMU Multiplo
  £IQ3COP Operatore
  £IQ3CDF Valore default
  £IQ3COB Obbligatorio
  £IQ3CCT Controllare
  £IQ3CDI Calcolo dinamico
  £IQ3CSC Shortcut
  £IQ3CCS Case sensitive
  £IQ3CFU Funzione
  £IQ3CPA Parametro
  £IQ3CHI Hidden


Il caricamento dei campi è dipendente dalla sua tipologia : 

>  - S/xx - Filtri dello script.
     Vengono caricati tramite programma B£IQRS, sono definiti nel file di script SCP_QRY      SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).

  - yy/xx - Filtri definiti dal programma di fonte.
     Vengono caricati dal programma di fonte, dove yy=fonte xx=schema (vedi £IQ5).

  - ** - 	Filtri del programma chiamante
     La schiera £IQR3I e opzionalmente la schiera £IQR3D devono essere valorizzate dal programma chiamante.
     I campi vengono impostati a valorizzazione dinamica £IQ3CDI='1', vengono quindi supposti OAV.



## CAR : VAL - Caricamento valore campi
Viene valorizzata la schiera £IQR2V in base ai parametri FLT() e CFG() in £IQ3IN.

Se passato il parametro FLT() in £IQRIN, vengono caricati i valori di filtro secondo la sintassi : 
FLT(£IQR3I(x)(valore_x))
Se passato il parametro Q3_CFG([MEIDOJ]) in £IQRIN, vengono caricati i valori di filtro dalla configurazione.
Se passato il parametro Q3_CFG(*USER) in £IQRIN, viene ricercata la configurazione del filtro utente.

## CMP : FLT - Completamento definizione campi
Viene completata la definizione di ogni singolo campo in base al tipo tracciato £IQ3DTT/£I32DOT.

In questa fase vengono estratti i campi di filtro con valore dinamico £IQ3DDI = '1'.
E' compito del programma di fonte valorizzare correttamente questi campi che per defaut assumono valore ='1'.

La nuova valorizzazione della DS £IQ3D è ritornata in £IQ3OU.

## CHK : FLT - Validazione oggetto valori del filtro
Controlla la validità del codice oggetto ricevuto in £IQ3ID rispetto ai valori in £IQR3V

## FMT : CFG - Formattazione struttura configurazione
Viene ritornata in £IQ3OU la struttura della configurazione in base a £IQR3D.

## FMT : VAL - Formattazione valori configurazione
Vengono ritornati in £IQ3OU i valori della configurazione in base £IQR3V.

## XML     - Funzioni su stringa XML (SV)
Data in input una stringa nel formato XML, permette di andare ad aggionare riscrivere i valori delle schiere
della £EQRDS relative ai filtri.
Con il metodo WRI vengono cancellati i precedenti valori e riportati esclusivamente quelli contenuti nella
stringa XML.
Con il metodo UPD vengono riscritti solo i valori indicati nella stringa XML.

## SAV : VAL - Salvataggio valori configurazione
Vengono salvati in B£MEDE i valori della configuarazione.

## CTR     - Funzioni di controllo di validità di un record

- RECINI dato in input un filtro, predispone la struttura necessaria al controllo di validità di un record rispetto a tale filtro
- RECCHK dato in input un record (nel campo £IQ3IN) permette di verificarne la validità rispetto al filtro indicato con la precedente chiamata con metodo RECINI


# ESEMPI DI UTILIZZO

## Aggiornamento cieco del filtro


- CAR : VAL -> Carico i filtri ed i suoi valori
- XML : WRI -> Aggiorno i valori del filtro a partire da una stringa XML passata. In alternativa si possono modificare direttamente i valori contenuti nelle schiere della £EQRDS.
- SAV : VAL -> Salvo i valori aggiornati del filtro






