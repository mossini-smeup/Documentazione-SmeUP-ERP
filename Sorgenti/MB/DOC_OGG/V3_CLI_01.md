# CLI -  LISTENER DI FILE E CARTELLE
Implementa un ascoltatore di file e cartelle nel file system windows

## Il codice del listener
Il codice di questo listener è 01

## Cosa fa
Il listener controlla i file e le cartelle contenute in una cartella, che si specifica nella definizione del listener.


## Che struttura dati passa al server AS
Il listener genera una funzione F(EVT; < nome servizio > ; < nome metodo >) 1(J1; PATHFILE/PATHDIR; <nome file>) P(PATH( < percorso del file/cartella > ) )LISTENER( < codice listener >). Fatto questo legge l'XML che viene tornato dall'AS e reagisce di conseguenza.


- Se si modifica,cancella o crea un file il parametro dell'oggetto1 è PATHFILE
- Se si cancella o crea una cartella il parametro dell'oggetto1 è PATHDIR


Il percorso del file o della cartella sono specificati nel Parametro con la variabile PATH(<percorso>)

 T(Campo Funzione.metodo)
- File modificato :  DIR.MOD
- File o cartella cancellata :  DIR.DEL
- File o cartella creata :  DIR.NEW


## I parametri specifici
Oltre a gestire i parametri generali dei listener Loocup per i quali si rimanda alla documentazione in
- [Listeners di Loocup](Sorgenti/MB/DOC_OGG/V3_CLI)
il listener 09 gestisce anche i seguenti parametri riportati nel campo Parameter : 

- WaitTime :  definisce il tempo di attesa con cui viene scatenato il giro
- DirUrl :  definisce la cartella sulla quale mettersi in ascolto


 T(Sviluppi futuri)
- FileFilter :  Specifica quali file monitorare. Se blank monitora tutto il contenuto della cartella
- FileFoder :  Specifica quali cartella da monitorare
- Recursive :  specifica se monitorare anche il contenuto delle cartelle incluse
- MaxDepth :  Specifica la profonità del controllo
- ContentType :  Specifica il contenuto del file e come interpretarlo. qui si indica una configurazione di un questionario apposito.



## Esempi di impementazioni
 :  : PAR T(Desktop listener)
 :  : C.LST Cod="01.01" Txt="desktop file listener" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=[user.home]\Desktop;TESTXML=;Service=LOSER_11;Method=" LoadOnStartup="1" MaxDelay="10000" DebugMode="1" EnableLog="1"


 :  : PAR T(Listener di scansioni generate dalla stampante multifunzione CANON 3100C)
 :  : C.LST Cod="01.10" Txt="Immagini acquisite da multifunzione" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=[AZI.HOM.01]\Sviluppo\canon_3100c\Immagini;TESTXML=;Service=LOSER_11;Method=" LoadOnStartup="1" MaxDelay="10000" SendEvt="1" DebugMode="1" EnableLog="1"

 :  : C.LST Cod="01.11" Txt="Documenti acquisite da multifunzione" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=[AZI.HOM.01]\Sviluppo\canon_3100c\Documenti;TESTXML=;Service=LOSER_11;Method=" LoadOnStartup="1" MaxDelay="10000" SendEvt="1" DebugMode="1" EnableLog="1"

 :  : C.LST Cod="01.12" Txt="Fatture acquisite da multifunzione" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.dirlookup.DirectoryLookupJavaExternalListener;DirUrl=[AZI.HOM.01]\Sviluppo\canon_3100c\Fatture;TESTXML=;Service=LOSER_11;Method=" LoadOnStartup="1" MaxDelay="10000" SendEvt="1" DebugMode="1" EnableLog="1"

