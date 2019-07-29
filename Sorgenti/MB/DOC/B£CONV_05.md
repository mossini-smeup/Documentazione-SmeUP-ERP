# PREPARAZIONE AMBIENTE
Per la preparazione del nuovo ambiente si rimanda al documento del progetto Time To Run : 
- [Installazione Sme.UP&-x2f;Looc.UP](Sorgenti/MB/DOC/A£BASE_INS)

Per crare un nuovo ambiente pulito copiandolo da SMEUP_FIL utilizzare l'istruzione 'sbmjob cmd(cpylib fromlib(SMEUP_FIL) tolib(SMEDATXXX)) *jobq(qbatch)'

# CREAZIONE AZIENDA
Creare l'ente AZI relativo all'azienda in conversione

# TABELLE

Vanno ripresi da modello gli elementi delle seguenti tabelle in modo da avere in linea i passi dei flussi di conversione con le relative variabili e la tebella di impostazione degli alias di conversione : 

 :  : DEC T(ST) P() K(B£H)
 :  : DEC T(ST) P() K(B£JCV)
 :  : DEC T(ST) P() K(B§VCV)
 :  : DEC T(TA) P(C£K) K(CON)

Vanno completate le seguenti tabelle : 

 :  : DEC T(ST) P() K(B§W)
Nella tabella B§W sarà necessario indicare quali tabelle andranno convertite e in che modalità.
Vanno ovviamente definiti precedentemente i settori da convertire. Quindi, se ad esempio si vorrà convertire il piano dei conti dell'azienda 03 sarà prima di tutto necessario creare l'eventuale sottosettore C5B03 ed inserire poi nella tabella B§W l'elemento C5B03.

 :  : DEC T(ST) P() K(PER)
Sarà necessario creare il sottosettore XX della tabella PER (dove XX corrisponde al codice dell'azienda). Per la compilazione degli elementi della tabella PERXX è disponibile la /copy PE8 con funzione MAN e metodo CRE.
 :  : INI Test PE8      >>
 :  : CMD CALL TSTPE8
 :  : FIN

Verificare inoltre l'impostazione delle tabelle : 
 :  : DEC T(ST) P() K(B£1)
 :  : DEC T(ST) P() K(B£2)

# ALIAS

Impostazione degli alias di conversione : 

 :  : INI Data entry Alias      >>
 :  : CMD CALL C£AL01G
 :  : FIN

# STRUMENTI DI LETTURA DATABASE

Da loocup è possibile convertire file di altri database in file as400 tramite il menù Strumenti -> Migrazione DB

Le /COPY £G80 legge file dall'IFS e la £G43 scompatta file .csv
 :  : INI Test G80      >>
 :  : CMD CALL TSTG80
 :  : FIN
 :  : INI Test G43      >>
 :  : CMD CALL TSTG43
 :  : FIN

# SQL DI CONTROLLO
E' presente nella scheda del modulo B£CONV una sezione "SQL di controllo" in cui sono presenti alcune selezioni preparate per effettuare delle verifiche di pre-conversione.
E' possibile aggiungere ulteriori istruzioni SQL modificando lo script LOA25_ CodiceAmbiente (ad esempio LOA25_ A7 ) in SCP_SET.
