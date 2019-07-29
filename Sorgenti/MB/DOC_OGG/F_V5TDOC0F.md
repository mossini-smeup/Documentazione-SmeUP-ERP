 :  : DEC T(OJ)  P(*FILE) K(V5TDOC0F)
## Contenuto
Dati generali di un documento del ciclo esterno.

## Codice Oggetto (in TA/*CNTT)
'DO'                               £FUNT1

## Chiave primaria
T§TDOC   Tipo documento      (TA/V5D)      £FUNP1
T§NDOC   Numero documento                  £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
Identificativo oggetto T§IDOJ.

## Tabelle guida
Le impostazioni che condizionano questo archivio sono contenute nei settori di tabella : 
V5D (Tipo documento)
 :  : DEC T(ST) K(V5D)
V5A (Modello documento)
 :  : DEC T(ST) K(V5A)

## Autorizzazioni
 * _2_Autorizzazione gestione testate documenti, Classe = V5DO01, Funzione = Tipo documento
 * _2_Autorizzazione gestione testate x modello, Classe = V5DO01M, Funzione = TTTMMM (TTT = Tipo documento, MMM = Modello documento)
 * _2_Autorizzazione per stato/flag, Classe = V5DO01D, Funzione = Tipo documento
 * _2_Autorizzazione campi specifici, Classe = PLC-V5TDOC, Funzione = Tipo documento
 * _2_Autorizzazione dati riservati da "lista campi" di un oggetto, Classe = RIS-, Funzione = V5D-TTT (dove TTT = Tipo documento)
 * _2_Autorizzazione dati riservati da "lista numeri" di un oggetto, Classe = RIS-, Funzione = VL_DOTTT (dove TTT = Tipo documento)
 * _2_Autorizzazione "sintesi conti spese tasse" di un documento, Classe = RIS-, Funzione = V5DTTT (dove TTT = Tipo documento)
 * _2_Autorizzazione "Funzioni aggiuntive - F14" di un documento, Classe = ABILITA, Funzione = V5DO01D
 * _2_Autorizzazione "Funzioni di un oggetto - F10", Classe = B£FUN0, Funzione = DO .

## Note strutturate (Tabella NSC)
Il contenitore note si assume dalla tabella V5A.
Chiave 1 - Tipo Documento
Chiave 2 - Nro Documento
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella V5A.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-DOyyy, dove yyy è il tipo documento; se assente viene associato il flusso x-DO.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
Il visualizzatore viene impostato nel modello (Tab. V5Axx).

## Programmi di controllo
Nella tabella V5A si può impostare : 
- il suffisso del programma di caricamento in lista
 :  : DEC T(CS) P(T/V5A) K(T$V5AK) R(1)
- il suffisso del programma di inizializzazione
 :  : DEC T(CS) P(T/V5A) K(T$V5A7) R(1)
- il suffisso del programma di controllo campi
 :  : DEC T(CS) P(T/V5A) K(T$V5A1) R(1)
- il suffisso del programma di controllo ente
 :  : DEC T(CS) P(T/V5A) K(T$V5A3) R(1)

## /COPY
Interfaccia testate documenti (£IDO) : 
 :  : DEC T(MB) P(QILEGEN) K(£IDO)

Inizializzazione testata documenti (£V5Y) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5Y)

Azioni su documenti (£V5C) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5C)

Funzioni valorizzazione (£V5F) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5F)

Funzioni note documento (£V5N) : 
 :  : DEC T(MB) P(QILEGEN) K(£V5N)

## Gruppi flag
Il gruppo flag è impostato nel modello (Tab. V5Axx). Se bianco si risale al tipo documento (Tab. V5D).

## Workflow e popup
Sensibile alla gestione popup, se attivata in B£2.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD T§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella V5A.
Se assente si assume il livello di nascita dalla tabella V5D.
Se assente, si assume il livello 2.

 :  : FLD T§STAT **Stato**
Il suo subsettore  è definito in tabella V5D.
In inserimento si assume lo stato inserito in tabella V5A.
Se assente si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD T§NDOC**Numero documento**
Si utilizza il numeratore (di tabellla CRN, sottosettore V5) , imopostato in tabella V5A.

 :  : FLD T§DT01 **Data 1**
Si possono trattare fino a 10 date definite nel sottosettore 'V5' della tabella C£J. I significati sono dati dagli elementi 'Xyy' dove X è il flag N.21 dell'archivio e yy va da 01 a 10. L'elemento 'X ' dà il significato al titolo del gruppo date. Se il secondo flag non è impostato non si gestiscono le date interne.
 :  : FLD T§DT02.T§DT01 **Data 2**
 :  : FLD T§DT03.T§DT01 **Data 3**
 :  : FLD T§DT04.T§DT01 **Data 4**
 :  : FLD T§DT05.T§DT01 **Data 5**
 :  : FLD T§DT06.T§DT01 **Data 6**
 :  : FLD T§DT07.T§DT01 **Data 7**
 :  : FLD T§DT08.T§DT01 **Data 8**
 :  : FLD T§DT09.T§DT01 **Data 9**
 :  : FLD T§DT10.T§DT01 **Data 10**

 :  : FLD T§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella V5A.
 :  : FLD T§COD2.T§COD1 **Codice 2**
 :  : FLD T§COD3.T§COD1 **Codice 3**
 :  : FLD T§COD4.T§COD1 **Codice 4**
 :  : FLD T§COD5.T§COD1 **Codice 5**
 :  : FLD T§CD06.T§COD1 **Codice 6**
 :  : FLD T§CD07.T§COD1 **Codice 7**
 :  : FLD T§CD08.T§COD1 **Codice 8**
 :  : FLD T§CD09.T§COD1 **Codice 9**
 :  : FLD T§CD10.T§COD1 **Codice 10**

 :  : FLD T§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella V5A.
 :  : FLD T§NUM2.T§NUM1 **Numero 2**
 :  : FLD T§NUM3.T§NUM1 **Numero 3**
 :  : FLD T§NUM4.T§NUM1 **Numero 4**
 :  : FLD T§NUM5.T§NUM1 **Numero 5**
 :  : FLD T§NR06.T§NUM1 **Numero 6**
 :  : FLD T§NR07.T§NUM1 **Numero 7**
 :  : FLD T§NR08.T§NUM1 **Numero 8**
 :  : FLD T§NR09.T§NUM1 **Numero 9**
 :  : FLD T§NR10.T§NUM1 **Numero 10**
