### Prerequisiti
Devono esistere i programmi
 :  : DEC T(OJ) P(*PGM) K(B£UT24A)

### Verifiche di corretta impostazione
Ricompilare manualmente un programma (Esempio "BRAR01L di &SMESRC")

### Modo 1 - Richiamo manuale del programma B£UT24
  :  : INI    Esecuzione richiamo manuale (modo1)
  :  : CMD B£UT24 FUNZ(CCO) METO(UI) SMEM(T) FILO(&SMESRC/BRSRC)  MEMS(BRAR01L) FILD(&SMEUPOBJ/SRC) MEMD(BRAR01L)
  :  : FIN

 ### Modo 2 - Opzione del PDM
* Impostare sul PDM file opzioni QAUOOPT di &SMEDEV oppure &SMEUPOBJ
* Aggiungere manualmente se necessario (Sostituire la e commerciale)

      **XI**=B£UT24 FUNZ(CCO) METO(UI) SMEM(T) FILO(eL/eF) MEMS(eN) FILD(SMEUPUIOJ/SRC) MEMD(eN)
      **X0**=SBMJOB CMD(B£QQ02 B£CMD(B£UT24 FUNZ(CCO) METO(UI) SMEM(T) FILO(eL/eF) MEMS(eN) FILD(SMEUPUIOJ/SRC) MEMD(eN))) CPYENVVAR(*YES)
      **XS**=? SBMJOB CMD(B£QQ02 B£CMD(B£UT24B FUNZ(CCO) METO(UI) SMEM(N) FILO(eL/eN) FILD(SMEUPUIOJ/SRC))) JOB(eN) JOBQ(QBATCH2) CPYENVVAR(*YES)
      **Xx**=Eccetera a piacimento

### Ricompilazioni ambiente di base completo
La prima volta, se ricevuti solo i sorgenti o al caricamento delle sucessive PTF bisogna riadeguare l'intero applicativo eseguendo il comando descritto sotto
Tale programma compila tutti i sorgenti delle seguenti librerie : 
    **>**Libreria cliente  LIBPER      :  : DEC T(OJ) P(*LIB) K(&LIBPER) I(*NONE)
    **>**Libreria ß Test   SMETST      :  : DEC T(OJ) P(*LIB) K(&SMETST) I(*NONE)
    **>**Libreria sviluppo SMEDEV      :  : DEC T(OJ) P(*LIB) K(&SMEDEV) I(*NONE)
    **>**Libreria rilascio SMESRC      :  : DEC T(OJ) P(*LIB) K(&SMESRC) I(*NONE)
  :  : INI   Compilazione di tutto il sistema impostato (Richiede conferma)
  :  : CMD ?SBMJOB CMD(B£QQ02 B£CMD(CALL PGM(B£UT27CL) PARM(QBATCH))) CPYENVVAR(*YES)
  :  : FIN
 ### Compilazione di un singolo file sorgente
  :  : INI   Compilazione di un singolo file sorgente (Richiede conferma)
  :  : CMD ?SBMJOB CMD(B£QQ02 B£CMD(B£UT24B FUNZ(CCO) METO(UI) SMEM(N) FILO("<MyLib>"/"<MyFile>") FILD("<MyLbUI>"/SRC))) JOB(UISRC) JOBQ(QBATCH) CPYENVVAR(*YES)
  :  : FIN

### Ricompilazioni libreria personalizzazioni
    **>**Libreria person.  LIBPER      :  : DEC T(OJ) P(*LIB) K(&LIBPER) I(*NONE)
  :  : INI   Ricompilazione dei programmi modificati oggi
  :  : CMD ?SBMJOB CMD(B£QQ02 B£CMD(CALL PGM(B£UT26CL) PARM(&LIBPER))) CPYENVVAR(*YES)
  :  : FIN

### Allineamento
Per avere un'ambiente conforme a quello in uso bisogna eseguire l'allineamento dei programmi personali modificati giornalmente. E' opportuno impostare nello schedulatore il seguente lavoro.
  :  : INI   Aggiunta allo schedulatore giornaliero delle modifiche del giorno. (Da oggi)
  :  : CMD ?ADDJOBSCDE JOB(UI_DAY) CMD(CALL PGM(B£UT26CL) PARM(&LIBPER))
 FRQ(*WEEKLY) SCDDATE(*NONE) SCDTIME(180000)
 TEXT('Ricompilazioni ogegtti modificati nel giorno')
  :  : FIN
