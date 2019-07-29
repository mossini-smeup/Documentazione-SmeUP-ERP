# CONSIDERAZIONI GENERALI
Il fine di tale pgm di utility è la creazione delle rate mancanti di una conversione a partire dai dati reperibili tramite le righe di registrazioni contabili, nonchè l'attribuzione delle rate di pagamento create alle rate di dovuto.

# PREREQUISITI
 :  : PAR l(PUN)
- La tabella C5D i tipi di registrazione di incasso/pagamento devono aver impostato i modelli 05/06
- Sulla tabella BRE (tipo contatto) deve esserci il flag di natura ente per gli enti clienti/fornitori
- Sulla righe dei soggetti siano sempre presenti il numero e la data documento riempiti con i riferimenti della partita cui appartengono (sia per i dovuti che per i pagamenti) e possibilmente il codice pagamento in base al quale verranno eventualemente ricreate le rate di dovuto mancanti, nonchè i flag 11/12
- Sulle righe di pagamento la data libera 01 deve essere riservata all'indicazione della data di scadenza (di default viene messa la data documento); i codici alfabetici 03 e 04 devono invece essere riservati alla banca (TAC5F) e al rapporto bancario (TAC5J)
- Sulle righe di dovuto la data libera 05 deve essere invece riservata all'indicazione della data di inizio pagamento nel caso non corrisponda alla data documento
- Siano stati impostati nell'opportuno modo i campi della tabella C53 che riguardano il pareggio partite
- Sulle righe di pagato la data libera 01 deve essere invece riservata alle scadenze degli effetti :  se non è presente questa indicazione sulla rata viene assunta la data di scadenza della fattura che potrebbe non coincidere con quella dell'effetto (es. assegni, tratte). Altrimenti andrà previsto un pgm specifico.
- Se su una rata proviene da un programma di conversione specifico, viene controllato che se per essa è presente il flag 36 a 1, essa non sara oggetto di abbinamento incassi/pagamenti o pareggio partite.

 :  : DEC T(ST) P() K(C5D&AZ)
 :  : DEC T(ST) P() K(BRE)
 :  : DEC T(ST) P() K(C53)

# PARAMETRI DI LANCIO
## AZIONI SU ARCH.RATE
 * _2_Pulizia  ------> Prima della creazione vengono cancellate le rate che si voglio ricreare :  se lancio solo la pulizia o solo le rate di dovuto verranno cancellate tutte le rate di pagato, se lancio solo le rate di pagato verranno cancellate tutte le rate di pagato od originate da una riga con il FL11 = '-', mentre se lancio con solo le rate di pareggio partite verranno cancellate solo le rate di tipo RR
 * _2_Dovuto -------> Verranno elaborate le righe con causale/FL11='+' per la creazione delle rate di dovuto
 * _2_Pagato -------> Verranno elaborate le righe con causale/FL11='-' per la creazione delle rate di pagato
 * _2_Pareggio partite -------> Verranno elaborate le rate aperte al fine di pareggiare le pareggiabili di pagato. Se vale 1 verrano pareggiate solo le rate aperte della partita la cui somma da 0, se invece vale 2 verranno pareggiate positive/negative della stessa partita per l'importo pareggiabile.

## CAUSALE PAGAMENTO
 * _2_Pagam.per giroconto  -------> indica il codice di pagamento da usare come default nel caso non sia presente sulla riga
## MESSAGGI
 * _2_Stampa warning -------> stampa gli eventuali messaggi informativi
 * _2_Stampa processo  -------> stampa il log dell'elaborazione

## PARZIALIZZAZIONI
 * _2_Azienda -------> l'azienda che si vuole elaborare
 * _2_Tipo ente  -------> restringe il campo di elaborazione ad una tipologia di enti
 * _2_Codice ente  -------> restringe il campo di elaborazione ad un codice ente

## RICREA RATE ESISTENTI
 * _2_Dovuto -------> nel caso non abbia utilizzato la pulizia indica se le rate di dovuto preesistenti debbano essere ricreate o meno
 * _2_Pagato -------> come sopra per le rate di pagato

## DATA LIMITE
 * _2_Data Iniziale -------> indica il limite iniziale della data di registrazione
 * _2_Data Finale -------> indica il limite finale della data di registrazione

## DOCUMENTO
 * _2_Data Documento -------> imposta un filtro sulla data documento
 * _2_N° Documento -------> imposta un filtro sul n° di documento

