<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Modelo</title>
<script type="text/javascript">
  function mudancaSelecao(elemento){
    var selecionada = elemento.options[elemento.options.selectedIndex];
	document.location=('inserirmodelo.php?Categoria=' + selecionada.value);
  }
</script>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head><body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega o valor da URL
$id = $_GET["Categoria"];

//Verifica se é para cadastrar
if(isset($_POST['cmbCategoria'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if($cmbCategoria==1){
		if(empty($txtModelo)){
			$msg = $msg . "Modelo inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
		if(empty($cmbFabricante)){
			$msg = $msg . "Fabricante inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
		if(empty($cmbTracao)){
			$msg = $msg . "Tra&ccedil;&atilde; inv&aacute;lida! <br>";
			$erro = $erro + 1;
		}
	} elseif ($cmbCategoria==2){
		if(empty($cmbTipoVag)){
			$msg = $msg . "Tipo inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
		if(empty($cmbPesoVag)){
			$msg = $msg . "Peso inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
	} elseif ($cmbCategoria==3){ //Carros de passageiro
		if(empty($cmbTipoCarro)){
			$msg = $msg . "Tipo de carro inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
		if(empty($cmbMatCarro)){
			$msg = $msg . "Material do carro inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
	} elseif ($cmbCategoria==4){ //Autos de linha / Serviço
		if(empty($txtModelo)){
			$msg = $msg . "Modelo inv&aacute;lido! <br>";
			$erro = $erro + 1;
		}
	} elseif ($cmbCategoria==5){ //Outros
	}
	if($erro == 0){
		
		//Fixa as variáveis nulas
		if ($cmbFabricante=="") { $cmbFabricante = 0; }
		if ($cmbTracao=="") { $cmbTracao = 0; }
		if ($cmbTipoVag=="") { $cmbTipoVag = 0; }
		if ($cmbPesoVag=="") { $cmbPesoVag = 0; }
		if ($cmbTipoCarro=="") { $cmbTipoCarro = 0; }
		if ($cmbMatCarro=="") { $cmbMatCarro = 0; }
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblModelos WHERE Modelo = '" . $txtModelo . "' AND Categoria = " . $cmbCategoria . " AND Fabricante = " . $cmbFabricante . " AND CodTipoVag = " . $cmbTipoVag . " AND CodPesoVag = " . $cmbPesoVag . " AND CodTipoCarro = " . $cmbTipoCarro . " AND CodMatCarro = " . $cmbMatCarro . ";";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblModelos (Categoria, Modelo, Tracao, CodPesoVag, CodTipoVag, Fabricante, CodTipoCarro, CodMatCarro, Detalhes) VALUES(" . $cmbCategoria . ",'" . $txtModelo . "'," . $cmbTracao . "," . $cmbPesoVag . "," . $cmbTipoVag . "," . $cmbFabricante . "," . $cmbTipoCarro ."," . $cmbMatCarro . ",'" . $txtDetalhes ."');";
			
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
      <td colspan="2" class="headertabela"><div align="center">Cadastrar Modelo</div></td>
      </tr>
  <tr>
      <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($id == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        				
        <option value="1"<? if ($id == "1") { echo " selected='selected' "; } ?>>1 - Locomotivas</option>
        <option value="2"<? if ($id == "2") { echo " selected='selected' "; } ?>>2 - Vag&otilde;es</option>
        <option value="3"<? if ($id == "3") { echo " selected='selected' "; } ?>>3 - Carros de Passageiro</option>
        <option value="4"<? if ($id == "4") { echo " selected='selected' "; } ?>>4 - Autos de linha</option>
        <option value="5"<? if ($id == "5") { echo " selected='selected' "; } ?>>5 - Outros</option>
        </select></td></tr><? if ($id == "1") { ?>
    <tr>
      <td width="119" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="196" bgcolor="#FFFFFF"><input name="txtModelo" type="text" id="txtModelo" size="30" maxlength="8" /></td>
    </tr>
    <tr>
      <td width="119" class="headertabela"><div align="right">Fabricante:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbFabricante" id="cmbFabricante">
        <?
	   
			$sql = "SELECT CodFabricante, NomeFabricante FROM tblFabricantes ORDER BY NomeFabricante;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFabricante'];
				echo ">" . $row['NomeFabricante'] . "</option>";
			 }
	 ?>
            </select></td>
    </tr>
    <tr>
      <td width="119" class="headertabela"><div align="right">Tra&ccedil;&atilde;o:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbTracao" id="cmbTracao">
        <?
	   
			$sql = "SELECT CodTracao, Tracao FROM tblTracao ORDER BY Tracao;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodTracao'];
				echo ">" . $row['Tracao'] . "</option>";
			 }
	 ?>
            </select></td>
    </tr>
    <? } elseif ($id == "2") { ?>
    <tr>
      <td width="119" class="headertabela"><div align="right">Tipo do Vag&atilde;o:</div></td>
      <td width="196" bgcolor="#FFFFFF"><label>
        <select name="cmbTipoVag" id="cmbTipoVag">
       <?
	   
			$sql = "SELECT CodTipoVag, TipoVag, Descricao FROM tblTipoVags ORDER BY TipoVag;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodTipoVag'];
				echo ">" . $row['TipoVag'] . " - " . $row['Descricao'] . "</option>";
			 }
	 ?>
        </select>
      </label></td>
    </tr>
    <tr>
      <td width="119" class="headertabela"><div align="right">Peso Total Max:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbPesoVag" id="cmbPesoVag">
        <?
	   
			$sql = "SELECT CodPesoVag, PesoVag, LetraPesoVag FROM tblPesoVags ORDER BY LetraPesoVag;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodPesoVag'];
				echo ">" . $row['LetraPesoVag'] . " - " . $row['PesoVag'] . " tons. máx.</option>";
			 }
	 ?>
      </select></td>
    </tr>
	<? } elseif ($id == "3") { //Carros de passageiro ?>
    <tr>
      <td width="119" class="headertabela"><div align="right">Tipo do Carro:</div></td>
      <td width="196" bgcolor="#FFFFFF"><label>
        <select name="cmbTipoCarro" id="cmbTipoCarro">
       <?
	   
			$sql = "SELECT CodTipoCarro, LetraTipoCarro, TipoCarro FROM tblTipoCarro ORDER BY TipoCarro;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodTipoCarro'];
				echo ">" . $row['LetraTipoCarro'] . " - " . $row['TipoCarro'] . "</option>";
			 }
	 ?>
        </select>
      </label></td>
    </tr>
    <tr>
      <td width="119" class="headertabela"><div align="right">Material do Carro:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbMatCarro" id="cmbMatCarro">
        <?
	   
			$sql = "SELECT CodMatCarro, LetraMatCarro, MatCarro FROM tblMatCarro ORDER BY LetraMatCarro;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodMatCarro'];
				echo ">" . $row['LetraMatCarro'] . " - " . $row['MatCarro'] . " tons. máx.</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <? } elseif ($id == "4") { //Auto de linha / Serviço ?>
    <tr>
      <td width="119" class="headertabela"><div align="right">Modelo (Sigla):</div></td>
      <td width="196" bgcolor="#FFFFFF"><input name="txtModelo" type="text" id="txtModelo" size="30" maxlength="3" /></td>
    </tr>
    <tr>
    <? } elseif ($id == "5") { //Outros ?>
    <? } ?>
    <tr>
      <td valign="top" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea></td>
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
