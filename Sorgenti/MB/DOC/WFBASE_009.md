# VARIABILI

In tutto lo script di workflow sono utilizzabili le variabili gestite dalla routine £G91.
In particolare le variabili specifiche di workflow sono : 

- &_AWF.NWF :  Numero ordine di workflow;
- &_AWF.TMS :  Tipo Oggetto master dell'ordine di workflow;
- &_AWF.PMS :  Parametro Oggetto master dell'ordine di workflow;
- &_AWF.OMS :  Oggetto master dell'ordine di workflow;
- &_AWF.OOW :  Oggetto owner dell'ordine di workflow;
- &_AWF.PRO :  Processo;
- &_AWF.SCP :  Script utillizzato;
- Infine, tutti gli impegni dell'ordine di workflow, con la sintassi :  &_AWF.IMPxxxdove xxx è il codice dell'impegno.


Nelle condizioni e funzioni relative alle conseguenze (sia sui luoghi sia esterne), che sono legate ad un'attività, oltre alle variabili precedenti, è disponibile anche &_AWF.ATT :  Numero attività

E' possibile costruire puntare a OAV di tutte queste variabili (anche in cascata), con la sintassi &xxx%yyy%zzz%..., dove : 

- &xxx è in nome della variabile;
- yyy è un suo OAV (ad esempio I/21);
- zzz è un OAV dell'oggetto ritornat dall'OAV precedente;
- è così via.


# VARIABILI GENERALI

E' possibile definire, in testa allo script, variabili generali utilizzabili in aggiunta a quelle definite in precedenza. Il tag con cui si definiscono è ;;VAR.

Gli ulteriori parametri definiscono se la variabile è statica oppure se è un alias :  in particolare, se il parametro 'Alias' è valorizzato, non sono significativi i parametri tipo e valore.

## VARIABILI STATICHE
Si assegna un valore che viene mantenuto per tutto lo script. Un possibile utilizzo è quello di concentrare in un unico punto le parametrizzazioni, in modo da facilitarne la modifica.

## VARIABILI ALIAS
Si possono inserire variabili che costutuiscono alias di altre variabili definite in precedenza, il cui valore è dinamicamente aggiornato. In questo modo è possibile riferirsi, all'interno dell' script, a variabili complesse (ad esempio OAV di OAV) in modo snello e parlante.

