<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Untitled Document</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<?
//Includes
include "includeslocalhost.php";

//Pega variaveis vinda do formulário via POST
foreach( $_POST as $campo => $vlr){
   $$campo = AntiInjection($vlr);
}

$digito = 0;
if ($txtNumero != "") {
	//Calculo do dígito verificador
	for ($i = 0; $i <= 5; $i++) {

		$x = substr($txtNumero, $i, 1);
		$num[$i] = (7 - $i) * $x;
		//$digito = $digito + $num;
		//echo $x;
		//echo $num;
	}
	$digito = $num[0] + $num[1] + $num[2] + $num[3] + $num[4] + $num[5];
	$verificado = 11 - ($digito % 11);
	
	if ($verificado==11) { $DV = 1; } 
	elseif ($verificado==10) { $DV = 0; }
	else { $DV = $verificado; }
	//$DV = substr($digito, -1)
}

?>
<body><table width="100%" height="480" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="digito.php">
  <table width="200" border="1" cellspacing="0" cellpadding="0">
    <tr>
      <th colspan="2" class="headertabela" scope="col"><div class="header" style="">C&aacute;lculo do D&iacute;gito Verificador</div></th>
      </tr>
    <tr>
      <th class="headertabela" scope="row">Numero: </th>
      <td bgcolor="#FFFFFF"><input name="txtNumero" type="text" id="txtNumero" value="<? echo $txtNumero; ?>" maxlength="6" /></td>
    </tr>
    <tr>
      <th class="headertabela" scope="row">D.V.:</th>
      <td bgcolor="#FFFFFF"><input name="txtVerificado2" type="text" id="txtVerificado2" value="<? echo $DV; ?>" size="1" maxlength="1" readonly="readonly" /></td>
    </tr>
    <tr>
      <th class="headertabela" scope="row">Verificado:</th>
      <td bgcolor="#FFFFFF"><input name="txtVerificado" type="text" id="txtVerificado" readonly="readonly" value="<? echo $txtNumero . "-" . $DV; ?>" maxlength="8" /></td>
    </tr>
    <tr>
      <th colspan="2" class="headertabela" scope="row"><input type="reset" name="Reset" id="reset" value="Limpar" />
          <input type="submit" name="submit" id="submit" value="Enviar" /></th>
      </tr>
  </table>
  </form></td></tr></table>
</body>
</html>
