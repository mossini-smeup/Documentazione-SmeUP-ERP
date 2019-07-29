# Configurazione

## Modulo
Il modulo delle statistiche è all'interno dell'applicazione D5 ed è stato denominato D5NUOG (Tabella B£A-Sottosettore MO-Elemento D5NUOG).


## Tabelle
Attivazione del modulo
_2_TAB£7 :  Personalizzazione B£ Ambiente
_2_TAV5D :  Tipi documento

 :  : DEC T(TA) P(B£7) K(*)
 :  : DEC T(TA) P(V5D)


## Script
**SCP_AZI    Script Azioni**
Gli script in SCP_AZI sono gestiti dal pgm B£AP00G (Lanciatore Universale).

Per un approfondimento sulla sintassi degli script si rimanda alla documentazione specifica. Lo script definisce le azioni permesse, i parametri di lancio, le impostazioni ed eventuali filtri.

In generale le azioni associate al modulo sono contenute in uno script denominato in SCP_AZI come : 
_2_ M_+Nome modulo .

I membri relativi al modulo statistico sono i seguenti : 

 * _2_M_D5NUOG Azioni modulo D5NUOG :  definisce tutte le azioni di gestione dei numeri oggetto.


**SCP_SET    Script SETUP**

Il membro D5NUOG contiene : 

- la struttura del menù della scheda D5NUOG


 * _2_Schede : 
 ** SCP_SCH - Script Schede LoocUp
 ** D5NUOG      Numeri di un Oggetto
 ** D5NUOG_01   Numeri di un Oggetto - Valori memorizzati
 ** D5NUOG_02   Numeri di un Oggetto - Valori oggetto
 ** D5NUOG_03   Numeri di un Oggetto - Statistiche
 ** D5NUOG_04   Numeri di un Oggetto - Navigazione
