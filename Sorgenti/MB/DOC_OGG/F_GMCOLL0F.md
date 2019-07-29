## Contenuto
Dati anagrafici dei colli.

## Codice Oggetto (in TA/*CNTT)
 'CZ'                               £FUNT1

## Chiave primaria
Numero collo                        £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo collo               (TA/GMD)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostaziooni che condizionano questo archivio sono contenute nel settore di tabelle GMD (Tipo collo) : 
 :  : DEC T(ST) K(GMD)

## Autorizzazioni
La classe di autorizzazione è GMCZ01G.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella GMD (tipo collo).
Chiave 1 - Numero collo
Chiave 2 - N.A.
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La  categoria si assume dalla tab. GMD.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-CZyyy, dove yyy è il tipo collo; se assente viene associato il flusso x-CZ.

## Costruzione automatica campi (tabella B£C)
 La struttura della matrice risultante quando è stata inserito in tabella GMD il campo "Domande cost. codice" (elemento di tabella B£F)  è la seguente : 
>         Descrizione                    Riga £SC Da  A
         Numero Collo                       1    01  15


## Presenza monitor - visualizzatore
La forma di presentazione viene assunta da quella impostata in tabella GMD.

## Programmi di controllo
In tabella GMD si imposta il suffisso del programma di aggiustamento per implementare controlli specifici.

## /COPY
Interfaccia generalizzata Colli (£ICZ) : 
 :  : DEC T(MB) P(QILEGEN) K(£ICZ)

Inizializzazione Colli (£GML) : 
 :  : DEC T(MB) P(QILEGEN) K(£GML)

Funzioni sui colli (£GMB) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMB)

Scansione packing list di un documento (£GMQ) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMQ)

## Gruppi flag
I gruppi flag vengono presi dalla tabella GMD.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD Z§NCOL **Numero Collo**
In inserimento manuale può venire determinato tramite le domande di costruzione del codice (se presenti), alternativamente in risalta, dal numeratore di GMD, di GM1 e da quello fisso "NCOL".

In creazione colli da un documento (routine GMQ) è possibile invece eseguire un programma specifico di determinazione del numero del collo (presente in tabella GM1). Se assente, viene assunto il numeratore di questa tabella.

In creazione collo da funzioni sui colli (routine GMB), si utilizza il numeratore di GMD e, in assenza, quello fi GM1.

In inizializzazione collo (routine GML), si utilizza il numeratore di GMD e, in assenza, lo stato (sempre di GMD), ed infine il numeratore fisso "NCOL".
In realtà, la routine di inizializzazione è richiamata solo dal dettaglio del collo, con il mumero già impostato, e quindi questa risalita non è mai sfruttata.

 :  : FLD Z§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella GMD.
Se non codificato, si assume il livello 2.

 :  : FLD Z§STAC **Stato Collo**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD Z§CARC **Unità di movimentazione**
In inserimento assunto il campo corrispondente di tabella GMD.

 :  : FLD Z§TIDO **Tipo Documento 1**
In inserimento assunto il campo corrispondente di tabella GMD.

 :  : FLD Z§NRDO **Codice Documento 1**
Tipizzato dal tipo Documento 1.

 :  : FLD Z§TIEO **Tipo Ente 1**
In inserimento assunto il campo corrispondente di tabella GMD.

 :  : FLD Z§COEO **Codice Ente 1**
Tipizzato dal tipo Ente 1.

 :  : FLD Z§TIDD **Tipo Documento 2**
In inserimento assunto il campo corrispondente di tabella GMD.

 :  : FLD Z§NRDD **Codice Documento 1**
Tipizzato dal tipo Documento 2.

 :  : FLD Z§TIED **Tipo Ente 2**
In inserimento assunto il campo corrispondente di tabella GMD.

 :  : FLD Z§COED **Codice Ente 2**
Tipizzato dal tipo Ente 1.

 :  : FLD Z§COD1**Codice 1**
 Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMD.
 :  : FLD Z§COD2.Z§COD1**Codice 2**
 :  : FLD Z§COD3.Z§COD1**Codice 3**
 :  : FLD Z§COD4.Z§COD1**Codice 4**
 :  : FLD Z§COD5.Z§COD1**Codice 5**

 :  : FLD Z§NUM1**Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMD.
 :  : FLD Z§NUM2.Z§NUM1**Numero 2**
 :  : FLD Z§NUM3.Z§NUM1**Numero 3**
 :  : FLD Z§NUM4.Z§NUM1**Numero 4**
 :  : FLD Z§NUM5.Z§NUM1**Numero 5**

 :  : FLD Z§DT01**Data 1**
 Il suo significato è assunto dall'elemento XYY della tabella C£JCZ, dove X può essere il Flag 2 del record oppure (se il flag 2 è bianco) il campo "Tipo date implicite" di tabella GMD e YY è il progressivo data (01, 02, ...).
 :  : FLD Z§DT02.Z§DT01**Data 2**
 :  : FLD Z§DT03.Z§DT01**Data 3**
 :  : FLD Z§DT04.Z§DT01**Data 4**
 :  : FLD Z§DT05.Z§DT01**Data 5**

