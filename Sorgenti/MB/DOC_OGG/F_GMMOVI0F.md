## Contenuto
Tutte le informazioni significative di una transazione di magazzino (quantità, valori, date, codici, documenti, ecc..).

## Codice Oggetto (in TA/*CNTT)
'E1'                               £FUNT1

## Chiave primaria
S§NURE  Numero registrazione       £FUNK1

## Altri condizionamenti facoltativi in ricerca

## Ulteriore chiave primaria

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle GMC (Causale movimento) : 
 :  : DEC T(ST) K(GMC)

## Autorizzazioni
Le autorizzazioni si reperiscono nel seguente modo : 
 *  classe di autorizzazione ABILITA
 *  funzione MOV-MAGx, dove x è il gruppo di autorizzazione impostato nella causale di movimentazione.

## Note strutturate (Tabella NSC)
Definito in impostazioni generali GM (Tab. GM1).
Chiave consigliata = oggetto E1.

Il contenitore si assume dalla tabella GM1. Se non inserito si assume AR.
Chiave 1 - Numero registrazione
Chiave 2 - N.A.
Chiave 3 - N.A

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-E1yyy, dove yyy è la causale del movimento :  se assente viene associato il flusso x_E1.
NB :  il flusso per causale non è attivo per le Azioni eseguibili.
Ogni programma che esegue la transazione imposta il proprio nome nel contesto (campo della £FUNDS1).

In  tabella GMC ad un movimento possiamo anche associare gruppi di azioni di movimentazione (Tab. GMH) queste azioni possono essere lanciate : 
 * in fase di creazione del movimento, dal programma monitor di inserimento
 * in fase di scrittura del movimento, dal programma di applicazione.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
Il visualizzatore del dettaglio del movimento viene definito in Tab. GMC.
Nella movimentazione manuale a 2 causali (PGM -  GMMV02I) esiste una seconda possibilità di definire il programma di visualizzazione :  impostato nella tabella B££xx.

## Programmi di controllo

## /COPY
Interfaccia movimenti di magazzino (£IE1) : 
 :  : DEC T(MB) P(QILEGEN) K(£IE1)

Scansione movimenti di magazzino (£GMD) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMD)

Azioni su archivio GMMOAR (£GMF) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMF)

Filtro movimenti di magazzino (£GMG) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMG)

Statistiche di magazzino (£GMS) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMS)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.

## CONTENUTO DEI CAMPI

 :  : FLD S§NURE **Numero registrazione**
Si assume il numeratore definito in tabella GM1, (tabella CRN, sottosettore GM).

 :  : FLD S§TIMO **Tipo movimento**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCM) R(1)

 :  : FLD S§TIGC **Area giacenza**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCA) R(1)

 :  : FLD S§SOGC **Tipo giacenza**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCT) R(1)

 :  : FLD S§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella GMC.
 :  : FLD S§COD2.S§COD1 **Codice 2**
 :  : FLD S§COD3.S§COD1 **Codice 3**
 :  : FLD S§COD4.S§COD1 **Codice 4**
 :  : FLD S§COD5.S§COD1 **Codice 5**

 :  : FLD S§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella GMC.
 :  : FLD S§NUM2.S§NUM1 **Numero 2**
 :  : FLD S§NUM3.S§NUM1 **Numero 3**
 :  : FLD S§NUM4.S§NUM1 **Numero 4**
 :  : FLD S§NUM5.S§NUM1 **Numero 5**
