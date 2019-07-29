# OBIETTIVI
Questa /COPY permette la memorizzazione dei tempi di esecuzione.

La memorizzazione viene fatta per "Istanza" e "Momento"

# L'ISTANZA
Per Istanza si intente un raggruppamento di momenti, un'istanza è tipicamente l'esecuzione di un servizio.

# MOMENTO
Il momento racchiude in sè le caratteristiche temporali e di esecuzione dell'oggetto sotto osservazione. Se non dichiarato il nome del momento in modo esplicito, viene assunto "INI".
Si possono attivare all'interno dell'istanza più momenti, registrando in maniera puntuale, alcune funzioni del servizio. La dichiarazione di un nuovo momento è implicitamente la chiusura del'ultimo momento aperto. Se non specificato il tipo di momento si assume sia di tipo "SER" servizio.

# ESEMPIO
Assumiamo che il PGM.A richiami il PGM.B che è posto sotto osservazione.
>. _________         _________
.|         |______>|         |__> MOM.INI() _> Crea una nuova istanza "I1" e Apre il momento "INI"
.| PGM.A   |___    | PGM.B   |__> MOM.CHI() _> Chiude il momento "INI" dell'istanza "I1" e calcola i
.|_________|  |    |_________|                 millisecondi trascorsi
.             |     _________
.             |___>|         |__> MOM.INI() _> Crea una nuova istanza "I2" e Apre il momento "INI"
.                  | PGM.B   |__> MOM.CHI() _> Chiude il momento "INI" dell'istanza "I2" e calcola i
.                  |_________|                 millisecondi trascorsi


Assumiamo che il PGM.A richiami il PGM.C che è posto sotto osservazione con un secondo momento denominato "NEW".

>.                        _____> MOM.INI() ____> Crea una nuova istanza "I1" e Apre il momento "INI"
.                       |   __> MOM.APE(NEW) _> Chiude il momento "INI" dell'istanza "I1" e calcola i
.                  _____|__|                    millisecondi trascorsi e apre il nuovo momento "NEW"
.                 |         |                   nell'istanza "I1"
.              __>| PGM.C   |_> MOM.APE() ____> Chiude il momento "NEW" dell'istanza "I1" e calcola i
.             |   |_________|                   millisecondi trascorsi e apre il nuovo momento "INI"
.             |            |                    nell'istanza "I1"
. _________   |            |_> MOM.CHI() _____> Chiude il momento "INI" dell'istanza "I1" e calcola i
.|         |__|                                 millisecondi trascorsi
.| PGM.A   |__
.|_________|  |
.             |         _____> MOM.INI() _____> Crea una nuova istanza "I2" e Apre il momento "INI"
.             |        |    _> MOM.APE(NEW) __> Chiude il momento "INI" dell'istanza "I2" e calcola i
.             |    ____|___|                    millisecondi trascorsi e apre il nuovo momento "NEW"
.             |   |         |                   nell'istanza "I2"
.             |__>| PGM.C   |__> MOM.APE() ___> Chiude il momento "NEW" dell'istanza "I2" e calcola i
.                 |_________|                   millisecondi trascorsi e apre il nuovo momento "INI"
.                          |                    nell'istanza "I2"
.                          |___> MOM.CHI() ___> Chiude il momento "INI" dell'istanza "I2" e calcola i
.                                               millisecondi trascorsi

# FUNZIONI/METODI

## MOM - Momento

### . INI - Nuova  Istanza
Inizializza una nuova istanza e apre un nuovo momento. Usata all'inizio del servizio

### . APE - Nuovo Momento
Apre un nuovo momento e chiude l'ultimo momento aperto. Usata all'inizio e alla fine delle funzioni che si voglio analizzare, definendo un nome di momento appropriato.

### . CHI - Chiude l'ultimo Momento aperto
Chiude l'ultimo momento aperto. Usata alla chiusura del servizio

## STA - Statistiche

### . TIP.POS - Posizionati sui tipi
Posizionati all'inizio e inizia la scansione raggruppata per tipi di momenti.

### . TIP - Scansione sui tipi
Continua la scansione raggruppata per tipi di momenti.

### . SER.POS - Posizionati sui Servizi
Posizionati all'inizio e inizia la scansione raggruppata per Servizio e Funzione. E' implicito che il tipo di momento sia "SER"

### . SER - Scansione sui Servizi
Continua la scansione raggruppata per Servizio e Funzione.

### . MOM.POS - Posizionati sui Momenti
Posizionati all'inizio e inizia la scansione dettagliata per momento.

### . MOM - Scansione sui  tipi
Continua la scansione per momenmto.

## INF - Informazioni
### . MOM - Memoria occupata
Numero di momenti memorizzati. Il limite massimo è stato posto a 20.000 oltre il quale la memoria viene ripulita e persi i momenti in essere.
