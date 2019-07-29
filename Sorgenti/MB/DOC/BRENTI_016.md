# "CN_F" Script Dati Aggiuntivi su Campi per Contatto
Questo script permette di parametrizzare a livello di tipo contatto, alcuni dati riguardanti il singolo campo o la singola estensione. Il nome del membro è dato dalla radice fissa "CN_F" + il tipo contatto (tabella TABRE).

Lo script può essere compilato con i tag E.FLD. Per il dettaglio delle funzionalità si veda l'help di campo dal richiamo del wizard del tag.

 :  : DEC T(MB) P(SCP_SET) K(CN_F[TA.BRE]) I(**Script Campi >>)
 :  : DEC T(ST) P() K(BRE) I(**Tipi contatto  >>)

# "CN_£NO" Script Dati Nominativo
Questo script è unico per applicazione e va a definire nel caso di attivazione della gestione dei nominativi quali vengono gestiti a tale livello. In questo script vanno semplicemente elencati i nomi di tali campi (per le estensioni scrivo "BRI"+ codice estensione)
 :  : DEC T(MB) P(SCP_SET) K(CN_£NO) I(**Script Campi Nominativo >>)

# "CN_P" Script Prospettive
Tramite questi script si definisce l'insieme dei dati che vanno a definire un metodo di interrogazione dei dati anagrafici. Il codice dello script, fermo restando la radice "CN_P", può essere costruito secondo i seguenti criteri : 
 - CN_P + un numero progressivo da 1 a 30 definisce una prospettiva comune a tutti i tipi contatto
 - CN_P + elemento TABRE + un numero progressivo da 1 a 30 definisce una prospettiva specifica di un certo tipo contatto
 - CN_P£ + un numero progressivo da 1 a 30 definisce le prospettive standard fornite di default

Lo script può essere compilato con i tag E.PRO, E.PAR e E.FUN.
Per il dettaglio delle funzionalità si veda l'help di campo dal richiamo del wizard di ogni tag.

 :  : DEC T(MB) P(SCP_SET) K([MB.SCP_SET.CN_P.CN_P999999]) I(**Script Prospettive >>)
 :  : DEC T(ST) P() K(*CNIE) I(**Intestazioni prospettive  >>)
