## Contenuto
Movimenti dei cespiti.

## Codice Oggetto (in TA/*CNTT)
'A5'                               £FUNT1

## Chiave primaria
IDOJ del movimento       (A5)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
La natura di questo movimento è definita dalla tabella : 
 :  : DEC T(ST) K(A5B)

## Autorizzazioni
La classe di autorizzazione è A5MO01.
La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * A5MO01G   -    Formato guida

### Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella A5W (Inizializzazioni A5), collegata alla causale del movimento del cespite (Tab. A5B).
Se non inserito si assume CE.
Chiave 1 - IDOJ del movimento
Chiave 2 - N.A.
Chiave 3 - N.A.

### Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella A5W (Inizializzazioni A5), collegata alla causale di movimento del cespite (Tab. A5B).

### Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-A5yyy, dove yyy è il la causale del cespite; se assente viene associato il flusso x-A5.

## Costruzione automatica campi
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
E' impostabile un programma di aggiustamento, lanciato in  immissione e variazione, definito, come suffisso, in tabella A5B (utilizzato per exit stadard).
E' impostabile un programma di aggiustamento, lanciato in  immissione e variazione, definito, come suffiso, in tabella A5W (utilizzato per exit utente).

## /COPY
Interfaccia movimenti (£IA5) : 
 :  : DEC T(MB) P(QILEGEN) K(£IA5)

Inizializzatore movimenti (£A5A) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5B)

Calcolo ammortamento (£A5D) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5D)

Ritorno movimenti e totalizzatori (£A5E) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5E)

Ritorno schiera totalizzatori (£A5F) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5F)

Esecuzione movimenti di ammortamento (£A5I) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5I)

## Gruppi flag
Il gruppo flag si assume dalla tabella A5W (Inizializzazioni A5), collegata alla causale di movimento del cespite (Tab. A5B).

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD TALIVE **Livello** (TAbella B£W_00)
In inserimento si assume il livello di nascita dalla tabella tabella A5W (Inizializzazioni A5), collegata alla causale dem movimento (Tab. A5A). Se non codificato, si assume il livello 2.

 :  : FLD TASTAT **Stato**  (TAbella B£W_A5)
In inserimento si deriva il primo stato valido del livello determinato. In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD TAIDOJ **ID movimento**
Si assume il numeratore OG.A5 (tabella CRN, sottosettore A5).

 :  : FLD RADT01 **Data 1**
Campo data di definizione e utilizzo libero.

 :  : FLD RADT02.RADT01 **Data 2**

 :  : FLD RADT03.RADT01 **Data 3**

 :  : FLD RADT04.RADT01 **Data 4**

 :  : FLD RADT05.RADT01 **Data 5**

 :  : FLD RAAA01 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella A5W (Inizializzazioni A5), collegata alla causale del movimento (Tab. A5B).

 :  : FLD RAAA02.RAAA01 **Codice 2**

 :  : FLD RAAA03.RAAA01 **Codice 3**

 :  : FLD RAAA04.RAAA01 **Codice 4**

 :  : FLD RAAA05.RAAA01 **Codice 5**

 :  : FLD RANU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella A5W (Inizializzazioni A5), collegata alla causale del movimento (Tab. A5B).

 :  : FLD RANU02.RANU01 **Numero 2**

 :  : FLD RANU03.RANU01 **Numero 3**

 :  : FLD RANU04.RANU01 **Numero 4**

 :  : FLD RANU05.RANU01 **Numero 5**
