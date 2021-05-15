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

if(isset($_POST['txtPrefixo'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($cmbFerrovia)){
		$msg = $msg . "Ferrovia inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtPrefixo)){
		$msg = $msg . "Prefixo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbOrigem)){
		$msg = $msg . "Origem inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbDestino)){
		$msg = $msg . "Destino inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblPrefixos WHERE CodFerrocia = " . $cmbFerrovia . " AND Prefixo = '" . $txtPrefixo . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo "<title>ERRO</title></head><body>";
			echo "<strong>J&aacute; existe um registro id&ecirc;ntico no sistema!</strong>";
			exit;
		} else {
			$sql = "INSERT INTO tblPrefixos (CodFerrovia, Prefixo, Origem, Destino, Detalhes) VALUES(" . $cmbFerrovia . ",'" . $txtPrefixo . "'," . $cmbOrigem ."," . $cmbDestino . ",'" . $txtDetalhes . "');";
			
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
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Prefixo</div>
        <div align="left"></div></td>
  </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Ferrovia:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbFerrovia" id="cmbFerrovia">
          <option disabled="disabled" selected="selected">SELECIONE</option>
        <?
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				echo ">" . $row['Nome'] . "</option>";
			 }
	 ?>
      </select>
      </div></td>
    </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Prefixo:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtPrefixo" type="text" id="txtPrefixo" size="50" maxlength="255" />
      </span></div></td>
  </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Origem:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbOrigem" id="cmbOrigem">
          <?
			$sql = "SELECT CodLocal, Sigla, Nome FROM tblLocais ORDER BY Sigla;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodLocal'];
				echo ">" . $row['Sigla'] . " - " . $row['Nome'] . "</option>";
			 }
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Destino:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbDestino" id="cmbDestino">
          <?
			$sql = "SELECT CodLocal, Sigla, Nome FROM tblLocais ORDER BY Sigla;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodLocal'];
				echo ">" . $row['Sigla'] . " - " . $row['Nome'] . "</option>";
			 }
	 ?>
        </select>
      </div></td>
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
