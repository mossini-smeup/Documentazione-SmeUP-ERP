## LE PTF

Una PTF è una lista di operazioni da effettuare presso un cliente per l'installazione di una  nuova versione di SMEUP.
Il nome di una PTF si compone nel seguente modo : 

- I primi 2 caratteri contengono l'applicazione (A£, B£ etc...)
- I successivi 5 contengno la data nel formato AMMGG
- 1 lettera per ovviare al problema della sovrapposizione dei nomi (se ho la PTF B£91013 potrebbe essere sia del 13 ottobre del 1999 che del 13 ottobre del 2009 quindi aggiungo una  lettera in fondo per differenziarli)

Ogni PTF è un membro del file PTF nella libreria SMEDEV, il cui nome è composto nel modo appena descritto. Nel tipo membro va la versione di rilascio di SMEUP (V2R1, V2R2 etc...)

## SCRIVERE UNA PTF
Con **UP PTF**  ho la possibilità di gestire le PTF.
Alla partenza il programma chiede : 

- Libreria :  libreria dei programmi
- Data minima PTF :  data da cui partire per visualizzare la lista delle PTF.

Con questo programma è possibile editare la PTF, cioè descrivere in formato documentazione attiva quello che fa e scrivere i passi (comandi) che vengono eseguiti per l'installazione della PTF stessa. Si tratta, in pratica, dell'editazione di un membro di script.
Per le spiegazioni sull'utilizzo dei vari TAG di script vedere qui : 
- [Elenco MACRO di documentazione](Sorgenti/MB/DOC/B£DOCU_40)
Le libreie non devono mai essere specificate in maniera diretta ma attraverso variabili. Sono presenti diversi tipi di variabili e in particolare : 
**Variabili di PTF**

|  Nam="Variabili di PTF" R="0000000050" |
| 
| .COL Txt="Variabile" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione"  LunAut="1" A="L" |
| _&_SY.LIB;<NomeFile> | libreria in cui è presente il file |
| _&_SY.LIB;<FIleSorgente>;<NomeFIle) | libreria in cui è presente la definizione del file |
| _&_LIBDAT | libreria in cui creare il nuovo file |
| _&_LIBPER | libreria verticale del cliente |
| _&_LIBSYS | libreria di sistema |
| 


**ALtre variabili**

|  Nam="Altre Variabili" R="0000000050" |
| 
| .COL Txt="Variabile" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione"  LunAut="1" A="L" |
| _&_<B§V> | tutte le variabili definite nella tabella B§V |
| _&_AM. | tutte le variabili di ambiente |
| 


Per le spiegazioni sulle variabili vedere qui : 
- [Variabili (Lato SERVER)](Sorgenti/MB/DOC_OGG/V3_EVA)

**NOTA : ** La prima riga della PTF deve essere **..REL D(GG/MM/AAAA)** per indicare a quale  data si riferisce (ovviamente si devono sostituire i __".."__ con i __due punti__).
Una PTF viene creata quando le modifiche introdotte in SMEUP richiedono degli adeguamenti all'installazione effettuata presso il cliente. Tali adeguamenti comportano l'esecuzione di una serie di operazioni preliminari di controllo, operazioni di aggiornamento e operazioni/controlli di post-aggiornamento.

Tipicamente si crea una PTF quando viene cambiato il tracciato di un file e c'è quindi necessità di : 

- effettuare dei controlli propedeutici all'installazione del nuovo file   (Esistenza di dipendenze, file logici etc...)
- effettuare copie di salvataggio dei vecchi archivi e cancellazione degli oggetti   dipendenti
- travaso dei dati dal file vecchio al file nuovo
- rigenerazione dei logici precedentemente cancellati
- eventuali controlli post esecuzione

Da qui si può quindi dedurre una sorta di __"template"__ da cui partire per scrivere una PTF : 

- OBIETTIVO, cioè una spiegazione del perchè la PTF è stata creata e a quale risultato   porterà la sua esecuzione
- VERIFICHE PRELIMINARI
  -- PREREQUISITI cioè cosa serve perchè la PTF giri correttamente (OAV etc...)
  -- VERIFICHE DI AMBIENTE cioè la lista librerie, piuttosto che la presenza del/dei file      nella libreria che io ho settato essere la libreria dati etc...
- ESECUZIONE della PTF stessa :  la lista (compresa tra **INI** e **FIN**) dei comandi che     la PTF esegue quando viene lanciata
- VERIFICHE POST ESECUZIONE :  cosa controllare una volta che la PTF è girata (possono essere  anche programmi da lanciare)
- DETTAGLIO MODIFICHE SUL TRACCIATO :  una lista (sotto forma di tabella) dei campi modificati con i tipi e le lunghezze.

**NOTA** : ci sono PTF che hanno come versione di rilascio la V999. Queste vanno eseguite __AD OGNI RILASCIO DI SMEDEV
