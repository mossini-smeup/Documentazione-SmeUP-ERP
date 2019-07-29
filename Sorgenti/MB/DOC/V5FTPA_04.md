
# Estrazione Fatturazione Elettronica

## Operatività
Per effettuare la generazione degli XML fatturaPA/B2B eseguire il programma V5ED04A e impostare i parametri di parzializzazione per determinare quali fatture estrarre.
Il programma è richiamabile dalla voce di menù "Estrazione fatture" del modulo V5FTPA "Fatturazione Elettronica"
Impostare **Prima estrazione** per estrarre solo fatture mai estratte (viene scritto EDSEND)
Impostare **Estrazione non inviate (anche già estratte)** per riestrarre tutte le fatture non ancora inviate all'SdI tramite l'intermediario (vengono lette le fatture non inviate ovvero con T§FL12 blank presenti in EDSEND).
Impostare **Riestrazione non inviate con XML errato** per riestrarre solo le fatture per le quali sia stato generato un xml errato (in caso di errore viene scritto il tracciato EDFEIT08).
Impostare **Riestrazione già inviate a SdI** per riestrarre delle fatture già inviate al SdI (flag 12 della testata documento a '1')

**I file validi vengono generati su IFS nella cartella**
/Smedoc/FatturaElettronica/[CodiceAzienda]/[RegistroIVA]/[DataFattura]/[NumeroFattura]
Qualora in B£2 sia impostato il campo **ambiente di test** al codice azienda viene accodato _TST .
I file xml non validi (a causa di informazioni obbligatorie mancanti) vengono generati nella sottocartella /Smedoc/FatturaElettronica/[CodiceAzienda]/[RegistroIVA]/[DataFattura]/[NumeroFattura]/Errati/ e il nome file ha prefisso ERR_ .
Viene generato inoltre uno spool di stampa per segnalare per le incongruenze delle fatture non valide.

In caso si desideri **variare il percorso** di scrittura degli xml è possibile agire personalizzando il programma V5FE01 che determina il percorso della root e della singola fattura.
Il programma richiamato con funzione GET e metodo ROT restituisce la root della fatturazione elettronica.
Richiamato con funzione GET e metodo PAT restituisce invece il percorso dove verrà scritto l'xml della singola fattura.
Si tenga comunque presente che la presenza di un numero elevato di sottocartelle o di file in una singola cartella,rende impraticabile la visualizzazione della cartella sia tramite Navigator che tramite Esplora Risorse.

### Validare la fattura elettronica
E' possibile validare i file xml generati utilizzando lo schema xml fornito dal Sistema di Interscambio.
I file xml generati **dal 1 gennaio 2017** devono essere validati con lo schema xml della versione 1.2 Schema_del_file_xml_FatturaPA_versione_1.2.xsd scaricabile da http://areariservata.smeup.com/area-tecnica/aggiornamenti-sme-up-erp.html cartella **FatturaElettronica**  o dal link http://www.fatturapa.gov.it/export/fatturazione/sdi/fatturapa/v1.2/Schema_del_file_xml_FatturaPA_versione_1.2.xsd .

Per eseguire la validazione è stata preparata la scheda CHKFTPA richiamabile dal modulo 'Fatturazione elettronica' sotto la voce 'Controlli fatture', tab 'Validazione XML'. La scheda riceve come parametri la cartella in cui si trovano gli xml da controllare e il percorso dove si trova lo schema xml.
La scheda restituisce una matrice in cui per ogni xml viene indicato OK se il file è valido o il primo errore riscontrato se il file non è valido.
L'utilizzo di tale scheda presuppone un Looc.UP versione Roma Rev. 2 a cui sia stato applicato l'ultimo upgrade disponibile.
N.B. :  il controllo può richiedere diverso tempo, in particolare in presenza di un numero elevato di file xml da validare.

E' anche possibile validare un singolo documento selezionando il tab 'Controllo singola fattura'.

### Visualizzare la fattura elettronica
Per visualizzare l'xml della fattura in un formato più facilmente leggibile è sufficiente copiare nella cartella in cui si trovano i file xml il foglio di stile distribuito dal Sistema di Interscambio.

I file xml generati a partire **dal 1 gennaio 2017** devono essere visualizzati con il foglio di stile della versione 1.2 fatturapa_v1.2.xsl scaricabile da http://areariservata.smeup.com/area-tecnica/aggiornamenti-sme-up-erp.html cartella **fatturaPA_n_ o dal link http://www.fatturapa.gov.it/export/fatturazione/sdi/fatturapa/v1.2/fatturapa_v1.2.xsl .

N.B. :  Per visualizzare l'xml con il foglio di stile aprire il file xml del messaggio usando i browser Mozilla Firefox, Microsoft Edge o Microsoft Internet Explorer.
Google Chrome non supporta i fogli di stile in cartelle locali.

In alternativa è possibile usufruire di software gratuiti che rendono gli XML ancora più leggibili.
Un software d'esempio è quello messo a disposizione da Assosftware a questo indirizzo : 

http://www.assosoftware.it/assoinvoice


### Visualizzare i messaggi di notifica
Per visualizzare l'xml dei messaggi di notifica contenenti le risposte da parte del Sistema di Intercambio in un formato più facilmente leggibile è sufficiente copiare nella cartella in cui si trovano i file xml dei messaggi i fogli di stile distribuiti dal Sistema di Interscambio.
I fogli di stile sono scaricabili da http://areariservata.smeup.com/area-tecnica/aggiornamenti-sme-up-erp.html cartella **fatturaPA -> Fogli_stile_messaggi  o dal link http://fatturapa.gov.it/export/fatturazione/it/normativa/f-3.htm .

N.B. :  Per visualizzare l'xml con il foglio di stile aprire il file xml del messaggio usando i browser Mozilla Firefox, Microsoft Edge o Microsoft Internet Explorer.
Google Chrome non supporta i fogli di stile in cartelle locali.
 :  : NPG

## Flusso di post-creazione xml

In concomitanza con la corretta creazione dell'xml della fattura è stato previsto un apposito flusso di azioni che permette all'avverarsi di questo evento di eseguire le azioni che può risultare opportuno applicare in questo dato momento.

L'oggetto del flusso è la fattura (oggetto FT) ed il codice del flusso azioni (B£H) è "V5FE00".

Sono inoltre forniti due sorgenti di esempio che prendono l'xml della fattura e lo spostano in un'altra cartella dell'IFS (V5FEES1) o in una cartella di rete con £H80 (V5FEES2).

 :  : DEC T(TA) P(B£H) K(V5FE00)
 :  : DEC T(MB) P(V5SRC) K(V5FEES1)
 :  : DEC T(MB) P(V5SRC) K(V5FEES2)

