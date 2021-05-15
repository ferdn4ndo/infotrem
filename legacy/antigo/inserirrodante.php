<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Material Rodante</title>
<script type="text/javascript">
  // Função personalizada que é chamada sempre que
  // houver uma mudança de item no elemento select
  // Note que a função recebe, como argumento, o elemento
  // select no qual o evento onchange foi disparado 
  function mudancaSelecao(elemento){
    // vamos obter a opção selecionada
    var selecionada = elemento.options[elemento.options.selectedIndex];

    // vamos exibir o texto da opção selecionada
    //window.alert("Texto da opção: " + selecionada.text);

    // vamos exibir o valor da opção selecionada
    //window.alert("Valor da opção: " + selecionada.value);
	
	document.location=('inserirrodante.php?Categoria=' + selecionada.value);
	
  }
</script>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$id = $_GET["Categoria"];

//Verifica se é para executar
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
	if(empty($cmbModelo)){
		$msg = $msg . "Modelo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNumero)){
		$msg = $msg ."N&uacute;mero inv&aacute;lido! <br>";
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
		
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblRodante WHERE CodModelo = " . $cmbModelo . " AND Numero = " . $txtNumero . ";";

		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblRodante (Categoria, CodModelo, Numero, Regional, FerroviaAtual, FerroviaOrigem, UltimoLocal, UltimaData, Estado, Detalhes) VALUES(" . $cmbCategoria . "," . $cmbModelo . "," . $txtNumero . "," . $cmbRegional . "," . $cmbFerroviaAtual .  "," . $cmbFerroviaOrigem . "," . $cmbUltimoLocal . ",'" . gravaData($txtUltimaData) . "'," . $cmbEstado . ",'" . $txtDetalhes . "');";
			
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
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Cadastrar Material Rodante</div></td>
      </tr>
  	<tr>
    <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($id == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaRodante ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				if ($id == $row['CodCategoria']) { echo " selected='selected'"; }
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select></td>
    </tr>
    <tr>
    
      <td width="119" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbModelo" id="cmbModelo">
       <?
	   if ($id != 0) {
	   		if ($id == "1") {
				//$sql = "SELECT tblModelos.CodModelo, tblModelos.Modelo, tblFabricantes.NomeFabricante FROM (tblModelos INNER JOIN tblFabricantes ON tblModelos.Fabricante = tblFabricantes.CodFabricante) WHERE tblModelos.Categoria = 1 ORDER BY tblModelos.Modelo;";
				$sql = "SELECT tblModelos.CodModelo, tblModLoco.ModeloLoco FROM (tblModelos INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) WHERE tblModelos.Categoria = 1 ORDER BY tblModLoco.ModeloLoco;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					//echo ">" . $row['Modelo']; . " (" .  $row['NomeFabricante'] . ")</option>";
					echo ">" . $row['ModeloLoco'] . "</option>";
			 	}
			} elseif ($id == "2") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM ((tblModelos INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblModelos.Categoria = 2 ORDER BY tblTipoVags.TipoVag;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['TipoVag'] . $row['LetraPesoVag'] . "</option>";
			 	}
			} elseif ($id == "3") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM ((tblModelos INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblModelos.Categoria = 3 ORDER BY tblTipoCarro.LetraTipoCarro;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['LetraTipoCarro'] . $row['LetraMatCarro'] . "</option>";
			 	}
			} elseif ($id == "4") {
				//$sql = "SELECT CodModelo, Modelo FROM tblModelos WHERE Categoria = 4 ORDER BY Modelo;";
				$sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE tblModelos.Categoria = 4 ORDER BY tblTipoAuto.TipoAuto;";

				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['TipoAuto'] . "</option>";
			 	}
			} elseif ($id == "5") {
					//$sql = "SELECT CodModelo, Modelo FROM tblModelos WHERE Categoria = 4 ORDER BY Modelo;";
					$sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE tblModelos.Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz;";

					echo $sql;
					$res = @mysql_query($sql);

					//Exibe as linhas encontradas na consulta
					while ($row = mysql_fetch_array($res)) {
							echo "<option value=" . $row['CodModelo'];
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
        <input name="txtNumero" type="text" id="txtNumero" size="10" maxlength="6" />
        *Sem DV</span></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Regional:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbRegional" id="cmbRegional">
	<option value=0 selected='selected'>-</option>
        <?
                        $sql = "SELECT CodLetraRegional, LetraRegional, Regional FROM tblRegional ORDER BY LetraRegional;";
                        $res = @mysql_query($sql);

                        //Exibe as linhas encontradas na consulta
                        while ($row = mysql_fetch_array($res)) {
                                echo "<option value=" . $row['CodLetraRegional'];
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
				echo ">" . $row['Sigla'] . " - " . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">&Uacute;ltima Data:</div></td>
      <td bgcolor="#FFFFFF"><input name="txtUltimaData" type="text" id="txtUltimaData" size="10" maxlength="10" /></td>
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
				echo ">" . $row['CodEstado'] . " - " . $row['Estado'] . "</option>";
			 }
	 ?>
            </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="43" rows="5" id="txtDetalhes"></textarea></td>
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
