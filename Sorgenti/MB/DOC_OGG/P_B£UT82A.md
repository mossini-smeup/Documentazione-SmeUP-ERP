# FUNZIONI DI CONTROLLO SU SORGENTI

## OBIETTIVI
 Effettuare controlli/comparazioni tra sorgenti.
 I sorgenti specificati nel data entry, vengono salvati su un file di database,  interrogando il quale è possibile  procedere ai controlli voluti.

## OPZIONI
 I parametri richiesti sono di seguito specificati : 
 **- Libreria Sorgente        -**  se non specificata, si assume *LIBL
 **- File     Sorgente        -** Obbligatorio  
 **- Membro   Sorgente        -**  specificare un membro o in alternativa valorizzare  il campo Lista
 **- Lista    Membri          -**  è possibile specificare una lista di Membri Sorgente.
 **- Libreria Salvataggio     -**  se non specificata, si assume QTEMP
 **- File di  Salvataggio     -**  se non specificato, si assume B£UT82A0F
 **- Sostituz./Aggiunta Rec.  -**  specificare se si vuole aggiungere records al file o  sostituirli con i nuovi

## CAMPI FILE SALVATAGGIO
 I campi che vengono scritti sul file , sono i seguenti : 
 **- Libreria Sorgente        -**  Lunghezza  10  char
 **- File     Sorgente        -**  Lunghezza  10  char
 **- Membro   Sorgente        -**  Lunghezza  10  char
 **- Numero di Sequenza       -**  Lunghezza   6  char
 **- Data scrittura/modifica  -**  Lunghezza   8  char
 **- Dati di specifica pgm    -**  Lunghezza  100 char
