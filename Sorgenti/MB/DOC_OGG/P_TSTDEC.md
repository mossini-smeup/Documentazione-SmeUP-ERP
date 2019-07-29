# OBIETTIVO

Tramite questo programma è possibile ottenere la decodifica ed il controllo di consistenza di qualsiasi oggetto di smeup.

# PARAMETRI DI INPUT

* £DECCD :  Codice Oggetto
* £DECTP :  Tipo Oggetto
* £DECPA :  Parametro Oggetto
* £DECAM :  Ambiente - Determina un particolare codice/programma di riferimento che può poi essere utilizzato dalle interfacce dei vari oggetti
* £DECCO :  Contesto - Determina la modalità di utilizzo della decodifica (se utilizzato normalmente contiene i valori da 11 a 15 per indicare le modalità di gestione in cui la decodifica viene utilizzata).
* £DECDT :  Data di Riferimento - Se passata viene utilizzata nel caso in cui l'oggetto abbia una definizione che cambia nel tempo (es. Anagrafica Enti).
* £DECR1 :  Intestazione - Valorizzato ad S comporta il riempimento del campo di output £DECIN con la decodifica della classe dell'oggetto, mentre con il valore I lo stesso campo viene riempito con la /COPY o il pgm che viene utilizzato come interfaccia dell'oggetto
* £DECR2 :  Aggiornare le tabelle
* £DECR3 :  Livello di richiamo - Definisce quale copia richiamare del programma B£DEC0
* £DECR4 :  Presenta Funzioni - Se valorizzato non viene eseguita la decodifica ma viene aperta la finestra delle funzioni dell'oggetto.

