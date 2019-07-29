# BRC - Modello di configurazione
 :  : DEC T(ST) K(BRC)
## OBIETTIVI
 :  : PAR
-    Caratterizzare il modello di configurazione associato ad un oggetto definendone i comportamenti ed i vincoli.
-    Il modello di configurazione ha due scopi :  definire la configurazione dell'oggetto quando è un assieme (configurazione orizzontale o verticale) e/quando è un componente (criterio di selezione). Questi due aspetti possono essere presenti contemporaneamente.

## INTRODUZIONE
Per ogni oggetto di cui si vogliono gestire più configurazioni possono porsi diverse modalità di gestione.
Esempi di configurazione sono : 
 :  : PAR
-    Colori di un materiale
-    Versione speciale di un prodotto finito
-    Offerta di un impianto

## CONTENUTO DEI CAMPI
 :  : FLD T$BRCA **Configurazione obbligatoria**
Si imposta l'obbligatorietà della configurazione.
Può assumere i seguenti valori : 
 :  : PAR
- '1'  Obbligatoria sia in anagrafica articoli, sia in gestione (righe di documenti di ciclo esterno, movimentazione di magazzino, ordini di produzione, ecc..)
- '2'  Facoltativa in anagrafica articoli e obbligatoria nei rimanenti casi. In questo caso non esiste una configurazione 'principale', ma deve essere selezionata ogni volta.

 :  : FLD T$BRCB **Codifica**
Se l'oggetto ha più di una configurazione possibile e s'intende memorizzarle preventivamente, in modo da poter scegliere la configurazione, si deve impostare questo campo (elemento della tabella C£B), che definisce il tipo di oggetto. Tali configurazioni sono memorizzate nell'archivio C£VARI0F, con chiave di ricerca dato dall'oggetto, da questo elemento e dalla configurazione.
 :  : FLD T$BRCC **Struttura orizzontale**
Indica una delle due metodologie di configurazione.
Questa è un insieme di caratteri eventualmente costruiti rispondendo a domande che condizioneranno la selezione dei componenti e/o delle fasi del ciclo. Il criterio di selezione (o modifica del contenuto) è descritto nella tabella BRS.
 :  : FLD T$BRCE **Modo di formattazione**
Il modo permette di indicare la struttura del questionario di costruzione : 

- A)   Collegamento al modello di struttura di una stringa definito nella tabella B£F.
-- Parametro :  Elemento della tabella B£F
- B)   Collegamento ad una tabella di gestione varianti. Parametro :  Elemento della tabella C£P
- C)   Collegamento ad un altro oggetto. Parametro :   Tipo e parametro oggetto
- D)   Descrizione libera. Parametro :  Libero
- E)   Barcode EAN13. Parametro :  Libero
- F)   Lancio di un programma specifico utente. Parametro :  Nome del programma


 :  : FLD T$BRCI.T$BRCE **Parametro di formattazione**
 :  : FLD T$BRCF **Struttura verticale**
(alternativa alla struttura orizzontale)
 :  : FLD T$BRCG **Modo di formattazione**
Il modo permette di indicare la struttura del questionario di costruzione : 

- A)   Gestito mediante domande /risposte. Parametro :  Elemento della tabella C£B
- B)   Gestito mediante parametri. Parametro :  Elemento della tabella C£E
- C)   Gestito mediante Build.UP. La struttura deve essere un modello (M.AR : X). La configurazione restituita sara un        progressivo numerico univoco all'interno del modello.


 :  : FLD T$BRCH.T$BRCG **Parametro di formattazione**
 :  : FLD T$BRC1 **Ridirezione distinta**
Permette di indicare alla funzione di scansione della distinta base un metodo diverso da quello classico (scansione della distinta per codice o per gruppo distinta) per ottenere i componenti di un prodotto.
_9_Esempio :  Per conoscere la distinta di un prodotto di stampaggio in ottone uso il peso, la percentuale di calo e il codice barra ottone, presente sulla classe materiale. In tal modo non devo costruire la distinta ma ho tutte le funzioni che la userebbero.
Tale funzione deve ovviamente essere implementata in modo specifico in fase di avviamento del sistema.
 :  : FLD T$BRC2 **Ridirezione ciclo**
Idem come sopra per il ciclo
 :  : FLD T$BRC3 **Univocità**
Campo introdotto a scopo documentativo, ma non utilizzato nell'applicazione
 :  : FLD T$BRCD **Criterio selezione per distinta**
È un elemento della tabella BRS :  se impostato, viene proposto all'atto dell'inserimento dei legami di distinta base, se il componente è un articolo con questo criterio di configurazione.
