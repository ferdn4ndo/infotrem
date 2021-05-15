<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Inserir Link</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if(isset($_POST['txtNome'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNome)){
		$msg = $msg . "Nome inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtLink)){
		$msg = $msg . "Link inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblLinks WHERE Link = " . $txtLink . " AND Nome = '" . $txtNome . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo "<title>ERRO</title></head><body>";
			echo "<strong>J&aacute; existe um registro id&ecirc;ntico no sistema!</strong>";
			exit;
		} else {
			$sql = "INSERT INTO tblLinks (Categoria, Nome, Link, Detalhes) VALUES(" . $cmbCategoria . ",'" . $txtNome . "','" . $txtLink . "','" . $txtDetalhes . "');";
			
			//echo $sql;
			
			$ask = mysql_query($sql);
			if ($ask!=0){
				$Exibe = $Mensagem['sucesso'];
			}
			else {
				$Exibe = $Mensagem['erro'];
			}
		}
	} else {
		$Exibe = $Mensagem['erromsg1'] . $msg . $Mensagem['erromsg2'];
	}
}
?>
<body>
<? echo $Exibe; ?>
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="100%" border="0" cellspacing="1" cellpadding="1" align="center"><tr><td align="center"><table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Link</div>
        <div align="left"></div></td>
  </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Nome:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNome" type="text" id="txtNome" size="50" maxlength="255" />
      </span></div></td>
  </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria">
          <option disabled="disabled" selected="selected">SELECIONE</option>
          <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaLink ORDER BY Categoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				echo ">" . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Link:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtLink" type="text" id="txtLink" size="50" maxlength="255" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea>
      </div></td>
    </tr>

    
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
    </tr>
  </table></td>
    </tr>
</table>
  </div>
</form>
</body>
</html>
