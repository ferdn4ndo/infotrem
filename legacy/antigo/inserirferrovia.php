<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Ferrovia</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if(isset($_POST['txtNome'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtNome)){
		echo "Nome inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblFerrovias WHERE Nome = '" . $txtNome . "';";
		
		if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblFerrovias (Nome, Detalhes) VALUES('" . $txtNome . "','" . $txtDetalhes ."');";
			
			$ask = mysqlexecuta($id,$sql);
			If ($ask!=0){
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
  <table width="454" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" class="headertabela"><div align="center" class="header">Cadastrar Ferrovia</div></td>
      </tr>
    <tr>
      <td width="136" class="headertabela"><div align="right">Nome:</div></td>
      <td width="318" bgcolor="#FFFFFF"><input name="txtNome" type="text" id="txtNome" size="53" maxlength="50" /></td>
    </tr>
    <tr>
      <td valign="top" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="39" rows="5" id="txtDetalhes"></textarea></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td>
</tr></table>
</body>
</html>
