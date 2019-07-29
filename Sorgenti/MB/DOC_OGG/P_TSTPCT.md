# FUZIONI DI TRASFERIMENTO A PC
Crea un file elaborabile da PC. E' indispensabile avere nella libreria
SMEDAT il seguente file di riferimento :  B£PCT00W.
Le funzioni sviluppate sono : 
INZ :  PREPARA / INIZIALIZZA L'ARCHIVIO DI RIFERIMENTO
Mediante questa funzione viene inizializzato il file B£PCT00W : 
Se il file sopra citato esiste già nella QTEMP viene eseguito un
CLRPFM.
Se il file non esiste nella QTEMP viene fatto un DUPOBJ del file di riferimento presente nelle SMEDAT.
STE/SRI SCRITTURA TESTATA/RIGA
Per questa funzione è stato sviliuppato un solo metodo denominato FOE che permette di creare dei record compatibili
con EXCEL.
Ogni record è costituito da un campo lungo 2560 ottenuto concatenando i valori in ordine di indice schiera delle due
schiera di lavoro utilizzate £PC1 (valori Alfanimerici Lung. 200) e £PC2 (Valori numerici lung. 26,9). Ogni chiamata
scrive un record nell'archivio.
PRE :  PRESENTAZIONE DATI CARICATI
Esegue un DSPPFM del file di riferimento presente in QTEMP.
TRA :  TRASFERIMENTO FILE
Esistono attualmente due metodi di trasferimento :  BATCH e Interattivo.
nel primo caso vengono utilizzati i parametri passati dalla /COPY, nel secondo caso si visualizza una finestra in cui
sono pre-compilati i parametri passati dalla /COPY con possibilità di aggiunta o modifica.
FUNZIONE CAMPI : 
£PCTCS :  Identifica il numero di colonne sinificative del file che si stà costruendo.
£PC1 :  Schiera di valori alfanumerici di lunghezza 256 (200 elem.) £PC2 :  Schiera valori Numerici di lunghezza 26,9 (200
elem.) £PCTST :  Mettendo non bianco questo campo viene effuttuata la chiamata al PC support e la conseguente apertura
dell'applicazione Win ricevente il file.
£PCTCA :  Viene specificato in questo campo la cartella su AS/400 che conterrà il file .CSV da trasferire  su PC.
£PCTNF :  Viene indicato il questo campo il nome del file da creare.
£PCTAS. Accetta o meno la sostituzione del file presente nella cartella specificata.
