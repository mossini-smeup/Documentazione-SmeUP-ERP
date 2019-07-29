_3_Diverse modalità di Accesso ai dati e di Importazione
_7_(creato in data 03-09-2006) 
_7_(aggiornato in data 07-09-2007) 
_7_(aggiornato in data 16-12-2008)


# Note generali sull'importazione
Se la tabella sorgente contiene caratteri particolari questi verranno sostituiti dal segno "_".
Sono ammessi solo i numeri, le lettere, il segno "_" e il segno "£" .

Se il nome della tabella sorgente è più lungo di 8 caratteri questo verrà troncato. Nella descrizione del file creato su AS400 verrà riportata il nome della tabella sorgente per esteso, privato dei caratteri con codice ascii minore di 32 o maggiore di 122.

[http://www.asciitable.it](http://www.asciitable.it)



# Accedere o importare da CSV


## Cos'è il formato CSV?
E' un formato di file testuale (visualizzabile anche tramite un semplice editor di testo) utilizzato solitamente per lo scambio di dati fra fogli di calcolo(per esempio Excel) o database. I singoli campi di dati sono separati da una carattere definito a priori (a volte la virgola, a volte il punto e virgola, a volte il simbolo di pipe...).

### Come oggettizzare le colonne
NOTA :  Questo paragrafo è valido anche per l'accesso a file Excel
Per facilitare la consultazione dei dati è possibile oggettizzarli, cioè definire a quale oggetto SmeUp corrispondono.
Questa operazione consiste nel definire, nella prima riga del file le caratteristiche della colonna.
La sintassi da utilizzare è la seguente : 
Descrizione_colonna(codice_colonna|oggetto|lunghezza)
esempi : 
 T(Esempi : )
- _7_Cod.Ogg. master(XXCDMA|[XXTPMA]|15)** definisce una colonna con codice **XXCDMA**, con descrizione **Cod.Ogg. master** di tipo **[XXTPMA]** e lunga 15
- _7_Tempo esecuzione(F2TEAS|NR|11;0) definisce una colonna con codice _F2TEAS_, con descrizione **Tempo esecuzion** di tipo **NR** con 11 cifre di cui 0 decimali


NOTA :  Questa sintassi che segue è  obsoleta anche se il componente la sà riconoscere

Nome_colonna | Oggetto_SmeUp | Numero_caratteri | DescrizioneColonna.
 T(Esempi : )
- _7_CodCli|CNCLI|15|Clienti** definisce una colonna con codice **CodCli**, di oggetti CN CLI, lungai 15 caratteri
- _7_XXPREZ|NR|21-6|Prezzo Unitario**definisce una colonnacon codice **XXPREZ**,  numerica, composta da 21 cifre di cui 6 decimali


 T(Casi Particolari)
- Sono ammesse tutte le combinazioni, con l'accortezza che se una caratteristica non viene specificata bisogna mantenere il separatore : 
-- Se ad esempio si desidera definire il codice e la lunghezza la sintassi da usare è la seguente :  _R_Testo||30000
-- Se ad esempio si desidera definire il codice e la descrizione la sintassi da usare è la seguente :  _R_Testo|||Testo libero
-- Se indico solo il codice posso utilizzare la segunte sintassi :  **Codice**


## Come accedere ad un file CSV

- Aprire il file CSV tramite un editor di testo per individuare il carattere di separazione tra le colonne ( in futuro sarà forse possibile visualizzare un anteprima in Looc.Up) e se il file contiene una prima riga con i nomi delle intestazioni dei campi.
- Selezionare il file CSV
- Indicare il _7_carattere separatore csv (di default viene preso il punto e virgola)
- se presente la riga con le intestazioni segnare il campo _7_Nomi colonne in prima riga.
-- se si desidera oggettizzare le colonne modificare la prima riga se contiene i nomi delle colonne o ggiungerla rispettando la sintassi espressa al capitolo **Come oggettizzare le colonne**
- Modificare la _7_ampiezza campi destinazione (E' consigliato portarla ad un valore che tenga conto della dimensione delle colonne per evitare che i campi vengano troncati). Questo valore viene usato nel caso in cui non sia stata definita la larghezza della colonna nell'intestazione.
- Utilizzare la funzione F(EXB;JA_00_19;MAT.CSV) 1(J1;PATHFILE;path_file_csv_da_importare) P(da definire in funzione delle caratteristiche del file).


La funzione creata va posta in una sezione o subsezione di tipo EXB.

**NOTA :   per la creazione della funzione da utilizzare esiste un apposito wizard.**

### Esempio di accesso ad un file CSV
Per testare l'accesso ai dati di un file in formato CSV, copiare le ter righe seguenti in un file di testo e salvarlo con estensione CSV.
 :  : PAR
CodiceCliente|CNCLI|15;Descrizione|**|35;Data|D8DDMMYY|8
C0001;Primo cliente;12092005
C0002;Secondo cliente;24082006


Dopo aver creato il file secondo la sintassi espressa sopra utilizzare la seguente funzione, inserendola in una apposita scheda : 

F(EXB;JA_00_19;MAT.CSV) P(FILE(C : \TEMP\NOME_DEL_FILE.CSV) SEPA(PunVir) HEAD(1) NMAXROW(-1) )

TERMINARE
Aprire la scheda del servizio JA_00_19 e selezionare la sottoscheda esempi
 :  : DEC T(V3) P(ASE) K(JA_00_19) D(Importazione e accesso ai dati) I(D) O(D)


## Come importare un file CSV?
L'importazione condivide con l'accesso ai dati i primi 5 punti.
Compiute tali operazioni si procede con le seguenti : 

- Creare (se necessario) una libreria su AS in cui verranno salvati i file creati durante l'importazione
- Indicare nel tab _7_Destinazione_AS400 il nome della libreria di destinazione dei file
- Avviare la procedura di Import tramite il tasto OK


**NOTA : ** Utilizzando il servizio JA_00_19 la procedura di importazione avviene in modo batch. Va in questo caso configurata appositamente la chiamata al servizio.


## Accedere o importare da un file file Excel
L'accesso ad un file in formato Excel può avvenire sia direttamente, sia mediante il salvataggio in uno o più file in formato CSV.

## Come oggettizzare le colonne
In maniera analoga al formato CSV si possono oggettizzare le colonne del floglio Excel da importare.
Riferirsi al paragrafo **Comme oggettizzare le colonne** del capitolo **Accedere o importare da CSV.

### Accesso diretto al file.
Mediante i metodi MAT.XLS o EXP.XLS si accede direttamente al file.
Per creare una matrice è necessario fornire il nome del file ed il foglio da cui attingere i dati.
L'esportazione invece necessita di definire il file e la destinazione su AS400. La mancanza del foglio porta all'esportazione su AS400 di tutti i fogli.


### Salvataggio del file in formato CSV
Prima di importare i dati da un file excel è necessario salvare i dati in CSV.  Per far ciò si apra il foglio EXCEL e tra le opzioni possibili nella voce di menù SALVA CON NOME c'è il salvataggio come CSV. Non preoccuparsi di eventuali messaggi di warning e salvare il file in una cartella che poi sia facile da ricordare per indicarla nel campo _7_Singolo File o _7_Tutti i file nella directory del componente DBM.

### Come importare un file CSV partendo da un file Excel con più fogli di lavoro
La procedura da utilizzare per importare un file excel con più fogli di lavoro inclusi è uguale alla precedente con la particolarità che per ogni foglio
presente è necessario salvarlo con un nome CSV differente spostandosi man mano sul foglio da esportare. Se tutti i fogli vengono salvati nella stessa cartella è possibile poi importarli facilmente con un singolo comando indicando non più il singolo file CSV da importare ma tutta la cartella specificandola nel campo _7_Tutti i file nella directory del componente.

### Problematiche note
Esistono varie problematiche legate a BUG dei driver ODBC-JDBC : 
 - le colonne che contengono valori di tipo diverso, ad esempio numerici e alfanumerici, non restituiscono correttamente uno o più tipi. Se ad esempio nella colonna sono presenti in maggioranza valori alfanumerici non vengono restituiti i valori numerici. La soluzione è di esportare il foglio in formato CSV e poi di importarlo. NOTA :  forzare le colonne di tipo solo testo non ha alcun effetto.
 - non è possibile accedere a documenti protetti da password se non sono aperti in Excel.
 - durante il processo di esportazione non è possibile apportare modifiche al foglio excel
 - la prima riga è sempre considerata di intestazione
 - le celle contenenti formule non vengono valutate correttamente :  salvare il foglio in formato CSV e importarlo.
 - le celle contenenti valori numerici senza virgola possono venire restituiti come numeri terminanti con ".0". Salvare il foglio in CSV e poi importarlo.
 - Non è possibile accedere a fogli con nomi contenenti i seguenti caratteri : 
 -- " - apice doppio
 -- ! - punto eclamativo
 -- [ - parentesi quadra aperta
 -- ] - parentesi quadra chiusa
 -- { - parentesi graffa aperta
 -- } - parentesi graffa chiusa
NOTA1 :  l'apice singolo, il ?, il | (pipe), la / e la \ non sono ammessi come nomi dei fogli.

NOTA2 :  è consigliato limitare il set dei caratteri a lettere, numeri e "_".

Maggiori dettagli nel documento seguente (in inglese)
[ http://support.microsoft.com/default.aspx?scid=kb;en-us;257819]( http://support.microsoft.com/default.aspx?scid=kb;en-us;257819)

## Accesso o importazione di dati da database ORACLE
DA FARE

## Accesso o importazione di dati da database ACCESS
Mediante i metodi MAT.ACC o EXP.ACC si accede direttamente al file.
 T(Vanno specificate le seguenti informazioni : )
- iil percorso del file di access, indicandolo o nell'oggetto 1 (J1-PATHFILE-nome_file.MDB) o nel parametro FILE.
- il nome della tabella a cui accedere.


## Accesso o importazione da database che supportano l'ODBC
DA FARE

## Accesso o importazione da database che supportano il JDBC

Per debug, ci sono funzioni che permettono di

- visulizzare l'elenco delle tabelle
F(EXB;JA_00_19;INF.JDB) P(TPIMP(02) JDBCDRV(<driver>) JDBCCON(j<jdbc-url>) JDBCUSR(<user>) JDBCPWD(<pass>) JDBCALLTAB(1) LIB(W_SCM)  INFOT(TABLES)) SS(Context(JA_00_19/MDB) CGr(EXB) )

- visualizzare il contenuto di una tabella in matrice : 
F(EXB;JA_00_19;MAT.JDB) P(JDBCDRV(<driver>) JDBCCON(<jdbc-url>) USER(<user>) PASS(<pass>) TAB(<tabella>) NMAXROW(100)) SS(Context(JA_00_19/MDB) CGr(EXB))
