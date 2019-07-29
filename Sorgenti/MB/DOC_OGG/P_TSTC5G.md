# FUNZIONI SU RAPPORTI BANCARI

## OBIETTIVI

 Svolgere una serie di funzioni di carattere eterogenee aventi in comune come oggetto di analisi un  rapporto bancario.

## FUNZIONI/METODI

### INZ/SCA  - Scansione Movimenti

 Tramite la combinazione delle funzioni INZ/SCA è possibile scandire i movimenti di un dato rapporto bancario  secondo i criteri definiti dal metodo.

**METODI**

* OPE :  Movimenti Contabili per data operazione
* VAL :  Movimenti Contabili per data valuta
* CST :  Scadenze presentate sul c/sbf
* STI :  Scadenze da contabilizzare attribuibili al rapporto. L'attribuzione si basa sull'indicazione esplicita del rapporto bancario o sulla sola indicazione della banca azienda. In ques'ultimo caso per le riba viene attribuito il c/sbf mentre per tutto il resto viene attribuito il c/c.


**DATI INPUT**

* AZ Azienda - Obbligatorio
* RP Rapporto Bancario - Obbligatorio
* CO Conto Contabile - Obbligatorio
* NF N° Finanziamento - Facoltativo
* DI Data Inizio - Obbligatoria
* DF Data Fine - Obbligatoria
* PE Pertinenza - Facoltativo
* CD Condizione - Facoltativo
* RR Ritorno Record - Forza il ritorno dell'intero record del movimento nel campo £C5GRE



**DATI OUTPUT**

* TO Tipo Oggetto Movimento
* OG Codice Oggetto Movimento
* DA Data Movimento (a seconda del metodo assume alternativamente la data operazione o la data valuta)
* DO Data Operazione Movimento
* DU Data Valuta Movimento
* IM Importo Movimento
* VA Valuta Movimento
* CA Cambio Movimento
* IV Importo Valuta Movimento


### SAL - Calcolo Saldo

 Dato un rapporto ritorna il saldo ad una data secondo il criterio definito dal metodo.

**METODI**

* OPE :  Movimenti Contabili per data operazione
* VAL :  Movimenti Contabili per data valuta
* CST :  Scadenze presentate sul c/sbf


**DATI INPUT**

* AZ Azienda - Obbligatorio
* RP Rapporto Bancario - Obbligatorio
* CO Conto Contabile - Obbligatorio
* NF N° Finanziamento - Facoltativo
* DF Data Situazione - Obbligatoria
* PE Pertinenza - Facoltativo
* CD Condizione - Facoltativo


**DATI OUTPUT**

* ST Saldo
* FD Fido
* SD Saldo Definitivo
* SL Saldo Simulate
* DD Saldo Dare Definiti
* DL Saldo Dare Simulate
* DT Saldo Dare Totale
* AD Saldo Avere Definit
* AL Saldo Avere Simulat
* AT Saldo Avere Totale
* SV Saldo Def.- Valuta
* SY Saldo Sim.- Valuta
* SX Saldo Tot.- Valuta
* DV Saldo Dare Def.- Va
* DY Saldo Dare Sim.- Va
* DX Saldo Dare Tot.- Va
* AV Saldo Avere Def.- V
* AY Saldo Avere Sim.- V
* AX Saldo Avere Tot.- V


### FIA - Scansione Finanziamenti Aperti ad una Data

 A seconda che venga passata solo la data finale o sia la data iniziale che finale, su rapporto ritorna : 
 - I finanziamenti aperti (se passo solo la data finale)
 - I finanziamenti aperti alla data finale o chiusi fra data iniziale/finale (se passo entrambe le date)

**METODI**

* INZ :  Inizializza ed esegue la prima scansione
* RIT :  Continua la scansione


**DATI INPUT**

* AZ Azienda - Obbligatorio
* RP Rapporto Bancario - Obbligatorio
* CO Conto Contabile - Obbligatorio
* IN Data Iniziale - Facoltativa
* DF Data Finale - Obbligatoria


**DATI OUTPUT**

* NF Numero Finanziamento


### FIN - Funzioni su un Finanziamento

 A seconda del metodo da un rapporto/finanziamento ritorna i riferimenti della registrazione di apertura
 o il suo residuo.

**METODI**

* APE :  Ritorno Riferimenti Apertura
* RES :  Calcolo Residuo


**DATI INPUT**

* AZ Azienda - Obbligatorio
* RP Rapporto Bancario - Obbligatorio
* CO Conto Contabile - Obbligatorio
* NF Numero Finanziamento - Obbligatorio
* E4 N° Registrazione - Facoltativo, solo per funzione RES, permette di escludere la registrazione passata dal calcolo
* DF Data Situazione - Facoltativo, solo per funzione RES


**DATI OUTPUT - METODO APE**

* E4 N° Registrazione
* DO Data Operazione Movimento
* DU Data Valuta Movimento
* IM Importo Movimento
* VA Valuta Movimento
* CA Cambio Movimento
* IV Importo Valuta Movimento


**DATI OUTPUT - METODO RES**

* IM Residuo
* IV Residuo in Valuta


### GEN - Generazione Registrazioni Automatiche

 Tramite questa funzione vengono generate alcune forme di registrazioni automatiche.

**METODI**

* PFI :  Piano Ammortamento Finanziamento (con richiesta di conferma)
* PFI_BLI :  Piano Ammortamento Finanziamento - Cieca (senza richiesta di conferma)


**DATI INPUT**

* AZ Azienda - Obbligatorio
* RP Rapporto Bancario - Obbligatorio
* CO Conto Contabile - Obbligatorio
* NF Numero Finanziamento - Obbligatorio


### BAA - Riferimenti Rapporti Bancari

 Questa funzione è l'unica che non elabora movimenti, ma elabora la struttura anagrafica dei rapporti bancari.

**METODI**

* RIC :  Ritorno Riferimenti da AbiCab di una Banca Azienda
* RAP :  Ritorno Riferimenti da Rapporto Bancario


**DATI INPUT**

* AZ Azienda - Obbligatorio
* AB Codice AbiCab - Obbligatorio per funzione RIC
* RP Rapporto Bancario - Obbligatorio per funzione RAP


**DATI OUTPUT

* RB Rapporto Bancario
* RD Descrizione Rapporto Bancario
* RS DS Rapporto Bancario
* CO Conto Contabile
* DC Descrizione Conto Contabile
* CS DS Conto Contabile
* DK Data Consolidamento Rapporto
* DN Data Successiva al Consolidamento
* BA Banca Azienda
* BD Descrizione Banca Azienda
* BS DS Banca Azienda
* RC Rapporto di c/c della Banca azienda
* RF Rapporto di sbf della Banca azienda


