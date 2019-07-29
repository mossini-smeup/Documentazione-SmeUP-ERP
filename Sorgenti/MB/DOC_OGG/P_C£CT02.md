# MANUTENZIONI DI MASSA E CONTROLLATE PER UN ANAGRAFICO ARTICOLI
## OBIETTIVO
Permettere una manutenzione di massa e parametrica dei dati anagrafici dell'articolo attraverso una definizione tabellare dei campi ammessi e delle relative caratteristiche.
Ammettere quindi le principali funzioni di un SQL su un archivio ma con tutti i controlli sul contenuto dei valori modificati.

## CARATTERISTICHE
A.   L'applicazione delle modifiche avviene un campo per volta. Se si vogliono modificare la classe e il disegno bisogna eseguire due chiamate al programma di gestione.
B.   La funzione, benchè concepita per l'anagrafico articoli (ITEMAS del MAPICS DB) ha caratteristiche generali quindi potrà essere facilmente applicata (mediante la scrittura di alcuni semplici programmi) a diversi altri archivi.

## TABELLE COLLEGATE
C£F  Tabella archivi descritti alle manutenzioni di massa
C£M  Tabella di definizione campi
C£C  Tabella condizioni sui campi

## SOTTOFUNZIONI
Programma di impostazione delle scelte possibili

Definita una sottotabella di C£M (quindi il file) vengono visualizzati tutti gli elementi (campi) presenti e sono permesse le azioni specifiche sul campo.

Su ogni elemento visualizzato potranno essere richiamate le funzioni seguenti : 
1.   Funzione di richiesta del valore da inserire.

Una volta scelto un campo mediante questo programma è possibile chiedere le condizioni dei valori da attribuire a tale
campo.

Si distingueranno due condizioni : 
 * Numerico
 ** B1.  Valore
 ** B2.  Azione
 *** S = Sostituzione
 *** + = Somma Ecc. per altre operazioni)
 ** B3.  Condizione dell'azione
 *** % = Se +/- significa che si vuole applicare una percentuale

 * Alfanumerico
 ** B1.  Nuovo valore

2.   Funzione di impostazione delle condizioni di selezione
In base ad un campo questo programma permette di definire le seguenti condizioni : 
1.   Condizione di AND/OR
2.   Limiti iniziale e finale
3.   Elenco di valori possibili
3.   Funzione di ordinamento della selezione

Sulla lista presentata è possibile indicare l'ordinamento desiderato per la funzione desiderata.

## AGGIORNAMENTO
Premendo F6 si passa all'esecuzione delle funzioni richieste. Il programma richiede se si desidera solo una lista preliminare di verifica o si vuole aggiornare l'archivio.
Viene eseguita la selezione richiesta e inizia il processo di applicazione attraverso i passi seguenti : 
1.   Verifica delle condizioni di ogni aggiornamento
Per ogni riga letta vengono passati vecchi e nuovo valore al programma di CONTROLLO. Questo procederà alla verifica delle condizioni impostate nell'apposito archivio e indicherà se permesso o meno l'aggiornamento.
