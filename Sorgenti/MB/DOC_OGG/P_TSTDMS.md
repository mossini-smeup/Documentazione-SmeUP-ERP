## COPY PREVISTE NELLA FUNZIONE <£DMS>    . .   3
# GESTIONE MESSAGGI APPLICATIVI
## OBIETTIVO
Avvicinare l'UTENTE FINALE alla diagnostica applicativa, uno strumento che se ben utilizzato aiuta a capire meglio i
problemi che la gestione del Sistema Informativo Aziendale puo' causare.
Per poter realizzare l'obbiettivo la funzione £DMS e' stata applicata a due diverse aree e precisamente : 
-    All'elaborazione dei dati in modo interattivo
All'UTENTE FINALE verra' fornita una completa e dettagliata informazione sulla messaggistica applicativa evidenziata
dai controlli formali effettuati sui dati immessi a video.
-    All'elaborazione dei dati in modo differito;
Le funzioni utilizzate in modo differito avranno un tabulato che segnalera' all'UTENTE
FINALE le anomalie riscontrate durante l'elaborazione dei dati.
N.B. Il tabulato potra' elencare fino ad un massimo di 100 anomalie per elaborazione.
## FUNZIONI
B£DMS1CL  reperimento messaggio
B£DMS1    visualizzazione messaggi
Un programma interattivo a finestre per la visualizzazione dei messaggi di primo livello,da dove e' possibile
richiamare per ognuno diessi il messaggio di secondo livello.
- finestra messaggi di primo livello
- finestra messaggi di sec. livello
. COMANDO OS/400 "CHGMSGD"
Record video per la manutenzione del messaggio e dei suoi attributi. La manutenzione e' permessa solo ad utenti con
classe *PGMR o *QSECOFR.
B£DMS2    stampa messaggi
Un programma batch per segnalare le anomalie riscontrate durante l'elaborazione differita dei dati.
## COPY PREVISTE NELLA FUNZIONE <£DMS>
£DMSE     Definizione delle schiere di lavoro
£DMSI     Definizione delle variabili di lavoro
£DMS      Composta dalle seguenti routine : 
£DMSC1
Dichiarazione e inizializzazione delle variabili
2 £DMSC2
Se il reperimento avviene da Msgf AS/400 : 
Memorizzazione del messaggio e del Msgf in £D1
Memorizzazione dei valori associati al messaggio in £D2
Se il reperimento avviene da Pgm RPG : 
Memorizzazione del codice messaggio (PGM) in £D1
Memorizzazione del testo del messaggio (PGM) in £D3
3 £DMSC3
Visualizzazione o stampa dei messaggi memorizzati
4 £DMSC4
Visualizzazione del primo messaggio applicativo  memorizzato
5 £DMSC5
Reperimento messaggi applicativi 6 £DMSC6
Concatenazione automatica variabili variabili associate al messaggio
## COME UTILIZZARE LA FUNZIONE
1) Dichiarare : 
. con la COPY £DMSE  le schiere di lavoro;
. con la COPY £DMS le strutture necessarie al funzionamento, che sono qui brevemente riassunte : 
la routine di inizializzazione delle
variabili;
2 la routine di memorizzazione; 3 la routine di gestione a video o su stampa dei messaggi memorizzati;
4 la routine di gestione a video del primo messaggio di errore;
(Solo per applicazioni interattive) 5 la routine di reperimento del messaggio applicativo messaggio di errore; 6 la
routine di concatenazione delle variabi- li associate al messaggio di errore
2) Richiamare la routine di inizializzazione delle variabili di lavoro : 
. Se si sta sviluppando una funzione BATCH, la routine andra' richiamata una sola volta e dall'inizio del programma,
nella fase delle operazioni preliminari.
. Se si sta sviluppando una funzione ON LINE, la routine andra' richiamata ogni volta che si inizieranno per la
videata in gestione, i con trolli formali sui dati immessi a video.
3) Ad ogni anomalia, con il richiamo alla apposita routine, si memorizzera'il messaggio e le sue caratteristiche.
4) Infine : 
. Per i programmi ON LINE : 
Dopo aver effettuato i controlli, sara' richiamata la routine per l'emissione del primo messaggio di errore.
Solo a richiesta dell'UTENTE FINALE, (per esempio attraverso un tasto comando) sara' richiamata la routine per la
gestione interattiva dei messaggi.
(Preimpostando il parametro di entrata con il valore ONLINE "V").
. Per i programmi BATCH : 
La routine per la stampa dei messaggi, sara'richiamata una sola volta e alla fine dell'elaborazione.
(Preimpostando il parametro di entrata con il valore BATCH "S").
## DATI TECNICI SULLE STRUTTURE
. COPY ----> £DMSE
Sono definite tutte le schiere di lavoro.
£D1 : 
Numero elementi.... :  100 da 17 bytes
Struttura elemento. :  CCCCCCCMMMMMMMMMM (C=Codice messaggio    (Dalla 1 alla 7)) (M=Message file AS/400 (Dalla 8 alla
17))
Esempio : 
....5...10.....17
BAS0020MSGBA
BAS0030MSGBA
£D2 : 
Numero elementi.... :  100 da 45 bytes
Struttura elemento. :   nn XXXX nn XX ..
(nn= lunghezza fisica variabile) (X = Variabile)
Regola inserimento. : 
. nn
(Spazio + dimensione a due caratteri)
. XXXX
(Spazio + Variabile)
(Dalla 1 alla 45)
Esempio : 
nn XXXXXX nn XXXXXXXXXXXXXXX
921010 30 SMEUP
....5...10...15...20...25...30...35...40...45
06 921020 30 SANTA ROMEA SPA
£D3 : 
Numero elementi.... :  100 da 80 bytes
Struttura elemento. :  PGMnnnnXXXXX...........X (PGM=I primi 3 caratteri dovranno essere sempre 'PGM'; cio' servira'
alle routines per identificare un messaggio gestito internamente al programma)
(nnnn=Saranno i caratteri identificativi del messaggio d'errore; Per default farli coincidere con la posizione del
messaggio all'interno della schiera)
(X..X=Sara' il vero e proprio testo di errore)
Esempio : 
....5...10...15...20...25...30...35...40...45
PGM0001Codice non trovato in archivio
PGM0002Data formalmente errata
. COPY ----> £DMSI
Sono definite le variabili di lavoro.
.    £DMS1M
(Testo 1° messaggio di errore)
.    £DMS1L
(Messaggio di 1° livello restituito dalla retrive)
.    £DMS2L
(Messaggio di 2° livello restituito dalla retrive)
.    £DMSST
(Concatenazione variabili associate al singolo messaggio)
. COPY ----> £DMSC1
E' la routine di inizializzazione delle variabili.
£D : 
Puntatore elemento di schiera.
£D1 : 
Schiera codice messaggio. Se il reperimento avviene da un Membro messaggi AS/400 contiene anche il rispettivo Msgf.
£D2 : 
Schiera valori associati al messaggio.
Utilizzata solo se il reperimento avviene da un membro messaggi AS/400.
£D3 : 
Schiera codici e testi messaggi di errore.
Utilizzata solo se il reperimento avviene dall'interno di un pgm RPG.
£DMSNR
Valore incrementato ad ogni registrazione, per sovrapporlo poi al puntatore £D ogni qualvolta si voglia indicare un
elemento di schiera.
£DMSTP
Tipo reperimento messaggio (Da Msgf o da Pgm).
Se i primi 3 bytes sono uguali a 'PGM', rilevo la descrizione del messaggio dalla schiera dichiarata internamente al
programma.
£DMSTR
Tipo retrive da Msgf : 
G= Senza passaggio delle variabili.
(Programmatore).
X= Con passaggio delle variabili.
(Utente).
£DMSME
Codice messaggio da reperire e memorizzare.
£DMSVA
Stringa di valori da associare al messaggio da memorizzare.
£DMSEL
Contiene la descrizione del messaggio reperito opportunamente dall'elemento di schiera.
Attenzione !!
Il valore di questo campo determina il reperimento da pgm RPG anziche'da Msgf.
£DMSVS
Indica se l'elaborazione dei messaggi memorizzati deve essere interattiva (V=a video) oppure diffe- rita (S=su
stampa).
£DMSFI
Nome del Message file AS/400 da dove reperire il messaggio e i suoi attributi.
Se si sta utilizzando un messaggio definito internamente al programma, questa variabile deve essere formattata a
blanks.
. COPY ----> £DMSC2
E'la routine di memorizzazione.
In ingresso deve ricevere : 
1) Codice del messaggio (Obbligatorio)
2) Nome del Message File AS/400 (Obbligatorio se non e' definito un Msgf di default)
3) Stringa di valori da associare al messaggio (Facoltativo; utilizzabile solo se il reperimento avviene da un membro
Messaggi
AS/400)
. COPY ----> £DMSC3
E' la routine di gestione a video o su stampa dei messaggi memorizzati;
In ingresso deve ricevere obbligatoriamente : 
1) Il parametro guida per elaborare i messaggi memorizzati o in modo ON LINE o in modo BATCH.
. COPY ----> £DMSC4
E' la routine di emissione a video, del primo messaggio di errore.
In ingresso non riceve nessun parametro
In uscita restituisce : 
£DMS1M
Codice messaggio
£DMS1L
Testo di primo livello
£DMS2L
Testo di secondo livello
(Solo se reperimento da message file)
. COPY ----> £DMSC5
E' la routine di reperimento messaggi applicativi da Message file AS/400.
. COPY ----> £DMSC6
E' la routine di concatenazione automatica variabili associate al messaggio file AS/400.
