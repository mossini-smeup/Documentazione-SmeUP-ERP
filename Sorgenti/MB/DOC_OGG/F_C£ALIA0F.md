## Contenuto
Impostare le correlazioni tra due oggetti.

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
E$TIP1     Tipo parametro cod.1
E$COD1     Codice 1
E$TIP2     Tipo parametro cod.2
E$COD2     Codice 2
E$CONT     Contesto   (Tab. C£K)

## Ulteriore chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle C£K (Contesto gestione alias).
 :  : DEC T(ST) K(C£K)

## Autorizzazioni
La classe di autorizzazione è C£AL01.
La funzione è il contesto.

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Si può inserire in tabella C£K il suffisso x del programma di aggiustamento C£AL01_x, eseguito durante la gestione dell'alias.

## /COPY
Gestione alias (£C£AL) : 
 :  : DEC T(MB) P(QILEGEN) K(£C£AL)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD E$TIP1 **Tipo parametro cod.1**
Vengono copiati (concatenandoli) il tipo e il parametro 1 da tabella C£K

 :  : FLD E$COD1 **Codice 1**
E' l'oggetto tipizzato dal corrispondente tipo classificazione

 :  : FLD E$TIP2 **Tipo parametro cod.2**
Vengono copiati (concatenandoli) il tipo e il parametro 2 da tabella C£K

 :  : FLD E$COD2 **Codice 2**
E' l'oggetto tipizzato dal corrispondente tipo classificazione

 :  : FLD E$SCD2 **Suffisso codice 2**
E' l'oggetto tipizzato dal tipo e parametro suffisso di tabella C£K (campi che non vengono riportati nell'archivio).

 :  : FLD E$LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella C£K.
Se non codificato, si assume il livello 2.

 :  : FLD E$STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.


 :  : FLD E$CD01 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C£K.
 :  : FLD E$CD02.E$CD01 **Codice 2**
 :  : FLD E$CD03.E$CD01 **Codice 3**
 :  : FLD E$CD04.E$CD01 **Codice 4**
 :  : FLD E$CD05.E$CD01 **Codice 5**

 :  : FLD E$NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C£K.
 :  : FLD E$NUM2.E$NUM1 **Numero 2**
 :  : FLD E$NUM3.E$NUM1 **Numero 3**
 :  : FLD E$NUM4.E$NUM1 **Numero 4**
 :  : FLD E$NUM5.E$NUM1 **Numero 5**

