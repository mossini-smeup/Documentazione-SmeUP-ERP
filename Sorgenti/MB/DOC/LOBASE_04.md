# Informazioni generali sugli ambienti di Sme.up
- [Ambienti Sme.up](Sorgenti/MB/DOC/B£AMBI)
# Quali menù vengono presentati
Sono omessi i menù ACG e di sitema operativo.
In assenza della definizione di ambienti verrà caricato come menù inizale l'elenco di tutti i  tipi di menù esistenti.

Per la gestione degli ambienti vedere il programma B£UT55
Non è necessario che l'utente abbia il programma di avviamento che lo richiama perchè  LOOC.up legge comunque l'ambiente come definito in tabella B§1

# Tipologia delle azioni
Sono riconosciute e gestite le seguenti azioni dei tipi seguenti
##  =Chiamata ad un programma
Esegue il richiamo al programma richiesto.
## A=Azione ACG
Deve essere impostato il sistema informativo e l'azione da eseguire.     L'utente deve essere presente nell'architettura, se non fosse presente può essere     creato automaticamente accedendo al sistema informativo tramite il comando KUSOACG     Per errori fare riferimento alla documentazione di secondo livello sul messaggio di errore.
## M=Menù di SME_up
Il Menu è considerato un nodo. LOOC.up lo apre controllando l'eventuale ricorsione
## T=Titolo
Il Titolo è considerato un nodo, viene costruito soltando in presenza di azioni     valide al suo interno.     E' prevista una sola indentazione di livello, deve essere impostato nel Programma/Azione il carattere**L**seguito dal livello se si vuole identare più titoli.
## J=Funzione grafica client
Nel parametro si deve impostare una funzione del tipo F(xxx;yyy;zzz) 1 ecc
