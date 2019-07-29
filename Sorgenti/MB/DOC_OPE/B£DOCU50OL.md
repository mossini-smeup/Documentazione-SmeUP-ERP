# Struttura della documentazione
## Documentazione applicazione
La documentazione di ogni applicazione deve essere strutturata in tre capitoli distinti, in base al contenuto : 

- _2_Documentazione generale :  contiene argomenti di tipo generico relativi all'applicazione;
- _2_Documentazione specifica per modulo :  contiene l'elenco delle documentazioni specifiche per ciascun modulo;
- _2_Documentazione particolare :  tratta di argomenti molto particolari, anche FAQ.


## Documentazione modulo
La documentazione di ogni modulo deve essere strutturata in cinque capitoli distinti, in base all'utente destinatario : 

- _2_Documentazione Commerciale :  utile a chi si dedica alla vendita (contenuti di brochures, corsi, presentazioni, ecc...);
- _2_Documentazione Visione :  tracciano visioni generali e introduttive dell'argomento;
- _2_Documentazione Operativa :  rivolta all'utilizzatore generico dell'applicativo;
- _2_Documentazione Applicativa :  rivolta ai consulenti e a chi deve customizzare l'applicativo;
- _2_Documentazione Tecnica :  rivolta a programmatori e installatori.


# Membri
## Ubicazione dei membri
 :  : PAR L(LET)
- File DOC in ambiente di sviluppo       in libreria SMEDEV      per documentare i moduli delle applicazioni
- File DOC in ambiente di modelli        in libreria SMEMOD
- File DOC_VIS in ambiente di sviluppo     in libreria SMEDEV      per i documenti visione delle applicazioni
- File DOC_PER per le personalizzazioni  in libreria PER_xxx
- File DOC_DEM per le esempi / demo      in libreria SMEUP_DEM
- File DOC_OGG per gli oggetti           in libreria SMEDEV      per documentare oggetti quali :  programmi, tabelle, archivi, servizi, ecc...)
- File DOC_SER per i servizi                               in libreria SMEDEV
- File DOC_SCH per le schede                               in libreria SMEDEV


## Denominazione doc. di applicazione
Prende il nome dell'applicazione e i documenti a questo livello vanno denominati come : 

- aa_xxx
  aa         = Applicazione (tabella B£A)
  xxx       = Capitolo per il modulo (libero)


## Denominazione doc. di modulo
Prende il nome del modulo stesso (es. :  'B£BASE', 'C£MODI', ecc...)
I documenti a questo livello vanno denominati come : 

- aabbbb_xxx
  aa         = Applicazione (tabella B£A)
  bbbb       = Modulo dell'applicazione (tabella B£AMO)
  xxx       = Capitolo per il modulo (libero)


## Denominazioni doc. oggetti

- o_xxxxxxxx
  o_         = Tipo oggetto (P = Programma, T = Tabella, F = File, ...)
  xxxxxxxx  = nome oggetto


## Denominazioni doc. servizi

- aaSER_xx
  aa         = Applicazione (tabella B£A)
  SER        = Fisso servizio
  _xx        = Progressivo (libero)






