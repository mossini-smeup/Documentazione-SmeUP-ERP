# Introduzione

Nella preparazione di un sistema informativo misto (ACG V3R3, TIM e SMEUP) gli scenari che possono verificarsi sono almeno due : 
- Anagrafiche deviate
- Anagrafiche da convertire
Il prossimo paragrafo elenca i passi da seguire per attivare la deviazione degli enti.
In caso di anagrafiche da convertire si rimanda alla documentazione del modulo B£CONV.

 :  : DEC T(MB) P(A8_SM) K(DOC_C5) D(Conversioni ACG V3.3)  I( Conversioni ACG V3.3 >>)
 :  : PAR
**Nota benissimo :  Obbligatorie in linea le libreria acg sia dati per le conversioni, sia oggetti per interfaccie.


# Passi per attivare la deviazione
 T(_1_Azioni sulle tabelle)
- TA B£1 :  compilare A7/ A8 su Clienti, fornitori, articoli

  :  : DEC T(TA) P(B£1) K(*) D(B£1 PERSONALIZZAZIONE B£ >>) I(B£1 PERSONALIZZAZIONE B£ >>)
 C(*CONT)
- TA B§O :  codifica oggetti deviati (CNCLI, CNFOR, ecc) compilando nome file, campo_1, campo descrizione. Rispettivamente
ANCL200F, CDCLI, RASCL
ANFO200F, CDFOR, RASFO

  :  : DEC T(TA) P(B§O) K(CNCLI) D(B§O Relazione oggetto-database >>)  I(B§O Relazione oggetto-database >>)
  :  : DEC T(TA) P(B§O) K(CNFOR) D(B§O Relazione oggetto-database >>) I(B§O Relazione oggetto-database >>)
 C(*CONT)
- TA BRE :  Su clienti e fornitori indicare codice interfaccia e Ambiente x interfaccia ente/articolo

  :  : DEC T(TA) P(BRE) K(CLI)  D(BRE Tipo contatto >>)  I(BRE Tipo contatto >>)
  :  : DEC T(TA) P(BRE) K(FOR)  D(BRE Tipo contatto >>)  I(BRE Tipo contatto >>)
 C(*CONT)
- TA B£I :  deviare la tabella Banche. Indicare l'oggetto O, tipo e parametro oggetto CN BAN e flaggare l'attivazione come globale e specifica.
Nel caso in cui la gestione dell'elemento BAN nella tabella B£I restituisse un messaggio di errore verificare l'esistenza della definizione della tabella BAN.
Se assente crearla con l'UP DEF.

  :  : DEC T(TA) P(B£I) K(BAN) D(B£I Deviazione tabelle >>)  I(B£I Deviazione tabelle >>)

 T(_1_Prerequisiti per il funzionamento della deviazione enti)
Oltre alle interfacce A8 ACG V3.3 sono state incluse nel FILE SRC_A8 programmi di utilità.
Tali programmi sono suddivisi per argomento con un acronimo nella riga di descrizione del programma e ulteriormante commentati all'interno del sorgente.
Gli acronimi sono : 
. GB                 Archivi
. CA                 Contabilità
. IV                   IVA
. CE                 Cespiti
. PE                 Portafoglio effetti
. xx                   xxxxxxxxxxx
Come le interfacce anche i programmi sono disponibili solo come sorgenti e sono da compilare presso il cliente.
Quindi : 
- Verificare l'esistenza del file sorgente SRC_A8 o crearlo duplicando i sorgenti dal file sorgente SRC_A7
- Correggere le /copy £IRCA8 e £IRFA8
- Correggere/ Compilare i seguenti programmi nel file sorgente SRC_A8 : 
-- B£IFCO_A8  Interfaccia Anagrafico Clienti fornitori
-- B£ICSM  Interfaccia anagrafico
-- B£ICA8 clienti
-- B£IFA8 fornitori
-- B£IR*  ricerche clienti e fornitori (/copy £IRCA8, /copy £IRFA8) sotto Loocup
- Correggere le /copy £IRCA8 e £IRFA8


 :  : PAR T(_1_Nota bene) L(PUN)
- Occorre personalizzare l'ampiezza del video di ricerca clienti acg AR10A00V nella libreria dei sorgenti personalizzati a 132 e ricompilare AR10A. (Per sicurezza farlo anche per la ricerca fornitore).
- Verificare se è necessario allineati anche i programmi di deviazione, in caso affermativo andrà creato il file source SRC_A8.
- Ricerche alternative e personalizzate sotto Loocup : 
-- Impostare il setup configurazione per ricerche da SCP_QRY
oppure
-- Gestire nei programmi di interfaccia B£ICA8 e B£IFA8 se siamo in loocup o emulazione
XRCR01   ricerca clienti da loocup
XRCR02  ricerca fornitori da loocup
- Da approfondire il contenuto della SRC_A7 -> SRC_A8



 :  : REM
_4_Verifiche di presenza
 Se assenti impostare librerie con documento "Verifiche ambiente DEMO"
 Le impostazioni vengono acquisite al prossimo ingresso
> Principali archivi di dati
  :  : DEC T(OJ) P(*FILE) K(ANPA200F) I(Articoli          >>)
  :  : DEC T(OJ) P(*FILE) K(ANCL200F) I(Clienti           >>)
  :  : DEC T(OJ) P(*FILE) K(ANFO200F) I(Fornitori         >>)
  :  : DEC T(OJ) P(*FILE) K(ANCO200F) I(Conti / Vedi nota >>)
  :  : DEC T(OJ) P(*FILE) K(KPJBA) I(*NONE)
> Principali programmi
  :  : DEC T(OJ) P(*PGM) K(B£IAA8)   I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£ICA8)   I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£ICE_A8) I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£IE4_A8) I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£IE5_A8) I(*NONE)

_4_Oggetti gestiti
  :  : DEC T(TA) P(B£I) K(C5B) I(_7_Conti **(F A8 Programma C5PDC_A8))
  _7_Articoli
  _7_Clienti/Fornitori

_4_Esecuzione dei TEST
 :  : INI _7_Impostazioni deviatori
 :  : CMD CALL B£IFVE
 :  : FIN
 :  : INI **Ricerca Articoli
 :  : CMD CALL B£AR20 PARM('AR' ' ' '?')
 :  : FIN
 :  : INI **Ricerca Clienti
 :  : CMD CALL B£AR20 PARM('CN' 'CLI' '?')
 :  : FIN
 :  : INI **Ricerca Conti
 :  : CMD CALL B£AR20 PARM('CO' '' '?')
 :  : FIN
 :  : INI **Ricerca Cespiti
 :  : CMD CALL B£AR20 PARM('CE' '' '?')
 :  : FIN

_4_Compilazione programmi in libreria SMEUP_EXT
 :  : INI _7_Compilazione di tutti i programmi (BASE)
 :  : CMD CALL B£UT11 PARM('B£*' 'SRC_A8' 'SMESRC')
 :  : FIN

 :  : INI _7_Compilazione di tutti i programmi (IN SVILUPPO)
 :  : CMD CALL B£UT11 PARM('*ALL' 'SRC_A8' 'SMEDEV')
 :  : FIN
 :  : REM.END
