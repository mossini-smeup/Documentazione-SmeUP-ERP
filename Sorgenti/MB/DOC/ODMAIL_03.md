# Interazione con l'account IMAP
L'interfaccia IMAP prevede funzioni di interazione con i differenti componenti di un account :  account, folder, messaggi, header dei messaggi, componenti del messaggio
Ogni funzione prevede la possibilità di passare nel campo P i seguenti parametri : 

- S :  server IMAP
- U :  account
- W :  password dell'account suddetto

In alternativa questi parametri di collegamento possono essere definite nelle variabili Loocup espresse negli script in SCP_CLO tramite i seguenti nomi : 

- IMAP_SYSTEM
- IMAP_USER
- IMAP_PASSWORD

Qualora queste informazioni manchino quando venga richiesta un'operazione che preveda il collegamento al server, verrà presentata una dialog che permetterà di editarli

I parametri che possono esprimere nomi di folders possono esprimere anche un percorso che porta a subfolders secondo la seguente sintassi : 
INBOX.Subfolderlivello1.Subfolderlivello2

## Il servizio JA_EML
Il servizio che si occupa di interfacciarsi al server IMAP è il **JA_EML**
La funzione di interazione in questione è del tipo **F(INT;JA_EML** che poi è completata dai vari metodi che definiscono le vere e proprie "azioni" a disposizone.
I metodi sono i seguenti : 

- Visualizzazione lista folders come albero :  VIS.FLST
- Visualizzazione lista folders come matrice :  VIS.FLSM
- Contenuto folder :  VIS.FCNT
- Contenuto folder esteso (comprensivo degli attributi Smeup) :  VIS.FCNX
- Nomi attributi presenti nei messaggi del folder :  VIS.FCAN
- Attributi del folder :  VIS.FATR
- Contenuto messaggio :  VIS.MCNT
- Headers del messaggio :  VIS.MHDR
- Allegati del messaggio :  VIS.MATC
- Attributi del messaggio :  VIS.MATR
- Attributi del messaggio trasformati dal LOSER_33 :  VIS.TRM
- Attributi presenti nella chiave SM-UIKey :  VIS.MATK
- Messaggi filtrati per valore header :  VIS.MFAV
- Scrittura di un header del messaggio :  WRI.MHDR

- Trova messaggio :  MSG.FIND
- Elimina messaggio :  MSG.DEL
- Copia messaggio :  MSG.COPY
- Spostamento messaggio :  MSG.MOVE
- Registrazione messaggio :  MSG.REG
- Deregistrazione messaggio :  MSG.RED

- Trova allegato :  ATC.FIND
- Copia allegato :  ATC.COPY
- Eliminazione allegato :  ATC.DEL
- Apertura allegato :  ATC.OPN

- Connessione al server :  SRV.CON
- Chiusura connessione :  SRV.CLO
- Cambio connessione :  SRV.CHG

- Creazione folder :  FLD.CRT
- Eliminazione folder :  FLD.DEL
- Rinomina folder :  FLD.REN
- Attivazione listener su folder :  FLD.LSN

- Pulizia cache dati :  CAH.CLD
- Pulizia cache attributi :  CAH.CLA
- Pulizia cache folder :  CAH.CLF


## Funzioni sull'account
### Elenchi

- ELENCO FOLDER COME ALBERO :  F(INT;JA_EML;VIS.FLST) 1(;;[K1]) 2(;;[K2]) 3(;;[K3])
-- Parametri : 
--- K1= nome folder
--- K2= livelli di ricorsione
--- K3= numero di livelli di ricorsione nei subfolders
--- K4= filtro sul nome folder
- ELENCO FOLDER FILTRATI COME ALBERO :  F(INT;JA_EML;VIS.FLST) 1(;;[K1]) 2(;;[K2]) 3(;;[K3])  4([T4];[P4];[K4])
-- Parametri : 
--- K1= nome folder
--- K2= livelli di ricorsione
--- K3= numero di livelli di ricorsione nei subfolders
--- T4= tipo su filtro tipizzato
--- P4= parametro su filtro tipizzato
--- K4= filtro sul nome folder o codice su filtro tipizzato
- ELENCO FOLDER COME MATRICE :  F(INT;JA_EML;VIS.FLSM) 1(;;[K1]) 2(;;[K2]) 3(;;[K3]) 4([T4];[P4];[K4])
-- Parametri : 
--- K1= nome folder
--- K2= livelli di ricorsione
--- K3= numero di livelli di ricorsione nei subfolders
--- T4= tipo su filtro tipizzato
--- P4= parametro su filtro tipizzato
--- K4= filtro sul nome folder o codice su filtro tipizzato
- ELENCO FOLDER COME MATRICE CON ATTRIBUTI ESTESI :  F(INT;JA_EML;VIS.FCNX) 1(;;[K1])
-- Parametri : 
--- K1= nome folder


### Contenuti Folder

- CONTENUTO FOLDER FILTRATO PER VALORE ATTRIBUTO F(INT;JA_EML;VIS.MFAV) 1(;;[K1]) P([ATTRN]([ATTRV]))
-- Parametri : 
--- K1= nome folder
--- Parametro P : 
---- ATTRN= Nome attributo
---- ATTRV= Valore attributo
- MESSAGGI NON REGISTRATI NEL FOLDER F(INT;JA_EML;VIS.MFAV) 1(;;[K1]) P(SM-UIKey())
-- Parametri : 
--- K1= nome folder
--- Parametro P : 
---- ATTRN= Nome attributo (SM-UIKey è l'attributo delle chiavi Smeup di registrazione)
- MESSAGGI REGISTRATI NEL FOLDER F(INT;JA_EML;VIS.MFAV) 1(;;[Folder]) P(SM-UIKey(Key))
-- Parametri : 
--- K1= nome folder
--- Parametro P : 
---- ATTRN= Nome attributo (SM-UIKey è l'attributo delle chiavi Smeup di registrazione)
- ATTRIBUTI DI UN FOLDER F(INT;JA_EML;VIS.FATR) 1(;;[Folder])
-- Parametri : 
--- K1= nome folder
- ATTRIBUTI DEL CONTENUTO DI UN FOLDER F(INT;JA_EML;VIS.FCAN) 1(;;[K1])
-- Parametri : 
--- K1= nome folder



### Contenuti messaggio

- ATTRIBUTI MESSAGGIO F(INT;JA_EML;VIS.MATR) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- ATTRIBUTI MESSAGGIO VAGLIATI DA LOSER_33 F(INT;JA_EML;VIS.TRM) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- VALORI DELLE CHIAVI SMEUP F(INT;JA_EML;VIS.MATK) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- CONTENUTO MESSAGGIO F(INT;JA_EML;VIS.MCNT) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- ALLEGATI MESSAGGIO F(INT;JA_EML;VIS.MATC) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID


### Azioni sui Messaggi

- REGISTRAZIONE MESSAGGIO F(INT;JA_EML;MSG.REG) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- DEREGISTRAZIONE MESSAGGIO F(INT;JA_EML;MSG.RED) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- CANCELLAZIONE MESSAGGIO F(INT;JA_EML;MSG.DEL) 1(;;[K1]) 2(;;[K2])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
- COPIA MESSAGGIO F(INT;JA_EML;MSG.COPY) 1(;;[K1]) 2(;;[K2]) 3(;;[K3])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
--- K3= Folder di destinazione
- SPOSTAMENTO MESSAGGIO F(INT;JA_EML;MSG.MOVE) 1(;;[K1]) 2(;;[K2]) 3(;;[K3])
-- Parametri : 
--- K1= nome folder
--- K2= Message-ID
--- K3= Folder di destinazione
- INVIO MAIL F(INT;JA_EML;SEND) 1(;;[K1]) 2(;;[K2]) 3(;;[K3]) P(Testo messaggio)
-- Parametri : 
--- K1= Sender
--- K2= To
--- K3= Subject
--- Parametro P= Testo mail


### Azioni sulle cache

- PULITURA CACHE DATI F(INT;JA_EML;CAH.CLD) 1(;;[K1])
-- Parametri : 
--- K1= nome folder
- PULITURA CHACHE ATTRIBUTI F(INT;JA_EML;CAH.CLA) 1(;;[K1])
-- Parametri : 
--- K1= nome folder
- PULITURA CACHE FOLDER F(INT;JA_EML;CAH.CLF) 1(;;[K1])
-- Parametri : 
--- K1= nome folder



