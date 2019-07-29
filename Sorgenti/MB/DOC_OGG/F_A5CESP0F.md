## Contenuto
Dati descrittivi e classificazioni del cespite.

## Codice Oggetto (in TA/*CNTT)
'CE'                               £FUNT1

## Chiave primaria
Codice cespite           (CE)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Categoria cespite       (TA/A5A)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle A5A.
(Categoria cespite)
 :  : DEC T(ST) K(A5A)
Essa contiene, tra l'atro, un elemento della tabella Inizializzazione cespite (A5W) che contiene ulteriori campi di impostazione del cespite.
 :  : DEC T(ST) K(A5W)

## Autorizzazioni
La classe di autorizzazione è A5CE01.

La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * A5CE01G   -    Formato guida
 * A5CE01L   -    Lista richiamata dal formato guida
 * A5CE01LA  -    Lista richiamata dalla ricerca. Se si vuol permettere la manutenzione dalla ricerca (inserimento, variazione) si autorizza a questo livello.

### Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A).
Se non inserito si assume CE.
Chiave 1 - Codice Cespite
Chiave 2 - N.A.
Chiave 3 - N.A.

### Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A).

### Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-CEyyy, dove yyy è il la categoria fiscale del cespite; se assente viene associato il flusso x-CE.

## Costruzione automatica campi
 La struttura della matrice risultante quando è stata inserito in tabella A5A il campo "Domande cost. codice" (elemento di tabella B£F)  è la seguente : 
>         Descrizione                    Riga £SC Da  A
         Codice Cespite                     1    01  15


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
E' impostabile un programma di aggiustamento, lanciato in  immissione e variazione, definito, come suffisso, in tabella A5W.

## /COPY
Interfaccia cespiti (£ICE) : 
 :  : DEC T(MB) P(QILEGEN) K(£ICE)

Inizializzatora cespiti (£A5A) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5A)

## Gruppi flag
Il gruppo flag si assume dalla tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A).

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD TALIVE **Livello** (TAbella B£W_00)
In inserimento si assume il livello di nascita dalla tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A). Se non codificato, si assume il livello 2.

 :  : FLD TASTAT **Stato**  (TAbella B£W_CE)
In inserimento si deriva il primo stato valido del livello determinato. In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD TAIDOJ **Codice cespite**
Si può attivare la numerazione automatica (impostando opportunamente il passo di costruzione del codice).
In tal caso si assume il numeratore OG.CE (tabella CRN, sottosettore A5).

 :  : FLD TATC01 **Tipo classificazione 1**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel primo oggetto della griglia impostata nel campo "Griglia di classificazione 1" di tabella A5A.

 :  : FLD TATC02 **Tipo classificazione 2**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel secondo oggetto della griglia impostata nel campo "Griglia di classificazione 1" di tabella A5A.

 :  : FLD TATC03 **Tipo classificazione 3**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel terzo oggetto della griglia impostata nel campo "Griglia di classificazione 1" di tabella A5A.

 :  : FLD TATC04 **Tipo classificazione 4**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel primo oggetto della griglia impostata nel campo "Griglia di classificazione 2" di tabella A5A.

 :  : FLD TATC05 **Tipo classificazione 5**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel secondo oggetto della griglia impostata nel campo "Griglia di classificazione 2" di tabella A5A.

 :  : FLD TATC06 **Tipo classificazione 6**
Viene copiato il tipo di classificazione (tipo e parametro) contenuto nel terzo oggetto della griglia impostata nel campo "Griglia di classificazione 2" di tabella A5A.

 :  : FLD TACL01 **Codice classificazione 1**
E' l'oggetto tipizzato dal corrispondente tipo classificazione.

 :  : FLD TACL02.TACL01 **Codice classificazione 2**

 :  : FLD TACL03.TACL01 **Codice classificazione 3**

 :  : FLD TACL04.TACL01 **Codice classificazione 4**

 :  : FLD TACL04.TACL05 **Codice classificazione 5**

 :  : FLD TACL04.TACL06 **Codice classificazione 6**

 :  : FLD TADT01 **Data 1**
Campo data di definizione e utilizzo libero.

 :  : FLD TADT02.TADT01 **Data 2**

 :  : FLD TADT03.TADT01 **Data 3**

 :  : FLD TADT04.TADT01 **Data 4**

 :  : FLD TADT05.TADT01 **Data 5**

 :  : FLD TAAA01 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A).

 :  : FLD TAAA02.TAAA01 **Codice 2**

 :  : FLD TAAA03.TAAA01 **Codice 3**

 :  : FLD TAAA04.TAAA01 **Codice 4**

 :  : FLD TAAA05.TAAA01 **Codice 5**

 :  : FLD TANU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella A5W (Inizializzazioni A5), collegata alla categoria fiscale del cespite (Tab. A5A).

 :  : FLD TANU02.TANU01 **Numero 2**

 :  : FLD TANU03.TANU01 **Numero 3**

 :  : FLD TANU04.TANU01 **Numero 4**

 :  : FLD TANU05.TANU01 **Numero 5**

