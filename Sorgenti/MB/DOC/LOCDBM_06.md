# Gestire i file Excel - (XLS e XLSX)

Dalla release V3R3 di Loocup, Il modulo LOCDBM è in grado di leggere, in modo nativo, anche il contenuto di file Excel di tipo XLSX oltre che di tipo XLS.

I dati letti possono essere portati in un file su AS400, oppure salvati in un file PC in formato proprietario di Loocup.



# Come accedere ai dati
Nella scheda dell'oggetto Excel sono state aggiunte tre azioni nel gruppo **Utilizza**. Due modalità di accesso semplificato e una che consente lavorare su ogni singola colonna.
 - **Visualizza oggettizzato**  :  questa modalità utilizza la prima riga per oggettizzare i dati letti, ovvero, cerca di dare contenuto applicativo. In ogni colonna, mediante un'adeguata sintassi, si può specificare che tipo di dato è contenuto. Nel caso in cui la prima riga contenga dei dati, questi verranno comunque utilizzati per l'intestazione delle colonne, sarà pertanto necessario utilizzare un'altra modalità di lettura. Per i dettagli consultare la sezione **Informazioni tecniche**.
 - **Visualizza tutti i dati**   :  è una modalità semplificata per la lettura del contenuto del foglio excel. Legge l'intero contenuto del file e restituisce una matrice. Se sono presenti più fogli, questi vengono accorpati, uno dopo l'altro nella matrice restituita. La matrice restituita avrà un numero di colonne pari a quelle del primo foglio. Se i fogli successivi avranno più colonne, queste verranno perse.
 - **Visualizza dati - mod. avanzata** :  legge il contenuto del file ma è possibile scegliere il foglio ed eseguire operazioni più elaborate, ad esempio oggettizzare le colonne mediante uno script.

## la modalità avanzata.
La modalità avanzata consente di
 - selezionare il foglio da importare
 - saltare n righe
 - usare la prima riga utile come header
 - oggettizzare i dati mediante script - solo per sviluppatori

# Importare i dati su AS400
Nella scheda del file Excel, è presente la funzione **Importa in file AS400** :  consente di trasferire i dati letti in un file AS400.
Invocando questa funzione, comparirà un wizard nel quale si dovrà indicare
 - il nome del file di destinazione (obbligatorio)
 - il nome del foglio da importare, (facoltativo) se questo dato è mancante verranno importati tutti i fogli, ma il primo determinerà il numero di colonne del file di destinazione.
 - Numero di righe da saltare
 - Usa header per oggettizzare
 - Usa script per oggettizzare

NOTA :  se si attiva l'oggettizzazione mediante script, la sezione utilizzata è determinata dal nome del file di destinazione.


# Convertire un file Excel in un file S01
Nella scheda del file Excel è stata aggiunta la possibilità di esportare i dati in un file PC in formato proprietario di Loocup (S01).

Una volta convertito il file Excel in formato S01, lo si potrà consultare da Loocup, portare su AS400, convertiro il file Excel o generare dei report.

Consultare l'apposita scheda per i dettagli.


# Informazioni tecniche
In questa capitolo verranno raccolte le informazioni tecniche, utili agli sviluppatori e ad utenti con adeguate competenze.

## Sintassi per oggettizzare le colonne
Riportiamo qui uno stralcio del documento LOCDBM_03
- [Accesso ai dati - Importazione - tecnico](Sorgenti/MB/DOC/LOCDBM_03)
Descrizione_colonna(codice_colonna|oggetto|lunghezza[;decimali])
Dove
 - **Descrizione_colonna** :  è l'intestazione della colonna
 - **codice_colonna**  :  è il codice della colonna, utile nel caso si vogliano associare dinamismi
 - **oggetto** :  è l'oggetto SmeUp. E' possibile oggettizzare usando il valore di un'altra colonna mediante la sintassi standard [COD_COL_OGG]
 - **lunghezza** :  è il massimo numero di caratteri
 - **[;decimali]** :  nel caso di colonne numeriche è il numero di decimali. Informazione facoltativa.

Esempio 1
Clienti Esteri(CLIEXT|CNCLI|15)
Crea una colonna con descrizione Clienti Esteri, con codice CLIEXT di tipo CNCLI e di 15 caratteri.

Esempio 2
Fido(COLFIDO|NR|21;5)
Crea una colonna con descrizione Fido, con codice COLFIDO, ti tipo numerica di 21 cifre di cui 5 decimali.

## I servizi in gioco
L'accesso ai dati viene realizzato tramite due servizi interni, ovvero resi disponibili dal client Loocup.
Il servizio JA_00_39 consente l'accesso ai file XLS e XLSX.
Il servizio JA_00_19 può accedere a file XLSX solo se vengono configurati come fonti dati ODBC.



# Problematiche note

## Servizio JA_00_39
Non è in grado di leggere file molto grandi (indicativamente oltre 20MB), si consiglia di esportare in formato XLS o CSV e di accedere al file utilizzando il servizio JA_00_19.

## Servizio JA_00_19
 - Non è in grado di accedere a file di tipo XLSX, a meno che non venga configurata una fonte dati ODBC.
 - Non è in grado di leggere colonne contenenti dati numerici e alfanumerici :  in questo caso è necessario convertire il file in CSV prima di importarlo.
 - La prima riga del foglio Excel viene sempre considerata come riga di intestazione. Nel caso in cui contenga dei dati, verranno persi.



