# FUNZIONI JAVA-BASED DI GENERAZIONE PDF, MAIL, FTP
Permette di fare delle chiamate di azioni da As400 ad un qualsiasi Host in rete (PC, server ecc..), e di eseguire **utilities Java su As400**.
Azioni possibili :  fare FTP, mandare Email, eseguire Pgm in remoto, creare documenti PDF da spool.
# Prerequisiti di funzionamento e posibili malfunzionamenti
- [SmeNS - Network services](Sorgenti/MB/DOC/NSBASE_01)


# FUNZIONI IMPLEMENTATE
 Nota :  l'esecuzione di tutte le funzioni implementate è tracciata all'interno del file di trace tramite un SESSION ID (sid) formato da numero Lavoro + Data + Ora. Il file di Trace si trova nella cartella SMEUP/trace relativa al percorso d'installazione dell'IFS dell'AS400 e si chiama con NomeUtente+'_g53trace.log'.
## FTP
Esegue un FTP da e verso l'As400 rispetto ad un Host (server o Pc o altro As400 sul quale è installato e attivo lo Smens). Utente e Password As400 per eseguire l'FTP sono contenute nella tabella JA1 (obbligatoria per il funzionamento). Chiaramente deve essere attivo il servizio FTP su As400. Nei parametri vanno indicati i percorsi sia As400 che Pc. I metodi relativi alla funzione FTP sono i seguenti : 
### Metodo HOST_AS
£G53LI = Libreria AS di destinazione.
£G53AF = File AS di destinazione.
£G53AM = Membro AS di destinazione.
£G53BA = E' binario?
£G53SV = E' un SAVF?
£G53PL = Percorso libero in alternativa ai precedenti per depositare un file su IFS.
£G53NF = Nome file PC di origine.
£G53PA = Cartella PC di origine.
### Metodo AS_HOST
£G53LI = Libreria AS di origine.
£G53AF = File AS di origine
£G53AM = Membro AS di origine.
£G53BA = E' binario?
£G53SV = E' un SAVF?
£G53PL = Percorso libero in alternativa ai precedenti per prendere un file da IFS.
£G53NF = Nome file PC di destinazione
£G53PA = Cartella PC di destinazione.
## FTPSCP
E' l'unica funzione che non utilizza lo Smens, ma sfrutta un server FTP installato su un'altra macchina.

£G53PC = indirizzo FTP
£G53LI = Libreria AS di origine.
£G53AFF = File AS di origine
£G53AM = Membro AS di origine.
£G53BA = E' binario?
£G53F1 = Flusso Ini.
£G53F9 = Flusso Fin.
£G53PG = Exit per gestire la transazione ftp (quali istruzioni eseguire)
£G53UT = Utente di collegamento FTP
£G53PW = Password
£G53PL = Percorso libero
£G53FO = Name Format
£G53SL = Stampa Log
£G53PO = Porta

Per i dettagli sulla costruzione della exit si rimanda al prototipo appositamente creato : 
 :  : DEC T(MB) P(SMESRC) K(B£G53_XX)

Il campo £G53PC è di soli 15 caratteri.
In caso il nome server venga specificato come nome simbolico (e quindi potenzialmente oltre i 15 caratteri), si consiglia l'utilizzo del programma che converte il nome in IP : 
>C                   IF        %LEN(%TRIMR(NAM))>15
C                   CALL      'B£UT92CL'
C                   PARM                    NAM
C                   PARM                    IP
C                   ELSE
C                   EVAL      IP=NAM
C                   ENDIF
C                   EVAL      £G53PC=IP

## OPEN
Apre un file sull'Host, dove deve essere attivo e installato lo smens.

£G53PC = Host SMENS da chiamare perchè esegua la funzione. Preso dalla tabella **B§H**.
£G53NF = Nome file da aprire.
£G53PA = Cartella PC che contiene il file indicato in **£G53NF**.
## EXEC
Esegue un programma (EXE, BAT, VBS) sull'host dove deve essere attivo e installato lo smens.

£G53PC = Host SMENS da chiamare perchè esegua la funzione. Preso da B§H.
£G53NF = Nome file da eseguire.
£G53PA = Cartella PC che contiene il file indicato in £G53NF.
£G53PP = Eventuali parametri di lancio del programma indicato in £G53NF separati dal carattere ^.
## RAW
Chiamata libera (funzione tecnica per sviluppatori Java)
## PDF
Serve per _7_generare un documento PDF su As400 o sull'host. E' necessario creare un file con estensione .inv nell'Ifs dell'AS400 che contiene la forma di struttura e il testo contenuto (riferirsi alla documentazione specifica).
Compilando i parametri necessari, viene generato un documento PDF seguendo la logica sottodescritta : 

- viene cercato il file "inv" nella cartella di IFS specificata;
- le classi Java presenti nell'ambiente operativo Os400 si occupano della trasformazione del file inv il un file.pdf;
- il file Pdf viene creato nella cartella di IFS specificata.


£G53PR = Percorso IFS dove è presente il file di lavoro (il file .INV) che viene dato da elaborareal generatore PDF.
£G53PD = Cartella IFS dove verrà depositato il file pdf generato.
£G53DE = Nome del file pdf generato.
£G53DO = Indica se, una volta generato il PDF, deve essere eliminato il file indicato nella £G53PR.
£G53HV = Orientamento del documento :  orizzontale o verticale (il default).
£G53TF = Formato del foglio (A4, A3, etc.).
£G53CP = Si assicura, tramite la G80, che il percorso £G53PD esista.
£G53BT = Esecuzione della chiamata in batch.
£G53MP = Serve per passare alla classe di generazione del PDF una password di protezione sulla modifica
del file. Può assumere i seguenti valori : 

- ' ' :  la password non va passata e resta quella di default (gestita in file di configurazione con risalita prima sul campo T$JA1H della tabella JA1 e successivaente sul valore hard-coded nel componente)
- '*NONE' :  la password di protezione del documento viene DISABILITATA
- diverso da ' ' e da '*NONE' :  sul documento viene impostata la nuova password

## SPLPDF
 _7_Crea un Pdf   partendo da un file di spool che facoltativamente può utilizzare un file di layout per il documento(overlay). In questo caso, sempre in una cartella di IFS, è necessario avere un file di tipo pdf che funga appunto da layout.
Il flusso di questa funzione è il seguente : 

- viene generato uno spool tramite una qualsiasi stampa da AS400;
- lo spool viene trasformato in un file di estensione **.inv** (detto file intermedio poiché sta tra lo spool e il pdf) tramite specifiche informazioni di formato inserite all'inizio di ogni riga;
- il file "inv" viene creato nella cartella di IFS specificata;
- le classi Java presenti nell'ambiente operativo Os400 si occupano della trasformazione del file .inv in un file .pdf;
- il file Pdf viene creato nella cartella di IFS specificata.


E' possibile indicare un programma di aggiustamento (**B£G53P_x**) per intercettare la riga prima dell'emissione su PDF, allo scopo di formattarla in modo diverso dal default o per cambiare il testo contenuto.

All'interno di questa funzione posso anche inviare il Pdf direttamente via Email allegandolo a quest'ultima.

_r_ATTENZIONE :  se si utilizza la chiamata Batch (£G53BT) per la funzione/metodo SPLPDF/G_&_M assicurarsi che la coda batch abbia un solo lavoro attivo, altrimenti la creazione del pdf e l'invio della mail sarebbero contemporanee, col rischio che la seconda inizi ancor prima che l'allegato sia pronto.

### Metodo GEN
£G53SF = File di spool da cui prendere i dati.
£G53JA = Lavoro associato all spool.
£G53JU = Utente dello spool.
£G53JN = Numero job dello spool.
£G53SN = Numero dello spool.
£G53PR = Percorso IFS dove è presente il file di lavoro (il file .INV) che viene dato da elaborareal generatore PDF.
£G53PD = Cartella IFS dove verrà depositato il file pdf generato.
£G53DE = Nome del file pdf generato.
£G53FZ = Formattazione di riga (es. :   ROWCA-AC?BA). Per la sintassi di questa riga si rimanda alla documentazione contenuta nella sezione finale di questo documento intitiolata :  Sintassi SMEDG.
£G53FZ = Formattazione di riga (es. :   ROWCA-AC?BA). Per la sintassi di questa riga si rimanda alla documentazione contenuta in nel documento relativo al modulo NSPRINT.
£G53SK = Percorso IFS del file da utilizzare come foglio di "overlay".
£G53HV = Orientamento del documento :  orizzontale o verticale (il default).
£G53TF = Formato del foglio (A4, A3, etc.).
£G53OM = Disabilitazione offset modulo :  la sovrapposizione del modulo definito nel parametro £G53SK, imposta un margine assunto definito "offset", per tenere il modulo leggermente distante dal bordo formato foglio PDF; attraverso questo parametro è possibile disabilitare completamente questo bordo.
£G53ES = Indica se cancellare lo spool a generazione avvenuta.
£G53EP = Eventuale programma di aggiustamento.
£G53DO = Indica se, una volta generato il PDF, deve essere eliminato il file indicato nella £G53PR.
£G53CP = Si assicura, tramite la G80, che il percorso £G53PD esista.
£G53BT = Esecuzione della chiamata in batch.
£G53MP = Serve per passare alla classe di generazione del PDF una password di protezione sulla modifica
del file. Può assumere i seguenti valori : 

- ' ' :  la password non va passata e resta quella di default (gestita in file di configurazione con risalita prima sul campo T$JA1H della tabella JA1 e successivaente sul valore hard-coded nel componente)
- '*NONE' :  la password di protezione del documento viene DISABILITATA
- diverso da ' ' e da '*NONE' :  sul documento viene impostata la nuova password

generazione da uno spool appena creato (tutti i campi non specificati sono blanks)
 EVAL      £G53FU='SPLPDF'
 EVAL      £G53ME='GEN'
 EVAL      £G53SF='NOME SPOOL'
 EVAL      £G53JA='*'
 EVAL      £G53PR='SMEDOC/WORK'
 EVAL      £G53PD='SMEDOC/WORK'
 EVAL      £G53DE='NOMEPDF.PDF'
 EVAL      £G53FZ='ROWCA-AC?BA'
 EXSR      £G53



### Metodo G_&_M
£G53SF = File di spool da cui prendere i dati.
£G53JA = Lavoro associato all spool.
£G53JU = Utente dello spool.
£G53JN = Numero job dello spool.
£G53SN = Numero dello spool.
£G53PR = Percorso IFS dove è presente il file di lavoro (il file .INV) che viene dato da elaborareal generatore PDF.
£G53PD = Cartella IFS dove verrà depositato il file pdf generato.
£G53DE = Nome del file pdf generato.
£G53FZ = Formattazione di riga (es. :   ROWCA-AC?BA). Per la sintassi di questa riga si rimanda alla documentazione contenuta in SmeDG.doc allegato alle classi java.
£G53SK = Percorso IFS del file da utilizzare come foglio di "overlay".
£G53OM = Disabilitazione offset modulo :  la sovrapposizione del modulo definito nel parametro £G53SK, imposta un margine assunto definito "offset", per tenere il modulo leggermente distante dal bordo formato foglio PDF; attraverso questo parametro è possibile disabilitare completamente questo bordo.
£G53HV = Orientamento del documento :  orizzontale o verticale (il default).
£G53FR = Mittente mail.
£G53EM = Destinatari mail (multipli vanno separati da virgola senza spazi) - Campo ridotto (70)
£G53EE = Destinatari mail - Campo esteso (5000 - Non viene considerato se viene passatto quello ridotto)
£G53CC = Copia conoscenza mail (multipli vanno separati da virgola senza spazi) - Campo ridotto (70)
£G53CE = Copia conoscenza mail - Campo esteso (5000 - Non viene considerato se viene passatto quello ridotto)
£G53BC = Blind Copy mail (multipli vanno separati da virgola senza spazi) - Campo ridotto (70)
£G53BE = Blind Copy mail - Campo esteso (5000 - Non viene considerato se viene passatto quello ridotto)
£G53SJ = Oggetto mail.
£G53ES = Indica se cancellare lo spool a generazione avvenuta.
£G53DO = Indica se, una volta generato il PDF, deve essere eliminato il file indicato nella £G53PR.
£G53RC = Mail di conferma? Se si torna la ricevuta torna al £G53EM.
£G53EP = Eventuale programma di aggiustamento.
£G53CF = Eventuale file di configurazione di SMENS alternativo da usare (es :  per usare differenti mail server per l'invio).
£G53TF = Formato del foglio (A4, A3, etc.).
£G53CP = Si assicura, tramite la G80, che il percorso £G53PD esista.
£G53BT = Esecuzione della chiamata in batch.
£G53CA = Cancellazione allegato (in questo caso il file pdf generato) dopo invio mail.
£G53PT = Livello di Priorità della mail.
£G53UC = .
£G53CO = Conferma consegna; se valorizzato a '1' il mittente riceverà una mail di conferma alla CONSEGNA
£G53MP = Serve per passare alla classe di generazione del PDF una password di protezione sulla modifica
del file. Può assumere i seguenti valori : 

- ' ' :  la password non va passata e resta quella di default (gestita in file di configurazione con risalita prima sul campo T$JA1H della tabella JA1 e successivaente sul valore hard-coded nel componente)
- '*NONE' :  la password di protezione del documento viene DISABILITATA
- diverso da ' ' e da '*NONE' :  sul documento viene impostata la nuova password

della mail
## MAILTO / MAILTE
Permette di inviare una email da As400 (metodo As400) o da un Host indicato (metodo Blanks).    Fra i vari parametri ve ne sono alcuni duplicati con l'accezione ridotta ed estesa :  per questi è da considerare che la versione estesa viene utilizzata esclusivamente quando si utilizza la relativa funzione/metodo (MAILTE/G_&_ME/G_&_MEAS4). Inoltre è da considerare che l'utilizzo  parametri estesi, si basa ora sulla creazione di file temporanei posti nella cartella //SMEDOC/TEMP con un nome costruito secondo questo criterio :  i due caratteri di desinenza del campo ridotto "_" + numero job + ".txt" (es. nel caso dei destinatari avrei EM_xxxxx.txt).
Tali file vengono cancellati al termine di ogni elaborazione.
Per quel che riguarda l'utilizzo degli indirizzi è possibile indicarli in modo non esplicito tramite le seguenti regole : 

- *USER viene automaticamente cercato l'indirizzo collegato all'utente corrente. L'indirizzo viene ricercato nell'ente indicato nella B£U corrispondente all'utente.
-  _&_TipoOggettoParametroOggetto.Codice(.Funzione aziendale). In questo modo la G53 richiama la G85 che restituisce la lista degli indirizzi mail dell'ente specificato (es. _&_TAAGE.xx per la mail di un agente, _&_AZ.xx.2000 per mail aziendale dell'ufficio commerciale, _&_CNCLI.xx per la mail di un cliente)
- _&_SSNSL.CodiceSottosettore viene costruita la mailing list corrispondente alla definizione della lista di distribuzione.

**NOTA BENE** :  attualmente queste risalite vengono applicate solo se la relativa variabile inizia con le suddette codifiche, non è perciò ancora possibile indicare tali variabili in sequenza o all'interno di un elenco di mail esplicite.
Tra i parametri passati permette di indicare : 

- il from della mail
- a chi va inviata ( separata con "," o ";" per invio multiplo)
-- è possibile definire delle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail (uno per riga) e passarli come nel campo destinatario. Verranno copiati dal file i destinatari effettivi
- a chi si vuole inviare per conoscenza (CC)
-- è possibile definire delle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail (uno per riga) e passarli come nel campo destinatario. Verranno copiati dal file i destinatari in copia effettivi
- a chi si vuole inviare per conoscenza ad insaputa del destinatario (Bcc)
-- è possibile definire delle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail (uno per riga) e passarli come nel campo destinatario. Verranno copiati dal file i destinatari in copia nascosta effettivi
- il titolo della email
- il testo della email
-- se il campo contiene caratteri particolari o è molto esteso si può utilizzare il metodo di crearsi il testo in un file **IFS** e passare il parametro -TEXT-/percorsoIFS/nomefile nel campo **£G53TX**, in questo modo viene compilato il testo email esteso
-- è possibile anche inserire il contenuto in forma HTML. Analogamente a quanto visto per -TEXT-, è possibile, utilizzare lo stesso tag e costrudendo il file perchè il contenuto cominci con <html> e finisce per </html>, specificando poi il percorso come visto precedentemente
- allegato (con nome file e percorso relativo all'as400)
- allegato con trasformazione PDF (con nome file e percorso relativo all'as400 del file partenza e arrivo)
o **£G53TE**, testo esteso (30000) - Non viene preso in considerazione se viene passato il campo £G53TX

Nota di encoding : 
L'oggetto e il testo della mail sono in grado di gestire tutti i caratteri gestiti dalla codepage con cui il programma Sme.UP è in esecuzione.

### Metodo AS400
£G53FR = Mittente mail.
£G53EM = Destinatari mail (multipli vanno separati da virgola senza spazi).  E' possibile definiredelle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail(uno per riga) e passarli nel campo Destinatario.
£G53CC = Copia conoscenza mail (multipli vanno separati da virgola senza spazi).  E' possibile definire delle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail (uno per riga) e passarli nel campo Copia Conoscenza.
£G53BC = Copia Conoscenza Nascosta (multipli vanno separati da virgola senza spazi).  E' possibile definire delle liste di destinatari creando dei files dell'**IFS** contenenti elenchi di indirizzi mail (uno per riga) e passarli nel campo Copia Nascosta.
£G53SJ = Oggetto mail.
£G53ES = Indica se cancellare lo spool a generazione avvenuta.
£G53DO = Indica se, una volta generato il PDF, deve essere eliminato il file indicato nella £G53PR.
£G53RC = Mail di conferma? Se si torna la ricevuta torna al £G53EM.
£G53EP = Eventuale programma di aggiustamento.
£G53CF = Eventuale file di configurazione di SMENS alternativo da usare (es :  per usare differenti mail server per l'invio).
£G53TF = Formato del foglio (A4, A3, etc.).
£G53CP = Si assicura, tramite la G80, che il percorso £G53PD esista.
£G53BT = Esecuzione della chiamata in batch.
£G53CA = Cancellazione allegato (in questo caso il file pdf generato) dopo invio mail.
£G53PT = Livello di Priorità della mail.
£G53UC = .
£G53AT = Percorso IFS files attachment.
Per inviare allegati multipli è possibile indicare nel campo £G53AT il percorso di un file che contenga l'elenco degli allegati da inviare (in ciascuna riga il percorso di un file da allegare).
Per far capire alla £G53 che il file contiene un elenco di allegati e non è un allegato esso stesso, far precedere il percorso con -TEXT- .
£G53IT = Se valorizzato ad 1 anche quando nella B£2 l'ambiente è definito come ambiente di test  invia la mail ai destinatari previsti
£G53CO = Conferma consegna; se valorizzato a '1' il mittente riceverà una mail di conferma alla CONSEGNA della mail

Esempio di richiamo rapido
  EVAL      £G53FU='MAILTO'
  EVAL      £G53ME='AS400'
  EVAL      £G53TX='Testo della Mail'
  EVAL      £G53FR='Mittente@mail.it'
  EVAL      £G53EM='destinatario@mail.it'
  EVAL      £G53SJ='Oggetto'
  EVAL      £G53AT='/SMEDOC/Allegato.PDF'
  EXSR      £G53

### Metodo BLANK
Come il metodo AS400 ma l'invio viene eseguito da un PC (che **DEVE** avere Smens in esecuzione al momento della chiamata) indicato dal £G53PC e il file attachment £G53AT è un percorso relativo al PC in questione.
## INI
Possibilità di creare una lista di comandi all'interno di un file IFS AS400. Questo file viene poi letto dalla classe java che esegue, in sequenza, tutte le azioni in esso contenute; ne consegue che la classe java e, quindi, la STRQSH vengono richiamati una sola volta per eseguire tutte le azioni con evidenti vantaggi di prestazioni e tempi. La funzione INI serve per segnalare al programma che, da questo momento in poi, tutte le operazioni che vengono effettuate dalla G53 NON devono essere eseguite immediatamente ma scritte all'interno di un file .txt. Può ricevere : 

- £G53DO='1' se voglio che i file .inv vengano eliminati dopo la creazione del .pdf corrispondente altrimenti ' '
- £G53CA='1' se voglio eliminare i file .pdf, altrimenti ' '
- £G53SU='1' se voglio che la G53 aggiunga automaticamente un suffisso in coda al nome file .inv e .pdf
Questo è utile nel caso di allegati che si chiamano tutti con nome identico; nel caso di lista di azioni
eseguite tutte in serie alla fine, rischierei di allegare sempre lo stesso file...In questo modo
ho la possibilità di "differenziare" i vari allegati

## FIN
Serve per segnalare che ho finito la memorizzazione delle azioni e che posso eseguire tutto quello che è scritto nel file di lista dei comandi. Non richiede nessun parametro

# Indicatore £G5335
L'indicatore di ritorno £G5335 è significativo in base al tipo di operazione eseguita.
Se viene acceso durante un'operazione di trasferimento FTP, significa che il trasferimento FTP non è andato a buon fine.
Se viene acceso durante un'operazione di invio mail, significa che la mail è stata correttamente presa in carico dal server di posta. Non significa ovviamente che la mail è stata sicuramente spedita ne tantomeno ricevuta.

# Trace
La £G53 dispone di un meccanismo di trace molto potente.
La gestione del trace (attivazione/disattivazione/interrogazione/ecc.) è completamente disponibile nella scheda del modulo NSBASE (voce "trace").
Per approfondimenti si rimanda alla documentazione di tale scheda : 
- [Trace della £G53](Sorgenti/MB/DOC/B£LOGG_L52)

# Sintassi SMEDG
Il generatore genera file in formato PDF partendo da file di testo semplice in un formato definito. Tale formato che le righe dei file dati hanno degli headers che definiscono il tipo di riga, il formato del testo contenuto e l'eventuale file di overlay.
Gli headers hanno il seguente schema : 
>....+....1....+....2....+....3....+....4....+....5
TAGattributi............Testo o altri dati (in base al TAG)

I primi tre caratteri definiscono il tipo di operazione, i valori disponibili sono : 

- NPG  :  sta ad indicare un salto pagina;
- INC :  sta ad identificare l'include di un file di schema;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (non sensibile);
-- Posiz. 4 :  Dimensione Font (non sensibile);
-- Posiz. 5 :  Stile Font (non sensibile);
-- Posiz. 6 :  Colore Font (non sensibile);
-- Posiz. 7 :  Altezza riga (non sensibile);
-- Posiz. 8 :  Salta questa riga (non sensibile);
-- Posiz. 9 :  Colore bordi (non sensibile);
-- Posiz. 10 :  Colore sfondo (non sensibile);
-- Posiz. 11 :  Pagina da selezionare nel PDF multipagina (opzionale, default 1, cioè la prima pagina) ;
-- Dalla posizione 24 in poi va indicato il path del file da includere che verrà utilizzato come overlay di pagina, nel caso di file con estensione .pdf, dalla versione del 1/12/2004, verrà assunto interamente tale file come overlay. Nel caso di un PDF multipagina verranno scandite tutte le pagine ed aggiunte al documento. Se si fa riferimento ad un PDF multipagine è possibile utilizzare una specifica pagina di quest'ultimo indicando alla posizione 11. In alternativa il file può essere un file di testo composte da specifiche SmeDG, in questo caso le specifiche vengono importate;
-- La Posiz. 8 può servire (assegnandogli il valore F) per omettere lo spaziatore di default del bordo di sinistra e allineare il foglio di overlay al foglio che dovrà contenerlo;


- PAG :  sta ad indicare la specifica per importare un'immagine;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (non sensibile);
-- Posiz. 4 :  Dimensione Font (non sensibile);
-- Posiz. 5 :  Stile Font (non sensibile);
-- Posiz. 6 :  Colore Font (non sensibile);
-- Posiz. 7 :  Altezza riga (non sensibile);
-- Posiz. 8 :  Salta questa riga (non sensibile);
-- Posiz. 9 :  Colore bordi (non sensibile);
-- Posiz. 10 :  Colore sfondo (non sensibile);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo in cui verrà inserita l'immagine nel documento PDF (il separatore delle coordinate, nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre. Successivamente alle coordinate va inserito il percorso del file immagine da inserire. Se non sono presenti le coordinate l'immagine verrà agganciata a grandezza naturale in alto a sinistra e occuperà spazio in testata nel foglio, quindi il testo gestito con le specifiche ROW comincerà ad essere scritto successivamente allo spazio occupato dall'immagine;
- ROW :  sta ad indicare la definizione di una riga ed il testo in essa contenuto;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga (opzionale, default "A", cioè 10);
-- Posiz. 9 :  Colore bordi (non sensibile);
-- Posiz. 10 :  Colore sfondo (non sensibile);
-- Dalla posizione 24 in poi va indicato il testo da inserire nel documento PDF relativamente a quella riga; è possibile modificare inline le specifiche grafiche della riga, vale a dire modificare il tipo font, il colore, la dimensione, etc ad un certo punto della riga. Si può fare ciò inserendo nella parte racchiusa fra [[ e ]] il testo di cui modificare lo stile separato dalla sezione di definizione dello stile da un punto (.) (es. :  ROWC7AA8?JB. Testo iniziale riga [[ROWEF-Dd?JB.Testo secondo stile]]  ritorno allo stile iniziale [[ROWC5AM6?JB.Testo terzo stile]] ancora stile iniziale [[ROWCeCAf?JD.Testo quarto stile]]) .
-La Posiz. 8 può servire (assegnandogli il valore F) per omettere lo spaziatore di default di quattro carattere che viene premesso alla riga, rinunciando a questo offset di default, il testo verrà posizionato a partire dal bordo del foglio.


- BOX :  sta ad indicare la definizione di un rettangolo (BOX appunto) e l'eventuale etichetta in esso contenuto;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga (non sensibile);
-- Posiz. 9 :  Colore bordi (opzionale, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (opzionale, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e, opzionalmente, il testo dell'etichetta (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre;


- ROX :  sta ad indicare la definizione di un rettangolo con gli angoli arrotondati (Round bOX appunto) e l'eventuale etichetta in esso contenuto;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga (non sensibile);
-- Posiz. 9 :  Colore bordi (opzionale, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (opzionale, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e, opzionalmente, il testo dell'etichetta (il separatore delle coordinate) nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre;
-- Per una questione di raggio di curvatura degli angoli le dimensioni devono essere ambedue superiori a 8 unità, quindi EndX-StartX>8 e EndY-StartY>8.


- BTX :  sta ad indicare la definizione di testo racchiuso in un rettangolo;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga (non sensibile);
-- Posiz. 9 :  Colore bordi (opzionale, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (opzionale, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo da inserire nel documento PDF e che racchiude il testo indicato che viene indicato successivamente alle coordinate;


- RTX :  la sintassi è identica alla specifica precedente l'unica differenza è che, in caso di bordi visibili, questi risultano arrotondati;
-- Per una questione di raggio di curvatura degli angoli le dimensioni devono essere ambedue superiori a 8 unità, quindi EndX-StartX>8 e EndY-StartY>8.
-- LIN :  sta ad indicare la definizione di una riga diagonale;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga;
-- Posiz. 9 :  Colore bordi (non sensibile, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (non sensibile, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che identificano i punti di partenza e di arrivo della riga da inserire nel documento PDF;


- TXT :  sta ad indicare la definizione di un testo libero da inserire ovunque del documento PDF;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga;
-- Posiz. 9 :  Colore bordi (non sensibile, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (non sensibile, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY; che definiscono il punto di inserimento del testo nel documento PDF (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La s-scelta avviene in cascata fra i tre. Se si ha la necessità di riportare nel testo da scrivere come carattere normale di testo il carattere usato come separatore (quindi avendolo dichiarato "carattere speciale" nella specifica) i modi di procedere possono essere due : 
a) cambiare carattere di separazione nella logica precedentemente spiegata
b) utilizzare la stringa di sostituzione indicata nella sezione CARATTERI SPECIALI NEL TESTO


- BCD :  sta ad indicare la definizione di un'immagine Barcode da inserire nel PDF;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo nella pagina con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Barcode (opzionale, default O, cioè CODE39_EXT);
-- Posiz. 4 :  Dimensione Font (non sensibile);
-- Posiz. 5 :  Stile Font (non sensibile);
-- Posiz. 6 :  Colore Font (opzionale, default A, cioè Nero);
-- Posiz. 7 :  Altezza riga (non sensibile);
-- Posiz. 8 :  R per ruotare di 90° il barcode (opzionale, default NON R, cioè orizzontale);
-- Posiz. 9 :  Colore bordi (non sensibile);
-- Posiz. 10 :  Colore sfondo (non sensibile);
-- Posiz. 11 :  Testo del barcode ("." indica di inserire il testo. Qualunque altro carattere indica invece di ometterlo);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY;EndX;EndY; che delimitano il rettangolo che conterrà il barcode da inserire nel documento PDF (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.
--- Es. :  Per un barcode semplice : 
---- BCDCC-AC?BA.............130,340,200,420,9780201615883
--- Per un Barcode ruotato : 
---- BCDCCRACRBA.............230,140,330,320,9780201615883
--- Attenzione :  Il valore che viene passato al barcode deve essere compatibile con il tipo di barcode che si vuole visualizzare, quindi per l'EAN13 è prevista una stringa alfanumerica di 13 caratteri, per l'UPCA una stringa alfanumerica di 12 caratteri, etc.. Per maggiori informazioni sulla sintassi dei vari codici barcode, si rimanda a documentazione specializzata.
--- E' inseribile un barcode in una riga di tipo ROW con lo stesso meccanismo con cui si cambia lo stile inline (vedere spiegazione nella sezione relativa alla specifica ROW) :  quindi con la specifica [[BCDC5AM6?JB.9780201615883]] inserita in un punto di una riga di tipo ROW si ottiene il barcode nella riga di testo e, venendo inserito direttamente nella riga, non vanno espresse le coordinate assolute del foglio per il posizionamento.
--- Nel caso del barcode la posizione che gestisce il Tipo Font (posiz. 3) è utilizzata per identificare la codifica del barcode (CODE39, EAN13, UPC, etc.). Vedere alle sezione TIPO BARCODE i valori da utilizzare per utilizzare per visualizzare i vari tipi di barcode.


- RGB :  permette di specificare dei colori personalizzati da utilizzare nel documento che si vuole generare. I colori saranno utilizzabili dal momento in cui vengono definiti in avavnti nel documento che si vuole generare, quindi è consigliabile definirli ad inizio documento. Se dovessero essere ridefiniti, la modifica avrà luogo dal momento della loro ridefinizione in avanti. La sintassi è la seguente : 
-- RGBTR225G067B118
Dal momento della sua definizione sarà disponibile, oltre ai colori standard, il colore utilizzabile con l'indicatore T di valore (nella codifica RGB) :  255, 067, 118
-- LBV :  sta per LinkaBle Value. Permette di dichiarare una variable e valorizzarla per poter poi essere riferita nel corso del file .inv nel processo di creazione del PDF.
--- Es. :  dichiarazione di una variabile VAR1 con assegnazione del valore VALORE : 
---- LBVBC-BA?BA.............VAR1,VALORE
-- LKV :  sta per LinKed Value. Permette di fare riferimento ad una variabile dichiarata tramite la specifica precedente. Il funzionamento è identico alla specifica TXT con la differenza che, invece di stampare quanto riportato nella specifica, estrarrà il valore della variabile indicata. Le variabili possono essere riferite anche prima della loro dichiarazione.
--- Es. :  utilizzo della variabile VAR1 (come dichiarata nell'esempio della specifica precedente) : 
---- LKVCC-AC?BA.............200,300,VAR1
In posizione 200,300 verrà stampata la stringa VALORE con lo stile definito dalle specifiche CC-AC?BA.


- PGT :  sta ad indicare l'inserimento di una stringa riportante il numero di pagina e le pagine totali del documento nella forma NUMEROPAGINA/TOTALEPAGINE ;
-- Dalla posizione 3 alla 24 vanno inseriti i flag che definiscono il formato del testo con il seguente ordine (i valori possibili per ogni singolo flag sono riportati di seguito) : 
-- Posiz. 3 :  Tipo Font (opzionale, default "C", cioè Courier);
-- Posiz. 4 :  Dimensione Font (opzionale, default A, cioè 10);
-- Posiz. 5 :  Stile Font (opzionale, default "-", cioè  Normal);
-- Posiz. 6 :  Colore Font (opzionale, default "A" , cioè Nero);
-- Posiz. 7 :  Altezza riga (opzionale, default "A", cioè 10);
-- Posiz. 8 :  Salta questa riga;
-- Posiz. 9 :  Colore bordi (non sensibile, default "A", cioè Nero);
-- Posiz. 10 :  Colore sfondo (non sensibile, default "A", cioè Nero);
-- Dalla posizione 24 in poi vanno indicate le coordinate (assolute nel foglio) StartX;StartY; che definiscono il punto di inserimento del testo nel documento PDF (il separatore delle coordinate), nelle ultime distribuzioni può essere sostituito da ^(apice) o ,(virgola) anziché ;(punto e virgola). La scelta avviene in cascata fra i tre.


Qualsiasi riga di specifica ha due possibilità per essere ignorata dal parser, la prima utilizzando il simbolo X per specificare il flag Posiz.8, la seconda è commentando la riga mettendo in prima posizione il simbolo - o ; .
COORDINATE ASSOLUTE  : 
Le coordinate assolute, supportate in alcune specifiche sono espresse in punti tipografici. Di seguito sono riportate le dimensioni dei principali formati PDF generabili : 

- il formato A2 verticale ha come dimensioni :  larghezza 1190 , altezza 1684
- il formato A2 orizzontale ha come dimensioni :  larghezza 1684 , altezza 1190
- il formato A3 verticale ha come dimensioni :  larghezza 842 , altezza 1190
- il formato A3 orizzontale ha come dimensioni :  larghezza 1190 , altezza 842
- il formato A4 verticale ha come dimensioni :  larghezza 595 , altezza 842
- il formato A4 orizzontale ha come dimensioni :  larghezza 842 , altezza 595
- il formato A5 verticale ha come dimensioni :  larghezza 421 , altezza 595
- il formato A5 orizzontale ha come dimensioni :  larghezza 595 , altezza 421
- il formato LT verticale ha come dimensioni :  larghezza 612 , altezza 792
- il formato LT orizzontale ha come dimensioni :  larghezza 792 , altezza 612

Per dare un'idea della proporzionalità fra CPI e punti tipografici :  10 CPI corrispondono a 12,545664208490477228218892550631 punti, 12 CPI a 10,467760016547598883248141693027 punti e 15 CPI a 8,3481927710843373493975903614448 punti.
Di seguito sono riportati gli elenchi dei valori consentiti per ogni flag di formato : 

## STILE TESTO : 
NORMAL= "-";
ITALIC= "A";
BOLD= "B";
BOLDITALIC= "C";
UNDERLINE= "D";
BOLDUNDERLINE= "E";
BOLDITALICUNDERLINE= "F";
ITALICUNDERLINE= "G";
STRYKE= "H";
BOLDSTRYKE= "I";
BOLDITALICSTRYKE= "L";
ITALICSTRYKE= "M";

## SCALA DELLE DIMENSIONI (font, altezza righe, altezza barcode) : 
Le dimensioni nei tag della G53 segue la seguente scala : 
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz.
La scala è operativa dal valore 5 in avanti.
Oltre questa scala di valori esistono dei valori aggiuntivi gestiti.
Fra questi vengono gestiti dei valori grandi predefiniti ed equivalenti a 70, 90, 110, 130, 150 punti.
Tali valori sono rappresentati da : 

- é  :  equivalente a 70
- è  :  equivalente a 80
- à  :  equivalente a 90
- ò  :  equivalente a 100
- ù  :  equivalente a 110
Vengono inoltre gestite quattro unità di misura espresse in CPI che sono espresse attraverso i seguenti simboli : 
- - che rappresenta i 15 CPI, in alternativa usare il caratterer 4;
- § che rappresenta i 12 CPI, in alternativa usare il caratterer 3;
- * che rappresenta i 10 CPI, in alternativa usare il caratterer 2;
- & che rappresente i 6 CPI, in alternativa usare il caratterer 1.
E' anche possibile esprimere l'unità di misura, utile per l'altezza righe, di 6 LPI attraverso il seguente simbolo : 
- % rappresenta la dimensione di 6 LPI, in alternativa usare il caratterer 0 (zero);


## TIPO FONT : 
ARIAL= "A";
HELVETICA= "B";
COURIER= "C";
COURIER NEW= "D";
TIMES NEW ROMAN= "F";
VERDANA= "H";

E' possibile estendere la categoria dei fonts con dei files TTF  personalizzati. Per far ciò è necessario posizionare i files di font .ttf nella cartella Fonts contenuta in smedg. Tali files dovranno avere un nome che comincia con P1_ , P2_ e P3_ e saranno associati alle categoria fonts "Z " , "Y" e "X" rispettivamente. Per esemplificare :  posizionando nella cartella smedg/Fonts il file P1_ lucidabrightregular.ttf esso sarà riferibile come "X". Tali files di font dovranno avere la licenza d'uso. Per questioni di compatibilità è sempre valido quanto appena detto, ma è possibile,  con un meccanismo simile, definire quanti font personalizzati si crede. Definendo i files di fonts con un prefisso P[un carattere]_ si può richiamare il tipo font con il carattere scelto (es. :  se si chiama un file font PS_nomefile.ttf sarà richiamabile con S, se lo si chiama PN_nomefile.ttf sarà richiamabile con N, etc.).

## TABELLA DEI COLORI (font, sfondo, bordi) : 
NERO= "A";
BIANCO= "B";
ROSSO= "C";
VERDE= "D";
BLU= "E";
GIALLO= "F";
VIOLA= "G";
AZZURRO= "H";
GRIGIO= "I";
GRIGIOCHIARO= "J";
VERDEPASTELLO= "L";
ROSAPASTELLO= "M";
SALMONE= "N";
GIALLOCANARINO= "O";
PERVINCA= "P";
TRASPARENTE= "-";
 Oltre a questi è possilbile definire dei colori "custom" come spiegato nella spcifica RGB.

## ALTEZZA RIGA : 
 L'altezza riga, come anche la dimensione font, segue la seguente scala : 
 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz.

## TIPO BARCODE : 
CODE39= "A";     Alfanumerico lunghezza libero
UPCA= "B";      Solo numerico 12 cifre
UPCAH= "C";     Solo numerico 12 cifre
EAN13= "D";
EAN13H= "E";
EAN13B= "E";     Solo numerico 13 cifre
EAN13BH= "F";     Solo numerico 13 cifre
EAN13HH= "G";     Solo numerico 13 cifre
INTERLEAVED25= "H";   Solo numerico 10 cifre
INTERLEAVED25NT= "I";    Solo numerico 10 cifre
CODE128= "J";
EAN_SUPP= "K";
PDF417= "L";
POSTNET= "M";
PLANET= "N";
CODE39_EXT= "O";    Alfanumerico lunghezza libero
QRCODE= "Q";    Alfanumerico lunghezza libero

## SALTA QUESTA RIGA : 
X= salta questa riga

## CARATTERI SPECIALI NEL TESTO : 
Può rendersi necessario utilizzare nel documento dei caratteri che per qualche motivo non sono riportabili direttamente nel file INV. Es. :  i caratteri che nella specifica sono utilizzati come "caratteri speciali" (,;^ utilizzati come separatori di coordinata nelle TXT,BTX,BOX,etc.) oppure non supportati dall'encoding dei files su As400 (es :  il carattere Euro).
Tali caratteri possono essere sostituiti con una sintassi di questo tipo CHR(codice-ascii-carattere).
Ad esempio : 
- l'equivalente del carattere , è CHR(44)
- l'equivalente del carattere Euro è CHR(8364)
