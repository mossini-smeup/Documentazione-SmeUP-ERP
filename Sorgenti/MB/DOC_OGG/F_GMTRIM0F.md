## Contenuto
Informazioni comuni ad un insieme di richieste per la movimentazione di articoli, sia all'interno dell'azienda, sia da/verso l'esterno.

## Codice Oggetto (in TA/*CNTT)
 'DM'                               £FUNT1

## Chiave primaria
T£NRDM     Numero Documento         £FUNK1

## Altri condizionamenti facoltativi in ricerca
T£TIDM     Tipo Docum.Movim.        £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle GMO (Tipo documento movimentazione) : 
 :  : DEC T(ST) K(GMO)

## Autorizzazioni
La classe di autorizzazione è GMRM01.

La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * GMOR01G   -    Formato guida
 * GMOR01L   -    Lista

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella GMO (Tipo Documento Movimentazione). Se non inserito si assume DM.
 Chiave 1 Numero Documento di movimentazione
 Chiave 2 N.A.
 Chiave 3 N.A.

## Parametri (Tabella C£E)
La categoria viene assunta dalla tabella GMO.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-DMyyy, dove yyy è il tipo richiesta movimentazione; se assente viene associato il flusso x-DM.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia testate rich.movimentazione £IDM : 
 :  : DEC T(MB) P(QILEGEN) K(£IDN)

Inizializzazione testate rich.movimentazione £GMW : 
 :  : DEC T(MB) P(QILEGEN) K(£GMW)

Funzioni GMO :  Stampa etichetta £GMO : 
 :  : DEC T(MB) P(QILEGEN) K(£GMO)

## Gruppi flag
I gruppi flag vengono assunti dalla tabella GMO.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD T£NRDM **Numero Documento**
Si utilizza il numeratore (elemento di tabeella CRN, sottosettore GM) impostato in tabella GMO.

 :  : FLD T£TORI **Origine documento di movimentazione**
Vieme ripreso il valore imopstato in tabella GMO.

 :  : FLD T£LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella GMO, e si deriva il primo stato valido di questo livello. Se non codificato, si assume il livello 2.

 :  : FLD T£STAT **Stato testata docum.**
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD T£TP01 **Generato da :  tipo**
Vieme ripreso il "Tipo oggetto di generazione" di tabella GMO.

 :  : FLD T£PA01 **Parametro tipo oggetto**
Vieme ripreso il "Parametro oggetto di generazione" di tabella GMO.

 :  : FLD T£CD01 **Generato da :  Codice**
Oggwetto tipizzato da "Tipo e parametro oggetto di generazione" di tabella GMO.

 :  : FLD T£TP02 **Origine :  tipo**
Vieme ripreso il "Tipo oggetto di origine" di tabella GMO.

 :  : FLD T£PA02 **Parametro tipo oggetto**
Vieme ripreso il "Parametro oggetto origine" di tabella GMO.

 :  : FLD T£CD02 **Origine :  Codice**
Oggwetto tipizzato da "Tipo e parametro oggetto di origine" di tabella GMO.

 :  : FLD T£TP03 **Origine :  tipo**
Vieme ripreso il "Tipo oggetto di destinazione" di tabella GMO.

 :  : FLD T£PA03 **Parametro tipo oggetto**
Vieme ripreso il "Parametro oggetto destinazione" di tabella GMO.

 :  : FLD T£CD03 **Destinazione :  Codice**
Oggwetto tipizzato da "Tipo e parametro oggetto di destinazione" di tabella GMO.

 :  : FLD T£COD1 1**Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMO.
 :  : FLD T£COD2.T£COD1**Codice 2**
 :  : FLD T£COD3.T£COD1**Codice 3**
 :  : FLD T£COD4.T£COD1**Codice 4**
 :  : FLD T£COD5.T£COD1**Codice 5**

 :  : FLD T£NUM1 1**Numero  1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMO.
 :  : FLD T£NUM2.T£NUM1**Numero  2**
 :  : FLD T£NUM3.T£NUM1**Numero  3**
 :  : FLD T£NUM4.T£NUM1**Numero  4**
 :  : FLD T£NUM5.T£NUM1**Numero  5**
