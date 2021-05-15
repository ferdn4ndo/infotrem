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

if(empty($txtNome)){
	echo "Nome inv&aacute;lido! <br>";
	$erro = $erro + 1;
}

if($erro == 0){
	
	//Consulta para verificar itens idênticos
	
	$sqlverifica = "SELECT * FROM tblFerrovias WHERE Nome = '" . $txtNome . "';";
	
	if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
		echo "<title>ERRO</title></head><body>";
		echo "<strong>J&aacute; existe uma ferrovia id&ecirc;ntica cadastrado no sistema!</strong>";
		exit;
	} else {
		$sql = "INSERT INTO tblFerrovias (Nome, Detalhes) VALUES('" . $txtNome . "','" . $txtDetalhes ."');";
		
		$ask = mysqlexecuta($id,$sql);
		If ($ask!=0){
			redirecionar("index.php");
			echo "<title>Inserir Ferrovia</title>";
			echo "<META HTTP-EQUIV=Refresh CONTENT=\"10; URL=index.php\">";
			echo "</head>";
			echo "<body>";
			echo "<strong>Cadastro concluído com sucesso!</strong>";
			echo "<p>Redirecionando...<br>Caso não redirecione automaticamente, <a href='index.php'> Clique Aqui!</a>";
		}
		else {
			echo "<title>ERRO</title></head><body>";
			echo "<br><strong>Erro ao interpretar dados!</strong>";
			exit;
		}
	}
}
?>
</body>
</html>
