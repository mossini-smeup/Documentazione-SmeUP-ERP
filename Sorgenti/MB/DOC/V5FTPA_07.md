# Caricamento Codici Univoci Ufficio PA FE con Sme.UP Provider

## Descrizione
E' stato implementato un pgm V5FTPA2 che è possibile schedulare per il reperimento e il caricamento dei codici univoci ufficio PA per la fattura elettronica.
Allo stato attuale l'elenco dei codici viene aggiornato dall'Indice PA ogni mattina alle 6 : 00.
Il programma scarica tramite Sme.UP Provider il file contenente l'anagrafica dei codici univoci uffico per la FE, mettendolo su IFS in /Smedoc/FatturaElettronica/[CodiceAzienda]/IPA
e provvede ad inserire / aggiornare dei contatti di tipo £PA nell'anagrafica degli enti.
I codici non più validi (rimossi dal file fornito dall'indice PA) vengono portati a livello 8.
La ricerca / controllo dei codici assegnati al cliente nell'estensione £51 dipende dall'attivazione in tabella V50.
**L'utilizzo di tale soluzione ha come prerequisito una versione di Sme.UP Erp V2R3**  **o superiore e uno Sme.UP Provider versione Tower Bridge a cui sia stato applicato l'ultimo **upgrade disponibile.**

## Configurazione
Installazione di uno Sme.UP Provider (versione Tower Bridge), a cui sia stato applicato l'ultimo upgrade disponibile, la cui documentazione specifica è inclusa in fondo al documento.
Fasatura degli elementi £PA delle tabelle BRE e BRZ.
La cartella /Smedoc su IFS deve essere raggiungibile dalla macchina su cu si sia installato lo Sme.UP Provider come condivisione in Lettura/Scrittura.
Impostare la variabile TMPSHRDFLD nell'SCP_CLO con una cartella temporanea condivisa accessibile dal provider.
Impostazione della tabella V50 con il campo T$V50H (Ctr Cod.Un.Uf.FE PA) a "1" e  con il nome della coda di comunicazione con il Sme.UP Provider nel campo "Sme.UP Provider Ft PA" .

Si consiglia la schedulazione dell'esecuzione del V5FTPA2 ogni mattina alle ore 7.
 :  : NPG
