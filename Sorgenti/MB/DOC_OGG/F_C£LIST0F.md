## Contenuto
Informazioni di valori collegati ad una griglia di oggetti.

## Codice Oggetto (in TA/*CNTT)
'LS'                          £FUNT1
## Chiave primaria
Identificativo      (LS)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
I logici 01 - 07 sono TUTTI chiavi primarie, essendo il record individuato dall'insieme dei loro campi.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute in tabella C£L (listino), nel sottosettore definito nell'area : 
 :  : DEC T(ST) K(C£L)
e in tabella C£V (Sezione), nel sottosettore  presente nell'elemento di tabella listino (C£L) : 
 :  : DEC T(ST) K(C£V)

## Autorizzazioni
La classe di autorizzazione è C£LIS0.
La funzione è il codice del listino.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella C£V (sezione).
Chiave 1 = IDOJ
Chiave 2 = N.A.
Chiave 3 = N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella C£V (sezione).

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-LSyyzzz, dove yy e zzz sono rispettivamente il sottosettore e l'elemento della sezione (C£V); se assente viene associato il flusso x-LS.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
E' possibile impostare, in tabella C£V, il suffisso x del programma di controllo C£LIS0D_x.
E' possibile inoltre impostare, sempre in tabella C£V, un programma specifico di calcolo, che sostituisce il programma base C£CL0R_C.

## /COPY
Interfaccia Listini gererale - £ILS : 
 :  : DEC T(MB) P(QILEGEN) K(£ILS)

Interfaccia Listini specifica - C£L : 
 :  : DEC T(MB) P(QILEGEN) K(£C£L)

## Gruppi flag
Il gruppo flag si assume dalla tabella C£V (sezione).

## Workflow e popup
N.A.

## Servizio di Update
- [C£LIST0F Listini e condizioni - Servizio Update](Sorgenti/MB/DOC_OGG/P_C£LIST0F)

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD L§IDLI **Identificativo**
(Tab CRN_C£) Si assume il numeratore definito nella tabella C£1 (personalizzazione classi SMEUP).

 :  : FLD L§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella C£V.
Se non codificato, si assume il livello 2.

 :  : FLD L§STAT**Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD L§COD1 **Codice 1**
E' l'oggetto tipizzato dal corrispondente oggetto della griglia di controllo di tabella C£V.
 :  : FLD L§COD2.L§COD1**Codice 2**
 :  : FLD L§COD3.L§COD1**Codice 3**

 :  : FLD L§VA01 **Valore 1**
E' il valore individuato (come elemento di C£H) dal corrispondente campo "Siginficato valore" di tabella X£V.
 :  : FLD L§VA02.L§VA01**Valore 2**
 :  : FLD L§VA03.L§VA01**Valore 3**
 :  : FLD L§VA04.L§VA01**Valore 4**
 :  : FLD L§VA05.L§VA01**Valore 5**

 :  : FLD L§DT01 **Data libera 1**
Il suo significato è assunto dall'elemento XYY della tabella C£J LS, dove X è il primo flag di questo archivio e YY è il progressivo data (01, 02, ...).
 :  : FLD L§DT02.L§DT01**Data libera 2**
 :  : FLD L§DT03.L§DT01**Data libera 3**
 :  : FLD L§DT04.L§DT01**Data libera 4**
 :  : FLD L§DT05.L§DT01**Data libera 5**

 :  : FLD L§CL01 **Codice libero 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C£V.
 :  : FLD L§CL02.L§CL01**Codice libero 2**
 :  : FLD L§CL03.L§CL01**Codice libero 3**
 :  : FLD L§CL04.L§CL01**Codice libero 4**
 :  : FLD L§CL05.L§CL01**Codice libero 5**

 :  : FLD L§NU01 **Numero libero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C£V.
 :  : FLD L§NU02.L§NU01**Numero libero 2**
 :  : FLD L§NU03.L§NU01**Numero libero 3**
 :  : FLD L§NU04.L§NU01**Numero libero 4**
 :  : FLD L§NU05.L§NU01**Numero libero 5**
