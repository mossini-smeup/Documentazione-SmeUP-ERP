 :  : HEA CLAS(A) STAT(10)

# OBIETTIVO

Centralizzare in un servizio generico gli aggiornamenti su file tramite matrice di aggiornamento / input panel, semplificando la creazione di matrici di aggiornamento rispetto alla realizzazione di servizi di aggiornamento specifici.
L'aggiornamento avviene tramite SQL dopo aver eseguito i controlli specifici predisposti per il file tramite apposito programma di controllo.


# PREREQUISITI
Perché sia possibile utilizzare il LOSUP_13 per l'aggiornamento sono necessari alcuni prerequisiti


- Il servizio di presentazione dei dati deve emettere una matrice nella quale i nomi delle colonne corrispondono ai nomi dei campi del file (il servizio di presentazione può essere il LOA13_SE o un servizio specifico)
- Il file su cui eseguire l'aggiornamento deve avere un logico unique
- deve essere indicato il file su cui eseguire l'aggiornamento tramite l'attributo **File()** all'interno del tag _UpdPar_ del setup della matrice o dell'input panel.
- Deve essere stato creato un apposito programma di controllo con denominazione [NOMEFILE]_A


E' possibile utilizzare il servizio in contemporanea su 500 matrici. In caso si raggiunga tale limite l'utente viene avvertito con un messaggio.

Per la comprensione dei concetti sotto riportati si rimanda alla documentazione della matrice di aggiornamento (componente EXU).
- [Matrice di aggiornamento](Sorgenti/MB/DOC/LOCEXU)

# PROGRAMMA DI CONTROLLO SPECIFICO
I controlli specifici vengono eseguiti tramite un programma di controllo per ciascun file il cui nome è  **[NOMEFILE]_A** .
Un prototipo essenziale è disponibile come LOSUP_13_A in JASRC, mentre chi volesse provare a visionare un programma di controllo più complesso può fare riferiemento al C£LIST0F_A in C£SRC.
E' possibile passare al programma di controllo alcuni parametri includendoli nell'attributo **ExitPar()** all'interno del tag _UpdPar** del setup della matrice o dell'input panel.

## FSETUP
Nella routine FSETUP è possibile completare la schiera di definizione dei campi. Tale schiera va definita in fondo al programma di controllo e, in caso sia necessario modificarne dei valori runtime, ciò va fatto nella routine FSETUP .
Per la compilazione della schiera fare riferimento alla DS £Lou13DSFld nella copy £LOU13DS.
E' possibile definire utente, data, ora e origine di inserimento e modifica come campi speciali tramite il sottocampo £Lou13TPC, ottenendone il completamento in automatico da parte delle procedure del programma di controllo e la conseguente scrittura sul file.
Sempre nella FSETUP vanno controllate le autorizzazioni specifiche per andare a reimpostare i flag £JayAutIns, £JayAutUpd e £JayAutDel che determinano le autorizzazioni di inserimento, modifica e cancellazione per la matrice di aggiornamento

## FINIT
La routine FINIT viene eseguita in inizializzazione della riga in inserimento. Per precaricare i valori è possibile qui modificare i valori delle schiere Before.

 ## FLOAD
La routine FLOAD permette il completamento campi dei ricevuti tramite la modifica delle schiere After.

## FAFTER
La routine FAFTER esegue i controlli di riga ed accende gli indicatori di errore.

## FAUTOENTER
Se la matrice è ad aggiornamento differito ed il campo ha il flag £Lou13FAR valorizzato, la convalida del campo causa una chiamata al programma di controllo con funzione AUTOENTER.
In questo caso nella routine FAUTOENTER è possibile andare a completare altri campi collegati modificando le schiere After.
La chiamata AUTOENTER esegue prima il richiamo AUTOENTER del programma di controllo, poi il richiamo LOAD. Non viene invece eseguito il richiamo AFTER.

## FAFTEXEC
La routine FAFTEXEC viene eseguita dopo che è stato eseguito l'aggiornamento del file senza errori.
Riceve ancora tutti i valori della riga e permette eventuali azioni successive all'inserimento, alla modifica o alla cancellazione. Le azioni in questione non possono prevedere l'apertura di un video in quanto vengono eseguite all'interno del job LO_E .

#  Autorizzazioni
In caso di **non esistenza del programma di controllo**  [NOMEFILE]_A i permessi di inserimento, modifica e cancellazione sono automaticamente inibiti.
E' inoltre possibile controllare autorizzazioni specifiche nella routine FSETUP del programma di controllo.

# FLUSSI
E' possibile attivare i flussi di post inserimento, post modifica e post cancellazione indicando l'oggetto del flusso tramite l'attributo **Flu(oggetto)** all'interno del tag _UpdPar** del setup della matrice o dell'input panel.
I flussi vengono eseguiti solo se la matrice di aggiornamento è monoline e se contiene il campo chiave dell'oggetto ricevuto.
I flussi vengono lanciati tramite una R function che richiama il LOSUP_13 come funzione A.

# DEMANDARE L'AGGIORNAMENTO AL PROGRAMMA DI CONTROLLO SPECIFICO
In alcuni casi può risultare necessario demandare l'esecuzione dell'aggiornamento al programma di controllo specifico anziché far eseguire l'aggiornamento al LOSUP_13 tramite SQL.
Questo per poter eseguire l'aggiornamento tramite /copy, che fa considerazioni aggiuntive sui campi o esegue dei flussi specifici.
Per attivare questa modalità e fare in modo che il programma di controllo provveda a informare il LOSUP_13 di non eseguire l'aggiornamento è necessario  restituire 'UPDEX' nel metodo della chiamata di SETUP.
Così facendo il LOSUP_13 non esegue l'aggiornamento del database, che deve invece essere eseguito  dal programma di controllo nella chiamata AFTEXEC.

**Affinché vengano correttamente ritornati a loocup i valori dei campi, i valori derivanti dall'inizializzazione per l'insert o da ragionamenti sull'update devono essere impostati nelle schiere after alla fine della chiamata AFTER  del programma di controllo.

# CONTROLLI DI CONSISTENZA
E' stato implementato nel servizio di aggiornamento generico LOSUP_13 il controllo di consistenza dei record, in modo da prevenire la modifica di un record che sia stato concorrentemente modificato da un altro utente dopo che la matrice dei dati è stata caricata.
Il controllo di consistenza è attivo in modo predefinito.

## Attenzione
Qualora si reimposti la variabile £JAYOP all'interno del programma di controllo (nomefile_A),
tipicamente caricando una riga vuota che si vuole gestire come in inserimento invece che come in
modifica, i controlli di consistenza bloccano l'operatività, in quanto il servizio cerca di leggere
la riga vuota sul file fisico senza trovarla.
In questo caso è necessario disabilitare il controllo di consistenza.

## Come disabilitare il controllo di consistenza

**NELLA ROUTINE FSETUP DEL PGM DI CONTROLLO nomefile_A IMPOSTARE A '1' LA VARIABILE**
**£JayDisCon PER DISABILITARE IL CONTROLLO DI CONSISTENZA SU TUTTI I CAMPI.**

>     C*--------------------------------------------------------------*
    RD*    SETUP (Completamento definizione campi)
     C*--------------------------------------------------------------*
     C* Completa la schiera di definizione dei campi
     C     FSETUP        BEGSR
     C ....
     C ....
     C                   EVAL      £JayDisCon='1'
     C*
     C                   ENDSR



**E' INOLTRE POSSIBILE DISABILITARE IL CONTROLLO DI CONSISTENZA SU UN SINGOLO CAMPO **
**ANDANDO AD IMPOSTARE A 'B' L' 87mo CARATTERE NELLA SCHIERA DEI CAMPI IN FONDO**
**AL PGM DI CONTROLLO nomefile_A .**
Questo è utile nel caso si voglia gestire dei campi della matrice di aggiornamento che non siano
campi del file.


# DS corrispondente alla schiera di definizione dei campi in fondo al programma di controllo

>
D £Lou13DSFld     DS                                                       DS Campo
D  £Lou13FNM                    10                                          Nome
D  £Lou13FIO                     1                                          B/O/I/H/K
D* O=Obbligatorio; N=Non obbligatorio
D  £Lou13FOB                     1                                          Obbligatorio (O)
D* A=AS400; B=No controllo; C=Loocup
D  £Lou13FNT                     1                                          Controllo
D  £Lou13FAR                     1                                          Avanzamento record
D  £Lou13FFM                    10                                          Formato (LC/UC)
D  £Lou13FOG                    20                                          Tipo/parametro
D  £Lou13FDV                    40                                          Default value
D* DI=Data ins.; DM=Data mod.; OI=Ora ins.; OM=Ora mod.;
D* UI=Utente ins.; UM=Utente mod.; UA=Utente ins./mod.;
D* GI=Origine ins.; GM=Origine mod.; GA=Origine ins./mod.;
D  £Lou13TPC                     2                                          Tipo campo speciale
D* A=Controlla B=No controllo
D  £Lou13FNC                     1                                          Contr. consistenza


