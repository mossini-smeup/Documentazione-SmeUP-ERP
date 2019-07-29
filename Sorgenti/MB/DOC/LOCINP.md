# Componente Input Panel

## Abstract

Il pannello di input (Input Panel - INP) è un componente utilizzato pervalentemente per la visualizzazione/modifica/eliminazione di un singolo record o per la richiesta di valori e parametri.
L'interazione con il server avviene tramite un servizio che si occupa di tutte le operazioni necessarie per il corretto funzionamento del componente.

Ogni record è costituito da diversi campi, ognuno dei quali può avere un componente grafico che determina la modalità di interazione con cui l'utente può cambiarne il valore.
Oltre alla forma standard di rappresentazione in colonna (o con i campi distribuiti su più colonne) è possibile definire tramite layout la disposizione dei campi del record.

La modificabilità e il componente grafico di interazione possono essere definiti : 
- nei dati
- nel setup inviato del servizio di aggiornamento
- nel layout



## Principali Funzionalità

- [Visualizzazione](Sorgenti/MB/DOC/LOCINP_F01)
- [Opzioni](Sorgenti/MB/DOC/LOCINP_F02)
- [Dinamismi](Sorgenti/MB/DOC/LOCINP_F03)
- [Funzionalità sui dati](Sorgenti/MB/DOC/LOCINP_F04)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Update :  L'evento scatta una volta che le informazioni sono arrivate al server AS400 ed è confermato che sono state accettate.
- Check :  L'evento scatta ogni volta che si scambiano informazioni con il server AS400 (ma non quando scatta l'Update). E' utilizzato per verificare lato server la correttezza delle informazioni inserite prima di confermarle, o per completare automaticamente campi non ancora valorizzati, tramite informazioni mandate dal server
- Click :  Funziona solo quando si utilizza l'input panel senza servizio di aggiornament e scatta una volta premuto "Invio" o alla pressione del bottone di conferma. Serve per invaire al target del dinamismo le variabili di tutti i campi dell'input panel.

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.INP))) L(1)

## Documenti applicativi
- [Introduzione](Sorgenti/MB/DOC/LOCINP_A)
- [Come si utilizza un input panel](Sorgenti/MB/DOC/LOCINP_B)
- [Costruzione delle sezioni](Sorgenti/MB/DOC/LOCINP_C)
- [Aggiornamento Caratteristiche Griglia&-x2f;Setup Campi](Sorgenti/MB/DOC/LOCINP_D)
- [Funzionalità sui dati](Sorgenti/MB/DOC/LOCINP_F)
- [Utilizzo Input Panel su Device Mobile](Sorgenti/MB/DOC/LOCINP_MO)
