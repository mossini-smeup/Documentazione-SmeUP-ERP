### Campo "Data" dell'Xml come data ultima bolla.

Con la circolare 14/E del 17 giugno 2019, l'agenzia delle entrate ha espresso il fatto che il campo "data" dell'xml delle fatture differite, possa corrispondere alla data dell'ultima operazione cui la fattura si riferisce.

Purtroppo questa affermazione ha creato confusione sugli operatori che nella consuetudine usavano come data fattura la data di fine mese.
A pro del fatto di poter continuare la data di fine mese non si è espressa l'agenzia ma lo hanno fatto importanti operatori come il sole 24 ore, assosoftware e l'associazione nazionale dei commercialisti.

Qualora ci si voglia attenere strettamente a quanto indicato dall'agenzia sarà possibile attivare tale possibilità tramite il campo "Data ultima bolla" della tabella V50.

In questo caso Smeup opererà nel seguente modo : 
* Le fatture potranno essere sempre stampate con le modalità usuali, usando come data fattura ancora la data di fine mese.
* In xml nel campo data, la data fattura, verrà usata solo in assenza di una data bolla. In presenza di una data bolla verrà usata l'unica o l'ultima presente in fattura.

NOTA BENE :  è importante notare che in questo modo il cliente non riceverà la nostra data fattura, che verrà ad indicare solo la data di "protocollazione" della fattura.
Sarà quindi importante notare che nella relazione con il cliente, solo il n° fattura permetterà di identificare in modo certo la fattura, in quanto non si potrà più fare affidamento sulla corrispondenza della data.

## CUP (Codice Univoco di Progetto) e CIG (Codice Identificativo della Gara)

In base all'art.25 DL.66/2014, la presenza di CUP e CIG e` essenziale per procedere al pagamento.

Per uniformare il reperimento di CIG e CUP sono stati creati due oav J/ dell'oggetto DO (J/C01 e J/C02) che dovranno essere personalizzati presso il cliente creando un apposito programma di calcolo dell'oav, indicandolo nel B£SLOT e impostando il flag di conservazione in costruzione.
In questo modo vengono normalizzate tutte le differenti implementazioni messe in atto presso i clienti.
L'oav distribuito a standard restituisce bianco per entrambe le informazioni.

Nel formato xml FatturaPA CIG e CUP sono contenuti nei blocchi relativi all'Ordine d'acquisto e al Contratto.
Questo comporta che per emettere una fattura per la quale sia possibile alla PA procedere al pagamento è necessario indicare il numero dell'ordine d'acquisto (il riferimento esterno) o il numero del contratto.
L'impostazione in base alla quale vengono scritti i blocchi relativi a ordine di aquisto e contratto, e ai campi dai quali vengono reperiti i dati corrispondenti, si trova nella tabella V50.

Se presente CUP o CIG deve essere valorizzato o il contratto o il riferimento esterno (contenente il numero di ordine di acquisto) in testata. In caso contrario viene segnalato errore in fase di generazione XML.
Il contratto ha la precedenza sul numero di ordine di acquisto (omettendo quindi la sezione relativa).
Essendo nel tracciato FatturaPA il campo contenente il riferimento dell'ordine di acquisto lungo 20 caratteri, mentre il riferimento esterno del documento è lungo 30, è stato implementato un programma di verifica V5UTX16 che segnala i documenti relativi a clienti della PA con riferimento esterno in testata più lungo di 20 caratteri (disponibile da V2R3).
A V4R1 è stato anche modificato il Kontroller della testata documenti V5V6Y0 in modo da impedire l'inserimento di riferimenti esterni maggiori di 20 caratteri per clienti della PA.

### Riferimento a livello di riga dell'ordine di acquisto

Nel caso si voglia specificare nell'xml il riferimento dell'ordine d'acquisto a livello di riga, anziché di testata, è possibile farlo attivando l'apposito flag T$V50L in tabella V50 e valorizzando di conseguenza il campo R§ORAQ del V5TDOC0F.
In questo modo ad ogni riga della fattura viene associato, anzichè un riferimento ad un ordine di acquisto, il riferimento ad una precisa riga dell'ordine di acquisto.
Questo consente peraltro anche di avere riferimenti a differenti ordini di acquisto per differenti righe di fattura.
Valori di T$V50L  : 
 *  ' '  Non considerare rif. riga (risale a T§ORAQ senza considerare R§ORAQ)
 *  '1'  Rif. Riga posizionale (20 caratteri per numero ordine + 10 caratteri per numero riga)
 *  '2'  Rif. Riga sep. ',' (Numero ordine e numero riga separati da ',')
 *  '3'  Rif. Riga sep. ';' (Numero ordine e numero riga separati da ';')
 *  '4'  Rif. Riga sep. '/' (Numero ordine e numero riga separati da '/')
 *  '5'  Rif. Riga sep. '-' (Numero ordine e numero riga separati da '-')
Qualora T$V50L sia diverso da '' e non venga trovato nessun riferimento all'ordine di acquisto sulle righe, viene utilizzato riferimento di testata se presente.

**N.B. :  I riferimenti a CIG e CUP rimangono comunque unici a livello di fattura.**
**Non è possibile avere CIG e CUP diversi per riga di fattura.**

### Omaggi

All'interno di una fattura è possibile avere due tipologie di omaggi : 
 * Omaggi non imponibili come sconti in merce (ART. 15), campioni gratuiti e promozioni (ART.2)
 * Omaggi imponibili (ART.2)

I suggerimenti di Assosoftware per la compilazione dell'XML in questi due casi sono i seguenti : 

__Omaggi non imponibili__

In questo caso il valore del campo _2.2.1.11 <PrezzoTotale>_ è = 0; nel campo _2.2.1.9 <PrezzoUnitario> va indicato il "valore normale"; nel codice IVA va indicato la motivazione dell'omaggio :  fuori campo IVA, articolo di esclusione, ecc.
In questo caso il valore del codice da utilizzare nella sezione <TipoCessionePrestazione> sarà "AB"
Poiché vengono valorizzati quantità, prezzo unitario e sconti, ma il campo 2.2.1.11 <PrezzoTotale> è valorizzato = 0; non verrebbe rispettata il controllo 00423 (<PrezzoTotale> = (prezzo - sconti) * qta)
Per superare il controllo occorre aggiungere come sconto di riga uno sconto = 100%

__Omaggi imponibili__
In questo caso l'IVA può essere o meno addebitata al cliente (con rivalsa o senza rivalsa).
Sarà necessario valorizzare i campi 2.2.1.5 <Quantita>, 2.2.1.6 <UnitaMisura>, 2.2.1.9 <PrezzoUnitario>, eventuali 2.2.1.10 <ScontoMaggiorazione> , e 2.2.1.11 <PrezzoTotale> riportando i valori del gestionale e rispettando le regole del controllo 00423.
In questo caso il valore del codice da utilizzare nella sezione <TipoCessionePrestazione> sarà "AB"
Riportare il blocco [2.2.1.16] AltriDatiGestionali, con TipoDato = "AswTRiga" e [2.2.1.16.2] <RiferimentoTesto> = "Omaggio senza rivalsa -OS-" oppure "Omaggio con rivalsa -OC-", a seconda del caso.
Se utile per rendere più comprensibile a chi legge la fattura, in queste righe si può sostituire la parte di dicitura "Omaggio senza rivalsa" o "Omaggio con rivalsa" riportata in <RiferimentoTesto> con la Descrizione del tipo sconto merce del gestionale.

### Fatture in valuta
Nel caso in cui la fattura sia emessa in valuta diversa dall'Euro il suggerimento è quello di compilare i dati dell'XML con i valori in euro e riportare il controvalore in valuta come dato informativo all'interno dei TAG liberi (causale di testata o altri dati gestionali di riga)


### Dispositivi medici
In base alla circolare del 19/02/2016 del Ministero dell'Economia e delle Finanze e della Salute, è necessario indicare nell'xml delle fatture alla pubblica amministrazione, relative a Dispositivi medici (direttiva 93/42) e dispositivi per la diagnostica in vitro (direttiva 98/79), i dati riguardanti il numero di registrazione alla Banca Dati del Ministero della salute.
Tali dati devono essere indicati all'interno del blocco <CodiceArticolo> nel seguente modo : 

| Tag | Descrizione |
| ---|----|
| <CodiceTipo> | DMx , con x=1 per "Dispositivo medico o dispositivo diagnostico in vitro" o x=2 per "Sistema o kit assemblato" |
| <CodiceValore> | Numero di registrazione attribuito al dispositivo medico nella Banca dati e Repertorio Dispositivi Medici, ai sensi del decreto del Ministero della salute 21/12/2009 (GU n. 17 del 22/01/2010) |
| 

Per uniformare il reperimento del CodiceTipo e CodiceValore creati due oav J/ dell'oggetto DR (J/P01 e J/P02) che dovranno essere personalizzati presso il cliente creando un apposito programma di calcolo dell'oav, indicandolo nel B£SLOT e impostando il flag di conservazione in costruzione.
In questo modo vengono normalizzate tutte le differenti implementazioni messe in atto presso i clienti.
L'oav distribuito a standard restituisce bianco per entrambe le informazioni.

### Esigibilità IVA

Per uniformare il reperimento dell'Esigibilità IVA è stato creato un oav J/C03 dell'oggetto DO.
A partire dalla V3R2 tale oav richiama la £C60 che restituisce se al cliente è applicata l'iva per cassa. Nelle release precedenti l'oav dovrà essere personalizzato presso il cliente creando un apposito programma di calcolo dell'oav, indicandolo nel B£SLOT e impostando il flag di conservazione in costruzione.
I valori che devono essere restituiti sono quelli dell'oggetto V4 ED.£FPAEI  : 
 * I         Immediata
 * D         Differita
L'oav distribuito a standard per release precedenti la V3R2 restituisce bianco.

**N.B. L'esigibilità IVA è una informazione obbligatoria nel formato fatturaPA.**

