# Obiettivo
Presentare tutte le informazioni relative alla fatturazione di documenti.
I documenti che possono comporre una fattura devono essere di tipo fatturabile (Vedi T§FL19).
Diversi documenti possono generare una stessa fattura solo se hanno lo stesso criterio di ordinamento, definito nel campo T§CORD della testata.
Il campo T§COR2, unitamente al campo T§CORD viene valorizzato a livello di ordine e può essere utilizzato per definire il raggruppamento/rottura durante la creazione della Bolla, ma il passaggio dalla Bolla alla Fattura viene gestito in raggruppamento/rottura dal solo campo T§CORD.
E' possibile fare in modo che un documento non sia cumulabile con altri ma generi una sola fattura (Vedi T§FDTA). Questa particolarità NON è gestita da questa funzione ma direttamente
nella stampa fattura.
# Utilizzo
L'ultilizzo si divide in quatto parti da eseguire sequenzialmente : 

- funzione di _3_inizializzazione. Da eseguire per ogni testata di documento. ("Gruppo" la prima volta e "Documento" per i documenti successivi);
- funzione _3_scansione delle "righe". Da eseguire per ogni riga di documento.;
- funzione di _3_fine "Gruppo". Da eseguire una volta alla fine della lettura di tutti i documenti;
- funzioni di _3_presentazione. Da eseguire dopo la funzione di _3_fine. Presenta i dati di fattura : 
--  Importi totali;
--  Provvigioni;
--  Tasse, IVA;
--  Spese, Maggiorazioni, Sconti;
--  Conti, Importi per conto;
--  Scadenze, Rate.

# Funzioni

- _2_INI :   Inizializzazione.
E' la funzione che inizializza i dati di fatturazione
Si possono eseguire due diversi tipi di inizializzazione : 
-- _3_GDO :  Gruppo documenti
L'inizializzazione di tipo GDO inizializza tutte le variabili con cui saranno costruiti i totali di fatturazione.
E' una funzione obbligatoria e deve essere eseguita come prima funzione.
Deve essere eseguita dopo la lettura della testata del primo documento.
Al suo interno esegue poi la INI/DOC.
-- _3_DOC :   Nuovo documento dello stesso gruppo
L'inizializzazione di tipo DOC inizializza tutte le variabili con cui saranno costruiti i totali del singolo documento (importi, iva e spese).
Deve essere eseguita dopo la lettura della testata del documento.
Carica tutte le informazioni di testata del documento necessarie per la sua fatturazione :  tabella di assoggettamento iva (eventualmente anche il 2° assoggettamento), tabella tipo e modello documento.
Controlla le autorizzazioni di classe "RIS-" e funzione "V5D"+T§TDOC
- _2_ELR :  Elaborazione righe.
E' la funzione che elabora la riga di un documento.
Deve essere eseguita dopo la lettura di ciascuna riga del documento.
-- _3_ALL :  Tutto
Elabora tutte le righe a quantità piena
-- _3_ALLR :  Tutto (Quantità residua)
Elabora tutte le righe a quantità residua
-- _3_NCO :  Tutto tranne conti
Come _3_ALL ma non costruisce i conti contabili
-- _3_NCOR :  Tutto (Quantità residua) tranne conti
Come _3_ALLR ma non costruisce i conti contabili
_2_Elaborazione della riga
-- NON elabora la riga se : 
--- la sua testata è annullata(Vedi T§LIVE),
--- se la stessa riga è annullata (Vedi R§LIVE),
--- se la riga è da NON fatturare(Vedi T§FL19).
-- Prezzo netto di riga : 
--- è il prezzo effettivo(R§PEFF) se diverso da 0 e il tipo modello del documento inizia per "P"(Ciclo passivo);
--- è calcolato da £V5V in tutti gli altri casi.
-- Quantità di riga esterna e interna : 
--- è la quantità della riga(Vedi R§FL06) se il metodo è _3_ALL o _3_NCO;
--- è la quantità calcolata dalla £V5Q (Quantità residua) in tutti gli atri casi.
-- Quantità master : 
--- La quantità master di default è quella esterna.
--- E' possibile decidere di usare come quantità master quella interna da un programma di exit definito in tabella V5D :  "Pgm aggius.qt.master".
--- In ogni caso se la quantità master è 0 assume come master quella interna.
-- Se il tipo documento lo richiede(campo "Calcolo Pesi/Volumi" della "V5D") e l'oggetto è un articolo calcola il peso e il volume come quantità interna per rispettivamente  peso e volume dell'articolo
-- Calcola l'importo : 
--- è quantita master * prezzo netto, se la quantità non è 0 e la riga non è di tipo forfettario (Vedi R§FL29)
---  è il prezzo netto in tutti gli altri casi.
-- Esegue un arrotondamento dell'importo mediante la £G51
-- Calcola assoggettamento IVA
-- Costruisce il conto contabile, la relativa descrizione, il segno dare o avere : 
--- Non costruisce il conto se
---- il metodo è _3_NCO o _3_NCOR
---- l'importo è 0
---- la riga è di sola iva o è omaggio non imponibilie (flag R§FL19='0', o '1', o '8' O 'A')
--- il conto è quello di riga (Vedi R§CONT), se non presente lo determina mediante la £G03 : 
--- se è attiva le gestione conti multipli :  campo "Att.Gest.conti mult." della tabella V51 chiama il programma "V5V5F0_C". Questo programma  gestisce una schiera di conti e relativi importi. Nella chiamata il primo elemento di schiera contiente il conto e l'importo di riga.
-- Ritorna i valori della riga. I numeri sono gli indici delle schiera
--- Codici e descrizioni £5FC, £5FD
---- 1 - Conto Contabile
---- 2 - Assoggettamento IVA
---- 3 - Dare/Avere
Per gestione multiconto
---- 4 - Conto contabile (2)
---- 5 - Dare/Avere conto conto contabile (2)
---- 6 - Conto contabile (3)
---- 7 - Dare/Avere conto conto contabile (3)
---- 8 - Conto contabile (4)
---- 9 - Dare/Avere conto conto contabile (4)
---- 10 - Conto contabile (5), non c'è più spazio per l'assoggettamento
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Imponibile
---- 2 - Imposta
---- 3 - Quantità
---- 4 - Prezzo netto
---- 5 - Peso
---- 6 - Volume
---- 2 - Assoggettamento IVA
-- Totalizza i valori di riga(sia per documento che per gruppo).
--- Importo TOTALE
---  _3_Netto merce (importo riga se R§FL19='4', '5', '6');
--- _3_Spese (importo riga se R§FL19='2', '3')
--- _3_Imposte
--- Imponibile
--- Sconti
--- _3_Omaggi (importo riga se R§FL19='1', '7', '8', 'A')
--- _3_Peso (peso riga)
--- _3_Volume  (volume riga)
--- _3_Quantità (quantità master riga)
--- _3_Omaggi con addeb.Iva (importo riga se R§FL19='7')
--- _3_Imponibile SOLO .Iva (importo riga se R§FL19='0')
--- Sconti/Magg.non su iva
--- Tasse
--- Conto contabile o conti contabili se gestione multipla conti
Per ogni conto contabile costruisce e totalizza la relativa analitica
- _2_FINE :  Fine
E' la funzione che esegue le operazioni di fine.
Deve essere eseguita obbligatoriamente dopo le lettura di tutti i documenti in elaborazione.
-- _3_GDO :  Gruppo documenti
--- fine documento (se presente almeno una riga)
calcola l totali del documento :  importo, iva, spese(Vedi £G04)
--- fine gruppo
calcola l totali del gruppo :  importo, iva, spese(Vedi £G04)
- _2_SCA :  Scansione
E' la funzione che presenta i risultati di fatturazione(le funzioni "VIS" ne sono la visualizzazione)
-- _3_IMP :  Importi
--- presenta tutti gli importi della fattura. E' una sola scansione. I numeri sono gli indici delle schiere.
--- Codici e descrizioni £5FC, £5FD
---- Nessuno
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Importo TOTALE
---- 2 - Netto merce
---- 3 - Spese
---- 4 - Imposte
---- 5 - Imponibile
---- 6 - Sconti
---- 7 - Omaggi
---- 8 - Peso
---- 9 - Volume
---- 10 - Quantità
-- _3_PRO :  Provvigioni
--- presenta tutte le provvigioni della fattura. Ogni scansione è una provvigione. I numeri sono gli indici delle schiere
--- codici e descrizioni £5FC, £5FD
---- 1 - Provvigione
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Importo documento
---- 2 - Importo provvigione
-- _3_SPE :  Spese, Sconti, Maggiornazioni
--- presenta tutte le spese, gli sconti, e le maggiorazioni della fattura. Ogni scansione è una spesa. I numeri sono gli indici delle schiere
--- codici e descrizioni £5FC, £5FD
---- 1 - Spesa, sconto, maggiorazione
---- 2 - Assoggettamento
---- 3 - Tipo di spesa, sconto, maggiorazione
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Importo
-- _3_TAX :  Tasse
--- presenta tutte le tasse della fattura. Ogni scansione è una imposta. I numeri sono gli indici delle schiere
--- codici e descrizioni £5FC, £5FD
---- 1 - Imposta
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Imponibile
---- 2 - Imposta
-- _3_CON :  Conti, Importi per conto. Ogni scansione è un conto contabile. I numeri sono gli indici delle schiere
--- presenta tutti i conti della fattura
--- codici e descrizioni £5FC, £5FD
---- 1 - Conto contabile
---- 2 - Dare/Avere
---- 3 - Tipo conto(merce, iva, contropartita)
---- 4 - Assoggettamento
---- Analitica Standard (Vedi tabella C51, campo "Dettaglio conti ")
---- 5 - Centro di costo
---- 6 - Commessa
---- 7 - Voce di spesa
---- Analitica da modello (Vedi tabella C51, campo "Dettaglio conti "=A)
---- 5 - Natura 1
---- 6 - Natura 2
---- 7 - Natura 3
---- 8 - Destinazione 1
---- 9 - Destinazione 2
---- 10 - Destinazione 3
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 -  importo
-- _3_SCA :  Scadenze, Rate
--- presenta tutte le scadenze della fattura. Ogni scansione è una scadenza. I numeri sono gli indici delle schiere
--- Codici e descrizioni £5FC, £5FD
---- 1 - Tipo Rata
---- 2 - Effetto a vista
--- valori (schiera £5FV, £5FE, £5FR rispettivamente in valuta documento, in valuta corrente, in valuta alternativa) : 
---- 1 - Scadenza
---- 2 - Importo
---- 3 - Numero rate (solo su prima scansione)
--- le scadenze sono costruite mediante la £G01. con inizio pagamento : 
---- data pagamento documento
---- risalita data fattura
---- risalita data bolla
---- risalita data documento
     (queste date, tranne la data fattura dopo la stampa,  non sono generalmente presenti nel "CORD" pertando in una gestione a documenti multipli sono quelle dell'ultimo documento analizzato).
---  presenta tutte le scadenze della fattura
-- _3_ALL :  Tutti in sequenza
--- presenta in modo sequenziale tutte le funzioni di cui sopra

