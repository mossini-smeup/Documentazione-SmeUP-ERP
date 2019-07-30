# OBIETTIVO
Questo servizio ha l'obiettivo di fornire le funzionalità relative alla visualizzazione della documentazione SME.up.

# FUNZIONI/METODI
## Visualizzazione come documentazione attiva (funzione DOC) _7_(VEDI NOTA SUCCESSIVA)
Restituisce un XML contenente il testo fornito in ingresso lasciato come documentazione attiva (con
' : '). In LOOC.up la visualizzazione può essere effettuata tramite editor (che interpreta i comandi d
attiva, se presenti) con modifica bloccata oppure HTML (comandi non interpretati).
Il sottometodo 'SCH' serve ad estrarre la documentazione da uno script di scheda, ignorando tutto il
primo titolo.
Il sottometodo 'HPG' serve ad estrarre l'help tecnico di un programma.
Il parametro TXT permette di formattare l'XML in modo che sia correttamente interpretato da una subsezione di tipo Text.
### Cosa legge

- Un membro di file, se l'Oggetto1 è 'MB' oppure 'OJ*PGM'. Se il membro letto è un help di tabella (
  TA_xxx di DOC_OGG) viene gestito in maniera particolare.
  Parametri : 
  £UIBP1-> Nome del file
  £UIBK1-> Nome del membro
  £UIBK2-> Nome della libreria (opzionale)
- Note strutturate, se l'Oggetto1 è di tipo 'TANSC'
  Parametri : 
  £UIBK1-> Tipo contenuto (TANSC)
  £UIBK2-> Chiave 1
  £UIBK3-> Chiave 2
  £UIBK4-> Chiave 3
  £UIBK5-> Tipo nota
- La documentazione per oggetto nel file JADOCU, negli altri casi (**IN SVILUPPO!**)
  Parametri : 
  £UIBT1+£UIBP1-> J§TIP1, £UIBK1-> J§COD1,
  £UIBT2+£UIBP2-> J§TIP2, £UIBK2-> J§COD2,
  £UIBK3-> J§DOCU, se presente, altrimenti J§DOCU='DOC'


## Visualizzazione come HTML (funzione VIS) _7_(VEDI NOTA SUCCESSIVA)
Restituisce un XML contenente il testo formattato in HTML, pronto ad essere visualizzato dal componente.
Anche questa funzione prevede il metodo 'SCH'.
### Cosa legge
Come la funzione 'DOC'.

## Nota importante sulle funzioni VIS e DOC
Se da Loocup viene richiamato il servizio con la funzione DOC, al server arriva la chiamata con funzione DOC, quindi restituisce un XML con i TAG SMEUP, tale XML non viene tradotto dal client e quindi viene mostrato il testo con i tag  :  : .
Se da Loocup viene richiamato il servizio con la funzione VIS, al server arriva la chiamata con funzione **DOC**, quindi (come prima) restituisce un XML con i TAG SMEUP, in questo caso però l'XML viene interpretato dal client che crea l'HTML e quindi viene mostrato il testo formattato.
All'AS non arriva mai la chiamata con funzione VIS. Quindi sia con VIS che con DOC il server restituitsce sempre i TAG SMEUP. La distinzione è a livello di client :  con metodo VIS traduco i TAG SMEUP in HTML, con metodo DOC non li traduco.
Riassumendo : 
 :  : PAR F(01) L(TAB) T()
- _1_Funzione inserita | _1_Funzione richiesta al server | _1_XML restituito | _1_XML passato al componente | _1_esempio di visualizzazione|
- F(HTM;JATRE_34C;VIS) 1(MB... | F(HTM;JATRE_34C;DOC) 1(MB... | con TAG SMEUP | con TAG HTML | :  : IMG P([SME.IMG]\V3ASE\JATRE_34C\VIS.jpg) H(134) W(184)|
- F(HTM;JATRE_34C;DOC) 1(MB... | F(HTM;JATRE_34C;DOC) 1(MB... | con TAG SMEUP | con TAG SMEUP | :  : IMG P([SME.IMG]\V3ASE\JATRE_34C\DOC.jpg) H(134) W(184)|


## Navigazione tra gli oggetti nella documentazione attiva (funzione OGG)
Questa funzione restituisce un albero degli oggetti referenziati in un membro di documentazione atti
 in Oggetto 1. Si può indicare nel Parametro il numero di livelli in cui scendere nella ricerca.
Può restituire i membri referenziati (metodo MBR) oppure gli oggetti di altro tipo (metodo OTH).


 :  : PRO.SER Cod="*FREE.1" Tit="Solo alcuni metodi documentati. " Fun="F(EXB;JATRE_34C;*FREE)"

 :  : PRO.SER Cod="DOC.SCH.2" Tit="Documentazione attiva. di scheda" Fun="F(EDT;JATRE_34C;DOC.SCH) 1(MB;;-(O;;MB;)) 2(**;;-(F;;**;)) 3(**;;-(F;;**;)) 4(**;;-(F;;**;)) 5(**;;-(F;;**;)) 6(**;;-(F;;**;)) P( TGID(-(F;;;TAG ID)) TXT(-(F;;V2SI/NO;Emissione in sub TXT)))"

 :  : PRO.SER Cod="DOC.SCH.3" Tit="Documentazione attiva. di scheda" Fun="F(HTM;JATRE_34C;DOC.SCH)" Ref="DOC.SCH.2"

 :  : PRO.SER Cod="VIS.SCH.4" Tit="HTML. di scheda" Fun="F(HTM;JATRE_34C;VIS.SCH) 1(MB;;-(O;;MB;)) 2(**;;-(F;;**;)) 3(**;;-(F;;**;)) 4(**;;-(F;;**;)) 5(**;;-(F;;**;)) 6(**;;-(F;;**;))"

 :  : PRO.SER Cod="VIS.HPG.5" Tit="HTML. Help tecnico di programma" Fun="F(HTM;JATRE_34C;VIS.HPG)" Ref="VIS.SCH.4"

 :  : PRO.SER Cod="OGG.MBR.6" Tit="Albero degli oggetti in un doc. Membri referenziati" Fun="F(TRE;JATRE_34C;OGG.MBR) 1(MB;;-(O;;MB;)) 2(**;;-(F;;**;)) 3(**;;-(F;;**;)) 4(**;;-(F;;**;)) 5(**;;-(F;;**;)) 6(**;;-(F;;**;)) P( NSUB(-(F;;NR;Numero di sottolivelli)))"

 :  : PRO.SER Cod="OGG.OTH.7" Tit="Albero degli oggetti in un doc. Altri oggetti" Fun="F(TRE;JATRE_34C;OGG.OTH)" Ref="OGG.MBR.6"

