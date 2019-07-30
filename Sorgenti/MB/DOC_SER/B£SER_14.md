 :  : HEA RESP(FD) STAT(10) USAG(FD) DTAG(20060113)
# OBIETTIVO
Fornire i dati necessari all'adempimento del Documento Programmatico per la sicurezza.

# FUNZIONI/METODI

## DGE Dati generali
Fornisce le informazioni relative a Sede, titolare trattamento, responsabile trattamento, responsabile della sicurezza e dei Sistemi informativi, incaricato alla custodia delle parole chiave e codici identificativi, incaricati al trattamento dati personali, incaricati al trattamento dei dati sensibili e giudiziari, terzi che trattano dati della società, non appartenenti in maniera diretta alla società stessa.
### DGE.SED
Questa chiamata al servizio ritorna una matrice contenente i dati realtivi alla Sede dell'azienda.
In _3_oggetto 1 è necessario passare l'azienda.
### DGE.TTR
Questa chiamata al servizio ritorna una matrice contenente i dati realtivi al titolare del trattamento dati per l'azienda.
Il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, parametro _1_X0.
In _3_oggetto 1 è necessario passare l'azienda.
### DGE.RES
Questa chiamata al servizio ritorna una matrice contenente i dati realtivi a : 
-responsabile trattamento;
il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, parametro _1_X1.
-responsabile della sicurezza e dei Sistemi informativi;
il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, parametro _1_X2.
-incaricato alla custodia delle parole chiave e codici identificativi;
il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, parametro _1_X3.
-incaricati al trattamento dati personali;
Si tratta di tutti i contatti di tipo **COL** che hanno _1_Stato=2** e _1_Livello=13/15**.
-incaricati al trattamento dei dati sensibili e giudiziari;
il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, nel parametro _1_X4.
-terzi che trattano dati della società, non appartenenti in maniera diretta alla società stessa;
Si tratta di tutti i contatti di tipo **COL** che hanno _1_Stato=2** e _1_Livello=13/15** e che hanno inserita in anagrafica _1_Zona=EXT.
In _3_oggetto 1 è necessario passare l'azienda.

## MFI Misure fisiche
Fornisce informazioni realtive agli ambienti in cui i dati vengono trattati.
Questa chiamata al servizio ritorna una matrice contenente il locale in cui sono presenti i dati e le misure fisiche che vi danno accesso.
il dato viene letto nella categoria dei parametri **AZI**+ **codice azienda**, nel parametro _1_X5.
In _3_oggetto 1 è necessario passare l'azienda.

## SSA Server e sistemi
Fornisce informazioni realtive agli ambienti e alle caratteristiche dei sistemi informatici utilizzati in azienda.
Questa chiamata al servizio ritorna una matrice contenente il cespite che costituisce sistema informatico, il luogo ove è posizionato e le sue caratteristiche tecniche.
Vengono scansionati i cespiti tramite la _2_£ICE filtrando su quelli con _1_classe implicita=A1,A2,A3,A5;
le caratteristiche vengono lette nella categoria dei parametri **A5D**+ classe implicita=A1,A2,A3,A5 nel parametro _1_C1.
In _3_oggetto 1 è necessario passare l'azienda.

## ELA Elaboratori e Apparecchiature di accesso per gli utenti
Fornisce informazioni realtive agli ambienti e alle caratteristiche degli elaboratori utilizzati dagli utenti.
Questa chiamata al servizio ritorna una matrice contenente il cespite che costituisce l'apparecchiatura, il luogo ove è posizionato e le sue caratteristiche tecniche.
Vengono scansionati i cespiti tramite la _2_£ICE filtrando su quelli con _1_classe implicita=A2;
le caratteristiche vengono lette nella categoria dei parametri **A5D**+ classe implicita=A2, nel parametro _1_C1.
In _3_oggetto 1 è necessario passare l'azienda.

## DCE Dispositivi di Connessione verso l'esterno
Fornisce informazioni realtive agli ambienti e alle caratteristiche dei dispositivi utilizzati dall'azienda.
Questa chiamata al servizio ritorna una matrice contenente il cespite che costituisce il dispositivo, il luogo ove è posizionato e le sue caratteristiche tecniche.
Vengono scansionati i cespiti tramite la _2_£ICE filtrando su quelli con _1_classe implicita=A4;
le caratteristiche vengono lette nella categoria dei parametri **A5D**+ classe implicita=A4, nel parametro _1_C1.
In _3_oggetto 1 è necessario passare l'azienda.

## CBD Censimento Banche Dati
Fornisce l'elenco delle banche dati utilizzate in azienda e le informazioni inerenti agli utenti autorizzati.
### CBD.CAR
Questa chiamata al servizio ritorna una matrice contenente l'elenco degli archivi cartacei presenti in azienda.
Gli archivi vengono letti dalla tabella **TA P0H**, nella quale sono presenti anche tutte le informazioni necessarie :  dati trattati, locale di collocamento, tipo di custodia, persona/e con accesso, metodo di accesso e trattamento dati.
In _3_oggetto 1 è necessario passare l'azienda.
### CBD.INF
Questa chiamata al servizio ritorna una matrice contenente l'elenco degli archivi informatici presenti in azienda.
Gli archivi vengono letti dalla tabella **TA P0G**, nella quale sono presenti anche tutte le informazioni necessarie :  caratteristiche, elaboratore, metodo di accesso, classe e funzione di autorizzazione.
In _3_oggetto 1 è necessario passare l'azienda.
### CBD.AUT
Questa chiamata al servizio ritorna una matrice contenente l'elenco delle persone autorizzate al trattamento dati della precedente sezione.
Vengono passati i codici Classe e Funzione letti dalla tabella TA XAW per l'archivio, e viene quindi eseguita la _2_£AUA** per ogni utente azienda presente nella **TA B£U** per il reperimento delle autorizzazioni.
In _3_oggetto 1 è necessario passare l'azienda.

## INF
Il gruppo di chiamate "INF" esegue tutte le azioni relative all'informativa in merito al Dpps : 
la funzione INF in particolare si occupa di recuperare tutti i membri di documentazione stampabili presenti nel file "**DOC_DPPS**" utilizzando la _1_/copy £G75**.
In _3_oggetto 1 è necessario passare il file di documentazione;
in _3_oggetto 2 la libreria (se diversa da SMEDEV).
_N.B. :  I membri che vengono estratti sono quelli la cui descrizione è maggiore di ciò che è indicato in _3_Oggetto 3.
### INF.INV
Questa chiamata al servizio ritorna una matrice contenente gli enti ai quali è necessario inviare la richiesta del trattamento dati inerentemente al Dpps.
L'estrazione avviente utilizzando la _1_/copy C£E, quindi leggendo i parametri; in particolare si occupa di andare a leggere nella **TAC£E** quale categoria è definita per i clienti, i fornitori ed i collaboratori e poi legge il sottosettore della **TAB£N** relativo. A quel punto controlla il parametro definito per stabilire se per l'ente va inviata la richiesta di trattamento, e se è positivo lo porta in matrice.
In _3_oggetto 1 è necessario passare la categoria di parametri per il tipo ente in questione;
in _3_oggetto 2 è necessario passare il parametro definito per il Dpps.
### INF.SCE
Questa chiamata al servizio ritorna un albero che elenca tutti gli enti di un tipo che hanno il valore del parametro di invio Dpps a "1". Il tipo viene passato tramite il pulsante delle "Scelte possibili".
Non sono necessari Oggetti in ingresso perché il servizio legge da una schiera che si calcola all'inizio è che poi confronta con la scelta effettuata.
### INF.SEL
Questa chiamata al servizio ritorna un albero che elenca gli enti selezionati dalla sezione "Scelte effettuate" caricati tramite il pulsante "Selezione".
In _3_oggetto 1 è necessario passare l'ente selezionato.


 :  : PRO.SER Cod="DGE.SED.1" Tit="Dati generali. Sede" Fun="F(EXB;B£SER_14;DGE.SED) 1(AZ;;-(O;;AZ;Azienda))"

 :  : PRO.SER Cod="DGE.TTR.2" Tit="Dati generali. Titolare trattamento" Fun="F(EXB;B£SER_14;DGE.TTR)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="DGE.RES.3" Tit="Dati generali. Responsabili" Fun="F(EXB;B£SER_14;DGE.RES)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="MFI.4" Tit="Misure fisiche. " Fun="F(EXB;B£SER_14;MFI)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="SSA.5" Tit="Server e sistemi. " Fun="F(EXB;B£SER_14;SSA)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="ELA.6" Tit="Elaboratori e Apparecchiature. " Fun="F(EXB;B£SER_14;ELA)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="DCE.7" Tit="Dispositivi di Connessione. " Fun="F(EXB;B£SER_14;DCE)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="CBD.CAR.8" Tit="Censimento Banche Dati. Archivi Cartacei" Fun="F(EXB;B£SER_14;CBD.CAR)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="CBD.INF.9" Tit="Censimento Banche Dati. Archivi Informatici" Fun="F(EXB;B£SER_14;CBD.INF)" Ref="DGE.SED.1"

 :  : PRO.SER Cod="CBD.AUT.10" Tit="Censimento Banche Dati. Autorizzazioni" Fun="F(EXB;B£SER_14;CBD.AUT) 1(TA;B£P;-(O;;TAB£P;Classe autorizzazione)) 2(;;-(O;;;Funzione aut.))"

 :  : PRO.SER Cod="INF.INV.11" Tit="Informativa Dpps. Invio informativa" Fun="F(EXB;B£SER_14;INF.INV) 1(TA;C£E;-(O;;TAC£E;Categoria parametri)) 2(;;-(O;;;parametro per invio))"

 :  : PRO.SER Cod="INF.SCE.12" Tit="Informativa Dpps. Scelta" Fun="F(TRE;B£SER_14;INF.SCE) 1(;;-(F;;;Nessun oggetto richiesto))"

