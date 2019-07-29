## Esempio apertura membro
 :  : I.XML
<?xml version="1.0" encoding="UTF-8"?>
<Base Testo="WETEST_TE1 SHOWCASE Text Editor - ">
 <Service Titolo1="" Titolo2="" Funzione="F(TED;*EDTLET;LET) 1(MB;SCP_SCH;....)"
  Servizio="JATRE_29C" TSep="." DSep="," IdFun="1228110434145" NumSes="848336"/>
   <Header>
 <Livello Caratteristiche="A01"/>
 </Header>
   <Key>
     <K1 Tipo="MB" Parametro="SCP_SCH" Codice="WETEST_TE1" Testo="" Obb="3" Mod="1"/>
     <K2 Tipo="OJ" Parametro="*LIB" Codice="SMEDEV" Testo="Sviluppo WebUP 3" Obb=" " Mod="2"/>
   </Key>
   <Setup>
     <Program>
       <EDT Tipo="FIX" Lung="100" NoMod="1" Control="EDT_SCH"/>
     </Program>
   </Setup>
   <Contenuto>
   <![CDATA[
   <p>Testo normale</p>
   <p>
   <strong>Testo grassetto</strong>
   </p>
   <p>
   <em>Testo corsivo</em>
   </p>
   <p>
   <strong>
   <u>Testo sottolineato</u>
   </strong>
   </p>
   <p>TESTO MONOSPACE</p>
   <ul>
   <li>elenco puntato</li>
   <li>elenco puntato</li>
   <li>elenco puntato</li>
   </ul>
   <h1>Titolo 1</h1>
   <h2>Titolo 2</h2>
   <p>
   <strong style="background-color :  rgb(0, 71, 178);">BOLD BLUE</strong>
   </p>
   <p>
   <br>
   </p>
   <p>
   <br>
   </p>
   <p>
   <br>
   </p>
   <br>
   ]]>
   </Contenuto>
     <Messaggi>
       <Esito Stato="OK"/>
     </Messaggi>
   </Base>
 :  : I.XML.END
