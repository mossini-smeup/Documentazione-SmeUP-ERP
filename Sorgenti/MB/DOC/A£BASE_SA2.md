
# Libreria SMESRC
Nella libreria SMESRC i file sorgenti dei programmi e dei file video sono organizzati per applicazione. Le applicazioni di Smeup sono codificate nella tabella B£A : 

 :  : DEC T(ST) K(B£A)

**Per ogni applicazione** della libreria SMESRC è presente**un apposito file sorgente** dato dalla seguente codifica :  **xxSRC**, dove _xx** indica l'applicazione.

Es. :  I programmi dell'applicazione della contabilità (codice C5) sono nel file sorgente _5_C5SRC.

Un'**eccezione** a questa regola sono i programmi dell'applicazione **B£** (applicazione delle funzioni base).
Questi, invece che essere contenuti nel file B£SRC,  si suddividono nei file **SMESRC** per le funzioni base e **SMEUTI** per le funzioni di utilità e le TST (applicazioni di simulazione delle /copy).

# Libreria SMESTD
Nella libreria SMESTD abbiamo **un file di dizionario per ogni applicazione** codificato nel seguente modo :  DIZ_+Applicazione
Vi si trovano inoltre i seguenti file : 


| QILEGEN | /COPY SMEUP |
| ---|----|
| SRCDB | Sorgenti delle definizioni dei file di dati |
| SRCDZ | Sorgenti delle definizioni dei Dizionari cui le definizioni dei file di dati fanno riferimento |
| SRCWK | Sorgenti delle definizioni dei file di work |
| QPARILE| /COPY SMEUP per definizioni esterne |
| QAPIGEN | Api IBM utilizzate nei pgm SMEUP (in questo modo si evita che i clienti abbiano versioni diverse delle Api ovviando a problemi di compatibilità) |
| 


# Libreria SMEDEV
Nella libreria SMEDEV viene replicata la stessa struttura dei file presente sia nella SMESRC che nella SMESTD e nella SMEUP_OBJ.
Si potranno quindi trovare, ad esempio, sia i file xxSRC (come nella SMESRC) che il file QILEGEN (come nella SMESTD), che gli oggetti compilati.
_Naturalmente nella SMEDEV si troveranno solamente sorgenti e oggetti dei file che hanno subito delle modifiche dall'ultimo rilascio.

**ECCEZIONE**
Nei file **DOC*** ci sono i sorgenti della documentazione; vengono copiati integralmente nella SMEDEV all'atto del rilascio perché il sistema non fa la risalita.
Lo stesso avviene per il file dei messaggi e altri sorgenti interpretati come i file **SCP*** degli script :  la ricerca dei membri viene fatta in una specifica libreria perché cercare in tutte non sarebbe accettabile in termini di performance.

# Librerie dei clienti
Nelle librerie dei clienti si trovano i seguenti file : 

| SMEUP | Personalizzazioni di programmi standard |
| ---|----|
| SRC | Programmi specifici o _exit_ (le exit a volte si trovano in SRC_E) |
| SRCDB | Sorgenti di file di dati personalizzati |
| SRC_x1 | Interfacce con altri gestionali (contengono solo i sorgenti perché vanno ricompilati presso il cliente. Applicativi codificati in tabella *CNTTAA). I sorgenti delle interfacce standard si trovano nella SMESRC |
| SCP_SCH | Contiene gli script delle schede di Looc.Up personalizzate del cliente |
| 


- [Personalizzazioni](Sorgenti/MB/DOC/A£BASE_SG)

# Modificare un sorgente
Utilizzare i branch
 :  : DEC T(SU) P(BAS) K(A£_103)

Le annotazioni delle modifiche nei pgm standard vanno sempre riportate in testa al sorgente nel modo riportato di seguito, dove :  gg/mm/aa=data di modifica, nn.mm=versione rilascio alla data di modifica, xx=Utente che ha effettuato la modifica, e nella Breve descrizione va descritta la modifica
> V* ==============================================================
 V* MODIFICHE Ril.  T Au Descrizione
 V* gg/mm/aa  nn.mm i xx Breve descrizione
 V* ==============================================================
 V* 13/09/05   V2R1      PF Creazione Programma
 V* ==============================================================


In modo simile vanno annotate le personalizzazioni fatte per il cliente : 
> V* ==============================================================
 V* PERSONALIZZAZIONI Ril.  T Au Descrizione
 V* gg/mm/aa  nn.mm i xx Breve descrizione
 V* ==============================================================


In aggiunta le modifiche di personalizzazione vanno bene evidenziate all'interno del sorgente, all'inizio e alla fine delle modifiche, come riportato di seguito.
> C* I.MOD.cli                xx inizio modifica  (con cli che indica il cliente)
    ...
 C* F.MOD                    xx fine modifica (con cli che indica il cliente)


Su una modifica importante, è buona abitudine effettuare un salvataggio della versione originale : 
 - Ridenomino il pgm aggiungendo **_O**
 - Anche il tipo viene ridenominato con suffisso _O
 - Sostituisco la descrizione del sorgente con _data di modifica e utente_

I file _O vengono periodicamente eliminati.
Un livello ulteriore di salvataggio consiste nello copiare il sorgente della vecchia versione nella libreria SMESAL.

# Eliminare un sorgente
Di seguito si illustra la modalità per eliminare un programma in modo corretto e ordinato : 
- Controllare tramite UP SCA o CERCA (e tutti gli strumenti che si ritengano necessari) che tale programma non sia richiamato da programmi esistenti o non sia citato in documentazione. In caso affermativo modificare di conseguenza i programmi e/o la documentazione
- Scrivere una PTF in cui si cita la cancellazione del programma (questo è indispensabile per le potenziali personalizzazioni del programma)
- Portare il sorgente in SMEDEV (se non già presente) e ridenominare il tipo in xxx_OBS. In questo modo al successivo rilascio il sorgente verrà portato in SRCOBS e non più compilato. E' necessario segnare in testa al programma tale modifica per mantenere traccia dell'utente che ha effettuato l'operazione
- In caso il programma sia "nuovo" (quindi non presente in SMESRC) è possibile saltare il passo precedente e cancellare direttamente il programma (sorgente, oggetto ed eventuali repliche) dopo aver spostato il sorgente (con le modifiche segnate in testa) in SRCOBS
- In caso di programmi particolarmente importanti o di gruppi di programmi particolarmente corposi è necessario scrivere una apposita NTI

## Ridenominare un sorgente
La tecnica dell'_OBS vista per la cancellazione non è indicata in quanto al successivo rilascio verrebbe portato in SRCOBS senza averne la necessità.
In questi casi è sempre necessario chiedere al laboratorio che darà le istruzioni più opportune (se è solo in DEV lo si ridenomina applicando le regole della cancellazione, se è anche in SMESRC si può anche pensare di cancellare il source oppure di dargli un tipo particolare - ad esempio _O -).

# Creare un sorgente
Un sorgente nuovo va creato sempre in SMEDEV.
Se lo si vuole creare in test (ad esempio in SMEUP_TST) è necessario crearlo in SMEDEV, copiarlo in SMEUP_TST e bloccarlo. In questo modo non sarà possibile che qualcunaltro crei un sorgente con lo stesso nome.

# Suffissi tipi membri

|  Nam="Suffissi tipi membri" |
| 
| .COL Txt="Significato" LunAut="1" |
| ---|----|
| 
| .COL Txt="Suffisso" LunAut="1" |
| 
| .COL Txt="Esempio" LunAut="1" |
| Sorgente oldato|_O|RPGLE_O |
| Sorgente obsoleto|_OBS|RPGLE_OBS |
| Sorgente di esempio|_ES|RPGLE_ES |
| Nome prenotato|_ES|RPGLE_ES |
| 

