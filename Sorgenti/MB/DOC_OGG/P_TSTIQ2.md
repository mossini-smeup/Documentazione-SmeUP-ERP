# OBIETTIVO
Gestire le operazioni base sull'oggetto Q2 Schema.

# FUNZIONI E METODI

## DAT - Ritorno dati
Viene ritorna in £IQ2OU la DS £IQ2D contenente le proprietà dello schema.

>   £IQ2DCD Codice
   £IQ2DDE Descrizione
   £IQ2DTT Tipo tracciato
   £IQ2DOT Oggetto tracciato
   £IQ2DSP Schema privato
   £IQ2DDI Campi dinamici
   £IQ2DKY Campo chiave


## INZ - Inizializzazione schema
Viene inizializzato lo schema. Prima dell'utilizzo di uno schema in un servizio, va sempre eseguita questa funzione.

### Parametri di input
Oltre che l'oggetto (£IQ2OG) e lo schema (£IQ2SC) possono essere opzionalmente passati nella campo di input (£IQ2IN), nella forma "codiceparametro(valoreparametro)" i seguenti parametri : 
* Context :  indica il contesto di riferimento per il quale gli eventuali setup utente verranno, salvati. A volte questa informazione può contenere delle informazioni che possono poi essere impiegate dal pgm di costruzione dello schema.
* SchPar :  Può contenere delle informazioni libere, che possono essere poi eventualmente sfruttate dal pgm di costruzione dello schema.
* Tp :  Se valorizzata a Yes allo schema verrà automaticamente aggiunta una colonna nascosta avente codice ID_TP, che conterrà il tipo oggetto di riferimento dello schema. Questo a meno che nello schema non sussista già una colonna con il medesimo codice.
* Id :  Se valorizzata a Yes allo schema verrà automaticamente aggiunta una colonna nascosta avente codice ID_LI, che conterrà il codice dell'oggetto di riferimento della riga. Questo a meno che nello schema non sussista già una colonna con il medesimo codice.
* Qry :  Se valorizzato a Yes allo schema come prima colonna verrà aggiunto una colonna avente codice $QR, tipizzata con Oggetto V2RADIO, che normalmente avrà la funzione di gestire il dinamismo di scelta della riga.
* Det :  Se valorizzato a Yes allo schema come prima colonna (o a seguito della colonna Qry) una colonna avente codice $DET, tipizzata con Oggetto VOCOD_VER, con valore fisso 000103 "Dettaglio", che normalmente viene utilizzata per gestire un dinamismo che lanci una funzione di "Dettaglio" correlata alla riga in oggetto.
* CndDet :  è del tutto simile alla precedente campo, ma con queste importanti differenze :  la colonna avrà codice $KD, nell'attributo invece di passare "Yes" dovrà essere passato l'OAV dell'oggetto attraverso cui verrà determinato se indicare per la riga il valore fisso 000103 o valore nullo. La scelta verrà effettuata in base al fatto che l'attributo abbia un valore o meno. Questa funzione permette di evidenziare la colonna di dettaglio solo, appunto in presenza di una certa condizione.
* IntDet :  intestazione della colonna dettaglio. Se viene aggiunta una colonna per effetto degli attributi Det o CndDet, su tale colonna può essere forzata come intestazione il testo passato in questoa attributo.
* Opz :  Se valorizzato a Yes allo schema, come prima colonna (o a seguito della colonna Qry e Det/CndDet) viene automaticamente aggiunta una colonna avente come codice $OP, come Oggetto VOCOD_VER, e come valore fisso 000102. Questa colonna va normalmente utilizzata, in concomitanza con le funzionalità della funzione/metodo FMP/EXB della £IQ2 che permette di agganciare in automatico a questa colonna le principali azioni di gestione dell'oggetto di riferimento della singola riga.

## DFT - Ritorno Schema di default
Dato input l'oggetto viene ritornato lo schema previsto default per tale oggetto.
Nell'output verrà ritornato nel campo £IQ2SC, il codice dello schema mentre nel campo, £IQ2OU verrà ritornata la DS di definizione dello schema £IQ2D.

La differenza fra il metodo blank e MDE sta nel fatto che nel primo caso verrà ritornato lo schema previsto come default, mentre nel secondo verrà considerata anche l'eventuale memorizzazione effettuata a livello di utente/gruppo utente o per tutti gli utenti.

## VIS.SCH - Visualizzazione
Viene visualizzata la definizione dei campi dello schema.

## LIS - Lista schemi
Viene ritornata la sequenza degli schemi pubblici disponibili per l'oggetto.
Gli schemi disponibili sono delle seuenti tipologie : 

>  - P/xx - 	Schemi del barratore.
     Sono schemi pubblici, utilizzabili quindi in ogni query, sono cablati nel programma
     xxxx_M (vedi £BAR)

  - S/xx - Schemi dello script.
     Definiti nello script, possono essere pubblici o privati.

  - I/xx - 	Schemi da £G25
     Sono anch'essi schemi pubblici e fanno riferimento alla tabella INT.



## CAR : SCH - Caricamento campi
Vengono valorizzate le schiere £IQR2I e £IQR2D contenenti la definizione dei campi dello schema.
Definizione della £IQR2D dipende dalla DS £IQ2C
>
  £IQ2CCD Nome
  £IQ2CIN Intestazione
  £IQ2COG Oggetto
  £IQ2CLU Lunghezza
  £IQ2CND Decimali
  £IQ2CMU Multiplo
  £IQ2CTP Tipo
  £IQ2CHI Hidden
  £IQ2CDI Calcolo dinamico
  £IQ2CFU Funzione
  £IQ2CPA Parametro



Il caricamento dei campi è dipendente dalla sua tipologia : 

>  - P/xx - 	Schemi del barratore.
     Vengono caricati dal programma xxxx_M (vedi £BAR)

  - S/xx - Schemi dello script.
     Vengono caricati tramite programma B£IQRS, sono definiti nel file di script SCP_QRY      SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).

  - I/xx - 	Schemi da £G25
     Viene richiamata la £G25(COSTES : TR/A)

  - yy/xx - Schemi definiti dal programma di fonte.
     Vengono caricati dal programma di fonte, dove yy=fonte xx=schema (vedi £IQ5).

  - ** - 	Schema del programma chiamante
     La schiera £IQR2I e opzionalmente la schiera £IQR2D devono essere valorizzate dal programma chiamante.
     I campi vengono impostati a valorizzazione dinamica £IQ2CDI='1', vengono quindi supposti OAV.



## CMP : SCH - Completamento definizione campi
Viene completata la definizione di ogni singolo campo in base al tipo tracciato £IQ2DTT/£IQ2DOT.
Viene estratto il campo chiave dello schema £IQ2DKY in base alla valorizzazione £IQ2CTP='K01' a livello campo.
In questa fase vengono estratti i campi di schema con valore dinamico £IQ2DDI = '1'.

Ritorna la DS £IQ2D in £IQ2OU.


## CMP : VAL - Completamento valore campi
Viene valorizzata la schiera £IQR2V dove mancante in base al codice oggetto ricevuto in £IQ2ID.
La valorizzazione dei campi è dipendente dalla sua tipologia : 

>  - P/xx - 	Schemi del barratore.
     Vengono caricati  valori dal programma xxxx_M (vedi £BAR)

  - I/xx - 	Schemi da £G25
     Vengono caricati i valori tramite la £G25(COSRIG : TR)



Tutti i campi a caricamento dinamico, quindi con £IQ2CDI='1', vengono valorizzati dinamicamente tramite chiamata
a B£IQRC(VAL;SCH).

## CLR : VAL - Pulizia valore campi
Viene pulita la DS £IQR2V

## FMI : EXB - Formattazione intestazione per matrice
Viene ritornato l'XML delle intestazioni della griglia di una matrice.
Vengono ritornati i valori dei campi separati da '|' in £IQ2OU. Il pgm specifico di costruzione dello schema, verrà richiamato con funzione OUT/EXB.GRI. Se tale pgm ritorna un output, per questa funzione, tale output verrà considerato come risultato della funzione.
Viceversa verrà costruito a partire dalle definizioni delle schiere £IQR2I/D.
E' possibile in questa funzione passare nell'input attributo ID, che se valorizzato permette di aggiungere in automatico allo schema, come colonna nascosta, una colonna con codice "ID_OG", contenente, l'identificativo dell'oggetto.

## FMI : CSV - Formattazione intestazione
Vengono ritornate le intestazioni dei campi separati da ';' in £IQ2OU.

## FMC : LOO - Formattazione record da schiera
Vengono ritornati i valori dei campi separati da '|' in £IQ2OU. Il pgm specifico di costruzione dello schema, verrà richiamato con funzione OUT/EXB.RIG. Se tale pgm ritorna un output per questa funzione, tale output verrà considerato come risultato della funzione.
Viceversa verrà costruito a partire dalle definizioni delle schiere £IQR2I/D.

In input, per questa chiamata, nel campo £IQ2ID, va passato il codice oggetto, mentre nel campo £IQ1IN può essere passato la DS dell'archivio cui appartire l'oggetto.

## FMK : LOO - Completamento e Formattazione (mantiene £IQR2V ricevuti)
Svolge una formattazione del tutto simile a quella della funzione/metodo FMK/LOO.

## FMS : LOO - Setup di Matrice dello Schema
Viene ritornato il setup di matrice associato allo schema. Il pgm specifico di costruzione dello schema, verrà richiamato con funzione OUT/EXB.SET. Se tale pgm ritorna un output, per questa funzione, tale output verrà considerato come risultato della funzione.
Viceversa verrà ritornato un setup di default generico.

## FMT : FIX - Formattazione record da schiera
Vengono ritornati i valori dei campi a tracciato fisso in £IQ2OU.
Vengono esclusi i campi hidden £IQ2CHI='1'.

## FMT : FIX_H - Formattazione record da schiera
Vengono ritornati i valori dei campi a tracciato fisso in £IQ2OU.

## FMT : CSV - Formattazione record da schiera
Vengono ritornati i valori dei campi separati da ';' in £IQ2OU.

## FMV : LOO - Formattazione schiera da record
Viene valorizzata la schiera £IQR2V da £IQ2IN e separatore '|'.

## FMV : FIX - Formattazione schiera da record
Viene valorizzata la schiera £IQR2V da £IQ2IN in base al tracciato fisso.

## FMV : CSV - Formattazione schiera da record
Viene valorizzata la schiera £IQR2V da £IQ2IN e separatore ';'.

## TRA : VAL - Trasformazione valori
Viene eseguita la trasformazione dei valori £IQR2V tramite £C£A dove : 

>
  £C£AFU='DER'
  £C£AME='OGG'
  £C£ACO=£IQ2CO
  £C£AT1=£IQ2OG
  £C£AAL=£IQR2V
  £IQR2V=£C£AO1



# PARAMETRI DI INPUT

Nel campo £IQ2IN (Input) è possibile passare nel formato attributo fra parentesi (es. campo(valore)) alcuni parametri.

* Det - Colonna Dettaglio, se valorizzata a Yes nelle funzioni di formattazione matrice e SQL, viene automaticamente aggiunta una colonna $DET tipizzata a VOCOD_VER, che nel dettaglio conterrà il valore "000103" (vai a dettaglio). L'utilizzo di questa colonna sarà poi di competenza del servizio/scheda specifico che utilizza lo schema.

* Opz - Colonna Opzioni. Può assumere i seguenti valori : 
** "Yes" - Nelle funzioni di formattazione matrice e SQL, viene automaticamente aggiunta un colonna opzione $OP tipizzata a VOCOD_VER, che nel dettaglio conterrà il valore "000102" (scelta opzione). Specularmente per effetto di questo nelle funzioni di ritorno popup vengono tornate le funzioni standard di gestione (si veda la £J14).
** "xxxxxx" - Se viene valorizzato un codice corrispondente ad un elemento di VOCOD_VER, tale elemento viene automaticamente aggiunto come colonna. Sarà poi di competenza del servizio/scheda specifico che utilizza lo schema.

* SchPar - Parametri Schema. Tramite esso è possibile passare al pgm di gestione dello schema una serie di dati che da esso possono essere utilizzati per contestualizzare la formattazione dello schema.

* Context - Contesto. Tramite esso è possibile passare la struttura del contesto in cui viene impiegato lo schema. A partire da tale informazione nel pgm dello schema possono essere implementate delle logiche di contestualizzazione non dissimili da quelle applicabili tramite lo sfruttamento dell'SchPar.

