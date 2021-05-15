<?

//---//
//UTILIZAR O SISTEMA DE OBTENÇÃO SIMPLES DO MODELO, E NÃO DE TODOS OS DADOS
//FAZER TRES CONSULTAS: MODELO, FERROVIA, LOCAL
//CRIAR NOME A PARTIR DOS TRES DADOS SIMPLES
//---//


function NomeFoto($Categoria,$CodModelo,$Numero,$CodFerrovia,$CodLocal,$Data,$Autor) {
	//Prepara dados
	$Sep = "_";
	
	//Prepara a consulta e obtem o modelo
	if ($Categoria == 1) { //Locomotivas
		$sql = "SELECT tblModelos.CodModelo, tblModLoco.ModeloLoco FROM (tblModelos INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) WHERE tblModelos.CodModelo = ". $CodModelo ." ORDER BY tblModLoco.ModeloLoco;";
		$res = @mysql_query($sql);
		while ($row = mysql_fetch_array($res)) {
			$Modelo = $row['ModeloLoco'];
		}
	} elseif ($Categoria == 2) { //Vagões
		$sql = "SELECT tblModelos.CodModelo, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM ((tblModelos INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblModelos.CodModelo = ". $CodModelo ." ORDER BY tblTipoVags.TipoVag;";
		$res = @mysql_query($sql);
		while ($row = mysql_fetch_array($res)) {
			$Modelo = $row['TipoVag'] . $row['LetraPesoVag'];
		}
	} elseif ($Categoria == 3) { //Carros
		$sql = "SELECT tblModelos.CodModelo, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM ((tblModelos INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblModelos.CodModelo = ". $CodModelo ." ORDER BY tblTipoCarro.LetraTipoCarro;";
		$res = @mysql_query($sql);
		while ($row = mysql_fetch_array($res)) {
			$Modelo = $row['LetraTipoCarro'] . $row['LetraMatCarro'];
		}
	} elseif ($Categoria == 4) { //Autos de Linha
		$sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE tblModelos.CodModelo = ". $CodModelo ." ORDER BY tblTipoAuto.TipoAuto;";
		$res = @mysql_query($sql);
		while ($row = mysql_fetch_array($res)) {
			$Modelo = $row['TipoAuto'];
		}
	} elseif ($Categoria == 5) { //Automotriz / Trem-unidade
		$sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE tblModelos.CodModelo = ". $CodModelo ." ORDER BY tblTipoMotrizes.TipoMotriz;";
		$res = @mysql_query($sql);
		while ($row = mysql_fetch_array($res)) {
			$Modelo = $row['TipoMotriz'];
		}
	}
	
	//Prepara a consulta e obtem o modelo
	$sqlfer = "SELECT CodFerrovia, Nome FROM tblFerrovias WHERE CodFerrovia = ". $CodFerrovia ." ORDER BY Nome;";
	$resfer = @mysql_query($sqlfer);
	while ($rowfer = mysql_fetch_array($resfer)) {
		$Ferrovia = $rowfer['Nome'];
	}
	
	//Prepara a consulta e obtem o local
	if(($CodLocal!="")&&($CodLocal!=3295)){
		$sqllocal = "SELECT CodLocal, Sigla, Nome FROM tblLocais WHERE CodLocal = ". $CodLocal ." ORDER BY Sigla;";
		$reslocal = @mysql_query($sqllocal);
		while ($rowlocal = mysql_fetch_array($reslocal)) {
			$Local = $rowlocal['Sigla'];
		 }
	}
	
	//Verifica se deve preparar o local
	if (($CodLocal!="") && ($Local!="")) {
		$LocalSep = $Sep . $Local;
	}
	
	//Verifica se deve preparar a data
	if (($Data!="") && (validaData($Data))) {
		$DataTratada = str_replace("/","-",$Data);
		$DataNova = substr($DataTratada,0,6).substr($DataTratada,8,2);
		$DataSep = $Sep . $DataNova;
	}
	
	//Verifica se deve preparar o autor
	if ($Autor!="") {
		$caracteresA = array("ã","Ã","â","Â","á","Á","à","À");
		$NomeTratadoA = str_replace($caracteresA,"a",$Autor);
		$caracteresE = array("é","É","è","È","ê","Ê");
		$NomeTratadoE = str_replace($caracteresE,"e",$NomeTratadoA);
		$caracteresI = array("í","Í","î","Î");
		$NomeTratadoI = str_replace($caracteresI,"i",$NomeTratadoE);
		$caracteresO = array("ó","Ó","ò","Ò","ô","Ô");
		$NomeTratadoO = str_replace($caracteresO,"o",$NomeTratadoI);
		$caracteresU = array("ú","Ú","ù","Ù","û","Û","ü","Ü");
		$NomeTratadoU = str_replace($caracteresU,"u",$NomeTratadoO);
		$AutorTratado = str_replace(" ","",$NomeTratadoU);
		$AutorSep = $Sep . $AutorTratado;
	}
	
	//Prepara o nome da foto
	$Nome = $Modelo . $Sep . $Numero . $Sep . $Ferrovia . $LocalSep . $DataSep . $AutorSep;
	
	//Retorna o nome da foto
	return $Nome;
}

?>