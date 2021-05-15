<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Tipo de Vag&atilde;o</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Verifica
if(isset($_POST['txtTipoVag'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtTipoVag)){
		$msg = $msg . "Tipo de Vag&atilde;o inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtDescricao)){
		$msg = $msg . "Descri&ccedil;&atilde;o inv&aacute;lida!<br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		//Converte as letras para maiúscula
		$tipo = strtoupper($txtTipoVag);
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblTipoVags WHERE TipoVag = '" . $tipo . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblTipoVags (TipoVag, Descricao) VALUES('" . $tipo . "','" . $txtDescricao . "');";
			//echo $sql;
			$ask = mysqlexecuta($id,$sql);
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
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="2" class="headertabela"><div align="center">Cadastrar Tipo de Vag&atilde;o</div></td>
      </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Tipo (2 Letras):</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtTipoVag" type="text" id="txtTipoVag" size="10" maxlength="2" />
      </span></td>
    </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Descri&ccedil;&atilde;o:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtDescricao" type="text" id="txtDescricao" size="10" maxlength="255" />
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
