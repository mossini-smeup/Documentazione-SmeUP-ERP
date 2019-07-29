L'estrazione delle frasi in italiano serve a definire quali frasi vanno trasferite nell'archivio A£TRDE0F per essere tradotte.
L'estrazione degli oggetti standard viene effettuata a standard in ambito 00.
L'estrazione di oggetti non standard viene effettuata presso il cliente in ambiti >=10.
Attenzione :  per oggetti personalizzati vengono estratte solo le frasi non già presenti nello standard; anche le descrizioni degli elementi di tabella vengono estratte solo se non già estratte a standard (perchè elementi di tabella del modello).

# Oggetti interessati

Sono estratti e tradotti i seguenti tipi di oggetti di Sme.UP : 
 * Programmi - OJ*PGM (frasi in schiera). Traduzione :  dinamica.
 * Display file - OJ*DSPF. Traduzione :  oggetto da generare in lingua. Attenzione :  l'oggetto in lingua serve SOLO per il 5250, in emulazione in Looc.UP la traduzione è dinamica.
 * Printer file - OJ*PRTF. Traduzione :  oggetto da generare in lingua.
 * Message file - OJ*MSGF. Traduzione :  oggetto da generare in lingua.
 * Script - MBSCP* (es. SCP_SCH, SCP_CFG). Traduzione :  dinamica.
 * Campi di file - REF-. Traduzione :  dinamica.
 * Campi di tabella - RET-. Traduzione :  dinamica.
 * Settori - ST. Traduzione :  dinamica.
 * Elementi di tabella - TA*. Traduzione :  statica/dinamica.
 * Schemi - OGSP.
 * Attributi - OA. Traduzione :  dinamica.

Attenzione ai programmi con video, dove le frasi si dividono in due contesti (OJ*PGM e OJ*DSPF).

# Contesti

La coppia frase/contesto è l'unità minima di traduzione.
Il contesto è, al minimo, un oggetto (tipo/parametro/codice); certi tipi di oggetto gestiscono maggiori livelli di dettaglio (ad esempio il formato nei file video).
Due considerazioni : 
 * In alcuni casi il livello di dettaglio del contesto non è il massimo ottenibile :  ad esempio, nei file video il livello di dettaglio è al formato, quindi due frasi uguali presenti nello stesso formato non possono avere due traduzioni diverse. Idem per gli elementi di una schiera.
 * Per praticità in diversi posti di Sme.UP vengono presentate insieme tutte le frasi appartenenti ad uno stesso oggetto (mettendo insieme diversi contesti, ad esempio i diversi formati di un video).

Oggetti e livelli di dettaglio : 
 * OJ*PGM (CODI=programm) :  DET1=nome schiera.
 * OJ*MSGF (CODI=file) :  DET1=codice messaggio.
 * OJ*DSPF (CODI=file) :  DET1=nome formato.
 * OJ*PRTF (CODI=file) :  DET1=nome formato.
 * RET- (CODI=settore+sottosettore) :  DET1=campo, DET2=V1/V2/V3/V4 se limiti/valori.
 * REF- (CODI=file) :  DET1=campo.
 * MB* (CODI=membro) :  DET1='DES' se descrizione del membro.
 * OGSP (CODI=sottosettore INT) :  DET1=elemento schema.
 * OA (CODI=classe) :  DET1=codice attributo (da cambiare).
 * TA* (CODI=elemento) :  non c'è maggior livello di dettaglio. Trattabili insieme per T/P.
 * ST* (CODI=settore) :  non c'è maggior livello di dettaglio.


# Estrazione

Sono previste due modalità di estrazione delle frasi in italiano : 
 * Estrazione globale schedulata, impostabile tramite exit.
 * Estrazione parziale di oggetti interessanti, lanciabile da menù.

**Attenzione : **
 * E' obbligatorio lanciare l'estrazione da un ambiente in italiano (non tradotto)
 * È sempre consigliabile avere in linea le librerie da cui si estrae quando si lancia un'estrazione. Per le tabelle questo è obbligatorio.

**Nota : **
Al termine dell'estrazione di un oggetto le frasi di quell'oggetto che non sono più esistenti non vengono cancellate ma vengono impostate con S1STOR='80'

Per approfondimenti sulle modalità di lancio vedere l'help del programma A£TR01.

# Casistiche particolari

## Contesti particolari

Segnaliamo : 
 * Menù e pop.up di Looc.UP :  TAMEA£L e TAMEA£S.
 * Frasi del client Looc.UP :  script LANGUAGE di MBSCP_CLO.

## Forzature su estrazioni

Non vengono estratte : 
 * Frasi nei programmi B£OA*, schiere SLT e SLI. Ne viene estratto direttamente l'output, da B£SLOT.
 * Descrizioni di script di schede cruscotto (SCP_SCH/*_CRU). Non vengono visualizzate.
 * Descrizioni di script di setup di prospettive clienti (SCP_SET/CN_*).

## Estrazioni multiple

Queste casistiche, seppur originate da un solo contesto, vengono per semplicità estratte in più contesti : 
 * Tabelle standard deviate;
 * Schiere di testo derivanti da inclusione di /COPY;
 * Testo derivante da inclusione di script.
In tutti questi casi vengono quindi estratte (e vanno tradotte) diverse versioni della stessa frase, una per ogni contesto.
Per mitigare lo svantaggio del dovere tradurre più volte la stessa frase è possibile attivare l'opzione di precompilazione traduzioni in tabella A£1.

## Casi non gestiti

Non vengono gestiti (o lo sono in maniera non ottimale) dalle traduzioni : 
 * Nei programmi, schiere con PERRCD>1 :  gestiti come una riga sola.
 * (Per adesso) Intestazioni nell'attributo Formulas nei tag G.SET.MAT. Per adesso portare nei servizi la composizione dei setup, portando in schiera tradotta le intestazioni.
 * Schiere nei programmi più lunghe di 300. Si consiglia di spezzare in più schiere.


