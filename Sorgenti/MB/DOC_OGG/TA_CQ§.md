# CQ§ - Personalizzazione Tipo NC
 :  : DEC T(ST) K(CQ§)
## OBIETTIVO
Definire le impostazioni e i valori di default che verranno utilizzati nella gestione delle Non Conformità.
## CONTENUTO DEI CAMPI
 :  : FLD T$CQ§A **Griglia di Controllo**
Definisce il significato delle 3 chiavi variabili del tipo Non Conformità (campo obbligatorio controllato nella tabella B£G).
 :  : FLD T$CQ§B **Contenitore Note**
Definisce il contenitore delle Note strutturate utilizzato dal tipo Non Conformità. Se non specificato assume un valore di default (NCO) (Campo controllato in tab. NSC).
 :  : FLD T$CQ§C **Parametri Impliciti**
Definisce il significato della parte variabile dell'archivio Non Conformità (5 valori alfanumerici + 5 valori numerici) campo controllato in Tab. C£I).
 :  : FLD T$CQ§D **Livello di Nascita**
Stabilisce il livello assunto in immissione della Non Conformità.
_9_Esempio :  Attiva, da approvare,ecc.(Tab.B£W).
 :  : FLD T$CQ§E **Gruppo Flag**
Stabilisce il significato dei flags contenuti sull'archivio delle Non Conformità.(Tab.B£Y).
 :  : FLD T$CQ§F **Categoria Parametri**
Configura i parametri aggiuntivi (Tab. C£E).
 :  : FLD T$CQ§G **Numeratore N.C.**
Configura la struttura del numeratore identificativo della Non Conformità(Tab CRNNC).
 :  : FLD T$CQ§H **Caratterizzazione N.C.**
Definisce alcuni attributi della N.C.
_9_Esempio :  Tipo costo, riclassifiche, ecc. (Tab. CQE).
 :  : FLD T$CQ§I **Sottosettore Difetti**
Definisce da quale sottosettore della Tab. CQD attingere il difetto.
 :  : FLD T$CQ§P **Ente Rilevatore**
Imposta per il tipo N.C.  il soggetto rilevatore
_9_Es. : 
Dipendente, Cliente, Fornitore, Reparto,ecc.
Imposta per il tipo N.C.  il soggetto responsabile
_9_Es. : 
Dipendente, Cliente, Fornitore, Reparto,ecc.
 :  : FLD T$CQ§L **Pgm Rif. Addebiti**
Chiamata ad un programma esterno per il trattamento dei dati relativi alla responsabilità della N.C.
_9_Esempio :  il tipo N.C. ART che supporta le NC derivanti dai lotti, esegue il programma CQNCX01 NCNF Fmt Esterno dati.
Lotto che si occupa di trattare tutte le forzature su NC derivanti da lotti qualità :  quadrature tra lotto responsabile, articolo responsabile, ente responsabile, esplosione distinta base, ecc.
Naturalmente il programma deve esistere ed avere parametri compatibili (vedi CQNCX01).
 :  : FLD T$CQ§Y **Suffisso pgm Quadratura**
Un carattere specificato in questo spazio chiama un programma specifico per il trattamento delle quantità.
_9_Esempio :  se stabilisco che la quantità X non può superare la quantità Y diviso per Q Z ecc,ecc. scriverò un pgm che fa queste considerazioni con nome CQNC01Q_(x) dove x è il carattere che poi andrò a specificare qui.
Se non specificato esegue il programma standard CQNC01Q.
 :  : FLD T$CQ§W **Suffisso pgm Aggiustamento**
Un carattere specificato in questo spazio chiama un programma definito di aggiustamento per il trattamento delle forzature di vario genere previste per il tipo NC. Il nome del programma è dato dal prefisso CQNC01D_(x) + il valore assegnato in questo spazio.
_9_Esempio :  il tipo NC ART che supporta gli aggiustamenti derivanti dal legame con il lotto qualità esempio Qta lotto, data collaudo, ecc. ha in questo spazio il valore A che esegue il pgm CQNC01D_A che si occupa di allineare i suddetti dati tra i due archivi.
 :  : FLD T$CQ§M **Gestione in Lista**
Campo controllato dai valori standard di Sme.up SI/NO
Se specificato SI, attiva in fase di inserimento Non conformità il programma di gestione in Lista delle NC(CQNC01R).
La gestione in Lista ha lo scopo di velocizzare l'inserimento di più NC sullo stesso Lotto.
