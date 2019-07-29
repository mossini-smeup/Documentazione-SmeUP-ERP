## OBIETTIVO
Gestire la suddivisione di quantità in 15 possibili dettagli.
L'esempio più immediato è lo sviluppo degli ordini in taglie.
## STRUTTURA DELLE INFORMAZIONI
I dati vengono registrati in un unico archivio scomposti per tipo riga e con un massimo di 15 valori (Taglie, Colori, Varianti ecc). Il significato di tali valori è definito nella tabella C£Q. Gli sviluppi si scompongono per contenitore (il cui significato è fissato) ed ogni riga si distingue per due codici (Es. ordine e riga)
Esempio
OV   ORD001 RIG001  OR   10   12   35
OV   ORD001 RIG001  SP   4         35
!                   !    !    !    !
!                   !    *--------------> Sviluppo quantità
!                   *--> OR=Ordinato SP=Spedito Ecc.
*----------------------> OVE=Ordini di vendita ORA=Ord.acquisto
## FORMATI VIDEO
## FORMATO GUIDA
Azione
Il significato delle azioni è prefissato. E' descritto nella tabella *CNSQ solo a scopo di descrizione e documentazione.
G    =    Gestione della riga
La gestione potrà essere una immissione, variazione, annullamento. La colonna da modificare è definita dalle azioni di  comportamento descritte in seguito.
I    =    Interrogazione
C    =    Calcolo dei totali per i tipi riga scelti
Contenitore
Specifica il significato delle chiavi e distingue i gruppi di righe.
Può essere codificato nella tabella B£G ma i significati gestiti sono prefissati : 
ORV  =    Ordini di vendita
ORA  =    Ordini di acquisto
...
Codice 1 / Codice 2
Significato variabile definito dal codice contenitore
Tipo sviluppo
Struttura del controllo 1/5
Tipo
E' il tipo della riga con significato prefissato dalla applicazione. Codificato a scopo descrittivo nella tabella
*CNTQ.
Avremo ad esempio : 
OR = Ordinato
SP = Spedito
AC = Accantonato
..
Azioni
M = Modificabile
R = Restituire
Formula
Una qualsiasi formula trattata dal programma di gestione delle formule
Condizione
>0 = Forzatura a 0 dei valori negativi
## PREREQUISITI
-    Tabella C£Q
