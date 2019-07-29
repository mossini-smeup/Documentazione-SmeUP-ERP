## Contenuto
Dati delle richieste di acquisto del ciclo esterno.

## Codice Oggetto (in TA/*CNTT)
'RA'                               £FUNT1

## Chiave primaria
Numero richiesta                   £FUNK1    Pos.1-10
Numero riga         (NR)           £FUNK1    Pos 12-15

## Altri condizionamenti facoltativi in ricerca
Tipo richiesta d'acquisto (GAR)    £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle GAR (Tipo richiesta d'acquisto).
 :  : DEC T(ST) K(GAR)

## Autorizzazioni
 Le classi di autorizzazione sono le seguenti : 
 - GARDAT  per la gestione / GARDATB per la validazione. Entrambe nei programmi GARDA0G (formato guida) e GARDA0L (lista).
 - GARD01  per il gestione di dettaglio (programma GARDA0D), con la funzione tipo richiesta TA/GAR.

## Note strutturate (Tabella NSC)
Il contenitore è fisso GAR.
Chiave 1 - Numero richiesta
Chiave 2 - Numero riga
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella GAR.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-RAyyy, dove yyy è il tipo richiesta (tabella GAR), se assente viene associato il flusso x-RA.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Si può impostare, in tabella GAR (con risalita a GA1) in nome completo di un programma, lanciato dal dettaglio della richiesta, per eseguire controlli specifici.

## /COPY
Interfaccia richieste d'acquisto (£IRA) : 
 :  : DEC T(MB) P(QILEGEN) K(£IRA)

Aggancio tabelle legate alla richiesta (£GAB) : 
 :  : DEC T(MB) P(QILEGEN) K(£GAB)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD R§NRIC**Numero richiesta**
Si utilizza il muneratore (di tabellla CRN, sottosettore GA), imopostato in tabella GA1.

 :  : FLD R§LIVE **Livello**
In inserimento si assume il livello 2 e si deriva il primo stato valido di questo livello.

 :  : FLD R§STAT **Stato**
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD R§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GAR.
 :  : FLD R§COD2.R§COD1 **Codice 2**
 :  : FLD R§COD3.R§COD1 **Codice 3**
 :  : FLD R§COD4.R§COD1 **Codice 4**
 :  : FLD R§COD5.R§COD1 **Codice 5**

 :  : FLD R§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GAR.
 :  : FLD R§NUM2.R§NUM1 **Numero 2**
 :  : FLD R§NUM3.R§NUM1 **Numero 3**
 :  : FLD R§NUM4.R§NUM1 **Numero 4_n
 :  : FLD R§NUM5.R§NUM1 **Numero 5**
