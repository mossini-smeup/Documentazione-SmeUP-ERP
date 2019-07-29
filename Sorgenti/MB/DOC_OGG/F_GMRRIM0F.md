## Contenuto
Richiesta di movimentazione di un articolo, con la quantità, le causali di movimenetazione, e gli altri codici eventualmente coinvolti (lotti, ubicaizoni, ecc..).

## Codice Oggetto (in TA/*CNTT)
'RM'                               £FUNT1

## Chiave primaria
R£IDDM     Identif.riga            £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo riga movimentaz.    (TA/GMZ)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostaziooni che condizionano questo archivio sono contenute nel settore di tabelle GMZ (Tipo riga richiesta movimentazione) : 
 :  : DEC T(ST) K(GMZ)

Altre impostazioni generali sono contenute nel settore di tabelle GMO (Tipo documento movimentazione) : 
 :  : DEC T(ST) K(GMO)

## Autorizzazioni
La classe di autorizzazione è GMRM10.

La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * GMOR10G   -    Formato guida
 * GMOR10L   -    Lista

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
La categoria viene assunta dalla tabella GMZ.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-RM.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella GMZ si può inserire il suffisso del programma di controllo GMRM10D_x.

## /COPY
Interfaccia Righe richieste movimentazione £IRM : 
 :  : DEC T(MB) P(QILEGEN) K(£IRM)

Inizializzazione righe richieste movimentazione £GMZ : 
 :  : DEC T(MB) P(QILEGEN) K(£GMZ)

Motore inferenziale £GMI : 
 :  : DEC T(MB) P(QILEGEN) K(£GMI)

Funzioni di dialogo GMQUAN <-> GMRRIM £GMJ : 
 :  : DEC T(MB) P(QILEGEN) K(£GMJ)

Funzione su GMRRIM di un'origine £GMR : 
 :  : DEC T(MB) P(QILEGEN) K(£GMR)

## Gruppi flag
I gruppi flag sono assunti dalla tabella GMZ.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD R£NRDM **Numero Documento**
Si utilizza il numeratore (elemento di tabella CRN, sottosettore GM) impostato in tabella GM1.

 :  : FLD R£TORI **Origine documento di movimentazione**
Viene ripreso il valore impostato in tabella GMO.

 :  : FLD R£LIVE**Livello**
In inserimento si assume il livello di nascita dalla tabella GMZ, e si deriva il primo stato valido di questo livello. Se non codificato, si assume il livello 2.

 :  : FLD R£STAT**Stato riga docum.**
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD R£ORCA**Causale origine**
In inserimento viene inserita la causale origine di tabella GMZ.

 :  : FLD R£ORAR**Area giacenza (origine)**
In inserimento viene inserita l'area della causale origine di tabella GMZ.

 :  : FLD R£ORTG**Tipo giacenza (origine)**
In inserimento viene inserito il tipo della causale origine di tabella GMZ.

 :  : FLD R£DECA**Causale destinazione**
In inserimento viene inserita la causale destinazione di tabella GMZ.

 :  : FLD R£DEORAR**Area giacenza (destinazione)**
In inserimento viene inserita l'area della causale destinazione di tabella GMZ.

 :  : FLD R£DETG**Tipo giacenza (destinazione)**
In inserimento viene inserito il tipo della causale destinazione di tabella GMZ.

 :  : FLD R£COD1 1**Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMZ.
 :  : FLD R£COD2.R£COD1**Codice 2**
 :  : FLD R£COD3.R£COD1**Codice 3**
 :  : FLD R£COD4.R£COD1**Codice 4**
 :  : FLD R£COD5.R£COD1**Codice 5**

 :  : FLD R£NUM1 1**Numero  1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMZ.
 :  : FLD R£NUM2.R£NUM1**Numero  2**
 :  : FLD R£NUM3.R£NUM1**Numero  3**
 :  : FLD R£NUM4.R£NUM1**Numero  4**
 :  : FLD R£NUM5.R£NUM1**Numero  5**
