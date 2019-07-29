# Schede e setup
## Introduzione
Dal rilascio V2R2M061003-01A è stata attivata la possibilità di specificare setup multipli utente per ogni sezione di una scheda.
Tali setup vengono memorizzati su AS/400 nel file B£MEDE0F con i seguenti campi chiave : 

- METIPA   REU-
- MECODI  GRA_<TipoSottosezione> Es :  GRA_MAT
- MECODI  GRA_<TipoSottosezione> Es :  GRA_MAT
- METIPO  blank
- MECOD1  <NomeMembroScriptScheda>/<IdSottosezione> Es :  ESE1B/MATSTILI
- MECOD2  Nome Utente (** = tutti)
- MECOD3  Nome del setup salvato

Non è garantita l'univocità del campo MECOD1 che contiene l'identificazione della sezione al quale il setup appartiene.
Infatti la combinazione "NomeMembroScriptScheda"+"/"+"IdSottosezione" può superare i 15 caratteri ammessi come lunghezza massima dal campo MECOD1.
Inoltre la libreria che contiene il nome dello script non viene presa in considerazione per determinare il setup da caricare.
Nel caso in cui "NomeMembroScriptScheda"+"/"+"IdSottosezione" possa non essere univoca occorre intervenire o sul NomeMembroScriptScheda o sull'IdSottosezione, accorciandoli opportunamente.

Il setup viene salvato come testo XML nel campo MEDATI che ha una lunghezza massima di 30.000 bytes che dovrebbe essere sufficiente per qualunque tipo di memorizzazione.

## Come attivare la gestione dei setup utente nelle schede
La gestione dei setup utente è attiva per default.
E' soggetta ad autorizzazioni relativamente all'attivazione della voce del menu di popup di sottosezione (e la corrispondente SubSectionCommandBar (vedi sotto)).
Il livello di autorizzazione della classe MNU.BAR è '00'.
Se non si è autorizzati, sarà comunque possibile utilizzare e specificare i setup utente memorizzati (quelli relativi al proprio utente e quelli generici) e gli eventuali setup definiti nello script di scheda, ma non sarà possibile modificare, creare e cancellare i setup.

## L'Attributo UserSetup
Esiste (da parecchio) un attributo, a livello di sottosezione, che determina l'esistenza di setup utente.
Da questo rilascio, l'esistenza dei Setup Utente è principalmente determinata dalla presenza nell'XML di definizione della scheda di nodi UserSetup all'interno delle sottosezioni.
La gestione nodo UserSetup elimina la necessità di richiamare servizi aggiuntivi per conoscere l'esistenza dei Setup utente per la Sottosezione interessata, velocizzando considerevolmente l'elaborazione e consentendo di non dover personalizzare le schede per la sola attivazione del Setup Utente.
Da questo rilascio quindi **ogni** sottosezione può avere il proprio setup utente, senza considerevoli ripercussioni sulle performance dell'insieme.

## La gestione dei Setup
Un Setup può essere : 

- Creato
- Salvato
- Duplicato
- Modificato

Tutte queste operazioni sono possibili dal nuovo modulo di Gestione Setup richiamabile da ogni sottosezione della scheda.
Esistono inoltre delle shortcuts in forma di menu o bottoniera per effettuare le principali operazioni (Salva, Apri).

## La SubSectionCommandBar
La SubSectionCommandBar è l'espressione evidente della presenza di Setup Utente che si manifesta nella visualizzazione di una bottoniera sul bordo inferiore delle sottosezioni nella quale è attivata.
La sua visualizzazione è in funzione dell'attributo "ShowCommandBar" che può assumere i seguenti valori : 

- Yes :  la SubSectionCommandBar viene sempre visualizzata
- No :  la SubSectionCommandBar non viene mai visualizzata (è comunque possibile accedere alle funzione della SubSectionCommandBar attraverso il sottomenù "Impostazioni.. : " del Popup del Tabsheet di Sottosezione)
- Auto (default) La SubSectionCommandBar viene visualizzata solo se esistono Setup Utente o Setup Multipli.


## Coesistenza con vecchie versioni di DEV
Nel caso in cui la nuova versione di Loocup sia installata con "vecchie" (antecedenti il 03/10/2006) versioni di DEV, la gestione di Setup Utente Multipli non sarà possibile ed inoltre occorrerà specificare "UserSetup=On" (come nei precedenti rilasci di Looc.up) sulle sottosezioni interessate poiché l'XML di definizione dei setup non è compreso nell'XML di definizione della scheda.

## Ripresa dei Setup da versioni precedenti
Purtroppo è cambiata la modalità di identificazione della sottosezione alla quale il setup appartiene.
Nei rilasci precedenti di Loocup il campo  MECOD1 veniva impostato come segue : 
 :  : PAR F(04)
<NomeMembroScriptScheda>_<TipoSottosezione>_<IdSottosezione>

Es :  ESE1B_MAT_MATSTILI che viene troncato a ESE1B_MAT_MATST
Oggi : 
 :  : PAR F(04)
<NomeMembroScriptScheda>/<IdSottosezione>

Es :  ESE1B/MATSTILI

Se si vogliono quindi conservare i Setup Utente preesistenti occorrerà intervenire manualmente sul file B£MEDE0F.
