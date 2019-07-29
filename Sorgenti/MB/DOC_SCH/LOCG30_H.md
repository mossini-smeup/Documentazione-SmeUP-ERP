# Help
## Cosa riceve la scheda di help contestuale

Sono possibili 3 casi : 

### Configurazione di questionari RE Q- o RE L-

Oggetto 1 :  il questionario da cui è stata invocata.
From :  da quale componente è giunta la richiesta
Sect :  la sezione contenente la domanda
Posi :  la domanda di cui si richiede l'help


### Configurazione di tag di script
Oggetto 1 :  il questionario da cui è stato estratto il questionario associato al tag
From :  vale UIG30TagDialog
Sect :  è il nome del tag che si sta configurando
Posi :  la domanda di cui si chiede l'help


### Configurazione di parametri di servizi

Se la richiesta è giunta da un questionario di configurazione di un parametro di un servizio si ha che : 
l'oggetto 1 è il servizio
From ha il valore "Dialog"
Sect è la funzione.metodo del servizio
Posi è la domanda. Nel caso di parametri posizionali il codice della domanda è QST_xx dove xx è un progressivo.

# Scheda Help Wizard Script
Nel wizard degli script, dato un tag (es.  :  : DEC) si può aprire direttamente il configuratore che guida la compilazione. Quando non si conosce il tag da utilizzare è possibile, digitando solo  :  :  (due volte duepunti) e premendo il bottone del wizard, aprire l'albero dei tag applicabili nel contesto (es. i tag di scheda nello script di scheda, i tag di documentazione attiva editando un membro di doc., ecc..)

## Albero di selezione
![LOCTRE_041](http://localhost:3000/immagini/MBDOC_SCH-LOCG30_H/LOCTRE_041.png)
L'albero presenta i vari tag possibili organizzati in sezioni e sotto sezioni.
Il doppio click sul tag voluto chiude l'albero e ritorna all'editor dello script aprendo il configuratore del tag scelto, lo stesso si può fare inserendo il tag nel campo di "**Selezione**" in basso all'albero.

Il bottone "**Sezione**" apre altre funzioni : 

![LOCTRE_042](http://localhost:3000/immagini/MBDOC_SCH-LOCG30_H/LOCTRE_042.png)
Tra cui una menzione particolare meritano

## F20 - Editor configuratore
Apre lo script del confguratore permettendone l'editazione

![LOCTRE_043](http://localhost:3000/immagini/MBDOC_SCH-LOCG30_H/LOCTRE_043.png)
## F18 - Ricarica configuratore
Dopo averne editato lo script permette di ricaricare la nuova versione dell'albero direttamente senza uscire e rientrare.

## F19 - Scheda di help
Presenta la schedda che porta ai vari help contestuali dei vari campi di condizionamento del configuratore di un tag

![LOCTRE_044](http://localhost:3000/immagini/MBDOC_SCH-LOCG30_H/LOCTRE_044.png)