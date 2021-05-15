<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Material de Carro</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head><body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Verifica se é para cadastrar
if(isset($_POST['txtLetra'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtLetra)){
		$msg = $msg . "Letra inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtTipo)){
		$msg = $msg . "Material n&atilde;o preenchido!<br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		//Converte a letra para maiúscula
		$letra = strtoupper($txtLetra);
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblMatCarro WHERE LetraMatCarro = '" . $letra . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblMatCarro (LetraMatCarro, MatCarro) VALUES('" . $letra . "','" . $txtTipo . "');";
			
			$ask = mysql_query($sql);
			if ($ask!=0){
				echo $Mensagem['sucesso'];
			}
			else {
				echo $Mensagem['erro'];
			}
		}
	} else {
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
}
?>
<table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="2" class="headertabela"><div align="center">Cadastrar Material de Carro</div></td>
      </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Letra:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtLetra" type="text" id="txtLetra" size="10" maxlength="1" />
      </span></td>
    </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Material:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtTipo" type="text" id="txtTipo" size="50" maxlength="255" />
      </span></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
