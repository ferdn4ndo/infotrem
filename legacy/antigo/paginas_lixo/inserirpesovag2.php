<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega variaveis vinda do formulário via POST
foreach( $_POST as $campo => $vlr){
   $$campo = AntiInjection($vlr);
}
$erro = 0;

if(empty($txtLetra)){
	$msg = $msg . "Letra inv&aacute;lida! <br>";
	$erro = $erro + 1;
}
if(empty($txtPeso)){
	$msg = $msg . "Peso n&atilde;o preenchido!<br>";
	$erro = $erro + 1;
}
if(!is_numeric($txtPeso)){
	$msg = $msg . "Peso inv&aacute;lido! <br>";
	$erro = $erro + 1;
}

if($erro == 0){

	//Converte a letra para maiúscula
	$letra = strtoupper($txtLetra);
	
	//Consulta para verificar itens idênticos
	
	$sqlverifica = "SELECT * FROM tblPesoVags WHERE LetraPesoVag = '" . $letra . "';";
	
	if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
		echo "<title>ERRO</title></head><body>";
		echo "<strong>J&aacute; existe uma letra id&ecirc;ntica cadastrada no sistema!</strong>";
		exit;
	} else {
		$sql = "INSERT INTO tblPesoVags (LetraPesoVag, PesoVag) VALUES('" . $letra . "'," . $txtPeso . ");";
		
		$ask = mysqlexecuta($id,$sql);
		if ($ask!=0){
			echo "<title>Inserir Peso de Vag&atilde;o</title>";
			echo "<META HTTP-EQUIV=Refresh CONTENT=\"5; URL=index.php\">";
			echo "</head>";
			echo "<body>";
			echo "<strong>Cadastro concluído com sucesso!</strong>";
			echo "<center><p>Redirecionando...<br>Caso não redirecione automaticamente, <a href='index.php'> Clique Aqui!</a></center>";
		}
		else {
			echo "<title>ERRO</title></head><body>";
			echo "<br><strong>Erro ao interpretar dados!</strong><br>";
			exit;
		}
	}
} else {
	echo $msg;
}
?>
</body>
</html>
