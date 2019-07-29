# Configurazione

## Modulo
Il modulo delle statistiche è all'interno dell'applicazione V5 ed è stato denominato V5STAT (Tabella B£A-Sottosettore MO-Elemento V5STAT).


## Tabelle
I tipi di statistica sono definiti dall'oggetto di tipo V2-V5STA
 * _2_V2 :  Valori fissi SME-UP
 * _2_V5STA :  Tipo Record Statistiche

Allo stato attuale contiene i seguenti valori associati all'oggetto : 
 :  : DEC T(OG) P(V2) K(V5STA)

Tipo schiera programma : 
 * _2_AF :  Vendite Fatturato Contabilizzato
 * _2_AU :  Vendite Spedito NON contabilizzato
 * _2_AB :  Vendite Budget
 * _2_AO :  Vendite Ordini (residuo)
 * _2_AOT :  Vendite Ordini (ordinato)
 * _2_AOC :  Vendite Backlog (foto residuo a data)
 * _2_PF :  Acquisti Fatturato Contabilizzato
 * _2_PE :  Acquisti Ricevuto NON contabilizzato
 * _2_PO :  Acquisti Ordini Residuo



## Script
**SCP_AZI    Script Azioni**
Gli script in SCP_AZI sono gestiti dal pgm B£AP00G (Lanciatore Universale).

Per un approfondimento sulla sintassi degli script si rimanda alla documentazione specifica. Lo script definisce le azioni permesse, i parametri di lancio, le impostazioni ed eventuali filtri.

In generale le azioni associate al modulo sono contenute in uno script denominato in SCP_AZI come : 
_2_ M_+Nome modulo .

I membri relativi al modulo statistico sono i seguenti : 

 * _2_M_V5STAT Azioni modulo V5STAT :  definisce tutte le azioni di ripresa ed analisi sulla statistica, praticamente il menu.

 * _2_M_V5STAT02  Analisi dati  :  definisce i parametri di input dei report preparati

**SCP_SET    Script SETUP**

Nel file JASRC della libreria Smedev si trova il pgm V5SER_14, tramite cui è possibile cambiare le dimensioni dei report preparati.

Il membro V5STAT contiene : 

- la struttura del menù della scheda V5STAT
- l'elenco dei campi utilizzati come dimensioni per l'asse del pareto
- l'elenco dei campi utilizzati come valori nel pareto
- le configurazioni relative alla scheda dei Report Preparati


Il membro _V5STAT_CNG_  contiene delle istruzioni SQL relative alle "Verifiche di congruenza".
Il membro _V5STAT_COM_  contiene delle istruzioni SQL relative alle "Verifiche di completezza".
Il membro _V5STAT_COR_  contiene delle istruzioni SQL relative alle "Verifiche di correttezza".


**SCP_CFG**
V5STAT

**SCP_NAV**
V5STAT  Schemi standard per funzione SQL


## Programmi
 * _2_Lancio : 
 ** V5STA01 STAT   Ripresa Statistica - Ciclo su Insieme
 ** V5STA01S STAT  Ripresa Statistica - Singolo Oggetto (DO/E4)
 * _2_Creazione Documento su V5STAT : 
 ** V5STA05 STAT  Ripresa Statistica - Esecuzione
 ** V5STA03 STAT  Ripresa Statistica da Piano MP
 * _2_Configurazione : 
 ** V5STAT0F_F STAT  Gestione flag archivio V5STAT
 ** V5STA05_C STAT   Configurazione Parametri
 ** V5STA05_U STAT   Esempio exit aggiustamento
 * _2_Servizi : 
 ** V5SER*  in JASRC/SMEDEV
 ** LOA*  in JASRC/SMEDEV
 * _2_Schede : 
 ** SCP_SCH - Script Schede LoocUp
 ** V5STAT  scheda principale
 ** V5STATC_DO  Scheda Statistica - Singolo Doc.
 ** V5STATC_E4  Scheda Statistica - Singola Registrazione
