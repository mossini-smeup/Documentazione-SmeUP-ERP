
# Introduzione
In questo documento verranno elencate alcune funzioni di debug in forma domanda-risposta
I prerequisiti per poter utilizzare queste funzioni sono il terminale e la vista di debug, che sono illustrate nel video che segue

[https://www.youtube.com/embed/zC6z9WV7VVs](https://www.youtube.com/embed/zC6z9WV7VVs)

## Il terminale : 
Web.UP mette a disposizione un terminale per l'esecuzione di comandi testuali.
Il terminale è accessibile
* Quando si è loggati, usando la combinazione Ctrl-Shift-F8
* Quando si è loggati, usando l'icona del terminale, se attiva
* Quando non si è loggati, alla pagina http://<Indirizzo Webup>/views/terminal.jsf


Per abilitare i comandi è necessario attivare la modalità developer, scrivendo il comando
dm <password>
dove la password è quella definita nel file di configurazione.
Una volta attivate la modaltà developer è possibile eseguire comandi.
La modalità developer attiva altre funzionalità, come
* spotlight avanzato
* tootlip
* evidenziazione stringhe non tradotte
* possibilità di passare alla vista debug

## La vista di debug
Web.UP mette a disposizione una vista di debug, che permette di ridisegnare la pagina aggiungendo informazioni utili a capire quello che si sta vedendo.
La vista debug si può attivare solo entrando in developer mode dal terminale e usando il checkbox che compare nella barra del titolo.

Nella vista di debug tutti i componenti vengono arricchiti con un pannello che descrive : 
- fun
- variabili
- xml
- dinamismi

Nel video che segue viene illustrato l'editor XML
[https://www.youtube.com/embed/NvNJKdUmlL8](https://www.youtube.com/embed/NvNJKdUmlL8)

# F.A.Q

## Come faccio ad eseguire un fun per usare l'xml?

* Entrare nel termilale
* Abilitare la modalità developer
* esegure il comando

**fun "F(xxx;yy;xxx)"**

con la fun compresa tra doppie virgolette

## Come analizzo i componenti della pagina?

a)
* Entrare nel termilale
* Abilitare la modalità developer
* esegure il comando

**comp**

e le sue varianti

b)
* Entrare nel treminale
* Abilitare la modalità developer
* Uscire dal terminale
* Abilitare il flag debug

## Come disattivo la modalità developer?

* Entrare nel termilale
* Abilitare la modalità developer
* esegure il comando
**dm**

## Come accedo ai log?

* Entrare nel termilale
* Cliccare sull'icona in alto a sinistra

## Come accedo alle informazioni di connessione?

* Entrare nel termilale
* Abilitare la modalità developer
* esegure il comando

**env**


## Come accedo alle variabili?


* Entrare nel termilale
* Abilitare la modalità developer
* esegure il comando

**var**

e le sue varianti
