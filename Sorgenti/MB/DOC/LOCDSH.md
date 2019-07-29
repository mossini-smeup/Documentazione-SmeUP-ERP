# Componente Dash

## Abstract
Il componente Dash (DSH) mostra un dato tramite una forma a cruscotto, disponibile in diversi layout.
I layout che si possono scelgiere sono 8 e non possono essere aggiunti dall'utente.
E' possibile scegliere il layout di visualizzazione attraverso l'attributo di setup "SelectLayout".
Tutti gli esempi utilizzabili, sono consultabili nel nostro showcase dei componenti.

Per popolare il componente dash è possibile valorizzarlo anche passando i valori tramite G.SET del componente. utilizzando gli attributi ForceText, ForceUM, ForceValue e ForceIcon.
E' possibile, nel caso si abbia una matrice con più colonne, andare a specificare il nome della colonna da cui prendere i valori. utilizzando gli attributi TextColName, UmColName, ValueColName e IconColName.
In questo componente è anche possibile, specificando il nome della colonna, effettuare delle operazioni matematiche che forniscono un risultato, visualizzato poi all'interno del dash.
Grazie ad un attributo di setup è possibile formattare il valore mostrato.

Le informazioni che il componente può leggere nella griglia XML che rappresenta i suoi dati  sono (in ordine) : 
- Valore
- Unità di misura
- Descrizione
- Icona

Il componente supporta il dinamismo "click".


## Funzionalità principali
- [Visualizzazione dati](Sorgenti/MB/DOC/LOCDSH_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCDSH_F02)
- [Gestione dati](Sorgenti/MB/DOC/LOCDSH_F03)

## Eventi gestiti
Il componente gestisce i seguenti eventi : 
Il componente supporta il click.

## Formato dati
Tipo di XML utilizzato :  XML Griglia.

## Attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.DSH))) L(1)

