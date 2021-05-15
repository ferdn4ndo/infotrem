<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Categoria de Mat. Rodante</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if(isset($_POST['txtCategoria'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	
	//Checa se não foram encontrados erros
	if($erro == 0){
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblCategoriaRodante WHERE Categoria = '" . $txtCategoria . "';";
		if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
			echo "<center><strong>J&aacute; existe uma categoria id&ecirc;ntica cadastrada no sistema!</strong></center>";
		} else {
			//Faz o cadastro
			$sql = "INSERT INTO tblCategoriaRodante (Categoria) VALUES('" . $txtCategoria . "');";
			$ask = mysqlexecuta($id,$sql);
			if ($ask!=0){
				echo "<p><center>";
				echo "<strong>Cadastro concluído com sucesso!</strong>";
				echo "<p><a href='index.php'> Clique Aqui para retornar &agrave; p&aacute;gina inicial!</a></p></center>";
			}
			else {
				echo "<p><br><strong>Erro ao interpretar dados!</strong><br></p>";
				exit;
			}
		}
	} else {
		echo "<p>ERRO: <strong>";
		echo $msg;
		echo "</strong></p>";
	}
}
?>
<body><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="2" class="headertabela"><div align="center">Cadastrar Categoria de Mat. Rodante</div></td>
      </tr>
    <tr>
    
      <td width="119"  class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF">
        <input name="txtCategoria" type="text" id="txtCategoria" size="30" maxlength="50" />
      </td>
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
