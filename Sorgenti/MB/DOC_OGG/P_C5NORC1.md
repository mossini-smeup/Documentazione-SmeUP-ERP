Lanciando questa funzione i movimenti che presentano una corrispondenza perfetta (costituita :  da conto, data valuta, importo).

Tramite l'opzione F17 si ha la possibilità di impostare i seguenti aspetti : 
*Criterio abbinamento  :  campo blank confronta movimento per movimento di banca e contabilità la perfetta corrispondenza tra conto, importo e data (confronta in base all'impostazione della Data1 Scelta data); se invece si imposta Uno a molti allora va a raggruppare i movimenti di tesoreria (secondo i criteri impostati sotto la voce Tesoreria) e confrontarli con quelli contabili presi singolarmente e viceversa :  la finalità è di individuare ad esempio  un pagamento unico ricevuto dalla banca che si riferisce a tre diverse fatture registrate in contabilità.
*Livello esito, se visualizzare la sintesi o il dettaglio dei movimenti spuntati.
*Ripresa note, riprende anche la descrizione di quello che passa la banca (faccio VB nello spazio bianco di ogni singola spunta nella schermata generale delle riconciliazioni)
*Movimenti da generare :  in caso non trovi registrazioni contabili,1 NO non li genera ,Blank si li genera e li spunta, 2 li genera ma non li spunta; con generazione di movimenti si intende che impostando tramite gli elementi della C5U con codifica RBAN + Causale ABI è possibile generare dei movimenti automatici a partire dai soli movimenti remote.

 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]) I(**Registrazioni automatiche da Corporate >>)
 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]D) I(**Registrazioni automatiche da Corporate solo Dare >>)
 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]A) I(**Registrazioni automatiche da Corporate solo Avere >>)
