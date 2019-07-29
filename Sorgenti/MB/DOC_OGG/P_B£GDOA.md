### COMPLETAMENTO SPECIFICHE INTERNE A UN PROGRAMMA RPG   . .   2
## LIMITI  CONSENTE LA LIMITAZIONE DEI CAMPI VIDEO DA PRESENTARE
# ELABORAZIONE FORMATI VIDEO
Questa funzione si propone di raccogliere tutte le funzioni di utilità tecniche legate al trattamento automatico di un formato video che si ottengono partendo da un oggetto.
Tali funzioni sono orientate a facilitare e automatizzare la produzione del software al fine di aumentarne la qualità e a produrre documentazione in forma automatica.
Si possono distinguere le seguenti funzioni : 
## AZIONE
### COSTRUZIONE /COPY PER SPECIFICHE I
Questa funzione costruisce un membro sorgente che descrive tutti i campi scelti a video nelle specifiche I. Tale membro potrà essere utilizzato per l'inclusione dopo la COPY MDV.
### COSTRUZIONE E COMPILAZIONE FILE DS ESTERNE
Questa funzione costruisce le specifiche di un file fisico e lo compila (senza membri). Tale file potrà essere utilizzato come DS esterna.
### COMPLETAMENTO SPECIFICHE INTERNE A UN PROGRAMMA RPG
Questa funzione legge i campi scelti a video. Scorre il membro
RPG scelto e usando le convenzioni descritte nel seguito costruisce le posizioni iniziali e finali dei campi. Il fine è quello di facilitare la costruzione delle strutture di memorizzazione parametri video lasciando libero l'utente di  aggiungere nuovi campi o modificare l'ordine, ecc.
Convenzioni
Si possono inserire alcuni caratteri prima della specifica I per condizionare il comportamento : 
/I   Individua l'inizio delle specifiche da trattere
/F   Individua la fine delle specifiche da trattare nnnd nnn  = lunghezza del campo
d    = numero di posizioni decimali
Il programmatore potrà pertanto scrivere specifiche del tipo seguente : 
/I   I*
I                                            CAMP02
I                                            CAMP01
I                                            CAMP03
/F   I*
Se dal formato video abbiamo la definizione dei campi CAMP01(alfanumerico di 5 caratteri) e CAMP03 (numerico di 4 con 3 decimali) avremo il seguente risultato : 
/I   I*
I                                        1    5 CAMP01
I                                        6    92CAMP02
I                                       10   133CAMP03
/F   I*
## ORIGINE
Definisce nome del file e libreria da cui dovranno essere ripresi i campi per la scelta
L'indicazione del membro è facoltativa e permette di limitare al solo membro scelto i campi da presentare.
## DESTINAZIONE
Indica il membro di aggiornamento o creazione a seconda della scelta. Il programma controlla la congruenza della scelta del nome del membro rispetto all'opzione di creazione o sostituzione per evitare errori che potrebbero cancellare membri importanti.
Il nome del membro se non specificato assume i seguenti valori in funzione della scelta : 
1.   Nome del file video con suffisso _P
2.   Nome del file video con suffisso _E
3.   Nome del file video
## CARATTERE IDENTIFICATIVO
Il carattere identificativo può essere usato come prefisso o suffisso sia unito che sostituito, al fine di caratterizzare e diversificare la struttura creata rispetto ai nomi utilizzati nel file video
## LIMITI
CONSENTE LA LIMITAZIONE DEI CAMPI VIDEO DA PRESENTARE PER LA SCELTA.
# SCELTA CAMPI
