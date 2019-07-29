# INTERFACCIA CONVERSIONI.
## OBIETTIVO
Permettere la conversione - aggiornamento di un FIle di dati da un'applicazione ad un altra. Viene impostato l'ambiente di origine; l'ambiente, l'applicazione e l'oggetto di destinazione.
Si costruisce secondo uno standard il programma da lanciare per la conversione specificata
## IMPOSTAZIONI
-    Codice ambiente applicativo destinazione
-   Applicazioni attive
-   Archivio di destinazione
-    Codice ambiente applicativo origine
## ALTRE CONDIZIONI
-    Conservare dati presenti in archivio destinazione
-    Membro destinazione
-    File origine S/36
-  S/36 XX.XXXXX in ££XXXXX
-  S/36  Y.XXXXX in ££XXXXX
-    Nome File origine
## FUNZIONI
/
Visualizza i parametri usati dalla funzione //
//
Imposta i parmetri specifici e chiama il B£CONV passandogli tali parametri
CONVERSIONI
Viene richiamata per la conversione del File o membro.
CREAZIONE POPOLAZIONE DATI
Non attiva
.................
## NOTE TECNICHE
Costruzione nome PROGRAMMA
1.   Il nome del programma da lanciare per la conversione è costruito automaticamente (se blanks) concatenando il codice dell'ambiente d'origine con i primi cinque caratteri dell'archivio di destinazione e con il codice dell'ambiente di destinazione.
## ESEMPIO
Nome programma
-    Destinazione             = SM   Appl. SMEUP
-    Applicazione             = BR   Dati di Base
-    Oggetto (Archivio)       = BRARES0F Articoli per ente
-    Origine                  = A2   ACG versione 2
-    Programma                = A2BRARESM
FIle origine S/36
1.   Se il File d'origine è di tipo S/36 è possibile specificare il tipo di denominazione usata : 
1  S/36 XX.XXXXX  in ££XXXXX
2  S/36  Y.XXXXX  in ££XXXXX
Automaticamente il file sarà ridenominato concatenando il prefisso ££ con i cique caratteri successivi al punto del file S/36. Con tale nome dovr'à essere  richiamato dal programma RPG che operea la conversione.
## ESEMPIO
-    Flle origine S/36        = OR.BRENT
-    File RPG                 = ££BRENT
