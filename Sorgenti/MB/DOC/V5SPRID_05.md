## Definizione
Il DM 24.05.2005 disciplina l'obbligo di apposizione della marca da bollo su fatture cartacee ed elettroniche.
Secondo tale decreto l'imposta di bollo è obbligatoria su documenti di importo superiore a 77,47¤ che riportano : 
 * Operazioni escluse dal campo di applicazione dell'IVA ai sensi dell'art. 15 DPR 633/72
 * Operazioni esenti ai sensi dell'art. 10 DPR 633/72
 * Operazioni fuori campo iva
 * Operazioni non imponibili relative ad operazioni assimilate alle esportazioni, ai servizi internazionali, ai servizi connessi agli scambi internazionali, le cessioni agli esportatori abituali o esportazioni indirette
 * Fatture nel regime dei minimi che non comportano l'addebito dell'IVA

L'importo del bollo attualmente in vigore è di 2,00¤

## Configurazione Tabelle
Per ottenere il calcolo automatico dell'apposizione bollo è necessario configurare tre tabelle : 
 * V5S :  all'interno di questa tabella è necessario creare due codici : 
 ** Un elemento che identifica la spesa automatica del bollo. Questo elemento dovrà riportare : 
 *** Importo o percent.=2,00
 *** Tipo : Fisso/Un/Pe/Nes = F
 *** Cod.valore applicaz.= E
 *** Tipo spe/mag/sco= BV
 *** Limite di Applic.= 77,47
 *** Spese di storno :  questo campo andrà compilato solo nel caso in cui si decida di non addebitare il bollo ai clienti e in questo campo andrà inserito il codice creato al successivo punto
 ** Un elemento che permette di stornare il bollo quando questo non viene addebitato al cliente. Questo elemento dovrà riportare : 
 *** Tipo : Fisso/Un/Pe/Nes = F
 *** Cod.valore applicaz.= E
 *** Tipo spe/mag/sco= BS
 *** Limite di Applic.= 77,47

Si sottolinea che la possibilità di gestire lo storno del bollo non addebitato è disponibile solo con un rilascio V5R1 con data successiva a settembre 2018

*  IVA
All'interno della tabella IVA sarà necessario compilare il campo Addebito Bolli per quegli assoggettamenti legati alle operazioni elencate nell'introduzione di questa documentazione e che, quindi, determinano l'apposizione del bollo sulla fattura.

* COASP
All'interno della tabella COASP sarà necessario creare due codici con lo stesso valore dei codici creati nella tabella V5S. In questi due codici sarà necessario indicare come conto acquisti il conto di costo per i bolli non addebitati mentre nel conto vendite sarà necessario indicare il conto di debito su cui rilevare il debito verso erario per il successivo versamento dei bolli rilevati in fattura

## Addebito bollo
Normalmente l'importo del bollo viene addebitato al cliente; se si tratta di una pubblica amministrazione, però, il bollo non viene addebitato.
Per modificare questo comportamento standard è possibile intervenire in due modi : 
* per i clienti PA all'interno dell'estensione £51 è possibile compilare il campo Addebita spese bollo a PA con 1 per addebitare il bollo al cliente
* per i clienti non PA all'interno dell'anagrafica è possibile compilare il campo Escl. Addebito Spesa Bollo (E§FL24) con 1 per fare in modo che al cliente non venga addebitato il bollo.

## Bollo in fattura elettronica

Compilando correttamente le tabelle sopra riportate il sistema sarà in grado di identificare i documenti assoggettati a bollo e compilare i relativi TAG.
Se il bollo viene addebitato al cliente viene anche aggiunta una riga alle righe di vendita dell'importo di 2¤ relativa proprio all'addebito del bollo
