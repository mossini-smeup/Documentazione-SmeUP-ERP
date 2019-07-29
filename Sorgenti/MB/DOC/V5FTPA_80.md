Si suggerisce di seguito un possibile flusso implementabile facilmente in SmeUP per la gestione completamente automatica della fattura elettronica.

Il flusso proposto avrà origine successivamente alla stampa della fattura e si compone di questi passaggi : 

- Lancio della contabilizzazione delle fatture stampate tramite schedulazione del programma V5FA05A_B
- Estrazione XML fatture contabilizzate tramite schedulazione del programma V5FE16. Da sottolineare che il programma per definire quali fatture estrarre e quali no non si basa sul T§FL19 ma sull'OAV J/G10 Registrazione contabile dell'oggetto FT che viene valorizzato solo nel momento ijn cui la fattura viene effettivamente contabilizzata e non quando la fattura si ferma nel batch. Il programma può essere lanciato con l'impostazione del parametro che può essere : 
 -- blank per il lancio della generazione XML delle fatture mai inviate (T§FL12= ' ')
 -- '2'  per il lancio della generazione XML delle fatture scartate (T§FL12= '2 ').
 -- '6'  per il lancio della generazione XML delle fatture rifiutate da PA (T§FL12= '6')
 - Invio fatture elettroniche tramite schedulazione del programma V5_061B03
 - Ricezione esiti tramite schedulazione del programma V5_082_05
 - Invio mail notifica mancata consegna tramite schedulazione del programma V5FE15


Si sottolinea che, per problemi di comunicazione normalmente imputabili all'intermediario, è possibile che il punto 3 di invio delle fatture elettroniche non venga completamente eseguito lasciando le fatture elettroniche in stato 'Errore invio' (R$FL02 del file EDSEND=' 4'). Per ovviare a questo problema è possibile schedulare il programma V5_061B03 passandogli il parametro '4' in modo tale che il programma effettui nuovamente l'invio delle fatture che si trovano in stato 'Errore invio'.

Si sottolinea, infine, che anche l'estrazione dell'XML potrebbe generare errori portando la fattura i stato 'XML errato' (R$FL02='1'). Per analizzare e gestire questi errori è ovviamente necessario l'intervento dell'utente.
Per questo motivo è necessario, in ogni caso, che l'utente verifichi ogni mattina il buon esito dei flussi di generazione e invio della fattura elettronica anche semplicemente tramite il monitoraggio della Dashboard presente nel Cruscotto Invio Fatture del modulo della fatturazione elettronica.
