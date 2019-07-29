 :  : HEA PRIV(001)

# MeteoOpenSmeupWS

Webservice installato su gilberto, una macchina della rete Smea.

Ha un metodo che riceve in ingresso una stringa (un indirizzo) e restituisce XML.

La stringa di input deve corrispondere a una località.
In output vengono fornite le previsioni del tempo della stessa località per i prossimi quattro giorni e le condizioni di oggi.

Es. : 

INPUT : 

Milano

OUTPUT : 

<?xml version="1.0"?>
<xml_api_reply version="1">
 <weather module_id="0" tab_id="0" mobile_row="0" mobile_zipped="1"
  row="0" section="0">
  <forecast_information>
   <city data="Milan, Lombardy" />
   <postal_code data="Milano" />
   <latitude_e6 data="" />
   <longitude_e6 data="" />
   <forecast_date data="2011-02-10" />
   <current_date_time data="2011-02-10 16 : 20 : 00 +0000" />
   <unit_system data="US" />
  </forecast_information>
  <current_conditions>
   <condition data="Rain" />
   <temp_f data="50" />
   <temp_c data="10" />
   <humidity data="Humidity :  66%" />
   <icon data="/ig/images/weather/rain.gif" />
   <wind_condition data="Wind :  S at 5 mph" />
  </current_conditions>
  <forecast_conditions>
   <day_of_week data="Thu" />
   <low data="30" />
   <high data="55" />
   <icon data="/ig/images/weather/sunny.gif" />
   <condition data="Clear" />
  </forecast_conditions>
  <forecast_conditions>
   <day_of_week data="Fri" />
   <low data="35" />
   <high data="55" />
   <icon data="/ig/images/weather/mostly_sunny.gif" />
   <condition data="Partly Sunny" />
  </forecast_conditions>
  <forecast_conditions>
   <day_of_week data="Sat" />
   <low data="39" />
   <high data="53" />
   <icon data="/ig/images/weather/chance_of_rain.gif" />
   <condition data="Chance of Rain" />
  </forecast_conditions>
  <forecast_conditions>
   <day_of_week data="Sun" />
   <low data="39" />
   <high data="57" />
   <icon data="/ig/images/weather/chance_of_rain.gif" />
   <condition data="Chance of Rain" />
  </forecast_conditions>
 </weather>
</xml_api_reply>


E' testabile all'indirizzo : 
 :  : DEC T(J1) P(PATHFILE) K( http://gilberto.smea.it:8080/MeteoOpenSmeupWS/MeteoOpenSmeupService?Tester) I(pagina di test)

**Va posta attenzione alla porta :  il WS utilizza la 8080**


Application Name : MeteoOpenSmeupWS
Tester : /MeteoOpenSmeupWS/MeteoSmeupService?Tester
WSDL : /MeteoOpenSmeupWS/MeteoSmeupService?WSDL
Endpoint Name : MeteoOpenSmeup
Service Name:http://ws.smeup.it/
Port Name : MeteoSmeupPort
Deployment Type : 109
Implementation Type : SERVLET
Implementation Class : it.smeup.ws.MeteoOpenSmeup
Endpoint Address URI : /MeteoOpenSmeupWS/MeteoSmeupService
Namespace : it.smeup.ws.MeteoOpenSmeup
