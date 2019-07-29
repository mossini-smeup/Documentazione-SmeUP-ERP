# CRR - Tipo Richiesta Intervento
 :  : DEC T(ST) K(CRR)
## OBIETTIVI
Permettere la caratterizzazione delle diverse tipologie di richiesta.
esempio :  Azioni Correttive, Azioni Preventive, Richieste di Deroga, ecc.
## CONTENUTO DEI CAMPI
 :  : FLD T$CRRA **Tipo Griglia**
Ha lo scopo di descrivere l'oggetto/i della Richiesta e relativa obbligatorietà di compilazione.
Definisce il significato delle 3 chiavi variabili del tipo Richiesta (campo obbligatorio controllato nella tabella B£G).
 :  : FLD T$CRRB **Contenitore Note**
Definisce il contenitore delle Note strutturate utilizzato dal tipo Richiesta. Se non specificato assume un valore di default (RIN) (Campo controllato in tab. NSC).
 :  : FLD T$CRRC **Livello di Nascita**
Stabilisce il livello assunto in immissione.
esempio :  Attivo, immesso non attivo, da approvare, ecc.
 :  : FLD T$CRRD **Parametri Interni**
Definisce il significato della parte variabile dell'archivio (5 valori alfanumerici + 5 valori numerici) campo controllato in Tab. C£I).
 :  : FLD T$CRRE **Parametri Espliciti**
Configura i parametri aggiuntivi
 :  : FLD T$CRRF **Gruppo Flag**
Stabilisce il significato dei flags contenuti sull'archivio delle R.I.
 :  : FLD T$CRRG **Tp./Param. ente des.**
Serve a preimpostare/fissare la tipologia dell'Ente designato/Responsabile evasione.
esempio :  Dipendente, profilo utente di sistema, centro di lavoro,ecc.
 :  : FLD T$CRRH **Tp.Enti Modificabile**
Serve a fissare la tipologia dell'Ente Designato/Responsabile Evasione. Se impostato "1" il tipo è solo precompilato ma
modificabile se " " il tipo viene fissato.
 :  : FLD T$CRRI **Numeratore RI**
Configura la struttura del numeratore identificativo della R.I.
 :  : FLD T$CRRJ **Intestazione campo 1**
Intesta il primo campo descrittivo della R.I.
 :  : FLD T$CRRK **Intestazione campo 2**
Intesta il secondo campo descrittivo della R.I.
 :  : FLD T$CRRL **Intestazione campo 3**
Intesta il terzo campo descrittivo della R.I.
 :  : FLD T$CRRM **Intestazione campo 4**
Intesta il quarto campo descrittivo della R.I.
 :  : FLD T$CRRN **Intestazione campo 5**
Intesta il quinto campo descrittivo della R.I.
 :  : FLD T$CRRO **Giorni Scadenza**
Indica il numero di giorni antecedenti la data di evasione programmata per i quali viene evidenziata la R.I.
 :  : FLD T$CRRP **Suffisso pgm Aggiustamento**
Un carattere specificato in questo spazio chiama un programma definito di aggiustamento per il trattamento delle forzature di vario genere previste per il tipo RI. Il nome del programma è dato dal prefisso CQRD01D_(x) + il valore assegnato in questo spazio.
 :  : FLD T$CRRQ **Workflow di gestione**
Indica quale processo di workflow si occupa della "vita" della richiesta di intervento dopo il suo inserimento.
