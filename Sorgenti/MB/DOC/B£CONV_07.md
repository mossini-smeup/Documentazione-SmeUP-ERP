### Controlli di post-conversione
### CONTROLLO CONGRUENZA ARCHIVIO
Tramite la funzione 20 del pgm B£RF01T è possibile verificare le incongruenze presenti su un archivio (es. la presenza di codici oggetto obsoleti e non più esistenti)

 :  : INI _9_Richiamo B£RF01T  >>
 :  : CMD CALL B£RF01T
 :  : FIN


Inoltre è presente nella scheda del modulo B£CONV una sezione "SQL di controllo" in cui sono presenti alcune selezioni preparate per effettuare delle verifiche di post-conversione.
E' possibile aggiungere ulteriori istruzioni SQL modificando lo script LOA25_CV in SCP_SET.
