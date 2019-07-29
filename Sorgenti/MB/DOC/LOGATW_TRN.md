 :  : PRO Cod(A01) Txt(Installazione Sme.UP Gateway) STAT(10) RESP(GIAGIU)

 :  : ATT Cod(001) Txt(Installazione su singolo server) STAT(10) RESP(GIAGIU)
01. Verificare i prerequisiti
- Java Virtual Machine in versione 1.8 o superiore
- Payara Web Server in versione 5.183 o superiore
- Apache Maven, versione 3.5 o superiore
- RabbitMQ, versione 3.5 o superiore

02. Configurare correttamente Payara
- Configurazione della JVM
- Configurazione del numero massimo di thread http attivabili
- Configurazione del numero massimo di thread attivabili

03. Download file .zip smeup-gateway-<versione>.zip
Il file contiene una serie di file in formato war che contengono le applicazioni web che compongono il framework (http://www.smeup.com)

04. Deploy applicazioni sul server Payara
E' consigliabile (ma non necessario) seguire un ordine prefissato nell'installazione delle applicazioni.
Inoltre è consigliabile definire in fase di deploy un "deployment order" che garantisca che le web application vengano avviate con un ordine specifico
Questi i micorservices : 

- gtw-hub.war
- gtw-logger
- gtw-resource-manager
- gtw-config-manager.war
- gtw-a37-dispatcher.war
- gtw-as400-adapter.war
- gtw-smeup-adapter.war
- gtw-as400-listener.war
- gtw-deployer.war
- gtw-smeup-ws.war

 :  : ATT Cod(002) Txt(Installazione docker) STAT(10) RESP(GIAGIU)
01. Verificare i prerequisiti
- Un sistema operativo GNU Linux server a 64 bit
- Docker CE (community edition) ver 18.06.0 o superiore
- Docker compose ver. 1.22 o superiore

02. Download software necessario da http://www.smeup.com come file zip
03. Unzip e copia della cartella smeup-gateway-docker sul sistema di destinazione
04. Configurazione dei servizi e avvio del sistema
- Controllare che tutte le cartelle contenute in docker-deploy siano accessibili in lettura/scrittura dagli utenti del gruppo docker
- Configurazione porte socket Docker
- Configurazione poerte Payara & RabbitMQ nel file file docker-compose.override.yml
- Da riga comandi linux lanciare il comenda build.sh
- Successivamente il comando up.sh da eseguire solo la prima volta.
- Avvi successivi al primo con comando start.sh
- Per lo spegnimento normale utilizzare il comando stop.sh
- Se è necessario fermare la macchina per aggiornaento framework, utilizzare il comando down.sh e successivamente up.sh

 :  : PRO Cod(A02) Txt(Post installazione Sme.UP Gateway) STAT(10) RESP(GIAGIU)
 :  : ATT Cod(001) Txt(Configurazione via HTTP) STAT(10) RESP(GIAGIU)
01. Aprire un browser e digitare "http://localhost:8080/gtw-hub/api/services/configMicroservices
Verrà presentata una lista di microservices da configurare, cliccare su ognuno e completare le informazioni

 :  : PRO Cod(A03) Txt(Verifica stato Sme.UP Gateway) STAT(10) RESP(GIAGIU)
 :  : ATT Cod(001) Txt(Utilizzando la UPP) STAT(10) RESP(GIAGIU)
01. Utilizzare la UPP LO_080 da modulo LOGATW
- Nel cruscotto del modulo LOGATW è presente la lista dei Gateway registrati sul sistema.
- Cliccando sul Gateway interessato si aprirà la UPP

02. Utilizzare la UPP LO_080
- Digitare nella spotlight il comanfo SU LO_080
- Scegliere lo Sme.UP Gateway sul quale si vuole lavorare

 :  : ATT Cod(002) Txt(Utilizzando l'HTTP) STAT(10) RESP(GIAGIU)
01. Aprire un browser e digitare "http://localhost:8080/gtw-hub/api/services/debug
Verrà presentata una pagina con le informazioni di base del gateway con la lista dei microservices attivi
