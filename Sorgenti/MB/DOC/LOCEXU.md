# Componente Matrice di aggiornamento

# Matrice d'aggiornameto
La matrice di aggiornamento (EXU) è un componente che serve per aggiungere/modificare/eliminare dei record in un insieme di dati.
L'interazione con il server avviene tramite un servizio che si occupa di tutte le operazioni necessarie per il corretto funzionamento della matrice di aggiornamento.

Ogni record (riga) è costituito da diversi campi, ognuno dei quali ha un componente grafico che determina la modalità di interazione con cui l'utente può cambiarne il valore.
La forma di rappresentazione della matrice di aggiornamento non è vincolata all'essere una griglia, tramite layout e altre opzioni è possibile cambiarne l'aspetto disponendo opprotunamente i campi di ogni record.

La modificabilità e il componente grafico di interazione possono essere definiti : 
- nei dati
- nel setup inviato del servizio di aggiornamento
- nel layout


## Principali Funzionalità

- [Visualizzazione](Sorgenti/MB/DOC/LOCEXU_F01)
- [Opzioni](Sorgenti/MB/DOC/LOCEXU_F02)
- [Funzionalità sui dati](Sorgenti/MB/DOC/LOCEXU_F03)
 :  : DEC T(MB) P(DOC) K(LOCEXU_F04) //Funzionamento sui dati

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Update :  L'evento scatta una volta che le informazioni sono arrivate al server AS400 ed è confermato che sono state accettate.
- Check :  L'evento scatta ogni volta che si scambiano informazioni con il server AS400 (ma non quando scatta l'Update). E' utilizzato per verificare lato server la correttezza delle informazioni inserite prima di confermarle, o per completare automaticamente campi non ancora valorizzati, tramite informazioni mandate dal server
- Click :  scatta al click su una cella e alla selezione di una riga
- Doubleclcik :  in Loocup scatta al doppio click su una cella
- Changerow :  L'evento scatta al cambio di riga
- Changecol :  In Loocup questo evento scatta al cambio di colonna
- Change :  scatta la cambio riga e in Loccup al cambio colonna
- Drop :  scatta al drop su una riga della matrice di aggiornamento

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.EXU))) L(1)

## Schede di esempio
Gli esempi del componente EXU sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;EXU) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TRE) 2(MB;SCP_SCH;WETEST_EXU)) L(1)

## Documenti applicativi
- [Introduzione](Sorgenti/MB/DOC/LOCEXU_A)
- [Servizi di aggiornamento&-x3a; funzionamento](Sorgenti/MB/DOC/LOCEXU_B)
- [Collegamento EXB&-x2f;EXU](Sorgenti/MB/DOC/LOCEXU_T01)
- [Costruzione di un servizio di aggiornamento](Sorgenti/MB/DOC/LOCEXU_T02)
- [Utilizzo Matrice d&-x27;Aggiornamento su Device Mobile](Sorgenti/MB/DOC/LOCEXU_MO)
