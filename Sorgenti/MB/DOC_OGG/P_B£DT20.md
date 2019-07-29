## Colonna Limite Inferiori Superiori/Valore 1-2-3-4    . .   6
# DEFINIZIONE STRUTTURA SETTORE
# DESCRIZIONE , VINCOLI E FUNZIONI DEI CAMPI SETTORE
## Scelta azione
Può assumere i seguenti valori : 
X    Esplode la riga nel dettaglio con tutti i suoi campi.
Sul campo di nome T$ELEM puo' essere indicato solo X.
F    Cessa l'azione delle scelte funzionali (di tipo globale) "B" e "C" sottoindicate a partire dall'attuale riga.
B    Azzera tutte le posizioni a video dei campi "Intestazione",
"Campo" (esclusa lunghezza) e "Decodifica" partendo dal campo su cui e' digitata sino al successivo campo con scelta
"F" escluso; se non indicata la Fine esegue la funzione per tutte le successive righe.
L'azione non e'eseguita sui campi di "Tipo" = /C , /V .
L'azione puo' essere eseguita col comando CMD9/Prova schermo o
CMD6/Posizionamento automatico.
La funzione deve essere eseguita  da sola.
C    Idenfica la riga durante la funzione di posizionamentoautomatico come riga di riferimento per l'incolonnamento
di :  "Intestazione",
"Campo", "Decodifica" di tutto il blocco di righe seguenti.
L'incolonnamento avviene incrementando di una riga alla volta.
Se pero' i campi di una riga base sono su piu' righe e sono incolonnati (iniziano alla stessa colonna) l'incremento
puo' essere di due o tre righe.
Intestazione e campo vengono posizionati solo se lo erano nella riga che fa da guida per l'ncolonnamento.
La decodifica, se nella riga guida non e' posizionata viene posta sulla stessa riga del campo cui si riferisce alla
colonna 42.
L'azione non e'eseguita sui campi di "Tipo" = /C , /V L'azione puo' essere eseguita solo con il comando F6 di
Posizionamento automatico.
Nel corso del posizionamento automatico i valori sono forzati anche se le posizioni sono gia' occupate (viene comunque
segnalato l'errore).
La funzione deve essere eseguita  da sola.
## Sequenza
Vincoli : 
Puo' assumere  valori da 10 a 9999.
Sul campo T$ELEM e' obbligatorio 0010 (peraltro protetto).
Sul campo T$DESC e' obbligatorio 0020 (peraltro protetto).
Sul campo di Tipo '/V' non puo' essere inferiore a 9000.
Su tutti gli altri campi puo' variare da 21 a 8999.
Non sono ammessi due valori di  sequenza uguali per campi diversi.
Funzioni : 
Indica la successione con la quale i campi sono presentati nel programma di definizione campi settore.
I suoi valori possono essere assunti in automatico con progressione aritmetica di base 10 .
Possono essere variati dall'utente rispettando i vincoli.
Il programma  se non sono presenti errori, risequenzializza automaticamente le righe secondo l'ordine indicato, e
ricalcola le posizioni iniziali dei campi sul file in funzione della sequenza , della lunghezza dei campi e dei filler
inseriti.
Non sono significative le posizioni iniziali sul file dei campi
T$ELEM e T$DESC (che sono per forza iniziali) e dei campi di Tipo
'/V' che sono per scelta finali e non entrano nella definizione del file.
## Nome campo
Vincoli : 
Possono essere immessi caratteri fino ad un massimo di 6.
Non vi possono essere spazi in BLANK prima dell'ultimo carattere.
I primi due campi devono avere obbligatoriamente nome T$ELEM e
T$DESC.Non vi possono essere, in un medesimo settore, due campi con lo stesso nome.
Funzioni : 
Tali nomi con la loro lunghezza (compresi gli eventuali decimali) e la posizione iniziale, determinerranno la
costruzione del sorgente nella tabella del settore in oggetto.
Per tale ed esclusiva funzione sono presenti i campi di tipo /C.
Non contribuiranno invece i campi di tipo /V.
## Intestazione del campo
Vincoli : 
Possono essere immessi caratteri fino ad un massimo di 20.
E' obbligatorio per il campo T$ELEM e per i campi di Tipo /V.
Funzioni : 
E' l'intestazione generica del campo, che comparira'per la lunghezza indicata (lunghezza intestazione) nel pgm di
gestione elementi tabelle. Il suo contenuto e' visualizzato anche nella
"Prova schermo".
## Tipologia del campo
Vincoli : 
Non puo' essere inserito se il nome campo e' T$DESC.
Se inserito deve essere presente in tabella.
Settore *CN Subsettore TT
Attivabile la ricerca alfabetica.
Esempi : 
Colonna :   Tipo (Significato)           Lunghezza (default)
/V   Solo Video
/C   Solo /Copy di Data Base
NR   Numerico
CL   Cliente                       6
FO   Fornitore                     6
CO   Conto                         12
VS   Voce di spesa                 6
CC   Centro di costo               6
AR   Articolo                      15
TA  Tabella
AA  Data in forma AAMMGG       6 0
AD  Data (odierna)AAMMGG       6 0
GG  Data in forma GGMMAA       6 0
GD  Data (odierna)GGMMAA       6 0
OJ  Oggetto
Per il dettaglio dei valori validi vedere la tabella *CNTT.
Funzioni : 
Indica la natura del campo.
La lunghezza viene assunta per default se non e' stata indicata.
Se il tipo campo e' una tabella, deve essere compilato il campo
Tabel e viceversa.
Se il tipo campo e' uguale a  :  'TA', 'CL', 'FO', 'CO','VS',  'CC',
'AR', 'OJ', la funzione di Posiz. automatica assumera' che il campo necessita della decodifica.
Si noti che un campo e' numerico quando il tipo campo indicato e'
NR o lo prevede implicitamente il tipo campo ( es.  :  GG ) .
Se il tipo campo e' 'OJ', il tipo oggetto deve essere indicato nel campo Valore 3  dei Vincoli/Limiti.
Il tipo campo /V  individua delle intestazioni esplicative della videata del pgm di gestione elementi tabelle.
La sequenza di tali campi deve essere > 8999 e deve obbligatoriamente essere compilata l'Intestazione campo.
Esclusivamente con lo scopo di essere presenti nel sorgente del DATA
BASE  con il nome indicato per la lunghezza e la posizione inserite, un campo si classifica con Tipo /C.

E' possibile derivare oggetti utilizzando le regole qui di seguito descritte.
 :  : PAR L(TAB) T(**Oggetti derivati**)
- Tipo|Parametro|Comportamento
- &&||Viene utilizzato l'ultimo oggetto valido
- **||Viene utilizzato l'ultimo oggetto definito con tipo **OG**
- TA|xxx==|Viene assunto il sottosettore della tabella in uso
- TA|*****|Viene utilizzata l'ultima tabella
- TA|xxx**|Viene utilizzato l'ultimo sottosettore di tabella


## Tabella
Vincoli : 
Se inserito deve essere  presente il sub-settore in esso indicato.
Attivabile la ricerca alfabetica, sia a livello di settore, che di subsettore.
Se inserito deve essere indicato 'TA' nel Tipo campo.
Non puo' essere compilato se tipo campo /C ,  /V  o di   nome T$DESC.
Funzioni : 
Puo',ad esempio, indicare al pgm di gestione elementi che l'elemento inserito deve essere presente nella tabella
indicata.
## Lunghezza e decimali
Descrizione : 
Lunghezza campo                        (3 crt numerici)
Decimali della lunghezza del campo     (1 crt numerico)
Vincoli : 
E' obbligatorio per tutti i campi non di Tipo /V e non di nome T$DESC.
La lunghezza massima e 100. Sui campi T$ELEM/T$DESC e' 15/30.
Ovviamente il n° dei decimali non puo' eccedere la lunghezza massima del campo.
Funzioni : 
E' la lunghezza del campo, ovviamente necessaria per tutti i campi su file.
## Obbligatorieta' inserimento campo
Vincoli : 
Non puo' essere presente sui campi tipo /C e /V .
Deve essere presente sul campo di nome T$ELEM.
Funzioni : 
Indica al pgm di gestione elementi tabelle se si deve obbligatoriamente inserire qualcosa.
## Campo da non controllare
Vincoli : 
Non puo' essere presente sui campi tipo /C , /V  e sul campo di nome
T$DESC.
Funzioni : 
Indica al pgm di gestione elementi tabelle se i valori  inseriti devono essere presenti nei relativi archivi  questo
e' tipico dei campi che prevedono la decodifica da archivio  : 
'TA','CL','FO','CO', 'VS','CC', 'AR','OJ' )
## Carattere di annullamento del campo
Vincoli : 
Non puo' essere presente sui campi di nome T$ELEM e T$DESC.
L'unico valore ammesso per l'annullamento e' A .
Funzioni : 
Indica che non si deve piu' considerare attivo tale campo a tutti gli effetti nella struttura del DATA BASE.
Gli elementi gia' inseriti nel file tabelle mantengonocomunque la preesistente struttura dati, che pero' non  puo'
essere manutenzionata col nuovo tipo di definizione.
## Posizione iniziale del campo sul DATA BASE
Vincoli : 
Non puo' essere inserita sui campi di nome T$ELEM e T$DESC, e sui campi di tipo /V  dove e' assunto 999 , ma solo per
indicare che sono gli ultimi ad essere elaborati a video e gli ultimi ad essere scritti sul file definizione campi di
settore.
E' tassativamente obbligatorio l'inserimento , da parte  dell'utente, in caso di campi di tipo /C, cioe' campi da
inserirsi nel sorgente di definizione del file struttura  settore.
A partire dalla posizione iniziale, la lunghezza non deve portare il campo a eccedere i caratteri liberi a
disposizione dell'utente, che sono 100.
Funzioni : 
Si tenga presente che la struttura del file tabelle e'  costituita dai seguenti campi : 
Annullamento elemento     1 crt
Settore/Subsettore        5 crt
Elemento                 15 crt
Descrizione              30 crt
Ad uso utente (libero)  100 crt
ELEMENTO e DESCRIZIONE saranno  allineati a sinistra nei campi occupandoli dalla prima posizione.
Sono viceversa da determinare le posizioni iniziali dei campi che occupano la parte ad uso utente e cio' avviene
automaticamente e obbligatoriamente in questo modo : 
Ciascun campo, elaborato nell'ordine indicato dalla sequenza di video, avra' come posizione iniziale la prima libera
(lasciata dai precedenti inserimenti) piu' gli eventuali caratteri liberi inseriti nel campo
Filler precedente.
Ovviamente la posizione finale dipendera' dalla sua lunghezza.
Non vengono considerati nell'automatismo gli eventuali campi di tipo /C.
## Filler precedente sul DATA BASE
Vincoli : 
Non puo' essere inserito sui campi di nome T$ELEM e T$DESC, sui campi di tipo /V e /C dove e' assunto 0.
Non puo' superare il valore 99.
Funzioni : 
Indica quanti caratteri liberi devono separare l'ultima posizione dell'ultimo campo di cui e' stata calcolata
(automaticamente) la posizione sul DATA BASE dalla prima posizione dell'attuale campo.Si vede a tal proposito
l'automatismo descritto  nelle funzioni del campo  Posizione iniziale.
## Esistenza Limiti/Valori
Vincoli : 
Ammette i valori L (Limiti) e V (Valori) o bianco se tali  vincoli non sussistono.
Possono essere presenti il Valore 3 e il Valore 4 anche in  assenza di vincoli previsti, se il tipo campo e' 'OJ', ma
in tal caso indica il tipo oggetto e la libreria di ricerca.
Funzioni : 
Indica la presenza (L-V) / l'assenza (' ') di vincoli sul valore del campo inserito.
## Colonna Limite Inferiori Superiori/Valore 1-2-3-4
Questi campi oltre a rappresentare vincoli o limiti vengono utilizzati per descrivere i parametri necessari ad
individuare un oggetto o un membro di un file.
Vincoli : 
Se indicato 'V'  deve essere compilato almeno uno dei  quattro valori.
Se indicato 'L'  deve essere compilato almeno uno dei  quattro valori e i limiti inferiori non possono superare i
corrispondenti (stessa riga) limiti superiori.
Funzioni : 
V :    Il pgm gestione tabelle controllera' che il valore del campo, se inserito, sia uno dei quattro Valori  ammessi.
L :    Il pgm gestione tabelle controllera' che il  valore del campo, se inserito, sia compreso almeno tra un limite
inferiore e il corrispondente superiore.
OJ :   Il terzo campo deve definire il tipo di oggetto (*PGM, *FILE ecc) e il quarto la libreria in cui tale oggetto si
deve trovare. E' ovviamente ammesso il valore *LIBL.
MB :   Il terzo elemento indica il file fisico nel quale il membro deve essere contenuto e il quarto la libreria in cui
tale oggetto si deve trovare. E' ovviamente ammesso il valore *LIBL.
## Colonna Riga  Colonna  Attr. Ini campo
Vincoli : 
La presenza di uno dei tre campi obbliga alla presenza  della riga e della colonna.
Riga e colonna sono obbligatori per il campo T$ELEM; se  assenti sono assunti valori di default.
Sono obbligatoriamente bianchi quando il tipo campo e' /C o /V; possono essere lasciati in bianco per un campo
"normale" in attesa che l'automatismo Posiz. automatico ne determini la posizione, che e' comunque obbligatoria.
La riga puo' variare da 5  a 22. da 4 a 9 se il campo e' T$ELEM.
Da 4 a 9 se il campo e' T$ELEM.
La colonna varia da 2  a 80.
Colonna + lunghezza non possono superare il valore 80.
L'attributo video deve essere presente in tabella settore Colonna CN subsettore AV ; attivabile la ricerca alfabetica.
Se l'attributo (nei due caratteri) non e' presente si controlla comunque la presenza di almeno uno dei due caratteri
nel settore
Colonna CN subsettore AV che se presente rimarra' solo quello.
Funzioni : 
Consentono di individuare posizione e attributi di visualizzazione del campo, come evidenziabile dalla "Prova
schermo", che simula la videata del pgm di gestione elementi tabelle.
## Lung Riga  Colonna  Attr. intestazione campo
Vincoli : 
La presenza di uno dei quattro campi obbliga alla presenza della riga e della colonna.
Lunghezza, riga e colonna sono obbligatori per il campo T$ELEM, se non inseriti, sono assunti valori di default.
Sono obbligatoriamente bianchi quando il tipo campo e' /C.
Sono obbligatori quando il tipo campo e' /V.
Possono essere lasciati in bianco per un campo "normale" in attesa che l'automatismo Posiz. automatico ne setermini le
caratteristiche video (il default per la lunghezza sara' comunque 20 crt).
La lunghezza non puo' superare il valore 20 e informa quanti caratteri dell'intestazione saranno visualizzati.
La riga puo' variare da 5 a 22.
Da 4 a 9 se il campo e' T$elem.
La colonna varia da 2 a 80.
Colonna + lunghezza non possono superare il valore 80.
L'attributo video deve essere presente in tabella settore colonna CN subsettore AV.
Attivabile la ricerca alfabetica.
Funzioni : 
Consentono di individuare posizione e attributi di visualizzazione dell'intestazione campo, come evidenziabile dalla
"Prova schermo" che simula la videata del pgm di gestione elementi tabelle.
## Lung Riga  Colonna  Attr. decodifica del campo
Vincoli : 
La presenza di uno dei quattro campi obbliga alla presenza della riga e della colonna.
Sono obbligatoriamente bianchi quando il tipo campo e' /C e /V Possono essere lasciati in bianco per un campo
"normale" in attesa che l'automatismo Posiz. automatico ne determini le caratteristiche video (il default per la
lunghezza sara' comunque 35 crt).
La lunghezza non puo' superare il valore 40 e informa quanti caratteri della decodifica saranno visualizzati.
La riga puo' variare da 5  a 22; da 4 a 9 se il campo e' T$ELEM.
La colonna varia da 2  a 80.
Colonna + lunghezza non possono superare il valore 80.
L'attributo video deve essere presente in tabella settore *CN subsettore AV ; attivabile la ricerca alfabetica.
Funzioni : 
Consentono di individuare posizione e attributi di visualizzazione della decodifica  campo, come evidenziabile dalla
"Prova schermo" che simula la videata del pgm di gestione elementi tabelle.
Tipicamente sono da utilizzarsi in presenza di tipo campo  che richiede la decodifica, cioe' per tipo campo : 
'TA','CL','FO','CO', 'VS','CC', 'AR','OJ' .
## Intestazioni stampa
Descrizione :    Prima intestazione per stampa
Seconda intestazione per stampa
Vincoli : 
Nessuno
Funzioni : 
In stampa tabelle, consentono la stampa di queste intestazioni, se non sono bianche, anziche' l'intestazione del
campo.
# FUNZIONI/AUTOMATISMI DI CARATTERE GENERALE
## Prova schermo (F9)
Dalla videata globale o da quella di dettaglio e' possibile richiedere la presente funzione.
Sono elaborati in ordine di sequenza tutti i campi  che abbiano per l'intestazione o per il campo o per la decodifica,
indicate le posizioni video.
Sono esclusi i campi : 
- tipo /C
- nome T$ELEM    (che ha una videata autonoma.
Se effettuata una scelta 'B' (sbiancamento cfr. Colonna Sc), questa viene preventivamente eseguita. La prova video e'
costruita emettendo l'effettiva intestazione per la lunghezza indicata, il campo per la lunghezza indicata utilizzando
il carattere fisso 'I'  per ogni posizione occupata e la decodifica per la lunghezza indicata utilizzando il carattere
fisso 'D' per ogni posizione occupata.
I campi sono emessi con gli attributi video previsti.
E' segnalato errore se un campo si sovrappone od e' contiguoad un campo gia' posizionato.
La prima posizione di errore (riga-colonna) e' emessa nel messaggio di errore.
## Formato condizionamenti costruzione video
Il tasto di comando F6, consente di attribuire valori automatici in lunghezza e posizione video ai campi che
presentano le seguenti caratteristiche : 
_ non sono campi di tipo '/C'
_ non sono campi di tipo '/V'
_ non di nome T$ELEM
_ non sono compilati nei campi : 
lunghezza - intestazione - decodifica - riga e colonna.
Si presenta un formato che ha le seguenti caratteristiche : 
Se inserito carattere in "Eliminazione caratteristiche video" l'effetto e' come aver indicato "B" sul primo campo,
sicche' sono preventivamente eliminate, prima della ricostruzione, tutte le caratteristiche video dei campi
compilabili.
Tale scelta si sovrappone e annulla altre scelte ("B" , "C" , "F") eventualmente immesse.
Se scelto "1 Colonna"  l'avnzamento avviene anziche' sulla prima mezzariga successiva libera, sulla prima riga
orizzontale libera.
Occorre effettuare una sola scelta "1 Colonna"  o  "2 Colonne". Le scelte di lunghezza intestazione e lunghezza
decodifica sono evidenti (intestazione comunque tra 1 e 20; decodifica tra 1 e 35).
Se l'intestazione e'<20 la lunghezza massima di un campo compilabile con decodifica, anziche' essere 18 fissa, e' (18
+ (20-lunghezza intestazione)).
L'ccupazione delle mezzerighe, in caso di incolonnamento, tiene conto dell'eventuale valore ridotto della decodifica.
Le scelte per gli attributi video sono ovvie; se attivi devono essere presenti nella tabella *CNAV.
I passi di costruzione del video sono i seguenti : 
1) Sbiancamento delle posizioni video dei campi secondo la scelta indicata.
2) La Costruzione della mappa video (cfr. Prova schermo) senza emissione avviene distribuendo le righe del video in
mezze righe.
Possono avere delle posizioni gia' occupate o nessuna posizione occupata; nel secondo caso la mezza riga sara' libera
per l'operatore.
3) Se il tipo campo e' : 'TA','CL','FO','CO', 'VS','CC', 'AR','OJ', si realizzano due  condizioni : 
a)se il campo prevede decodifica serve una riga completa per l'emissione, una riga completa serve anche nel caso il
campo non preveda la decodifica ma la sua lunghezza superi i 18 crt.
b)negli altri casi serve solo una mezza riga.
4)Per ogni campo posizionabile, ricerca la prima riga completa orizzontale libera e/o la prima mezzariga libera a
seconda che ci si trovi nella condizione 3a)/3b) che viene occupata dalla intestazione (lunghezza fissa 20) a partire
dalla seconda posizione libera, poi, partendo dal 23° carattere, viene posizionato il campo (se non e' lungo piu' di
18 crt
o si tratta del campo T$DESC ).
Anche la seconda mezzariga (condizione 3a)) viene occupata a partire dalla seconda posizione libera o dal campo (lungo
piu' di 18 ma non oltre 39 crt) o dalla decodifica (lunghezza fissa 35 ).Per il campo e' previsto attributo HC (alta
intensita' e separatori di colonne), se c'e' la decodifica l'attributo del campo sara' HL (alta intensita' e
separatori di colonne.
Se ha eseguito tutta la mappa senza aver posizionato tutti i campi, avverte con un messaggio, indicando il primo campo
che non riesce a posizionare.
Con l'Enter viene comunque accettata l'attivita' svolta, la quale e' comunque presentata a video, anche in assenza di
errori.
In aggiunta a quanto descritto per la funzione 4) puo' essere eseguito un posizionamento forzato tramite
incolonnamento (cfr. Colonna Sc la scelta 'C').
## Calcolo posizione iniziale (su Data Base)
## Controllo lunghezza emissione a stampa
La somma dei maggiori tra i valori Lunghezza campo,intestazione, decodifica, relativi a tutti i campi non di tipo /V o
/C non deve eccedere il valore 198
## Particolarita' di T$ELEM : 
posizionato sul DATA BASE dalla colonna 7 alla colonna 21,
T$ELEM  :   e' un campo obbligatorio di lunghezza fissa non superiore a
allineato a sinistra.
Il suo numero di sequenza  e' sempre 10 ed e' sempreil primo a comparire a video.
Non puo' essere annullato.
Gli e'riservata a video meta' videata, dalla riga 4 alla 9, senza sovrapposizioni con tutti gli altri campi, che sono
insieme in un'altra videata.
Per tale motivo su di esso non agiscono le funzioni di scelta per sbiancamento 'B' o incolonnamento 'C'.
Se le posizioni a video non sono compilate sono assunti valori di default.
## Particolarità di T$DESC
T$DESC  :   e' un campo di lunghezza non superiore a 30 (puo' essere anche 0). Occupa sul DATA BASE, il terzo campo,
dopo T$ELEM, allineandosi a sinistra, percio' la sua posizione iniziale ha sempre valore 1, e'poco significativa e non
puo' essere modificata.
Il suo numero di sequenza  e' sempre 20.
Non e' compilabile il "Tipo campo", quindi non sono compilabili il campo "Tabel"e il campo "Non ctr".
## Formato condizionamenti costruzione video
Se inserito carattere in "Eliminazione valori precedenti", sono eliminate, prima della ricostruzione, tutte le
caratteristiche video dei campi compilabili.
Tale scelta si sovrappone e annulla altre scelte ("B" , "C" , "F") eventualmente immesse.
Se scelto "1 Colonna"  l'avnzamento avviene anziche' sulla prima mezzariga successiva libera, sulla prima riga
orizzontale libera.
Occorre effettuare una sola scelta "1 Colonna"  o  "2 Colonne". Le scelte di lunghezza intestazione e lunghezza
decodifica sono evidenti (intestazione comunque tra 1 e 20; decodifica tra 1 e 35).
Se l'intestazione e'<20 la lunghezza massima di un campo compilabile con decodifica, anziche' essere 18 fissa, e' (18
+ (20-lunghezza intestazione)).
L'ccupazione delle mezzerighe, in caso di incolonnamento, tiene conto dell'eventuale valore ridotto della decodifica.
Le scelte per gli attributi video sono ovvie; se attivi devono essere presenti nella tabella *CNAV.
