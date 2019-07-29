# OBIETTIVO
Creazione di finestre di menù a scelta multipla, è possibile definire il numero di opzioni ed il numero di scelte,
oltre che il formato e la posizione della finestra di scelta.

# PREREQUISITI
D/COPY QILEGEN,£G08E
C/COPY QILEGEN,£G08

# PARAMETRI

## PARAMETRI DI INPUT

###  Funzione :  _Campo £G08FU_   Tipo Funzione

 :  : PAR T(AAAA)
01)  PRESENTARE -> Solo presentazione videata
02)  SCELTA SINGOLA
03)  SCELTA MULTIPLA
03nnn)  SCELTA MULTIPLA CON nnn RISPOSTE
04)  COMPLETAMENTO SCELTE ESISTENTI -> aggiungere testo alle scelte già presenti
05)  COMPLETARE ED AGGIUNGERE
06)  SCELTA CODIFICA/DECODIFICA
07)  TASTI FUNZIONALI ATTIVI
08)  SCELTA DECODIFICA
09)  VERIFICA CODIFICA/DECODIFICA


###  Metodo :    _Campo £G08ME_  Metodo
 :  : PAR
--> C) Visualizzazione COMPLETA --> finestra leggermente più piccola dello schermo
--> R) Visualizzazione RIDOTTA --> finestra grandezza standard
--> E) Visualizzazione ESTESA --> finestra a schermo intero
--> P) Visualizzazione PIEDE --> finestra nella parte bassa dello schermo
--> A) Visualizzazione SCELTA AUTOMATICA --> finestra adattata in modo eutomatico


### Posizionamento riga e colonna : _ campo riga £G08RI   campo colonna £G08CI_
*  Posizione in cui vengono inserite le varie scelte

###  Modello :   _Campo £G08MO _Modello visualizzazione
 :  : PAR

--> A) Stringa Libera : 
--> B) Oggetto/Tipo/Parametro
--> C) Campi Diversi (confronto 2 codici stesso oggetto :  solo <>)
--> D) Confronto Campi (confronto 2 codici stesso oggetto :  tutti)

### Ambiente :  _Campo £G08AM_
Nome programma di lancio (£PDSNP)
### Intest :  _Campo £G08IN_
       Intestazione della videata, posizionata a riga 1 colonna 1
### Testata :   _Campo £G08TE_
       Testata del menù di scelta
### Livello di chiamata
      A chiama B£G08GA
### Righe di input : _ Campo £G08A_ (Schiera)
       Descrizione possibili scelte del menù
       La costruzione della schiera è specificata tramite DS nella /COPY £G08DS
### Scelte effettuate :  _Campo £G08B_ (Schiera)
###  Schiera delle condizioni :  _Campo £G08C_ (Schiera)
### Codice :  _Campo £G08CO_

## PARAMETRI DI OUTPUT
### £G08MS :  Codice messaggio ritorno
### £G08FI :  File   messaggio ritorno
### £G0835 :  Errore (mess.<> ' ' o non effettuate scelte)


# GESTIONE VISUALIZZATORE
USO DELLA SCHIERA £08C
Questa schiera permette di condizionare la visualizzazione delle righe

Posizioni : 

__Posizione 1__
Non visualizzazione del campo di scelta multipla prima della riga


__Posizione 2__
Non visualizzazione dell'intera riga

__Posizione 3__
Attributi del campo di scelta
---->_A_   Visualizzazione del campo di scelta con attributo Reverse
---->_B_   Visualizzazione del campo di scelta con attributo Sottolineato
---->_C_   Visualizzazione del campo di scelta con attributo Lampeggiante
---->_D_   Visualizzazione del campo di scelta con attributo Posizionamento cursore
---->_ E_   Visualizzazione del campo di scelta con attributo Alta intensita
---->_ F_   Visualizzazione del campo di scelta con attributo Reverse e posizionamento


__Posizione 4-->15__
Si può specificare il tipo oggetto e il parametro oggetto in modo da poter decodificare il codice inserito nella
schiera £08A.
**Questa opzione non è disponibile in caso venga scelto il modello stringa libera.**


__Posizione 19__
Si può specifica una nuova decodifica che sostituisca quella ricavata dalla tabella

**Questa opzione è disponibile solo in caso vengano scelti il modello 3 o 4.**
