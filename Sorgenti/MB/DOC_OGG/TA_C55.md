# C55 - Impostazioni base Tesoreria
 :  : DEC T(ST) K(C55)
## OBIETTIVO
Definisce i parametri generali di impostazione per i programmi di gestione tesoreria
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C55A **Attiva la tesoreria**
Definisce l'attivazione di tutti i pgm relativi alla gestione e all'interrogazione della tesoreria.
 :  : FLD T$C55B **% Ritenuta**

 :  : FLD T$C55C **Calendario di rif. per il calcolo dei giorni valuta**
Definisce la risorsa di riferimento del calendario da prendere in considerazione per il calcolo dei giorni di valuta
 :  : FLD T$C55D **GG scostamento Data Operazione**
È il numero massimo di giorni per i quali la data operazione può scostarsi dalla data registrazione
 :  : FLD T$C55E **GG scostamento Data Valuta**
È il numero massimo di giorni per i quali la data operazione può scostarsi dalla data operazione
 :  : FLD T$C55G **Cond. per Operazione**
Tramite questo campo è possibile indicare se le condizioni per operazione vengono fissate per causale ABI o per causale contabile. Nel caso, l'elemento della D5OCN £RC dovrà essere adeguato sostituiendo l'utilizzo della TAV§O con la TAC5V&&.
 :  : FLD T$C55H **Analisi Giacienza Media**
Nell'analisi giacienza/indebitamento determina la modalità con cui viene determinato il totale dei gg del periodo di analisi, per tutte le dimensioni che non siano il rapporto bancario.
 :  : FLD T$C55I **Exit su Stimati**
Attiva pgm di exit C5C5G3_x, tramite il quale è possibile modificare o escludere (accendendo il 35) le scadenze che vengono elaborate come movimenti stimati.
 :  : FLD T$C55J **Fido Promiscuo**
Attiva nei pgm il controllo e delle logiche del Fido Promiscuo (ove sia stato previsto) nonche l'evidenza dello stesso nelle interrogazioni di tesoreria.
 :  : FLD T$C55K **Exit Fido Promiscuo**
Attiva l'exit C5C6E0_x, tramite esso sarà possibile intervenire sulle logiche standard di distribuzione del fido promiscuo. Come esempio può essere ripreso il programma standard stesso.
Per le logiche standard si veda la documentazione della /COPY £C6E (funzione CAL).
 :  : FLD T$C55L **Exit Rettifiche Previsionali**
Attiva l'exit C5C5G3_x, tramite esso e i metodi MOV dell'exit, sarà possibile applicare delle rettifiche previsionali ai movimenti di tesoreria. Si veda l'exit di esempio. La scopo per cui è nata l'exit è principalmente quello di poter diminuire l'importo di accredito degli effetti per una previsione di insoluti. NOTA BENE :  attivando questa exit si attiva nelle interrogazioni anche la scelta di considerare o meno le "rettifiche previsionali". Tale scelta arriverà nell'exit attraverso il campo £C5GRT :  per tale motivo è MOLTO importante applicare le rettifiche solo in funzione della valorizzazione di questo campo.

