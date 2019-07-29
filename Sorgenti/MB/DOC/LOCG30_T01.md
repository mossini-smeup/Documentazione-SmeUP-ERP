# Sezioni dell'XML

## Setup
Il setup viene nella modalità standard, nodi Setup, program, G30.

Il wizard è definito nello script GRA_G30.








## Setup - OLD
Xml di esempio : 
>. Setup
.  Pres  FormType="TREE/TAB/ONE-SEC"
.   AddAuxSection="1/blank"
.  Resp  InputType="RIS/FIX/SEC"
.   OutputType="RIS/FIX/SEC"
.  Rules  Execution="SECTION/QUESTION/blank"
.   Compile="1/blank"


### tag InputForm  - non ancora implementato(1)
Definisce come usare l'XML che descrive la struttura del form.

- TABLE :  l'xml contiene la struttrua del questionario secondo lo standard del configuratore
- SCRIPT :  l'Xml contiene un insieme di righe. Ogni riga è una riga di script e definisce domande e sezioni.
(1) il modulo G30 se trova nell'XML passato un tag Riga suppone che provenga da script e costruisce un Xml secondo la struttura standard.


### tag Resp
Definisce come utilizzare l'XML in input al questionario e come formattare l'XML in output al questionario delle risposte

- Attributo  InputType - non implementato(2)
Definisce come viene utilizzato l'XML delle risposte passato in input al questionario
    valori possibili
        RIS :  la risposta è contenuta in un tag Risposta (ogni risposta un tag)
        FIX :  le risposte sono contenute nel CDATA di un tag DATI in una stringa a larghezza fissa (usato per la manutenzione tabelle)
        SEC :  le risposte sono divise per sezioni
- Attributo  OutputType
Definisce come devono essere formattate le risposte dell'utente in output al questionario
    valori possibili
        RIS :  la risposta è contenuta in un tag Risposta (ogni risposta un tag)
        FIX :  le risposte sono contenute nel CDATA di un tag DATI in una stringa a larghezza fissa (usato per la manutenzione tabelle)
        SEC :  le risposte sono divise per sezioni

(2)  il modulo G30 cerca di decodificare l'XML delle risposte che arriva da AS400 :  se presente un tag DATI suppone che siano passate a larghezza fissa, se presenti tag <Risposta ....> carica i dati secondo il modo standard altrimenti analizza l'XML, che risulta suddiviso per sezioni e carica le risposte nel questionario.

### tag Pres
Definisce come viene mostrato il questionario
Questi sono gli attributi e i possibili valori : 

- FormType :  definisce la forma di presentazione
 --  ONE_SEC :  mostro una sola sezione. Se nel questionario ne sono presenti più di una viene mostrata solo la prima.
 --  TREE :  Il questionario mostra sulla sinistra l'albero delle sezioni e sulla destra la prima sezione visibile.
 --  TAB :  mostro le sezioni come un elenco di tab. Non vengono eseguite regole.
- AddAuxSection :  specifico se aggiungere la sezione con i dati ausiliari (data creazione, data modifica, utente creazione utente modifica
                           questionario, descrizione)


### tag Rules
Definisce il tipo di esecuzione della regola
attributi : 

-  Execution
    valori possibili : 
        SECTION :  le regole vengono eseguite al cambio di sezione
        QUESTION :  le regole vengono eseguite alla modifica di una risposta di una domanda
        blank :   le regole non vengono eseguite


## l'XML delle risposte (forma di input e di output)
Il modulo G30 è in grado di ricevere 3 formati di risposte in input e di restituire gli stessi formati in output.
Di seguito la descrizione di questi tre formati

- RIS :  ogni risposta viene inserita in un tag Risposta con i seguenti attributi
  . Ris è il codice della risposta
  . Ogg è il tipo parametro della risposta
  . Dec è la decodifica della risposta
  . Dom è il codice dellla domanda
  . Flg in posizione 1 riporta la forzatura della domanda, in posizione 3 riporta la forzatura della post regola
  . Cfg riporta le risposte delle domande configurate :  la risposta della domanda principale è  nell'attributo Ris, le altre in questo. Il campo è formattato a larghezza fissa.
- FIX :  le risposte vengono inserite nel CDATA di un campo DATI formattate a larghezza fissa. E' usato quando si passano le risposte di una tabella.
- SET :  le risposte sono passate divise per sezione. La divisione per ora è fatta con un XML stile a quello di setup dell'emulatore

