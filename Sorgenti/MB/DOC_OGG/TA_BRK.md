# BRK - Tipo risorse secondarie
 :  : DEC T(ST) K(BRK)
## OBIETTIVI
Caratterizzare la tipologia delle risorse secondarie.
## INTRODUZIONE
Permette d'identificare la tipologia della risorsa secondaria.
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC3 **Tipo e parametro codice 3**
Definiscono l'oggetto (elemento della tabella *CN/TT eventualmente tipizzato), che rappresenta il tipo risorsa a cui si può collegare il tipo trattato.
 :  : FLD T$PAR3.T$KYC3 **Tipo e parametro codice 3**
Vedi sopra
 :  : FLD T$BRKA **Parametri impliciti**
È un elemento della tabella C£I permette di gestire opzionalmente 5 valori alfanumerici e 5 valori numerici.
 :  : FLD T$BRKB **Modello**
Definisce il significato dei campi codice e valore.
Se inizia con '*' è uno dei modelli standard contenuti nel programma BRRS01DE.
Altrimenti è un programma specifico di cui si controlla l'esistenza.
 :  : FLD T$BRKC **Parametri Modello**
Definisce i parametri del modello.
 :  : FLD T$BRKD **Gestione date validità**
Stabilisce che per questo tipo risorsa sono utilizzate le date di validità
 :  : FLD T$BRKE **Gestione nota interna**
Stabilisce che per questo tipo risorsa è utilizzata la nota interna
 :  : FLD T$BRKF **Contenitore note**
Stabilisce che per questo tipo risorsa sono gestite le note struttutare. In questo campo viene definito il contenitore da utilizzare. Se questo campo è lasciato vuoto non verranno gestite le note strutturate per questo tipo risorsa.
 :  : FLD T$BRKG **Suffisso pgm di scrittura**
Se impostato, per le risorse secondarie di questo tipo, verranno scritti gli impegni nell'archivo S5IRSE.
Il programma di scrittura è S5FUSEC_x, dove x è il carattere qui impostato.
Vengono forniti, a standard, i seguenti programmi : 
S5FUSEC_A - da impostare per le risorse specifiche
S5FUSEC_B - da impostare per le altre risorse (fisiche, umane)
Si deve preventivamente abilitare la scrittura degi impegni secondari nell'elemento di tabella P5S relativo all'impegno principale (S5IRIS)
 :  : FLD T$BRKH **Durata utilizzo**
Definisce la durata di utilizzo di queste risorse
Questo campo può assumere uno tra i seguenti valori : 
' ' - Tempo totale dell'operazione
'1' - Solo tempo di attrezzaggio
'2' - Solo tempo di carico
Se si utilizzano risorse di questo tipo nella schedulazione fine Fine.Up, ed esse sono caricate solo nel tempo di attrezzaggio, si deve impostare il calcolo della data e ora fine dell'attrezzagio stesso, nello script dei parametri
**NB :  QUESTA IMPOSTAZIONE NON HA EFEFTTO SULLE RISORSE SECONDARIE DI VINCOLO**
**   ESSE SONO SEMPRE OCCUPATE PER IL TEMPO TOTALE DELL'OPERAZIONE**
 :  : FLD T$BRKI **Natura Risorsa secondaria**
Si inserisce la natura della risorsa secondaria a cui appartengono le risorse di questo tipo.
 :  : FLD T$BRKJ **Tipo vincolo Fine.Up**
Si imposta il tipo vincolo che le risorse di questo tipo costituiscono nella schedulazione Fine.Up.
Perchè esse siano effettivamente un vincolo gli impegni secondari devono essere memorizzati nell'archivio S5IRSE, e quindi deve essere impostato il suffisso del programma di scrittura.
Questo campo può assumere uno tra i seguenti valori : 
' ' - Nessun vincolo
'1' - Vincolo di segnalazione. La violazione di un vincolo (sovrautilizzo rispetto alla sua disponibilità nel tempo) viene segnalata al termine del processo di schedulazione.
'2' - Vincolo di obbligo. La violazione di un vincolo viene impedita nel processo di schedulazione.
Ricordiamo che, per ogni impegno risorse, viene controllato solom il primo impegno secondario di vincolo incontrato, in ordine di codice risorsa secondaria, tipo/parametro e oggetto della risorsa secondaria stessa.
 :  : FLD T$BRKK **Modo reperim.calendario**
Se impostato, nella schedulazione Fine.Up, il modo di reperimento del calendario verrà guidato da quanto impostato in questa tabella (dal calendario, dall'analisi disponibilità, ecc..).
Se questo campo è vuoto e si è impostato un vincolo, si assume che la risorsa secondaria sia sempre disponibile in quantità unitaria.
 :  : FLD T$BRKL **Esclusa se slave**
Se impostato, gli imepgni di questo tipo non verranno considerati negli impegni slave di un batch, essendo
comuni all'intero batch, e quindi assegnati al master.
Un esempio è costituito da uno stampo con più figure, che quindi è unico per tutti gli impegni del batch.
 :  : FLD T$BRKM **Costr.RSV per classe**
E' significativo solo se le risorse di questo tipo hanno vincolo di obbligo.
Se impostato, verrà eseguita una versione del calcolo RSV per
ogni classe di ogni BRK.
Se invece viene lasciato in bianco, verrè eseguita una versione del
calcolo per ogni istanza della BRK.
Sono state previste dieci diverse versioni del calcolo RSV.
Il motivio di questa impostazione è per sfruttare al meglio le memorie di lavoro.
Esempio :  sono stati codificati gli elementi di BRK :  BK1 e BK2, che
prevedono un vincolo di obbligo.
L'oggetto della BK1 ha 3 istanze.
L'oggetto della BK2 ha 4 istanze.
Se il presente campo vale ' ' vengono eseguite 3+4=7 versioni
del calcolo (la somma di tutte le istanze degli oggetti).
Se invece vale '1' vengono eseguite 2 versioni del calcolo
(la somma di tutte le istanze della BRK).
Normalmente questo campo va impostato per risorse che hanno molte istanze
a disponibilità "continua" (ad esempio attrezzi che hanno, a meno di
rilavorazioni previste, un solo elemento di calendario, vale a dire la loro disponibilità costante
nel tempo.
Va lasciato invece in bianco per risorse che hanno poche istanze ma un calendario
frammentato (ad esempi squadre di composizione diversa nelle diverse ore del giorno).




