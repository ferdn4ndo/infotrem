<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Editar Material Rodante</title>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados


//Pega os dados da URL
if (isset($_GET["Categoria"])) {
	$Categoria = $_GET["Categoria"];
} else {
	$Categoria = $_GET["CategoriaNova"];
}
if (isset($_GET["Cod"])) {
	$CodRodante = $_GET["Cod"];
} else {
	$CodRodante = $_POST["txtCodRodante"];
}

//Verifica se os dados foram pegos
if (($CodRodante == "")||($Categoria == "")) {
	echo "<br><center><strong>Erro ao recuperar dados da URL!</strong></center><br>";
}

//Verifica se é para executar
if(isset($_POST['cmbCategoria'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	if(empty($txtCodRodante)){
		$msg = $msg . "C&oacute;digo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbModelo)){
		$msg = $msg . "Modelo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNumero)){
		$msg = $msg . "N&uacute;mero inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if((empty($cmbRegional))&&($cmbRegional!=0)){
		$msg = $msg . "Regional inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFerroviaAtual)){
		$msg = $msg . "Ferrovia atual inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFerroviaOrigem)){
		$msg = $msg . "Ferrovia de origem inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if($txtUltimaData=='00/00/0000'){ $txtUltimaData = ""; }
	if(!empty($txtUltimaData)){
		if(ValidaData($txtUltimaData) == false){
			$msg = $msg . "Ultima data inv&aacute;lida! <br>";
			$erro = $erro + 1;
		}
	}
	if(empty($cmbEstado)){
		$msg = $msg . "Estado inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		//Caso o local esteja vazio
		if ($cmbUltimoLocal=="") { $cmbUltimoLocal = 0; }
		
			$sql = "UPDATE tblRodante SET Categoria = " . $cmbCategoria . ", CodModelo = " . $cmbModelo . ", Numero = " . $txtNumero . ", Regional = " . $cmbRegional . ", FerroviaAtual = " . $cmbFerroviaAtual .  ", FerroviaOrigem = " . $cmbFerroviaOrigem . ", UltimoLocal = " . $cmbUltimoLocal . ", UltimaData = '" . gravaData($txtUltimaData) . "', Estado = " . $cmbEstado . ", Detalhes = '" . $txtDetalhes . "' WHERE CodReg = " . $CodRodante . ";";
			//echo $sql;
			$ask = mysql_query($sql);
			if ($ask!=0){
				$Exibe = $Mensagem['sucesso'];
			}
			else {
				$Exibe = $Mensagem['erro'];
			}
		//}
	} else {
		$Exibe = $Mensagem['erromsg1'] . $msg . $Mensagem['erromsg2'];
	}
}
?>
<script type="text/javascript">
  function mudancaSelecao(elemento){
    var selecionada = elemento.options[elemento.options.selectedIndex];
		document.location=('editarrodante.php?CategoriaNova=' + selecionada.value + '&Cod=<? echo $CodRodante; ?>');
  }
</script>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Executa o comando
$sql = "SELECT * FROM tblRodante WHERE CodReg = " . $CodRodante . ";";
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	$CodReg = $row['CodReg'];
	$CodCategoria = $row['Categoria'];
	$CodModelo = $row['CodModelo'];
	$Numero = $row['Numero'];
	$Regional = $row['Regional'];
	$FerroviaAtual = $row['FerroviaAtual'];
	$FerroviaOrigem = $row['FerroviaOrigem'];
	$UltimoLocal = $row['UltimoLocal'];
	$Estado = $row['Estado'];
	$UltimaFoto = $row['UltimaFoto'];
	$Detalhes = $row['Detalhes'];
	$CodPlanta = $row['CodPlanta'];
	$UltimaData = mostraData($row['UltimaData']);
}
echo $Exibe;
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Editar Material Rodante</div></td>
      </tr>
  	<tr>
    <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($Categoria == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaRodante ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				if ($Categoria == $row['CodCategoria']) { echo " selected='selected'"; }
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select></td>
    </tr>
    <tr>
    
      <td width="119" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbModelo" id="cmbModelo">
       <?
	   if ($Categoria != 0) {
	   		if ($Categoria == "1") {
				$sql = "SELECT tblModelos.CodModelo, tblModLoco.ModeloLoco FROM (tblModelos INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) WHERE tblModelos.Categoria = 1 ORDER BY tblModLoco.ModeloLoco;";
				//echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
						echo ">" . $row['ModeloLoco'] . "</option>";
			 	}
			} elseif ($Categoria == "2") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM ((tblModelos INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblModelos.Categoria = 2 ORDER BY tblTipoVags.TipoVag;";
				//echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
					echo ">" . $row['TipoVag'] . $row['LetraPesoVag'] . "</option>";
			 	}
			} elseif ($Categoria == "3") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM ((tblModelos INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblModelos.Categoria = 3 ORDER BY tblTipoCarro.LetraTipoCarro;";
				//echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
					echo ">" . $row['LetraTipoCarro'] . $row['LetraMatCarro'] . "</option>";
			 	}
			} elseif ($Categoria == "4") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE Categoria = 4 ORDER BY tblTipoAuto.TipoAuto;";
				//echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
					echo ">" . $row['TipoAuto'] . "</option>";
			 	}
			} elseif ($Categoria == "5") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrzes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoMotriz'] . "</option>";
                                }
                        }			
		}
	 ?>
     </select>
        <input type="button" name="cadastrar" id="cadastrar" value="Cadastrar Novo Modelo" onclick="javascript:window.open('inserirmodelo.php?<? echo $_SERVER['QUERY_STRING']; ?>', 'Cadastrar Modelo', 'toolbar=no,location=no,status=no,menubar=no,scrollbars=no,resizable=no, width=650, height=270');" />
        </a></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">
        N&uacute;mero:
      </div></td>
      <td bgcolor="#FFFFFF"><span class="style2">
        <input name="txtNumero" type="text" id="txtNumero" size="10" maxlength="6" value="<? echo $Numero; ?>" />
        *Sem DV</span></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Regional:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbRegional" id="cmbRegional">
	<option value=0 <? if(($Regional==0)||($Regional=="")){ echo "selected='selected'"; } ?>>-</option>
        <?
                        $sql = "SELECT CodLetraRegional, LetraRegional FROM tblRegional ORDER BY LetraRegional;";
                        $res = @mysql_query($sql);

                        //Exibe as linhas encontradas na consulta
                        while ($row = mysql_fetch_array($res)) {
                                echo "<option value=" . $row['CodLetraRegional'];
                                if ($Regional == $row['CodLetraRegional']) { echo " selected='selected'"; }
                                echo ">" . $row['LetraRegional'] . "</option>";
                         }
         ?>
      </select></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia Atual:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbFerroviaAtual" id="cmbFerroviaAtual">
        <?
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				if ($FerroviaAtual == $row['CodFerrovia']) { echo " selected='selected'"; }
				echo ">" . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia de Origem:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbFerroviaOrigem" id="cmbFerroviaOrigem">
        <?
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				if ($FerroviaOrigem == $row['CodFerrovia']) { echo " selected='selected'"; }
				echo ">" . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">&Uacute;ltimo Local:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbUltimoLocal" id="cmbUltimoLocal">
      		<option selected="selected" disabled="disabled" value="0">SELECIONE</option>
        <?
			$sql = "SELECT CodLocal, Sigla, Nome FROM tblLocais ORDER BY Sigla;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodLocal'];
				if ($UltimoLocal == $row['CodLocal']) { echo " selected='selected'"; }
				echo ">" . $row['Sigla'] . " - " . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">&Uacute;ltima Data:</div></td>
      <td bgcolor="#FFFFFF"><input name="txtUltimaData" type="text" id="txtUltimaData" size="10" maxlength="10" value="<? echo $UltimaData; ?>" />
      <input name="txtCategoria" type="hidden" id="txtCategoria" value="<? echo $Categoria; ?>" />
      <input name="txtCodRodante" type="hidden" id="txtCodRodante" value="<? echo $CodRodante; ?>" />
      </td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Estado:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbEstado" id="cmbEstado">
        <option selected="selected" disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodEstado, Estado FROM tblEstadoRodante ORDER BY CodEstado;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodEstado'];
				if ($Estado == $row['CodEstado']) { echo " selected='selected'"; }
				echo ">" . $row['CodEstado'] . " - " . $row['Estado'] . "</option>";
			 }
	 ?>
            </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="43" rows="5" id="txtDetalhes"><? echo $Detalhes; ?></textarea></td>
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
