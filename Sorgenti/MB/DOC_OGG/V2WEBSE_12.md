 :  : HEA PRIV(001)

# MeteoOpenSmeupWS

Webservice installato su gilberto, una macchina della rete Smea.

Ha un metodo che riceve in ingresso una stringa (un indirizzo) e restituisce XML.

La stringa di input deve corrispondere ad un indirizzo.
In output vengono fornito l'xml con le informazioni relative a tale indirizzo :  se esiste, Stato, Regione, Provincia, Località, CAP, varie longitudini e latitudini.

Es. : 

INPUT : 

via Iseo 43, Erbusco

OUTPUT : 


<GeocodeResponse>
 <status>OK</status>
 <result>
  <type>route</type>
  <formatted_address>Via Walter Tobagi, 25035 Ospitaletto Brescia, Italy</formatted_address>
  <address_component>
   <long_name>Via Walter Tobagi</long_name>
   <short_name>Via Walter Tobagi</short_name>
   <type>route</type>
  </address_component>
  <address_component>
   <long_name>Ospitaletto</long_name>
   <short_name>Ospitaletto</short_name>
   <type>locality</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Brescia</long_name>
   <short_name>BS</short_name>
   <type>administrative_area_level_2</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Lombardia</long_name>
   <short_name>Lombardia</short_name>
   <type>administrative_area_level_1</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Italy</long_name>
   <short_name>IT</short_name>
   <type>country</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>25035</long_name>
   <short_name>25035</short_name>
   <type>postal_code</type>
  </address_component>
  <geometry>
   <location>
    <lat>45.5553037</lat>
    <lng>10.0844684</lng>
   </location>
   <location_type>GEOMETRIC_CENTER</location_type>
   <viewport>
    <southwest>
     <lat>45.5521448</lat>
     <lng>10.0811515</lng>
    </southwest>
    <northeast>
     <lat>45.5584400</lat>
     <lng>10.0874467</lng>
    </northeast>
   </viewport>
   <bounds>
    <southwest>
     <lat>45.5546831</lat>
     <lng>10.0831665</lng>
    </southwest>
    <northeast>
     <lat>45.5559017</lat>
     <lng>10.0854317</lng>
    </northeast>
   </bounds>
  </geometry>
 </result>
</GeocodeResponse>

E' testabile all'indirizzo : 
 :  : DEC T(J1) P(PATHFILE) [http://maps.googleapis.com/maps/api/geocode/xml?address=43+Iseo+Via,+Erbusco,+Italy&sensor=true+
](http://maps.googleapis.com/maps/api/geocode/xml?address=43+Iseo+Via,+Erbusco,+Italy&sensor=true+
)
) I(pagina di test)
