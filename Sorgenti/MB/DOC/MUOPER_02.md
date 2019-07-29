# Descrizione

Gli oggetti sono un concetto centrale in As.UP; alcuni sono incorporati, come i processi e le librerie, ma la maggior parte sono definiti dall'utente, ad esempio gli utenti, i files o le code lavori.

Gli oggetti vengono memorizzati in risorse raccolte a loro volta in librerie

## Oggetti
* JOBD JobDescription
* USRPRF UserProfile
* DTAQ DataQueue
* ..

# URI
Gli oggetti vengono identificati in base ad una URI
esempi di uri per oggetto sono : 
* asup : //SRVLAB/QSYS/Command-WRKACTJOB
* asup : //SRVLAB/SMEDEV/Program-B£DEC0
# Comandi

L'accesso ad un oggetto è in prima istanza fornito tramite shell comandi, tipicamente via telnet o interfaccia web.

La shell comandi ha il compito di fornire all'utente una prima interazione di carattere quanto più linguistico possibile; in questo senso abbiamo la possibilità di comporre verbi + aggettivi + oggetti/soggetti in relazione alla funzione che si intende sviluppare

## Verbi
* CRT Create
* CHG Change
* DLT Delete
* DSP Display
* PRT Print
* WRK Work

## Soggetti
* JOB Job
* SPLF SpoolFile
* --

## Aggettivi
* ACT Active
* END Ended
* ..

Comandi
* WRKACTJOB
* CRTDTAQ
* ENDJOB
* DLTSPLF
