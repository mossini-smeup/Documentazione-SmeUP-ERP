# Documentazione PHCOM componenti industriali per l'industria

## Indice

 * **Introduzione**
 * **Obiettivo finale**
 * **Digrammi dei componenti**
 * **Diagramma dello schema di una possibile soluzione aziendale**
 * **Alcune soluzioni**
 ** **TTS**
 ** **OPC RSLINX**
 * **Dizionario termini**
 * **Problemi**
 * **TODO**

## Introduzione
In questa documentazione cerchiamo di realizzare un modello che permetta di descrivere l'interazione con componenti industriali quali plc, sensori ... nel modo più generico e più neutro rispetto alle soluzioni tecniche che verranno poi realizzate sul campo.
Nelle prime fasi di progettazione si cercherà di realizzare alcuni schemi che rappresentino le **caratteristiche dei componenti**, alcune possibili **configurazioni**  di alcunii componenti all'interno di una possibile fabbrica e la creazione di **schede/programmi di test** che permettano di testare a livello logico le funzionalità dei componenti.

## Obiettivo finale
Realizzare uno schema in cui sia possibile descrivere a livello logico le funzionalità e le disposizioni di componenti quali plc,bilancie,sensori all'interno di una fabbrica con uno o più stabilimenti.

## Dizionario termini
 * **OPC (OLE for Process Control)** :  Gruppo di periferice definite alla OPC Foundation che definiscono uno standard di comunicazione tra un sorgente e una generica applicazione software. OPC è stato progettato per l'accesso a dati da server connessi in rete e le interfacce OPC possono essere usate all'interno di un'applicazione.
 * **JPC (Java for Process Control)**  :  Interfaccia Java per accedere ad un server OPC
