# STAMPA DOCUMENTAZIONE INTERNA AI PROGRAMMI
# SCELTE
## FILE / LIBRERIA
Si deve specificare il file contenente i membri di cui si vuole produrre la documentazione. Se non si specifica la libreria il programma utilizzerà come parametro la lista librerie.
## INTESTAZIONE
E' possibile specificare la costante che verrà stampata su tutte le pagine della documentazione prodotta. Se non si specifica nulla viene assunto il contenuto  "**
DOCUMENTAZIONE TECNICA **".
Il dettaglio delle scelte si riferisce in particolare ai membri di programma RPG. Per altri membri si parlerà genericamente di documentazione generale.
## DOCUMENTAZIONE GENERALE
Tipo RPG : 
Tutte le righe con tipo colonna D (documentazione) che precedono la prima specifica di definizione del file.
Tipo TXT : 
Tutte le righe.
Tipo CLP : 
Tutte le righe di commendo dove i primi caratteri sono /*D.
## DOCUMENTAZIONE DI DETTAGLIO
Sviluppo delle routine e di tutte le righe con tipo colonna
D (Documentazione) nell'ordine con cui si incontrano.
Il corpo del programma, ovvero tutte le specifiche di calcolo che precedono la prima routine verrà chiamato MAIN.
## ELENCO ROUTINES
Stampa in ordine alfabetico di tutte le ROUTINE presenti nel programma.
Le routine sono riconosciute dal codice operativo BEGSR e si assume come loro descrizione l'ultima riga con tipo colonna D preceduta da R (Cioè RD*).
## ELENCO  "/COPY RICHIAMATE"
Stampa in ordine alfabetico di tutti i pezzi di programma che sono incorporati al momento della compilazione, con l'indicazione del file da cui sono ripresi.
## ELENCO PROGRAMMI RICHIAMATI
Stampa in ordine alfabetico di tutti i programmi richiamati con la descrizione specifica dell'oggetto.
N.B. Viene stampato come nome programma il contenuto del
"Fattore 2" senza apici se presenti. Se il richiamo di un programma si realizza mediante l'impostazione di una variabile, il richiamo non sarà decodificato.
## ELENCO FILES UTILIZZATI
Stampa in ordine alfabetico di tutti i files utilizzati con la decodifica e una breve descrizione del tipo di elaborazione.
## STRUTTURA PROGRAMMA
Viene stampata la sequenza delle routine decodificate nell'ordine con cui vengono eseguite dal programma, e con una forma di rappresentazione simile ad una "distinta scalare" al fine di rendere leggibile la struttura del programma.
### INCLUSIONE ROUTINES STANDARD
A richiesta vengono stampate anche le routine standard (riconosciute dal fatto di iniziare con il carattere £) e che normalmente non vengono stampate perchè di importanza secondaria (Ad. Esempio controllo formale della data Ecc.)
## MEMORIZZAZIONE RIFERIMENTI INCROCIATI
Vengono memorizzate in un file tutti i richiami di un programma a : 
- COPY
- Programmi
- File utilizzati
L'utente potrà accedere a questo file mediante l'apposita funzione per sapere ad esempio quali file sono utilizzati in un programma o quali programmi utilizzano una determinata COPY ecc.
Si possono impostare i limiti per nome ma soprattutto per TIPO.
Potremo in tal modo stampare la sola documentazione contenuta in testi (TXT) o in programmi RPG.
# COMANDI
F3  = Fine lavoro
F11 = Modifica dei parametri di esecuzione programma
