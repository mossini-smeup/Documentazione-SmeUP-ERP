## FORMATI VIDEO
# GESTIONE ARCHIVI FORMATO GUIDA
OBIETTIVO
Gestione degli archivi del data base.
. SCELTE
= visualizza la lista per gestire i file selezionati;
2 = visualizza la lista  per gestire i membri selezionati.
. LIBRERIA
E' la libreria che contiene gli archivi da gestire.
. FILE
E' il file di cui si vogliono gestire i membri.
. MEMBRO
Indica il nome del membro da gestire.
. LIMITI
Permettono di definire le parzializzazioni per caricare la lista
# GESTIONE ARCHIVI LISTA FILE
OBIETTIVO
Gestione dei file del data base.
. LIBRERIA
Nome della libreria a cui appartengono i file da gestire.
. S (SELEZIONE OPZIONI)
C = visualizza la lista dei campi appartenenti al file selezionato;
L = visualizza la lista delle viste logiche del file selezionato;
M = visualizza i membri del file fisico selezionato;
R = ricostruisce i campi del file selezionato;
S = attiva il giornale;
D = visualizza le dipendenze e i collegamenti dei campi del file selezionato;
= modifica i parametri relativi al giornale del file
selezionato;
E = disattiva il giornale.
. FILE
Nome del file da gestire;
. DESCRIZIONE
Descrizione del file (dato informativo);
. NUM. MEMB.
Indica il numero del membro;
. LUN. KEY
Lunghezza del campo chiave;
. LUN. RECORD
Lunghezza del record relativo al file selezionato;
. RECORD INIZIAL.
Numero di record inizializzati;
. S
- Y = giornale attivo;
- N = giornale non attivo;
. NOME GIORNALE
Nome del giornale per il salvataggio del file selezionato;
# GESTIONE ARCHIVI LISTA MEMBRI
OBIETTIVO
Gestione dei membri del data base.
. LIBRERIA
Nome della libreria a cui appartengono i file da gestire.
. S (SELEZIONE OPZIONI)
= modifica alcuni parametri relativi al file selezionato;
5 = visualizza alcuni parametri relativi al file selezionato;
K = aggiorna il record relativo al file selezionato;
V = visualizzazione dei dati contenuti nel membro fisico;
C = comprime i dati contenuti nel membro fisico;
S = salvataggio del membro selezionato.
. MEMBRO
Nome del membro da gestire.
. FILE
Nome del file a cui appartiene il membro.
. NUM. RECORD ATTIVI
Indica il numero di record attualmente attivi.
. NUM. RECORD CANCELLATI
Indica il numero di record cancellati.
. OCCUPAZIONE
N° di Megabytes occupati dal membro selezionato.
. PROGR. PRERIORGANIZZAZIONE
Nome del programma di preriorganizzazione.
. SUPPORTO SALVATAGGIO
Nome del supporto di salvataggio del file selezionato.
# GESTIONE ARCHIVI DETTAGLIO MEMBRI
OBIETTIVO
Gestione dei parametri relativi al membro selezionato.
. LIBRERIA
Nome della libreria a cui appartiene il file da gestire;
. FILE
Nome del file da gestire.
. MEMBRO
Nome del membro relativo al file selezionato.
. CARATTERISTICHE
- N° record :    attivi;
cancellati;
- Occupazione :  n° di megabytes occupati dal membro.
. DATI DI SALVATAGGIO
- Espressione condizionamento :  condizione per eliminare i record durante la riorganizzazione;
- Programma :  nome del programma di preriorganizzazione;
- Supporto :  nome del supproto di salvataggio;
- Libreria :  nome della libreria in cui effettuare il salvataggio;
# GESTIONE ARCHIVI DETTAGLIO FILE
OBIETTIVO
Gestione dei parametri di salvataggio relativi al file selezionato.
. LIBRERIA
Nome della libreria a cui appartiene il file da gestire;
. FILE
Nome del file di cui si vuole attivare il giornale.
. GIORNALE
- File :  nome del file di giornale;
- Libreria : nome della libreria in cui risiederà il file di giornale.
