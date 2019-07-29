## Contenuto
Dati descrittivi e classificazioni dell'articolo.

## Codice Oggetto (in TA/*CNTT)
'AR'                               £FUNT1

## Chiave primaria
Codice articolo          (AR)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo articolo            (TA/BRA)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRA.
(Tipo articolo)
 :  : DEC T(ST) K(BRA)

## Autorizzazioni
La classe di autorizzazione è BRAR01G.

Sono prevista anche autorizzazioni per tipo articolo :  classe BRAR01 e funzione = tipo articolo.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella BRA. Se non inserito si assume AR.
Chiave 1 - Codice Articolo
Chiave 2 - N.A.
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella BRA.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-ARyyy, dove yyy  è il tipo articolo; se assente viene associato il flusso x-AR.

## Costruzione automatica campi
La struttura della matrice risultante quando è stata inserito in tabella BRA il campo "Domande cost. codice" (elemento di tabella B£F) è la seguente : 
>         Descrizione                    Riga £SC Da  A
         Codice Articolo                    1    01  15
         Descrizione Articolo               2    01  35
         Disegno                            2    36  55
         Barcode                            3    01  15
         Gruppo Distinta                    3    16  30
         Gruppo Ciclo                       3    31  45
         Unità di misura gestione           4    01  02
         Tipo Parte                         4    03  05
         Classe Materiale                   4    06  10
         Classe Programmazione              4    11  15
         Classe Gestione                    4    16  20
         Classe Contabile                   4    21  25
         Classe Fiscale                     4    26  30
         Classe Valore                      4    31  35
         Assoggettamento IVA                4    36  37
         Classe Funzionale                  4    38  42
         Data libera 1                      4    43  50
         Data libera 2                      4    51  58
         Data libera 3                      4    59  66
         Data libera 4                      4    67  74
         Data libera 5                      4    75  82
         Codice Alternativo                 5    01  15
         Cespite                            5    16  30
         Contenitore                        5    31  45
         Articolo di riferimento            5    46  60
         Rif. Catalogo di Vendita           5    61  75
         Nome Configurazione                6    01  20
         Cod. Sviluppo Quantità             6    21  25
         Cod. Sviluppo Varianti             6    26  30
         Nomenclatura Combinata             6    31  40
         Ente Interno Responsabile          6    41  43
         Articolo non di magazzino          6    44  44
         Flag 02                            6    45  45
         Flag 03                            6    46  46
         Flag 04                            6    47  47
         Flag 05                            6    48  48
         Flag 06                            6    49  49
         Flag 07                            6    50  50
         Flag 08                            6    51  51
         Flag 09                            6    52  52
         Flag 10                            6    53  53
         Flag 11                            6    54  54
         Flag 12                            6    55  55
         Flag 13                            6    56  56
         Flag 14                            6    57  57
         Flag 15                            6    58  58
         Flag 16                            6    69  59
         Flag 17                            6    60  60
         Flag 18                            6    61  61
         Flag 19                            6    62  62
         Flag 20                            6    63  63
         Descrizione 2                      7     1  35
         Classificazione 1                  7    36  50
         Classificazione 2                  7    51  65
         Classificazione 3                  7    66  80
         Codice 1                           7    81  95
         Codice 2                           8     1  15
         Codice 3                           8    16  30
         Codice 4                           8    31  45
         Codice 5                           8    46  60
         Numero 1                           8    61  75
         Numero 2                           8    76  90
         Numero 3                           9     1  15
         Numero 4                           9    16  30
         Numero 5                           9    31  45
         Peso                               9    46  57
         Volume                             9    58  69
         Lotto di riferimento               9    70  80


## Presenza monitor - visualizzatore
In tabella BR1 si deve impostare il flag "Visualiz.su Articoli".
In tal caso la forma di presentazione viene assunta da quella impostata in tabella BRA e, se assente, da quella in tabella BR1.

## Programmi di controllo
In tabella BRA, con risalita allo stesso campo di tabella BR1, si imposta il suffisso del programma di aggiustamento per implementare controlli specifici.

## /COPY
Interfaccia articoli (£IAR) : 
 :  : DEC T(MB) P(QILEGEN) K(£IAR)
In alcuni programmi è ancora utilizzata la precedente interfaccia £IFART.

Controllo campi Anagrafico articoli (£BRZ)
 :  : DEC T(MB) P(QILEGEN) K(£BRZ)

## Gruppi flag
N.A.

## Workflow e popup
Sensibile alla gestione popup, se attivata in B£2.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD A§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella BRA.

 :  : FLD A§STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.
 :  : FLD A§UNMS **Unità di misura di gestione**
Viene proposto il campo omonimo impostato in tabella BRA.
Il valore ottenuto dalla costruzione automatica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§BARC Barcode
La costruzione e il controllo di questo campo sono guidati dal campo "Codice EAN" impostato in
tabella BRA.
 :  : DEC T(CS) P(T-BRA) K(T$BRAZ) R(1)
 :  : FLD A§CASI **Assoggettamento IVA**
Viene proposto il campo "Codice IVA assunto" impostato in tabella BRA.
Il valore ottenuto dalla costruzione automantica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§CSVQ **Codice sviluppo quantità**
Viene proposto il campo omonimo impostato in tabella BRA.
Il valore ottenuto dalla costruzione automantica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§CSVA **Codice sviluppo varianti**
Viene proposto il campo "Criterio configurazione assunto" impostato in tabella BRA.
Il valore ottenuto dalla costruzione automatica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§ENIR **Ente interno responsabile**
E' il magazzino di competenza, quello in cui viene prodotto o approvvigionato questo articolo, se non specificato espressamente.
Se l'applicazione è monoplant questo campo non viene proposto.
Se l'applicazione è muntiplant e non è stato inserito il magazino di competenza in tabella B£2, questo campo è obbligatorio.
Se invece è stato inserito, questo campo è facoltativo.
 :  : DEC T(CS) P(T-B£2) K(££B£2G)
Il magazzino di competenza viene determinato con la seguente risalita : 
1. se l'applicazione è monoplant, è il magazzino unico (sempre in tabelle B£2)
2. se presente, è quello dell'anagrafica articoli
3. se questo campo è assente, è il magazzino di competenza di tabella B£2.
 :  : FLD A§CLMA **Classe materiale**
Viene proposto il campo "Classe materiale assunta" impostato in tabella BRA.
Il valore ottenuto dalla costruzione automatica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§CLPR **Classe programmazione**
Viene proposto il campo "Classe programmazione assunta" impostato in tabella BRA.
Il valore ottenuto dalla costruzione automatica dei campi, se non vuoto, ha la precedenza su di esso.
 :  : FLD A§TC01 **Tipo classificazione 1**
Viene copiato il tipo di classificaziome (tipo e parametro) contenuto nella "Griglia ricliassifiche" tabella BRA.
 :  : FLD A§TC02.A§TC01 **Tipo classificazione 2**
 :  : FLD A§TC03.A§TC01 **Tipo classificazione 3**
 :  : FLD A§CL01 **Codice classificazione 1**
Si inserisce il campo tipizzato nella griglia (B£G) riclassifica in tabella BRA.
 :  : FLD A§CL02.A§CL01 **Codice classificazione 2**
 :  : FLD A§CL03.A§CL01 **Codice classificazione 3**
 :  : FLD A§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BRA.
 :  : FLD A§COD2.A§COD1 **Codice 2**
 :  : FLD A§COD3.A§COD1 **Codice 3**
 :  : FLD A§COD4.A§COD1 **Codice 4**
 :  : FLD A§COD5.A§COD1 **Codice 5**
 :  : FLD A§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BRA.
 :  : FLD A§NUM2.A§NUM1 **Numero 2**
 :  : FLD A§NUM3.A§NUM1 **Numero 3**
 :  : FLD A§NUM4.A§NUM1 **Numero 4**
 :  : FLD A§NUM5.A§NUM1 **Numero 5**
 :  : FLD A§DT01 **Data 1**
Il suo significato è assunto dall'elemento XYY della tabella C£J AR, dove X è il campo "Tipo date implicite" di tabella BRA e YY è il progressivo data (01, 02, ...).
 :  : FLD A§DT02.A§DT01 **Data 2**
 :  : FLD A§DT03.A§DT01 **Data 3**
 :  : FLD A§DT04.A§DT01 **Data 4**
 :  : FLD A§DT05.A§DT01 **Data 5**
