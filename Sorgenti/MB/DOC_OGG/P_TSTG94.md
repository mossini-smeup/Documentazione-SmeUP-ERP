# EMISSIONE PRIMA PAGINA DI PARZIALIZZAZIONI/ORDINAMENTI
 :  : CONSIDERAZIONI
Tenuto conto che in SMEUP il numero di stampe non è elevatissimo ma neanche irrilevante,si è cercata
una soluzione che consentisse l'emissione del formato con un impatto minimo a livello di modifica
del codice sorgente.
Se il richiamo alla /COPY G94 fosse stato concepito a livello di ogni singolo programma di stampa
avremmo dovuto tener conto di fattori quali proliferazione e ridondanza di istruzioni pgm ma soprattutto
più tempo per modificarli col rischio di commettere errori oppure omissioni.
Per questo si è individuata la /COPY QILEGEN,£B£S_C0 come punto di intervento comune.
## OBIETTIVO
Non sempre ci è chiaro ciò che le stampe producano a livello di parametrizzazione.Lo scopo di
corredare la stampa di uno schema iniziale in cui vengono riportate parzializzazioni/ordinamenti ecc
 è proprio quello di completarle e di renderle più leggibili.
### TECNICA DI APPLICAZIONE DELLA MODIFICA
  -  1 L'emissione del formato di parzializzazione è condizionato dal flag stampa condizioni che
       si trova in tabella (UP TAB settore PGM ), il campo può assumere tre valori
       (Blank=non viene emesso il formato A=emissione del formato con salto pagina B=emissione del
       formato senza salto pagina)

  -  2 Ricompilare  il programma di stampa (solo pgm con specifiche "O" per intenderci)

                                                                          ---- utilizzato in ----
  -  3 elenco routines/pgm necessari alla compilazione  (QILEGEN/ £B£S_C0/...pgm stampa
                                                        ( "  "    £B£S_C2/...pgm stampa
                                                        ( "  "    £B£S_DS/£B£S_E
                                                        ( "  "    £B£S_E /...pgm stampa
                                                        ( "  "   £B£S_SCH/...pgm stampa
                                                        ( "  "    £G94   /£B£S_C2/pgm stampa
                                                        ( "  "    £G94DS /£B£S_E /£G94 /pgm stampa
                                                        ( "  "    £IR1   /B£G94G
                                                        (SRC      B£G94G
 :  : T04 METODO DI COSTRUZIONE
Attualmente,poi si vedrà,
condizione sine qua non,è che venga eseguita la parzializzazione con il lancio del programma
Es :  (CALL BRCM51A  stampa delle commesse) che consente la memorizzazione dei parametri in
LDA (local data area).
La fase successiva è quella di eseguire per il test il comando (T G94 ) che produrrà questo effetto
---------------------------------------------------------------------------------------------------
Funzione        SCA          Scansione                                                  £G94FU
Metodo          POS         Posizionamento                                              £G94ME
Nome file       BRCOMM0F   COMM Commesse                                                £G94FL
Nome programma  BRCM51B    COMM Stampa Commesse - Esecuzione S                          £G94PR
................................................................................................
................................................................................................
.................................................................................................
.............................................................................1M$CDMGM$TICMM$TICM
..............................................TATATAMAG.......BSA......BSA.......................
.................................................................................................
....................................1............................................................
..............................2........................M$COMM=%RANGE("A" "Z") & M$TICM>="A" & M$C
DMG=%RANGE("1" "9")..............................................................................
.............2...................................................................................
.................................................................................................
.................................................................................................
...................................................0020..................................
------------------------------------------------------------------------------------------
Le due fasi  del metodo sono (POS) per il posizionamento e (LET) per la lettura
La parte tratteggiata rappresenta la (LDA) che viene letta dal pgm (B£G94G) e che scandirà ad ogni
invio con metodo (LET)
Il risultato è restituito a colonna (20 e 21) leggendo il tracciato record del file definito in
(£G94FL) propone la decodifica solo dei campi selezionati dalla parzializzazione.
Il pgm tiene conto che esista almeno un parametro di parzializzazione
ES :  Al primo invio
*...+....1....+....2....+....3....+....4....+....5  ...+... 6 ...+... 7 ...+... 8 ...+... 9 ...+...
                           |  COMMESSA             0                  A
                    Z                         |
ES :  Al secondo invio
*...+....1....+....2....+....3....+....4....+....5  ...+... 6 ...+... 7 ...+... 8 ...+... 9 ...+...
                           |  Magazzino                               1
                    9                         |
e così via......
.
P.S.
ATTENZIONE  : 
Il pgm (BRAR51B) è da considerarsi fuori standard in quanto il pgm prevede la gestione dell'output
su (printer file) .Il richiamo della /COPY G94 avviene all'interno del programma stesso e non
dalla routine £B£S_C0
