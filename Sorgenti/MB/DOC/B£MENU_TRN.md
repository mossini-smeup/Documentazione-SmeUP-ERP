 :  : PRO Cod(BAS) Txt(Test Autorizzazioni) STAT(00) RESP(ARRSTE)
 :  : ATT Cod(APP) Txt(Per Applicazione)
01. Entrare nel menù di ingresso da loocup
02. Prendere una voce che richiama un sottosettore corrispondente ad un'applicazione e aggiungere ai preferiti
03. Entrare nel menù dell'applicazione ed aggiungere la voce di richiamo di un modulo ai preferiti
04. Entrare nel menù del modulo ed aggiungere una voce di emulazione ai preferiti
05. Cercare un fly di oggetto che vada su un modulo della medesima applicazione e aggiungerlo ai preferiti
06. Disattivare l'applicazione attraverso la classe OGG.MAS
07. Verificare che da menù di ingresso loocup sia scomparso il richiamo dell'applicazione
08. Verificare che dai preferiti siano scomparse tutte le voci aggiunte nei punti precedenti
09. Verificare che da menù 5250 sia scomparso il richiamo dell'applicazione

 :  : ATT Cod(VOC) Txt(Per Voce)
01. Prendere una qualsiasi voce di emulazione del menù di ingresso loocup e aggiungerla ai preferiti
02. Disattivare la voce attraverso la classe MNU
03. Verificare che la voce non sia più visibile nel menù di ingresso loocup
04. Verificare che la voce non sia più visibile nel menù di ingresso 5250
05. Verificare che la voce non sia più visibile nei preferiti

 :  : ATT Cod(OGG) Txt(Per Oggetto)
01. Entrare nel menù di un articolo (o in alternativa di un ente o una tabella).
02. Aggiungere ai preferiti una qualsiasi voce del menù
03. Entrare in un altro articolo ed aggiungere ai preferiti la stessa voce
04. Disattivare la classe AR (o quella utilizzata in alternativa) sulla classe OGG.MAS
05. Verificare che le voci aggiunte in precedenza ai preferiti siano scomparse
06. Verificare che le schede di entrambi gli articoli risultino non autorizzate
07. Riattivare la classe AR e disattivare solo il primo articolo
08. Verificare che delle voci aggiunte in precedenza sia scomparsa solo la voce del primo articolo
09. Verificare che la scheda del secondo articolo sia autorizzata

