<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Foto Externa</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
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
	
	document.location=('inserirfotoexterna.php?Categoria=' + selecionada.value);
	
  }
</script>
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados
include "function_nomefoto.php"; //Para renomear a foto

$id = $_GET['Categoria'];

if(isset($_POST['txtLink'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtLink)){
		$msg = $msg . "Link inv&aacute;lido! <br>";
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
		$msg = $msg ."N&uacute;mero inv&aacute;lido! <br>";
		$erro = $erro + 1;
	} elseif (!is_numeric($txtNumero)) {
		$msg = $msg ."N&uacute;mero n&atilde;o num&eacute;rico! <br>";
		$erro = $erro + 1;
	}
	if((empty($cmbLocal))||($cmbLocal==0)){
		$cmbLocal = 3295;
		//$msg = $msg . "Local inv&aacute;lido! <br>";
		//$erro = $erro + 1;
	}
	if(!empty($txtData)){
		if(ValidaData($txtData) == false){
			$msg = $msg . "Data inv&aacute;lida! <br>";
			$erro = $erro + 1;
		}
	} else {
		$txtData = "00/00/0000";
	}
	
	//Checa o tamanho do arquivo e, consequentemente, se ele existe
	if ( file($txtLink) ){
		//Checa o tamanho do arquivo
		$TamanhoArquivo = filesize($txtLink); 
		if ($TamanhoArquivo > 10000000) {
				$msg = $msg . "Arquivo muito grande! <br>";
				$erro = $erro + 1;
		}
		
		//Pega o nome do arquivo
		$NomeArquivo = basename($txtLink);
		
		//Checa a extensão do arquivo
		$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png");
		if (!in_array(strrchr($NomeArquivo, "."), $extensoes)) {
			$msg = $msg . "A extensão do arquivo <b>" . $NomeArquivo . "</b> não é válida";
			$erro = $erro + 1;
		}
	} else {
		$msg = $msg . "Arquivo n&atilde;o existe! <br>";
		$erro = $erro + 1;
	}
	
	//Checa se não foram encontrados erros
	if($erro == 0){
		//Prepara as strings
		$caminho = "uploads/fotos/";
		$novo = $caminho . $NomeArquivo;
		
		//Copia o arquivo para o servidor e checa
		if (!copy($txtLink, $novo)) {
			$msg = $msg . "Falha ao copiar <b>" . $NomeArquivo . "</b>! <br>";
			$erro = $erro + 1;
		}
		
		//Checa se não foram encontrados erros
		if($erro == 0){
		
			//Prepara o novo nome da foto
			if ($cmbCategoria==2) {
				$NomeNovo = NomeFoto($cmbCategoria,$cmbModelo,$txtNumero."-".CalculaDV($txtNumero),$cmbFerrovia,$cmbLocal,$txtData,$txtAutor);
			} else {
				$NomeNovo = NomeFoto($cmbCategoria,$cmbModelo,$txtNumero,$cmbFerrovia,$cmbLocal,$txtData,$txtAutor);
			}
			
			//Prepara para renomear
			$CaminhoCompleto = "/var/www/infotrem/uploads/fotos/";
			$CaminhoBD = "uploads/fotos/";
			$Extensao = strrchr(strtolower($NomeArquivo), ".");
			$NomeCompleto = $CaminhoCompleto.$NomeNovo.$Extensao;
			$NomeBD = $CaminhoBD.$NomeNovo.$Extensao;
			//Verifica se o nome podera ser utilizado
			if (file_exists($NomeCompleto)) {
				$NomeTmp1 = $CaminhoCompleto.$NomeNovo."_1".$Extensao;
				$NomeTmp2 = $CaminhoBD.$NomeNovo."_1".$Extensao;
				$i = 1;
				while (file_exists($NomeTmp1)) {
					$i++;
					$NomeTmp1 = $CaminhoCompleto.$NomeNovo."_".$i.$Extensao;
					$NomeTmp2 = $CaminhoBD.$NomeNovo."_".$i.$Extensao;
				}
				$NomeCompleto = $NomeTmp1;
				$NomeBD = $NomeTmp2;
			}
			//Renomeia a foto
			$Renomeia = rename("/var/www/infotrem/" . $novo, $NomeCompleto);
			//echo "/var/www/infotrem/" . $txtPath . "<br>" . $NomeBD . "<br>" . $NomeCompleto;
			if (!$Renomeia) {
				$msg = $msg . "Erro ao renomar foto! <br>";
			}
		
			//Consulta para verificar itens idênticos
			$sqlverifica = "SELECT * FROM tblFotos WHERE LinkOriginal = '" . $txtLink . "';";
			
			//Se já houver um registro igual		
			if(mysql_num_rows(mysql_query($sqlverifica)) > 0) {
				$msg = $msg . "J&aacute; existe um registro id&ecirc;ntico no sistema! <br>";
				$erro = $erro + 1;
			} else {
				//Registra a foto e pega o codigo
				$sql = "INSERT INTO tblFotos (Categoria, Ferrovia, Local, Data, Detalhes, Autor, CaminhoFoto, LinkOriginal) VALUES(" . $cmbCategoria . "," . $cmbFerrovia . "," . $cmbLocal .  ",'" . gravaData($txtData) . "','" . $txtDetalhes . "','" . $txtAutor . "','" . $NomeBD . "','" . $txtLink . "');";
                $ask = mysql_query($sql);
				$CodFoto = mysql_insert_id();

				//Checa se ja exite um registro de mat. rodante
				$sqlrod = "SELECT CodReg FROM tblRodante WHERE Numero = " . $txtNumero . ";";
				$askrod = mysql_query($sqlrod);
				$cntrod = mysql_num_rows($askrod);
				if($cntrod > 0) {
					//Se ja existe um registro de mat. rodante, atualiza
					while ($rowrod = mysql_fetch_array($askrod)){
						$CodRodante = $rowrod['CodReg'];
					}
					$sqlupd = "UPDATE tblRodante SET UltimaFoto = " . $CodFoto . " WHERE CodReg = " . $CodRodante . ";";
					$askupd = mysql_query($sqlupd);
				} else {
					//Senao, cria um novo mat. rodante
					$sqlins = "INSERT INTO tblRodante (Categoria, CodModelo, Numero, FerroviaAtual, FerroviaOrigem, UltimaFoto, UltimaData, UltimoLocal, Estado, Detalhes) VALUES (" . $cmbCategoria . "," . $cmbModelo . "," . $txtNumero . ",13,13," . $CodFoto . ",'" . gravaData($txtData) . "'," . $cmbLocal . ",5,'');";
					$askins = mysql_query($sqlins);
					
					//Pega o codigo
					$sqlcod = "SELECT * FROM tblRodante WHERE Numero = " . $txtNumero . ";";
					$askcod = mysql_query($sqlcod);
					$rowcod = mysql_fetch_array($askcod);
					while ($rowcod = mysql_fetch_array($askcod)){
								$CodRodante = $rowcod['CodReg'];
					}
					$CodRodante = mysql_insert_id();
				}
				
				//Atualiza o registro da foto
				$sqlfot = "UPDATE tblFotos SET CodRodante = " . $CodRodante . " WHERE CodFoto = " . $CodFoto . ";";
				$askfot = mysql_query($sqlfot);
				
				//Debugging
				$Debug = 0;
				if ($Debug==1){
					echo "CodFoto = " . $CodFoto . "<br>";
					echo "CodRodante = " . $CodRodante . "<br>";
					echo "ask = " . $ask . "<br>";
					echo "que = " . $que . "<br>";
					echo "askrod = " . $askrod . "<br>";
					echo "askupd = " . $askupd . "<br>";
					echo "askins = " . $askins . "<br>";
					echo "askcod = " . $askcod . "<br>";
					echo "cntrod = " . $cntrod . "<br>";
					echo "sql = " . $sql . "<br>";
					echo "cod = " . $cod . "<br>";
					echo "sqlrod = " . $sqlrod . "<br>";
					echo "sqlupd = " . $sqlupd . "<br>";
					echo "sqlins = " . $sqlins . "<br>";
					echo "sqlcod = " . $sqlcod . "<br>";
					echo "sqlfot = " . $sqlfot . "<br>";
					echo "askfot = " . $askfot . "<br>";	
				}

				//Checa se os processos foram executados
				if ($ask!=1){
					$msg = $msg . "Erro ao executar comando SQL! <br>";
					$erro = $erro + 1;
				}
			}
		}
	}
	if($erro == 0){
		echo $Mensagem['sucesso'];
	} else {
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
}
?><p><table width="100%" height="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Foto Externa</div>
        <div align="left"></div></td>
      </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
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
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Link:</div></td>
      <td width="300" bgcolor="#FFFFFF"><span class="style3">
        <input name="txtLink" type="text" id="txtLink" size="50" maxlength="255" />
      </span></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbModelo" id="cmbModelo">
          <?
		$Categoria = $id;
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
                                $sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE tblModelos.Categoria = 4 ORDER BY tblTipoAuto.TipoAuto;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoAuto'] . "</option>";
                                }
                        } elseif ($Categoria == "5") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE tblModelos.Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoMotriz'] . "</option>";
                                }
                        } elseif ($Categoria == "0") {
				echo "<option value='0' selected='selected'>Outros / Diversos</option>";
			}
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Numero:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNumero" type="text" id="txtNumero" size="10" maxlength="6" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Ferrovia:
        
      </div></td>
      <td width="300" bgcolor="#FFFFFF"><select name="cmbFerrovia" id="cmbFerrovi">
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Local:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbLocal" id="cmbLocal">
          <option value="0">-</option>
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Data:</div></td>

      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtData" type="text" id="txtData" size="10" maxlength="10" />
      </span></div></td>
    </tr><tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Autor:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtAutor" type="text" id="txtAutor" size="50" maxlength="30" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea>
        <span class="style2">
        <input type="hidden" name="txtPath" id="txtPath" value="<? 
	if ($path != "") {
	echo $path;
} else {
	echo $caminho . $arquivo_tratado;
}
?>" />
        </span></div></td>
    </tr>

    
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" onclick="createURL()" />
      </div></td>
    </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
