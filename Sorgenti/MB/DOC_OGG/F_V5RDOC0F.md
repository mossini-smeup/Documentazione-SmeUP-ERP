## Contenuto
Dati delle righe dei documenti del ciclo esterno.

## Codice Oggetto (in TA/*CNTT)
'DO'                               £FUNT1

## Chiave primaria
R§TDOC   Tipo documento      (TA/V5D)       £FUNP1
R§NDOC   Numero documento                   £FUNK1    Pos.1-10
R§NRIG   Numero riga         (NR)           £FUNK1    Pos 11-14

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
Identificativo oggetto R§IDOJ.

## Tabelle guida
Le impostazioni che condizionano questo archivio sono contenute nei settori di tabella : 
V5D (Tipo documento)
 :  : DEC T(ST) K(V5D)
V5A (Modello documento)
 :  : DEC T(ST) K(V5A)
V5A (Tipo riga)
 :  : DEC T(ST) K(V5B)

## Autorizzazioni
 * _2_Autorizzazione gestione righe documenti, Classe = V5DO05, Funzione = Tipo documento
 * _2_Autorizzazione gestione righe x modello, Classe = V5DO05M, Funzione = TTTMMM (TTT = Tipo documento, MMM = Modello documento)
 * _2_Autorizzazione interrogazione righe documenti, Classe = V5DO05I, Funzione = Tipo documento
 * _2_Autorizzazione campi specifici, Classe = PLC-V5RDOC, Funzione = Tipo documento
 * _2_Autorizzazione dati riservati da "lista campi" di un oggetto, Classe = RIS-, Funzione = V5D-TTT (dove TTT = Tipo documento)
 * _2_Autorizzazione dati riservati da "lista numeri" di un oggetto, Classe = RIS-, Funzione = VL_DRTTT (dove TTT = Tipo documento)
 * _2_Autorizzazione "sintesi conti spese tasse" di un documento, Classe = RIS-, Funzione = V5DTTT (dove TTT = Tipo documento)
 * _2_Autorizzazione "Funzioni aggiuntive - F14" di un documento, Classe = ABILITA, Funzione = V5DO05D
 * _2_Autorizzazione "Funzioni di un oggetto - F10", Classe = B£FUN0, Funzione = DR .

## Note strutturate (Tabella NSC)
Il contenitore note si assume dalla tabella V5A.
Chiave 1 - Tipo Documento
Chiave 2 - Nro Documento
Chiave 3 - Nro Riga

## Parametri (Tabella C£E)
La categoria si assume dalla tabella V5B.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-DRyyy, dove yyy è il tipo documento; se assente viene associato il flusso x-DR.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
Il visualizzatore viene impostato nel tipo riga (Tab. V5Bxx).

## Programmi di controllo
Nella tabella V5B si può impostare : 
- il suffisso del programma di inizializzazione
 :  : DEC T(CS) P(T/V5A) K(T$V5B£) R(1)
- il suffisso del programma di controllo campi
 :  : DEC T(CS) P(T/V5A) K(T$V5B4) R(1)

## /COPY
Interfaccia righe documenti (£IDR) : 
 :  : DEC T(MB) P(QILEGEN) K(£IDR) X(F(EXD;*SCO;) 1(MB;QILEGEN;£IDR) 2(;;))

Inizializzazione righe documenti (£V5Z) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5Z) X(F(EXD;*SCO;) 1(MB;QILEGEN;£V5Z) 2(;;))

Funzioni valori (£V5V) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5V)

Funzioni quantità (£V5Q) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5Q)

Funzioni note documento (£V5N) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5N)

## Gruppi flag
Il gruppo flag è impostato nel tipo riga (Tab. V5B). Se assente si risale al modelllo documento (Tab. V5A), e al tipo documento (V5D).

## Workflow e popup
Sensibile alla gestione popup, se attivata in B£2.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD T§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella V5B.
Se assente, si assume il livello 2.

 :  : FLD T§STAT **Stato**
Il suo subsettore  è definito in tabella V5B.
In inserimento si assume lo stato inserito in tabella V5B.
Se assente si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD R§DT01 **Data 1**
Si possono trattare fino a 10 date definite nel sottosettore 'V5' della tabella C£J. I significati sono dati dagli elementi 'Xyy' dove X è il flag N.21 dell'archivio e yy va da 01 a 10. L'elemento 'X ' dà il significato al titolo del gruppo date. Se il secondo flag non è impostato non si gestiscono le date interne.
 :  : FLD R§DT02.R§DT01 **Data 2**
 :  : FLD R§DT03.R§DT01 **Data 3**
 :  : FLD R§DT04.R§DT01 **Data 4**
 :  : FLD R§DT05.R§DT01 **Data 5**
 :  : FLD R§DT06.R§DT01 **Data 6**
 :  : FLD R§DT07.R§DT01 **Data 7**
 :  : FLD R§DT08.R§DT01 **Data 8**
 :  : FLD R§DT09.R§DT01 **Data 9**
 :  : FLD R§DT10.R§DT01 **Data 10**

 :  : FLD R§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella V5B.
 :  : FLD R§COD2.R§COD1 **Codice 2**
 :  : FLD R§COD3.R§COD1 **Codice 3**
 :  : FLD R§COD4.R§COD1 **Codice 4**
 :  : FLD R§COD5.R§COD1 **Codice 5**
 :  : FLD R§CD06.R§COD1 **Codice 6**
 :  : FLD R§CD07.R§COD1 **Codice 7**
 :  : FLD R§CD08.R§COD1 **Codice 8**
 :  : FLD R§CD09.R§COD1 **Codice 9**
 :  : FLD R§CD10.R§COD1 **Codice 10**

 :  : FLD R§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella V5B.
 :  : FLD R§NUM2.R§NUM1 **Numero 2**
 :  : FLD R§NUM3.R§NUM1 **Numero 3**
 :  : FLD R§NUM4.R§NUM1 **Numero 4**
 :  : FLD R§NUM5.R§NUM1 **Numero 5**
 :  : FLD R§NR06.R§NUM1 **Numero 6**
 :  : FLD R§NR07.R§NUM1 **Numero 7**
 :  : FLD T§NR08.R§NUM1 **Numero 8**
 :  : FLD T§NR09.R§NUM1 **Numero 9**
 :  : FLD T§NR10.R§NUM1 **Numero 10**
