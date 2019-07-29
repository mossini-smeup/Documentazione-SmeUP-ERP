## Installazione pacchetto
Scaricare da http://areariservata.smeup.com/area-tecnica/aggiornamenti-sme-up-erp.html , cartella **FatturaElettronica** il savf relativo alla versione di Sme.UP Erp in uso.
Restorare gli oggetti in una libreria di comodo.
Copiare i sorgenti contenuti nei file source DOC e PTF, presenti nel pacchetto di distribuzione, nella SMEDEV del cliente.
Creare i nuovi logici del file EDSEND e del V5TDOC.
Creare i file EDFEIT* a partire dai sorgenti in SRCWK.
Compilare i programmi contenuti nei vari file sorgenti. Fare riferimento alle note riportate nel file SCP_PTF/STXT_FE51 in caso di problemi di compilazione dei seguenti programmi : 
 * B£G02B
 * B£SER_90
 * B£SER_99
 * £G02D
 * B£G15G
 * B£OA_DO
 * B£OA_CN

Eseguire la PTF V580508A.

I parametri della categoria  £CA vengono creati in automatico (senza necessità di fasatura tabelle) dal programma  C£CRFS01 .


## Configurazione parametri

### Tabella V50
Compilare la tabella basandosi sulla documentazione della stessa per avere indicazioni relativamente al contenuto dei campi.

- [Fatturazione Elettronica](Sorgenti/MB/DOC_OGG/TA_V50)

### Tabella C5A
Compilare il campo Modello Cont.F.E.B2B indicando la causale da utilizzare per le fatture elettroniche verso privati (potrebbe essere la stessa usata per la PA) se diversa dalla causale contabile (e quindi dal registro IVA) delle altre fatture


### Parametri £CA

Compilare i parametri dell'azienda (categoria £CA) sotto elencati : 
* ABA  Capitale sociale (facoltativo)
* ABI  Numero Autorizz.Bollo :  si consiglia la compilazione per facilitare il reperimento del dato nel caso in cui si voglia inserire nelle note del documento questa informazione
* ABL  Ufficio Registro Imprese (obbligatorio)
* ABM  Numero REA (obbligatorio)
* ABN  Socio Unico (facoltativo)
* ABO  Stato liquidazione (obbligatorio)
* ABP  Regime fiscale (obbligatorio)
* AWJ  Tipo Rappr.Fiscale
* AWK  Cod. Rappr.Fiscale :  questo campo e il precedente vanno compilati solo se l'azienda è un rappresentante fiscale di un soggetto estero. Dovrebbe essere una casistica molto rara
* AWL  Tipo Sogg.Emitt. x FE
* AWM  Cod.Sogg.Emitt. x FE :  questo campo e il precedente vanno compilati solo se l'azienda emette fatture per conto di altri cedenti. Ad esempio potremmo avere il caso di un'azienda che emette in prima persona le fatture dei suoi agenti. In questo caso il cedente è l'agente ma la fattura viene emessa dall'azienda (che è il cessionario). Il campo è solo a titolo informativo. Attualmente non è gestito nei tracciati
* AWS  Attiva Fattura B2B :  indica da che data l'azienda aderisce alla fatturazione elettronica B2B, valido solo se antecedente al 01/01/2019. Dal 01/01/19 si consideranno attive tutte le cessioni verso soggetti italiani
* AWT Tipo Ente Trasmittente x FE
* AWU Cod. Ente Trasmittente x FE :  questo campo e il precedente vanno valorizzati nel caso in cui ci si avvalga di un intermediario per l'invio dei file al Sdi. In questi due campi va riportato l'ente che effettua la trasmissione. Ad esempio se la trasmissione viene effettuata da Able Tech in questi campi andrà indicato il tipo FOR e il codice fornitore di Able Tech.

I parametri sopra elencati vengono creati in automatico (senza necessità di fasatura tabelle) dal programma  C£CRFS01 .

### Anagrafica azienda

Nell'anagrafica dell'azienda deve essere obbligatoriamente valorizzata sia la partita IVA che il codice fiscale.

### Estensione £51

**Clienti B2B**
Attribuire a ciascun cliente a cui si intenda inviare fatture elettroniche B2B l'indirizzo di Posta Elettronica Certificata (PEC) oppure il Codice Destinatario di 7 caratteri necessario per l'inoltro della fattura al destinatario corretto.
Se il cliente si avvale di un intermediario per l'invio al Sistema di Intescambio bisogna valorizzare il Codice Destinatario che verrà comunciato dal cliente stesso. In caso contrario è necessario compilare la PEC.
La presenza di questa estensione (insieme al parametro 'Attiva fattura B2B' della £CA) determina la generazione o meno della fattura nel formato elettronico
E' possibile compilare l'estensione in anticipo e configurare correttamente il campo Data Partenza F.E. in modo da estrarre le fatture in modalità elettronica solo a partire dalla data impostata.
All'interno dell'estensione è presente anche il campo 'Estrazione di tutte le FT B2B' :  se lasciato vuoto fino al 31/12/18 verranno estratte elettronicamente **SOLO** le fatture con CUP/CIG. Se impostato a 1 verranno estratte tutte le fatture emesse verso il cliente.
Si ricorda inoltre che è possibile forzare il flag T§FL12 a Z per fare in modo che una determinata fattura non venga estratta come elettronica anche se il cliente prevederebbe la fatturazione elettronica

**Clienti PA**
Attribuire obbligatoriamente a ciascun cliente della Pubblica Amministrazione il Codice Univoco Ufficio PA necessario per l'inoltro della fattura al destinatario corretto.
Il codice deve essere richiesto al cliente prima di procedere alla fatturazione o cercato sul sito http://www.indicepa.gov.it/documentale/ricerca.php nella sezione informazioni **Servizi di Fatturazione Elettronica  di ciascun ente.

**Codice ufficio**
Con la pubblica amministrazione potrebbe verificarsi la casistica che uno stesso cliente fornisca due diversi codici identificativi. Gli enti pubblici hanno, infatti, la possibilità di richiedere un codice identificativo per ciascun ufficio. Così, ad esempio, la sede di Brescia dell'Agenzia delle Entrate avrà un codice e quella di Bergamo avrà un altro codice. Questo potrebbe comportare dei problemi nel caso in cui in anagrafica fosse codificato un unico cliente 'Agenzia delle Entrate'. Per risolvere quella casistica è stato predisposto all'interno della tabella V50 il campo Ente rif. est. £51. Impostando questo campo, infatti, il codice univoco non verrebbe letto sull'ente di fatturazione come avviene normalmente ma, ad esempio, sull'ente di conferma o sull'ente di spedizione.
Quindi nell'esempio riportato potrei configurare un unico cliente 'Agenzia delle entrate' e creare poi due enti di spedizione 'Ufficio brescia' e 'Ufficio bergamo' su cui imposterei l'estensione £51. Nella tabella V50 dovrei inoltre compilare il campo 'Ente rif. est. £51' con 1=Ente spedizione. In questo modo le fatture elettroniche estratte verso lo stesso cessionario riporterebbero due diversi codici identificativi.

L'estensione £51 contiene anche il campo facoltativo "Cod.Fornitore in gestionale PA". In alcuni casi, infatti, gli uffici pubblici chiedono di indicare all'interno del file XML il codice con cui il loro fornitore è identificato all'interno del loro ERP. Questo campo serve a questo scopo e, quindi, dovrò indicare il dato comunicatomi dall'ufficio pubblico dic ui sono fornitore. Il valore verrà poi riportato nel tag <RiferimentoAmministrazione> del tracciato xml FatturaPA.

### Attivazione FE B2B

**Per attivare la fatturazione elettronica compilare il parametro AWS  Attiva Fattura B2B dell'azienda (categoria £CA). Si tratta di un parametro datato che può assumere solo i valori 1 (attivo) o 0 (inattivo).

### Oggetti V4 per release precedenti a V3R2
**N.B. Il B£G15M distribuito esegue la conversione dei valori V4 da formato posizionale ad** **attributo riscrivendo gli script in SCP_TAB.**
**Fare quindi una copia degli script in SCP_TAB in un diverso sorgente per sicurezza.**
Si consiglia di far uscire tutti gli utenti prima di mettere in linea il B£G15M, in modo che tutti abbiano in linea la nuova versione.
