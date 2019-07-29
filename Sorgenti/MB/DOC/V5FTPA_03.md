## Documentazione integrativa di quanto al capitolo precedente
La libreria restorata precedentemente contiene i sorgenti necessari alla fatturazione verso la Pubblica amministrazione in ambiente STAR. I sorgenti sono contenuti nel file SRC_STAR.

Bisogna preoccuparsi che l'interfaccia contatti ritorni tutti i campi necessari. Nel file è presente un B£IFCO_QR come esempio, contenente il modo corretto di riempire questi campi. In particolare bisogna riprendere le specifiche PA01 per reperire il parametro dello Split Payment.

Creare il logico FATTTX1L nella libreria dati a partire dal sorgente in SRC_STAR
Prima di ricompilare gli altri sorgenti, bisogna adeguare la costruzione del numero di fattura nel programma V5ED02S2 :  il campo si chiama §§NFAT e si imposta solo all'inizio del programma.
Il numero di fattura deve essere coerente con quello usato nel programma di stampa fattura, quindi per intenderci a fronte della fattura 14FT060728 avremo queste possibilità
§§NFAT=060728     se in stampa mettiamo solo il numero
§§NFAT=14060728   se in stampa mettiamo anno e numero
§§NFAT=14FT060728 se in stampa mettiamo anno tipo e numero
Il programma in questione utilizza un flag di FATTT00F che non è usato nei programmi standard, FAFLT9, che però potrebbe essere utilizzato in qualche programma personalizzato. Verificate tale utilizzo nei sorgenti personalizzati.

L'OAV precedentemente segnalato per l'esigibilità iva(J/C03), non è stato implementato, è stato dato per scontato che l'iva sia sempre ad esigibilità immediata. Per modificare questo parametro, cercare nel sorgente V5ED02S2 il campo XINCA.

Una volta sistemato il numero di fattura e l'utilizzo del flag, è possibile compilare tutti i sorgenti.

Per modificare la coda lavori in cui far girare il programma ed eventualmente la coda di stampa per le segnalazioni di errore, utilizzate UP GPE con il nome programma V5ED02S1

### Conservazione sostitutiva solo per fatture alla PA
Se bisogna mandare in archiviazione sostitutiva solo le fatture verso la PA, è necessario creare un nuovo registro Iva e fare in modo che le fatture in questione non entrino in altri registri.

Per ottentere l'impostazione di un diverso registro (in modo da ottenere una numerazione sequenziale delle fatture conservate) è necessario fare una personalizzazione al programma VER11 per la fatturazione differita e bloccare una fatturazione immediata. Bisogna prima di tutto creare 3 nuovi parametri per azienda, dove mettere i tipi documenti di STAR(tabella 113)...
Per fare queà implementata solo la personalizzazione per la fatturazione differita con un parametro sul codice cliente per modificare il tipo fattura di STAR e il tipo registrazione di Sme.UP

### CUP (Codice Univoco di Progetto) e CIG (Codice Identificativo della Gara)
In base all'art.25 DL.66/2014, la presenza di CUP e CIG e` essenziale per procedere al pagamento.

Per uniformare il reperimento di CIG e CUP sono stati creati due oav J/ dell'oggetto DO (J/C01 e J/C02) che dovranno essere personalizzati presso il cliente creando un apposito programma di calcolo dell'oav, indicandolo nel B£SLOT e impostando il flag di conservazione in costruzione.
Nel file SRC_STAR è contenuto un esempio di reperimento CUP e CIG a partire dal numero di bolla(XB£OA_DO). La definizione dei due oav andrà corretta e il programma adeguato al vostro ambiente, l'esempio in questione è allineato alla versione V2R3.

 :  : T04 Split Payment
Per gestire lo split payment bisogna creare un parametro datato, chiamato "YPA", sui clienti.
Questo parametro insieme alla modifica dell'interfaccia enti permette la gestione corretta.

