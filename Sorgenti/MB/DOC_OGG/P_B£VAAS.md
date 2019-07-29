# GESTIONE VALORI ASSUNTI
# OBIETTIVO
Permettere il monitoraggio di tutti gli ogetti necessari all' installazione di un modulo o di una applicazione. .
# PREREQUISITI
E' necessario scrivere un programma sorgente in cui sono contenute le informazioni relative agli oggetti critici, le informazioni devono essere cablate tramite una tabella a tempo di compilazione utilizzando un tracciato fisso per ogni oggetto.
Il nome del programma e' cosi' composto : 
XXXXXXYYYY
XXXXXX = Applicazione o Modulo
YYYY   = _VAS (Valore Fisso)
I tracciati da usare per gli oggetti Sono  : 
Tipo Oggetto "SET" verifica e creazione settore tabella
2         3         4         5         6         7
1234567890123456789012345678901234567890123456789012345678901234567890
SET SetSS Descrizione                                              FPC
Tipo Oggetto "STC" verifica e creazione campo struttura tabella
1         2         3         4         5         6         7
1234567890123456789012345678901234567890123456789012345678901234567890
STC Set   Seq Campo  Descrizione          Tp Lgh D Tabe. Ob Nc Fil FPC
Tipo Oggetto "TEL" verifica e creazione elemento di tabella
1         2         3         4         5         6         7
1234567890123456789012345678901234567890123456789012345678901234567890
TEL SetSS Elemento        Descrizione          Dati Iniziali       FPC
Tipo Oggetto "TEV" Modifica valore campo elemento di tabella
1         2         3         4         5         6         7
1234567890123456789012345678901234567890123456789012345678901234567890
TEV SetSS Elemento        Campo  OP Valore 1        Valore 2 (Pre) FPC
Tipo Oggetto "OBJ" Controllo Oggetto
1         2         3         4         5         6         7
1234567890123456789012345678901234567890123456789012345678901234567890
OBJ Oggetto    Libreria   Tipo       Membro                        FPC
Le posizioni dalla 68 alla 70 sono comuni a tutti i tracciati ed identificano  : 
Posizione (68)  : 
E = Deve essere presente almeno un elemento
D = Il file deve contenere almeno un record
Posizione (69)  : 
V = Verifica (solo Controllo)
C = Crea Se Mancante
M = Modifica (se presente)
Posizione (70)  : 
* = è un commento non esegue nulla
# FORMATO GUIDA
Dal formato guida e' possibile  selezionare l'Applicazione o il modulo di cui si vuole controllare gli oggetti critici.
Le opzioni possibili sono  : 
G = Gestione
Permette di gestire i valori che vengono presentati a SUBFILE
A = Applicazione
Effettua l'applicazione di tutti quegli oggetti di cui e' stata rilevata o la mancanza o il disallineamento.
E = Solo le eccezioni
Se imputato il SUBFILE successivo contiene solo gli oggetti di cui e' stata rilevata o la mancanza o il disalineamento.
T = Tutti
Se imputato il SUBFILE successivo contiene tutti gli oggetti da monitorare .
# FORMATO LISTA
Contiene l'elenco degli oggetti critici ed i loro dati di completamento.
Opzioni disponibili  : 
= Immissione
Opzione disponiibile solo sulla testata dell' oggetto in modalita' di gestione.
Permette di inserire i dati di relativi all'oggetto.
2 = Modifica
Opzione disponibile solo sulle righe dati dell' oggetto in modalita' gestione.
Permette di modificare i dati relativi all' oggetto.
3 = Copia
Opzione disponibile solo sulle righe dati dell' oggetto in modalita' gestione.
Permette la copia dei dati dell' oggetto selezionato che saranno successivamente attribuiti ad un' altro oggetto.
4 = Cancellazione
Opzione disponibile solo sulle righe dati dell' oggetto in modalita' gestione.
Permette di cancellare dalla lista l' oggetto selezionato .
X = Applicazione
Opzione disponibile solo sulle righe dati dell' oggetto in modalita' di applicazione.
Permette di effettuare l' applicazione delle condizioni rilevate per l' oggetto.
Tasti funzione Disponibili  : 
F12=Precedente
Permette di tornare al formato guida.
F13=Ripetizione
A partire dal primo record del SUBFILE riprende l' opzione e la duplica su tutte le righe successive.
F14=Aggiornamento dati
Applica in effettivo le modifiche apportate ai dati tramite l'opzione
"2".
N.B. :  Effettua la modifica del programma sorgente con i dati relativi agli oggetti critici dell' applicazione o del modulo e successivamente effettua la compilazione.
# TABELLE COLLEGATE
