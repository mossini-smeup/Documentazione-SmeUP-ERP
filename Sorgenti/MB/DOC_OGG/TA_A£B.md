# A£B - Impostazioni di localizzazione
 :  : DEC T(ST) K(A£B)
## OBIETTIVO
In questa tabella vengono raggruppate le impostazioni di localizzazione.
Tali impostazioni possono poi essere associate ad un utente oppure (in risalita) ad un ambiente.

Questo è lo schema secondo cui vengono settate le impostazioni di localizzazione : 
Prima viene controllato se all'utente (tabella B£U) sono associate impostazioni di localizzazione (ossia
un elemento di questa tabella).
Se l'utente non ha impostazioni specifiche, tale controllo viene fatto sull'ambiente (ex tabella B£B ora ).
raggiungibile da UP UT5).
Se nemmeno nell'ambiente sono associate impostazioni di localizzazione, vengono lette le impostazioni
base dalla tabella B£2.

In B£U e B£B è quindi possibile specificare in un campo, un relativo elemento di A£B.
La risalita effettuata NON è a pettine.
Se sull'utente viene indicata una A£B, vengono considerate tutte le informazioni indicate in quella tabella.
Non viene controllato nulla sull'ambiente ne sulla B£2.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$A£BA **Lingua assunta**
È un elemento della tabella V§L :  definisce la lingua in cui verrà presentata l'interfaccia utente.
 :  : FLD T$A£BB **Formato data**
È un valore V2/FMDAT :  definisce il formato di presentazione della data :  DMY oppure MDY.
Può assumere i seguenti valori : 
  :  Formato DMY
1 :  Formato MDY
* :  In questo caso non viene forzato nessun formato data, rimane quindi valido quello di sistema o
   quello impostato tramite il campo T$A£BE (JOB attrib da lingua)
 :  : FLD T$A£BC **Separatore decimale**
Lasciando il campo ' ' la virgola separa gli interi dai numeri decimali, impostando '1' viene invertito il
significato con il '.' (punto).
Il valore speciale * invece non forza nessun separatore decimale, rimane quindi valido quello di sistema o
quello impostato tramite il campo T$A£BE (JOB attrib da lingua)
 :  : FLD T$A£BD **Lingua OS400**
Imposta l'eventuale lingua in cui verranno visualizzate tutte le informazioni di sistema operativo
 :  : FLD T$A£BE **JOB attrib da lingua**
E' possibile specificare la lingua da cui ricavare (e successivamente impostarea livello di JOB) i
seguenti valori : 
- Formato data (solo se impostato * in T$A£BB - Formato data)
- Separatore data
- Carattere separazione ora
- Identificatore lingua (non la lingua di traduzione!!!!)
- Identificatore nazione o regione
- Formato decimale (solo se impostato * in T$A£BC - Separatore decimale)

Attenzione che per il corretto funzionamento di questa opzione deve essere installata sul sistema la
relativa lingua secondaria (e quindi la libreria QSYS29xx e il file CPX8416 in essa contenuto)
