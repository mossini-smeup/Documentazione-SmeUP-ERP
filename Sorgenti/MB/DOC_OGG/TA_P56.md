# P56 - Rilevazioni
## OBIETTIVO
Definisce le impostazioni degli eventi di rilevazione, definite a livello del plant produttivo
Se assente il tipo evento £RI, al primo richiamo viene costruita l'intera struttura tabellare.
Basta entrare nel modulo rilevazioni e lanciare l'action "Elenco rilevazioni"
Per una descrizione completa digitare "HE" nel sottostante link.

 :  : DEC T(OJ) P(*PGM) K(B£G950) I(**HE = Documentazione della struttura**)

Ricordiamo che per rigenerare l'intero impianto tabellare è sufficiente eliminare l'elemento
£Ri della tabella P5D.

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
E'il codice del plant a cui si applicano le impostazioni del presente elemento di tabella
 :  : FLD T$DESC Descrizione
Descrizione

 :  : FLD T$P56A **Uscita Presenza**
Definisce la causale dell'evento di presenza in cui si registra l'uscita durante la
registrazione automatica della presenza

 :  : FLD T$P56B **Entrata Presenza**
Definisce la causale dell'evento di presenza in cui si registra l'entrata durante la
registrazione automatica della presenza

 :  : FLD T$P56C **Chiudi Presenza**
L'evento di presenza può essere utilizzato per alimentare il software di controllo presenze,
in questo caso l'evento viene chiuso quando verrà integrato.
In assenza di un software di controllo delle presenze bisogna impostare questa opzione per chiudere
immediatamente l'evento di presenza.

 :  : FLD T$P56F **Rileva presenza**
Se richiesto l'evento di presenza dell'operatore, gli eventi di rilevazione possono attivarsi
solo dopo la dichiarazione dell'evento di presenza dell'operatore stesso.
****, non rilevare
**1**, automatica, il sistema provevderà, se necessario, alla scrittura dell'evento di presenza
                     opportuno.
**2**, manuale,    l'operatore deve dichiarare l'evento di presenza di entrata per poter iniziare
                     la dichiarazione degli eventi di rilevazione.

 :  : FLD T$P56D **Modalità continua**
L'evento di rilavazione assume i codici (ordine, fase, risorsa) dell'ultimo
evento rilevato.

 :  : FLD T$P56E **Versamento continuo**
Questa opzione è valida solo per gli eventi di versamento, per fare in modo che l'attività
contenga sia il tempo sia la quantità.
La quantità dichiarata viene riportata sull'evento di rilevazione precedente, solo se
quest'ultimo è un attrezzaggio o una lavorazione.
Se impostato a 2 non verrà nemmeno scritto l'evento di versamento.

 :  : FLD T$P56H **Tipo intervallo**
E' il tipo di intervallo che verrà passato alla scrittura dell'attività.
Se non impostato verrà assunto un intervallo in secondi
