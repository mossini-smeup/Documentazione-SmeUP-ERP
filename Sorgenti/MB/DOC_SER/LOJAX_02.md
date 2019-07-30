## Obiettivo
Gestire, tramite un programma esterno ai servizi, la compilazione e completamento dell'XML permettendo così un'estensione dello stesso senza dover essere costretti ad una ricompilazione di massa.

## Gerarchia
La gerarchia viene costruita tramite il tipo nodo ricevuto.
Il tipo nodo rappresenta, oltre alla gerarchia, attraverso il suo primo carattere il gruppo di appartenenza.
L'XML verrà ritornato raggruppando i nodi per gruppo di appartenenza.

### Tipi Nodi
 :  : PAR L(TAB)
**Tipo Noto**|**Nodo XML**|**Default**|**Descrizione**
**EX**|<Setup><Program>
**EXBS**|<EXB><Setup>||Attraverso questo nodo si possono inviare i setup costruiti nel servizio.Devono essere inviati prima del noto EXBU.
**EXBU**|<EXB><UserSetups>||Attraverso questo nodo, richiamando il LOA20_SE, viene costruito il contenuto del nodo**UserSetups**non necessita quindi di ulteriori attributi.
**EXUA**|<EXU><Actions>
**EXUCO**|<EXU><Comandi><Oggetto>
**EXUFF**|<EXU><Fields><Field>
**EXUS**|<EXU><Config>
**EXUR**|<EXU><Search>
**GC**|<Gliglia><Colonna>|IO="O"
**M**|<Messaggi><Messaggio>
**MO**|<Opzioni><Opzione>


### Costruttori di nodi
 :  : PAR L(TAB)
**Tipo Noto**|Descrizione
***VAL**|Comunica i Tipi nodi attraverso la forma valori TNo(...) Dat(...) NVL(...)
***SCP**|Riceve lo script da leggere in formato Lib(...) Fil(...) Mem(...) Flt(...), il tag dello script deve essere G.SET.TipoNodo. Tramite il valore Flt viene passata la porzione di tag che si vuole filtrare. Crea i nodi letti dallo script.
**GE**|Riceve le colonne della griglia nella schiera**£JaxSWK**, crea i nodi GC
**EXUEF**|Riceve i field deli fields nella schiera **£JayFldLst**, crea i nodi EXUFF


La gerarchia viene quindi generata attraverso i tipi nodi conosciuti.
Se per esempio utilizziamo il tipo nodo EXUA, implicitamente, dichiariamo anche il nodo EX costruendo così la gerarchia : 
<Setup>
<Program>
<EXU>
<Actions>
Ad ogni dichiarazione di un nuovo tipo nodo, se questo è già presente nella struttura, viene automaticamente chiusa la struttura fino al livello dichiarato. (E' possibile passare un'attributo per omettere questo comportamento)

I nodi si chiudono anche per dichiarazioni di tipi nodi di diversa gerarchia.
Quindi se ora utilizziamo il tipo nodo EXUCO, otterremo la chiusura del nodo Action e l'apertura deli nodi Comandi e Oggetto in quanto la prima parte dei tipi nodi coincide EXU, e quindi viene chiuso il solo livello discordante "A".

### Nodi espliciti
E' possibile costruire nodi senza derivarli dal  tipo nodo, bisogna però attribuirgli una seguenza gerarchica coerente per non incorrere in chiusure inaspettate dei nodi.
Se si dichiara un Nodo questo non costruirà la gerarchia attraverso il proprio tipo nodo.

## Struttura e Contesto
I nodi sono raggruppati per Struttura e contesto, quindi prima di operare sulla costruzione dei nodi bisogna dichiarare l'apertura di un contesto appropriato.
Alla dichiarazione di un nuovo contesto viene automaticamente generata la variabile &ICon contenente il contesto.
Il contesto, e tutti gli attributi ad esso correlato, verrà distrutto una volta richiesto l'XML.

## Variabili
E' possibile definire delle variabili di contesto rendendo così possibile la generazione di script riutilizzabili.

## Programmazione
E' possibile inserire nei servizi sia il richiamo sia in formato /copy che in formato funzione.
### /copy
Per la /copy bisogna impostare i singoli campi e poi eseguire il richiamo alla routine £JAX_02
### Funzione
Se se si stà creando la struttura bisogna esegure il richiamo utilizzando l'operatore : 
**CALLP**P_RxJ02(Funzione : Metoto : TipoNodo : Immagine : Nodo : MantieniLivelliPrecedenti : Struttura : Contesto)
Mentre se in ritorno dell'XML
**EVAL**P_RxJ02(Funzione : Metoto : TipoNodo : Immagine : Nodo : MantieniLivelliPrecedenti : Struttura : Contesto), viene ritornato**CONT** se l'XML non è completo

**I parametri facoltativi sono** : 
Nodo
MantieniLivelliPrecedenti
Struttura
Contesto

Gli altri parametri sono obbligatori, il parametro Immagine, deve obbligatoriamente essere un campo**Varying con lunghezza 30000**l'xml verrà ritornato in questo campo.
