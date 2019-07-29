# CSA - Metodo attribuzione percentuale
 :  : DEC T(ST) K(CSA)
## OBIETTIVO
La tabella permette di scegliere le voci del costo alle quali devono essere applicate le percentuali di ricarica, presenti nella tabella CSR (famiglia ricariche).
_9_Esempio 
Potremo specificare che la prima percentuale del costo industriale si applica solo al costo lavoro e macchina, la seconda percentuale solo al costo materiale e così via.
Questa tabella risulta formata da 9 campi di 7 flags ognuno.
## CARATTERISTICHE
Questa tabella deve essere necessariamente compilata, nel caso in cui siano state specificate delle percentuali nelle tabelle CSR.
La tabella contiene un solo elemento, per cui il metodo di calcolo che essa definisce è univoco per tutti gli articoli e tutti i tipi costo.
## SIGNIFICATO DEI CAMPI
I nove campi sono così suddivisi : 
- 1 2 3 - Quota 1, 2, 3, dei costi indiretti (costo industriale)
- 4 5 6 - Quota 1, 2, 3, dei costi generali (costo pieno)
- 7 8 9 - Quota 1, 2, 3, delle ricariche (prezzo min di vendita)
_r_I sette flags di ciascun campo sono suddivisi in due gruppi.
**I primi 4 flags indicano quali voci del COSTO DIRETTO considerare nella base per il calcolo **percentuale della ricarica ed hanno il seguente significato : **

                                 **Valori possibili : **
1° flag - materiale               1 - c. variabile   (solo indice del costo variabile)
                                  2 - c. fisso       (solo indice del costo fisso)
                                  3 - entrambi costi (indice c.variabile + indice c.fisso)
2° flag - lavor.esterne           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
3° flag - lavoro    _R_*           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
4° flag - macchina  _R_*           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
.
                    _R_* La gestione del lavoro flag 3 e 4 nel caso di calcolo utilizzando
                        la tabella D0C viene rimodulata. Il flag 4 non viene gestito ed il
                        flag 3 assume il valore seguent :   _5_1 - Costi del livello
                                                          _5_2 - c. fisso
                                                          _5_3 - entrambi i livelli
**Gli ultimi 3 flags indicano quali voci delle RICARICHE considerare nella base per il calcolo **percentuale della ricarica ed hanno il seguente significato : **
                                 **Valori possibili : **
5° flag - costi industriali       1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
6° flag - costi generali          1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
7° flag - margini                 1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
_r_Per maggiori dettagli si faccia riferimento alla struttura del costo.

## CONTENUTO DEI CAMPI
 :  : FLD T$A,1 **Inc. 1.% Indiretti**
_r_I sette flags di ciascun campo sono suddivisi in due gruppi.
**I primi 4 flags indicano quali voci del COSTO DIRETTO considerare ed hanno il seguente **significato : **
**Valori possibili : **
1° flag - materiale               1 - c. variabile   (solo indice del costo variabile)
                                  2 - c. fisso       (solo indice del costo fisso)
                                  3 - entrambi costi (indice c.variabile + indice c.fisso)
2° flag - lavor.esterne           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
3° flag - lavoro    _R_*           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
4° flag - macchina  _R_*           1 - c. variabile
                                  2 - c. fisso
                                  3 - entrambi costi
.
                    _R_* La gestione del lavoro flag 3 e 4 nel caso di calcolo utilizzando
                        la tabella D0C viene rimodulata. Il flag 4 non viene gestito ed il
                        flag 3 assume il valore seguent :   _5_1 - Costi del livello
                                                          _5_2 - c. fisso
                                                          _5_3 - entrambi i livelli
**Gli ultimi 3 flags indicano quali voci delle RICARICHE considerare ed hanno il seguente **significato : **
                                 **Valori possibili : **
5° flag - costi industriali       1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
6° flag - costi generali          1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
7° flag - margini                 1 - solo primo
                                  2 - solo secondo
                                  3 - solo terzo
                                  4 - primo+secondo
                                  5 - primo+terzo
                                  6 - secondo+terzo
                                  7 - tutti e tre
_r_Per maggiori dettagli si faccia riferimento alla struttura del costo.
 :  : FLD T$A,2.T$A,1
 :  : FLD T$A,3.T$A,1
 :  : FLD T$A,4.T$A,1
 :  : FLD T$A,5.T$A,1
 :  : FLD T$A,6.T$A,1
 :  : FLD T$A,7.T$A,1
 :  : FLD T$A,8.T$A,1
 :  : FLD T$A,9.T$A,1
 :  : FLD T$A,10.T$A,1
 :  : FLD T$A,11.T$A,1
 :  : FLD DC1,02.DC1,01
