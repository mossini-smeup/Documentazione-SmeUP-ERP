 :  : HEA RESP(MAEOLI) STAT(10) USAG(FORFED) DTAG(20180612) ORAG(180000) AMBT(TE)


# La versione Roma Revision 2

Prendendo come base di conoscenza la NWS 2344, andiamo ad approfondire i temi tecnici.

## Nuova gestione dell'accesso ai file - PROVIDER_PATHS
Con la Rev. 2 è stata centralizzata la gestione delle autorizzazioni nell'accesso ai file, pertanto il provider accederà ai soli percorsi (e alle sottocartelle) specificate nella variabile PROVIDER_PATHS. Se il provider dovrà accedere a cartelle sull'IFS, anche queste dovranno essere indicate nei provider paths. Le uniche cartelle a cui il provider accede di default sono : 
 * Cartelle LOOCUP_ (cartella installazione)
 * Variabile *TMP, variabile Windows %TMP%
 * Variabile *TEMP, variabile Windows %TEMP%
 * Variabile *APPDATA, variabile Windows %APPDATA%
 * Variabile del provider PROVIDER_UPDATE_FOLDER

Sulla pagina di debug è stato aggiunto un pulsante per testare rapidamente i provider paths. Nel caso in cui il provider tenti di accedere a dei percorsi a cui non è autorizzato, comparirà un pulsante per scaricare tutti i path vietati.
**NOTA**
Nei PROVIDER_PATHS porre attenzione alla presenza di eventuali variabili :  il loro utilizzo è sempre sconsigliato.
Le variabili sono risolte nell'ambiente del provider e possono essere diverse da quelle dell'utente o cambiare in funzione dell'ambiente.
A fronte di problemi nell'accesso ai file, diventa complesso capirne il motivo.
Per tale motivo **i percorsi vanno sempre indicati in modo assoluto**.
Oltre al test rapido, è possibile compiere dei test puntuali :  scorrendo lungo la pagina si troverà un riquadro con scritto <b>verifica raggiungibilità file e cartelle</b> in cui si potrà testare l'accesso ad un file e/o a una cartella.
## La pagina di debug
La pagina di debug dovrebbe essere consultata appena si configura un nuovo provider o si riscontrano malfunzionamenti.
La pagina di debug risponde a http(s)://indirizzo_del_provider:porta/debug. Ad esempio https://localhost:9090/debug
da questa pagina è possibile : 
 * verificare se il provider è attivo
 * verificare i parametri di configurazione
 * verificare se accede all'AS400
 * verificare la coda server
 * verificare se non è connesso al sistema Sme.UP
 * verificare la raggiungibilità di un server AS400
 * verificare la raggiungibilità di cartelle e / o file in maniera puntuale
 * testare le credenziali di un utente

## Business continuity
Nella Rev. 1 si faceva riferimento al parametro --sbs, con cui era possibile specificare il sottosistema a cui lo Sme.UP Provider si aggancia.
Questo gli consente di gestire meglio le situazioni in cui il sottosistema viene chiuso.
Ci sono situazioni in cui questo tipo di controllo non è affidabile, ad esempio se a causa di problemi legati a un sottosistema, venga deciso che i lavori del provider debbano girare in un altro sottositema.
In questo caso il provider non sarà in grado di ricollegarsi all'AS400, perchè testerà sempre il sottosistema indicato nel parametro --sbs.
Senza parametro invece, il provider passerebbe da un sottositema all'altro in modo trasparente.
Si consiglia pertanto di rimuovere tale impostazione.
### Cosa succede quando cade il sottosistema
Quando cade il sottosistema, tutte le fun che il provider richiede all'AS400 vanno in timeout dopo 5 minuti.
Quando il provider ha delle letture che vanno in timeout chiude la connessione.
Nel caso della master, poi prova a ricollegarsi.
Se va in timout anche la connessione, la connessione viene chiusa e viene tentata un'altra connessione.
Se il sottosistema viene chiuso in maniera controllata, tutti i lavori che vengono immessi dal provider risultano congelati, appena il sottosistema riparte, tutti i lavori sottomessi si avviano, quindi eseguono la connessione, a cui però segue una disconnessione.
All'avvio del sottosistema è possibile che si abbiano tantissimi lavori sottomessi, ma si chiudono tutti nel giro di pochi minuti.
Rimarranno soltanto quelli della sessione master e dei plugin.

## Flussi batch e Server
 * Flussi Batch :  chiusi i Loocup batch che non si collegano a Sme.UP Provider dopo 20 tentativi.
 * Flussi batch :  portato timeout di connessione da 100 a 200 secondi.
 * Reso univoco nome batch.
 * Gestione parametro per forzare la pulitura della coda server in avvio.
 * Gestione parametro per preservare la coda server (in chiusura le code vengono distrutte)
## Log e file temporanei
 * la cancellazione avviene senza bloccare l'avvio.
## Revisione log
Sono stati aggiunti dei parametri nel wrapper che consentono di definire : 
 * Numero file di rolling (--
 * Periodo mantenimento
 * Cartella dove salvare i file (--logpath)
E' stata inoltre limitata la lunghezza del singolo messaggio a 128Kb

## Altre migliorie
 * Possibilità di produrre XML di matrice in formato JSON
 * Risorse remote :  controllo validità sessione remota e riconnessione del client in caso di riavvio provider.
 * migliorate informazioni su sessioni (data / ora avvio, raggiungibilità internet, indirizzi schede di rete, nome macchina)
 * Timeout lettura XML portato a 300 secondi anche per sessioni secondarie
 * Estesa la history di LoocUp
 * Velocizzati flussi interattivi
 * Wizard :  corretta gestione valori con apici singoli e/o doppi

## Servizi interni
### JA_00_39 - scheda oggetti J7 XLS/XLSX
 Segnalato errore quando si accede a un file Excel con estensione non congruente al formato.
### A_00_05
 * introdotto calcolo MD5
 * lettura di file con conversione in base 64 (GET.B64)
 * validazione ricorsiva (VAL.XSD)
 * Velocizzata procedura cancellazione di cartelle (DEL.ALL)
### Accesso DB esterni, componente DBM servizi JA_00_19 - JA_00_39
 * Importazione da file CSV :  portata lunghezza nomi colonne da 8 a 10 caratteri.
 * Controllato caso in cui il numero di decimali fosse indicato come minore di zero.
 * Possibilità di mantenere campi di tipo data senza conversione in formato SmeUp DATAMAPPING(RAW).
 * L'aggiornamento dei campi con LOSER_33 avviene solo se presente lo script.
### JA_00_07
Con la il metodo VER.SCP è possibile eseguire il controllo sintattico degli script di un'intera libreria.
