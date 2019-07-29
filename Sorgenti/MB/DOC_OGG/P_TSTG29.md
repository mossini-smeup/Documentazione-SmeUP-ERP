# PROTEZIONE A LIVELLO CAMPO.
## OBIETTIVO
Permettere l'associazione del livello di protezione relativamente ad un campo o gruppo di campi impostati dal
programmatore, per un utente in funzione contemporaneamente dei suoi livelli di autorizzazione e dei suoi desideri
## AUTORIZZAZIONI
-    Classe
-    Funzione
## MEMORIZZAZIONE SCELTE
-    Ambiente
## FUNZIONI
GESTIONE
Normalmente viene richiamata dall'interno del programma di dettaglio gestione dati per permettere all'utente di
modificare le impostazioni per la sessione in corso oppure i valori di default ripresi ad ogni prossima entrata
RECUPERO SCELTE PRECEDENTI
Richiamato automaticamente alla partenza di ogni programma a cui è applicata la funzione di "protezione livello
campo".
Se presente si recuperano i dati dalla memorizzazione di default "*". Tali opzioni sono filtrate in base alle
autorizzazioni del momento.
## NOTE TECNICHE
Definizione dei parametri di comportamento
1.   Se i dati gestiti sono tipizzati (esempio enti, distinte ecc) passare all'interno del campo
"AMBIENTE" con un massimo di 8 caratteri poichè gli ultimi sono riservati alla memorizzazione multipla
2.   La classe di protezione di default è la PLC-
3.   La funzione di protezione è normalmente il tipo del dato. Il valore assunto è ovviamente **
Trattamento dei dati ricevuti
1.   Per ogni riga di richiesta passata al programma si riceve una riga di due caratteri numerici che possono essere
mossi direttamente negli indicatori desiderati, quello a sinistra per non visualizzare, quello a destra per
proteggere.
## ESEMPIO
Protezione dei dati per anagrafico enti
-    Classe         = PLC-BRENTI
-    Funzione       = Elemento tabella BRE
-    Ambiente       = BREN-xxx dove xxx = tipo ente
Dati finanziari
-    Gruppi         =    01 Dati di base
03 Dati fiscali
-    Campi          = Indirizzo                   Gruppo 01 = Persona da contatare        Gruppo 01 = Partita IVA
           Gruppo 03
Attività preliminari
.    Definire le autorizzazioni per **/**/PLC-BRENTI
