# INTRODUZIONE
## Funzioni e metodi
 * GES       Gestione
 ** INT       Interrogazione
 ** MOD       Modifica
 ** IMM       Immissione
 ** AGG       Aggiornamento (Da svil.)
 * FUL       Funzioni su listino
 ** RIC       Ricerca listino valido
 ** VAL       Verifica validità listino
 ** SEZ       Presentaz.Sez.di un listino
 * SPO       Sezioni per oggetto
 ** PRE       Presentazioni
 * RIP       Ripresa valore listino
 ** DOD       Passi Ripresa Valori
 * SIG       Significato valori
 * STR       Analisi Struttura
 ** OGG       Ritorno Oggetti
 ** EOG       Esplosione Tipi Listino Per Oggetti
 ** ETI       Esplosione per Listino
 ** ESZ       Esplosione per Tipo Sezione
 ** EVA       Esplosione per Valori

## STR Analisi Struttura

La scansione inizia tramite la £C£LMS a blank. In questo campo il CONT significa che la scansione continua,
mentre FINE che è arrivata a conclusione.

### COM
Viene ritornata la struttura tabellare completa
* INPUT
** Nessuno
* OUTPUT
** £C£L_C£LSS
** £C£L_C£LEL
** £C£L_C£LDS
** £C£L_C£LLI
** £C£L_C£VSS
** £C£L_C£VEL
** £C£L_C£VDS
** £C£L_C£VLI
** £C£L_B£GEL
** £C£L_B£GDS
** £C£L_B£GLI

### OGG
* INPUT
** Se vengono passati £C£LAR/LI/SE vengono tornati solo gli oggetti della combinazione
** Se i precedenti parametri sono blank vengono tornati gli oggetti di tutto l'ambiente
* OUTPUT
** £C£L_OG

### EOG
* INPUT
** £C£LAR/LI
* OUTPUT
** £C£L_C£LSS
** £C£L_C£LEL
** £C£L_C£LDS
** £C£L_C£VSS
** £C£L_C£VEL
** £C£L_C£VDS
** £C£L_UT
** £C£L_KY

### ETI
* INPUT
** £C£LAR/LI
* OUTPUT
** £C£L_C£LSS
** £C£L_C£LEL
** £C£L_C£LDS
** £C£L_C£VSS
** £C£L_C£VEL
** £C£L_C£VDS
** £C£L_UT

### ESE
* INPUT
** £C£LSS/SE
* OUTPUT
** £C£L_C£LSS
** £C£L_C£LEL
** £C£L_C£LDS
** £C£L_C£VSS
** £C£L_C£VEL
** £C£L_C£VDS
** £C£L_UT

### EVA
* INPUT
** £C£LSV/£C£LVA
* OUTPUT
** £C£L_C£LSS
** £C£L_C£LEL
** £C£L_C£LDS
** £C£L_C£VSS
** £C£L_C£VEL
** £C£L_C£VDS
** £C£L_UT


## Formato video
![TSTC£L_01](http://localhost:3000/immagini/MBDOC_OGG-P_TSTC£L/TSTCXL_01.png)