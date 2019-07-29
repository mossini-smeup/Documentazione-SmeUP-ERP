## Creazione dello smartkit
Attraverso un script che viene elaborato da
[https://www.packer.io/intro](https://www.packer.io/intro)
viene prodotta un'immagine di macchina virtuale per diverse piattaforme (Virtualbox, VMWare, Hyper-V), con a bordo il necessario per deployare tutto il software richiesto dall'applicazione che si vuole attivare.
La base di questa macchina virtuale è un sistema operativo, costituito da una distribuzione linux
[https://www.centos.org/](https://www.centos.org/)
La seconda parte del processo, l'installazione del software, avviene attraverso un altro tool di deploy chiamato
[https://www.terraform.io/intro/index.html](https://www.terraform.io/intro/index.html)
grazie ad uno script elaborato da questo prodotto, viene in primo luogo configurato il sistema, compreso networking, archivi. In secondo luogo viene installata l'applicazione desiderta sotto forma di container Docker.
Il fatto di avere a disposizione il _codice sorgente_ che da origine allo smarkit, permette di poter ricreare istanze identiche su diverse piattaforme.
Terraform mette a disposizione anche un processo di simulazione che rende visibili le modifiche prima di produrle effettivamente.
La parte di deploy delle applicazioni vere e proprie avviene attraverso
[https://www.docker.com/resources/what-container](https://www.docker.com/resources/what-container)
L'utilizzo di Docker permette di containerizzare le applicazioni, quindi di deployare contenitori applicativi dedicati alle specifiche funzionalità :  container di provider, gateway, webup.
L'utilizzo di questi contenitori applicativi _standardizzati_ permette di controllarli, coordinatli e gestirli con grande precisione ed efficenza.
[https://www.saltstack.com/](https://www.saltstack.com/)
Saltstack è un'inftrastruttura di gestione, configurazione e monitoraggio remoto. La sua adozione permetterà di avere il controllo tecnologico ed applicativo degli smartkit e di ciò che vi è installato.
