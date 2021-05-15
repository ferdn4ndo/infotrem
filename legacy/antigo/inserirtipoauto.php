<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Tipo de Auto de Linha</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if(isset($_POST['txtTipo'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtTipo)){
		$msg = $msg . "Tipo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtDescricao)){
		$msg = $msg . "Descri&ccedil;&atilde;o inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	
	//Converte para maiúscula
	$tipo = strtoupper($txtTipo);
	
	//Checa se não foram encontrados erros
	if($erro == 0){
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblTipoAuto WHERE TipoAuto = '" . $tipo . "';";
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			//Faz o cadastro
			$sql1 = "INSERT INTO tblTipoAuto (TipoAuto, Descricao) VALUES('" . $tipo . "','" . $txtDescricao . "');";
			$ask1 = mysql_query($sql1);

			if ($ask1!=0){
				//Faz o cadastro do modelo
				$sqlcod = "SELECT * FROM tblTipoAuto WHERE TipoAuto = '" . $tipo . "';";
				$rescod = mysql_query($sqlcod);
				while ($rowcod = mysql_fetch_array($rescod)) {
					$Codigo = $rowcod['CodTipoAuto'];
				}
				$sqlins = "INSERT INTO tblModelos (Categoria, CodTipoVag, CodPesoVag, CodTipoCarro, CodMatCarro, CodTipoAuto, CodModLoco) VALUES (4,0,0,0,0," . $Codigo . ",0);";
				$askins = mysql_query($sqlins);
				if ($askins!=0){
					echo $Mensagem['sucesso'];
				} else {
					echo $Mensagem['erro'];
				}
			}
		}
	} else {
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
}
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="2" class="headertabela"><div align="center">Cadastrar Tipo de Auto de Linha</div></td>
      </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Tipo:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtTipo" type="text" id="txtTipo" size="30" maxlength="3" />
      </span></td>
    </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Descri&ccedil;&atilde;o:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtDescricao" type="text" id="txtDescricao" size="30" maxlength="255" />
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
