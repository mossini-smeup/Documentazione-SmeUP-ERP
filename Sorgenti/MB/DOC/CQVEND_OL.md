## DOCUMENTAZIONE GENERALE

>Il modulo permette di gestire la valutazione dei Fornitori (VENDOR RATING) e di qualsiasi ente aziendale interno o esterno es :  Dipendenti, Clienti, centri di lavoro,ecc. o combinazione di oggetti Fornitore-Famiglia prodotti, Dipendente-Centro di lavoro,ecc.
Per ogni tipo di valutazione viene associata una struttura di valutazione che può prevedere dati statici e/o dinamici.
Il periodo di valutazione viene definito liberamente e può avere cadenza mensile/trimestrale/quadrimestrale,ecc.

_7_Esecuzione        
_3_ Struttura Indice
Verifica la composizione degli Indici codificati nella tabella CRM,
costruite le tabelle richieste (vedi Tabelle) serve a verificar la
correttezza della struttura di valutazione ottenuta.
 :  : INI **Struttura Indice**
 :  : CMD CALL CQVR60
 :  : FIN
### Gestione Indici Statici
Gestione della parte Statica degli Indici codificati.
La funzione permette di assegnare un punteggio all'oggetto di valutazione
per il periodo desiderato, determinando cosi la lista degli oggetti
valutati.
ES :  Valutazione Fornitori
    Assegnare un punteggio al fornitore a seguito di Questionari/visita
    ispettiva.
    Non di tutti i Fornitori presenti in anagrafica, si è interessati ad
    ottenere una valutazione, la discriminante avviene attraverso la
    presenza della parte Statica.
 :  : INI **Gestione Indici Statici
 :  : CMD CALL CQVR70G
 :  : FIN
### Duplicazione Indici Statici
La funzione permette la gestione di massa degli Indici Statici.
Es :  Riportare i fornitori valutati nel 1 trimestre nel trimestre successivo.
 :  : INI **Duplicazione Indici Statici**
 :  : CMD CALL CQVR90
 :  : FIN
### Cocntrollo Valutazione Statica/Dinamica
La funzione permette di controllare per un determinato oggetto di valutazione
la presenza o meno degli Indici Statici/Dinamici
Es :  Il programma consente di verificare rapidamente i fornitori che hanno
    consegnato nel periodo di valutazione considerato ma che non hanno una
    valutazione Statica.
 :  : INI **Controllo Valutazione Statica/Dinamica**
 :  : CMD CALL CQVR80G
 :  : FIN
### Interrogazione Rating
Interroga il risultato globale del valore dell'oggetto Valutato incrociando
i dati statici/dinamici.
 :  : INI **Interrogazione Rating**
 :  : CMD CALL CQVR64G
 :  : FIN
### Stampa Rating
Stampare il risultato globale del valore dell'oggetto Valutato incrociando
i dati statici/dinamici.
 :  : INI **Stampa Rating**
 :  : CMD CALL CQVR63
 :  : FIN
### Stampa Prospetto Rating ed emissione File PC
La funzione permette di generare un File sulle cartelle condivise del sistema
che alimenta una Macro di Excel (CQVEND.XLS) che si occupa della presentazione
grafica della Valutazione Fornitori standard (Vendor Rating).
Oppure di ottenere una stampa di controllo formato AS/400
 :  : INI **Stampa Prospetto Rating ed emissione File PC**
 :  : CMD CALL CQVR68
 :  : FIN
### Lancio Calcolo Indici Dinamici
Il programma permette di eseguire/schedulare la funzione di calcolo della
parte dinamica degli indici
 :  : INI **Lancio Calcolo Indici Dinamici**
 :  : CMD CALL IGIND0
 :  : FIN
### Storicizzazione Rating i Indici Dinamici
Il programma permette di storicizzare il risultato della valutazione
globale di un periodo mediante la scrittura di record sul file IGSTOR0F
con chiave specificata in tabella CRM e i valori contenuti fino al
livello indicato nella medesima tabella
 :  : INI **Storicizzazione Rating i Indici Dinamici**
 :  : CMD CALL CQVR65G
 :  : FIN

### Programmi prerequisiti
Definiti attraverso la gestione legami area/tema/sintesi sono i programmi
che determinano la base dati dinamica. I programmi che determinano la
base per la valutazione standard sono CQVEN*

- [Rating](Sorgenti/MB/DOC/CQVEND_01)

## DOCUMENTAZIONE PARTICOLARE
_4_Versione D5COSO 
- [Struttura D5COSO per memorizzazione indici](Sorgenti/MB/DOC/D5)
_4_Versione IGSTOR 
- [Indici &-x2f; report](Sorgenti/MB/DOC/IG)
