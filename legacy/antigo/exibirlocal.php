<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Exibir Local</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$CodLocal = AntiInjection($_GET["Cod"]);

//Pega a categoria
$sql = "SELECT tblLocais.*, tblCategoriaLocal.Categoria AS NomeCategoria, tblBitolas.Bitola AS NomeBitola, tblEstadoLocal.Estado AS NomeEstado FROM tblLocais INNER JOIN tblCategoriaLocal ON tblLocais.Categoria = tblCategoriaLocal.CodCategoria  INNER JOIN tblBitolas ON tblLocais.Bitola = tblBitolas.CodBitola INNER JOIN tblEstadoLocal ON tblLocais.Estado = tblEstadoLocal.CodEstado WHERE tblLocais.CodLocal = " . $CodLocal . ";";

//Executa o comando
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	//Prepara os dados
	$Nome = $row['Nome'];
	$Sigla = $row['Sigla'];
	$Categoria = $row['NomeCategoria'];
	$Bitola = $row['NomeBitola'];
	$Estado = $row['NomeEstado'];
	$CodFerroviaOrgiem = $row['FerroviaOrigem'];
	$CodFerroviaAtual = $row['FerroviaAtual'];
		//TODO: $UltimaFoto
	$Detalhes = $row['Detalhes'];
	$Latitude = $row['Latitude'];
	$Longitude = $row['Longitude'];
}

//Prepara os demais dados

//Ferrovia de Origem (se disponivel)
if(($CodFerroviaOrigem!="")&&($CodFerroviaOrigem!=0)){
	$consultaorigem = "SELECT Nome FROM tblFerrovias WHERE CodFerrovia = ". $CodFerroviaOrigem . ";";
	$executaorigem = mysql_query($consultaorigem);
	while ($linhaorigem = mysql_fetch_array($executaorigem)) {
		$FerroviaOrigem = $linhaorigem['Nome'];
	}
} else {
	$FerroviaOrigem = "Desconhecido";
}

//Ferrovia Atual (se disponivel)
if(($CodFerroviaAtual!="")&&($CodFerroviaAtual!=0)){
	$consultaatual = "SELECT Nome FROM tblFerrovias WHERE CodFerrovia = ". $CodFerroviaAtual . ";";
	$executaatual = mysql_query($consultaatual);
	while ($linhaatual = mysql_fetch_array($executaatual)) {
		$FerroviaAtual = $linhaatual['Nome'];
	}
} else {
	$FerroviaAtual = "Desconhecido";
}

//Longitude
if(($Longitude!="")&&($Longitude!=0)) {
	if(strlen($Longitude)>10) {
		//$NumLongitude = str_replace(".",",",substr($Longitude,0,10));
		$NumLongitude = str_replace("0","",substr($Longitude,0,4)) . substr($Longitude,4,7);
	} else {
		$NumLongitude = $Longitude;
	}
} else {
	$NumLongitude = 0;
}

//Latitude
if(($Latitude!="")&&($Latitude!=0)) {
	if(strlen($Latitude)>10) {
		$NumLatitude = str_replace("0","",substr($Latitude,0,4)) . substr($Latitude,4,7);
	} else {
		$NumLatitude = $Latitude;
	}
} else {
	$NumLatitude = 0;
}

if(($NumLatitude!=0)&&($NumLongitude!=0)) {
?>
<style type="text/css">
  html { height: 100% }
  body { height: 100%; margin: 0px; padding: 0px }
  #map_canvas { height: 300px }
</style>
<script type="text/javascript"
    src="https://maps.google.com/maps/api/js?libraries=panoramio&sensor=false">
</script>
<script type="text/javascript">
  function initialize() {
    var latlng = new google.maps.LatLng(<? echo $NumLatitude; ?>, <? echo $NumLongitude; ?>);
    var myOptions = {
      zoom: 15,
      center: latlng,
	  //HYBRID = Híbrido, ROADMAP = Mapa, SATELLITE = Satelite, TERRAIN = Relevos
      mapTypeId: google.maps.MapTypeId.SATELLITE
    }
    var map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
	
//Adicionando um marcador
	var marker = new google.maps.Marker({
      		position: latlng,
		map: map,
      		title:"<? echo $Nome; ?>"
  	});

//Caso queria adicionar a camada do panoramio
//var panoramioLayer = new google.maps.panoramio.PanoramioLayer();
//panoramioLayer.setMap(map);
  
//Caso queria adicionar dados de um KML
//var ctaLayer = new google.maps.KmlLayer('http://gmaps-samples.googlecode.com/svn/trunk/ggeoxml/cta.kml');
//ctaLayer.setMap(map);


  // To add the marker to the map, call setMap();
  //marker.setMap(map);  
  }

</script>
<?
}
?>
</head>
<body onLoad="initialize()"><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Exibir Local</div></td>
      </tr>
    <tr>
    <td width="149" class="headertabela"><div align="right">C&oacute;digo:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $CodLocal; ?></td>
    </tr>
  	<tr>
    <td width="149" class="headertabela"><div align="right">Nome:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Nome; ?></td>
    </tr>
    <tr>
    <td width="149" class="headertabela"><div align="right">Sigla:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Sigla; ?></td>
    </tr>
    <tr>
    <td width="149" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Categoria; ?></td>
    </tr>
    <tr>
    <td width="149" class="headertabela"><div align="right">Bitola:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Bitola; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Estado:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Estado; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Ferrovia de Origem:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $FerroviaOrigem; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Ferrovia Atual:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $FerroviaAtual; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Detalhes; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Mapa:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? if(($NumLatitude!=0)&&($NumLongitude!=0)) { ?><!-- <iframe src="mapa.php?Lat=<? echo $NumLatitude; ?>&Lon=<? echo $NumLongitude; ?>&Nome=<? echo $Nome.' ('.$Sigla.')'; ?>" height="345" width="345" frameborder="0" scrolling="no"></iframe> --><div id="map_canvas" style="width:345; height:300"></div><? } else { ?>Indispon&iacute;vel<? } ?></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
  </div>
</td></tr></table>
</body>
</html>
