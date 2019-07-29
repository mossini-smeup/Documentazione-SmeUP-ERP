Gli ambienti di Sme.up sono attivabili attraverso elementi della tabella B§1 dove è definito il menù iniziale da richiamare e la lista iniziale di librerie (B£B).

I menù richiamabili sono : 

| 
| .COL Txt="Tipo" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
|  - **S**|Menù Sme.up |
|  - **P**|Menù Sme.up :  Richiamo con Parametri |
|  - **A**|Menù ACG |
|  - **G**|Menù Sme.up con controllo autorizzazioni per gruppo utente (B£UT54) |
|  - **C**|Stringa comando |
|  - **J**|Azione Java |
| 

>Nota Bene; per poter interscambiare i vari ambienti bisogna che questi siano definiti in ogni ambiente, in altri termini le tabelle B§1 e B£B devono essere viste (oppure replicate) da tutti gli ambienti.

Gli ambienti sono associabili a : 

- Utente
- Gruppo utente
- Nome

Dopo il collegamento verrà mostrata la lista degli ambienti presenti.

Per la definizione di ambienti fare riferimento al programma di gestione B£UT55
 :  : INI Gestione Ambenti
 :  : CMD CALL B£UT55
 :  : FIN
### Autorizzazioni
Per la definizione delle autorizzazioni per gruppo utente ad azioni e menù fare riferimento al programma di gestione B£UT54
 :  : INI Gestione Autorizzazioni azioni/menù per gruppo utente
 :  : CMD CALL B£UT54
 :  : FIN
