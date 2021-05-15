<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>

</head>

<body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

// esta variavel sera a query utilizada para insercao dos
// dados no banco, tendo o %d substituido pelo id_exemplo
// e o %s substituido pela descricao
//$query = ‘insert into exemplo (id_exemplo, descricao) values (%d, ”%s”)’;

// carregamos o conteudo do arquivo XML
//$xml = file_get_contents('estacoes.xml');

// transformamos o XML em um objeto, para que possamos trabalhar
// de forma mais simples com ele
//$sxml = new SimpleXMLElement($xml);

//$xmlstr = simplexml_load_file("estacoes.xml");
//echo $xmlstr->getName() . "<br />";
echo phpversion();
//print_r($xmlstr);

// aqui iteramos por todo o XML:
// a cada iteracao, $line ira conter um objeto to tipo
// SimpleXMLElement, sendo o equivalente a:
//
//  <line>
//      <id_exemplo>1</id_exemplo>
//      <descricao>Primeiro exemplo</descricao>
//  </line>
//
/*
foreach ($sxml as $linhaAtual) {
	// aqui vamos obter cada item do xml que seria referente
	// ao campo da tabela.
	// Necessario cast pelo fato de que a propriedade do objeto
	// tambem é um objeto do tipo SimpleXMLElement
	$sigla = (string) $linhaAtual->name;
	$descricao = (string) $linhaAtual->description;
	$coordenadas = (string) $linhaAtual->coordinates;
	$list = explode(',', $coordenadas);
	$latitude = $list[0];
	$longitude = $list[1];
	$zoom = $list[2];

	
	// aqui preparamos a query para ser utilizada
	$tmpQuery = sprintf($query, $id, $descricao);
	
	// exibimos a query que será executada
	//echo sprintf(‘Executando query: %s%s’, $tmpQuery, “\n”);
	echo "INSERT INTO tblTeste (Sigla, Nome, Lat, Long, Zoom) VALUES ('" . $sigla . "','" . $descricao . "','" . $latitude . "','" . $longitude . "'," . $zoom . ");";

	// e aqui executamos a query
	//mysql_query($tmpQuery);
}
*/

//$xmlDoc = new DOMDocument();
//$xmlDoc->load("estacoes.xml");

//$x = $xmlDoc->documentElement;
//foreach ($x->childNodes AS $item)
//  {
//  print $item->nodeName . " = " . $item->nodeValue . "<br />";
//  }

/*
echo "<table>";
for($i=2;$i<=3295;$i++) {
//for($i=2;$i<=5535;$i++) {
	echo "<tr><td>";
	//echo "=PROCV(A" . $i . ";Plan1!A2:H626;4;0)";
	//echo "=PROCV(A" . $i . ";Plan1!A2:H626;8;0)";
	echo "=PROCV(B" . $i . ";Plan2!A2:B5535;1;0)";
	echo "</tr></td>\n";
}
echo "</table>";*/

/*
echo "<table>";
for($i=599;$i<=530;$i--) {
	echo "<tr><td>";
	$n = str_pad($i, 3, "0", STR_PAD_LEFT); //Preenche os zeros
	echo "&#36;EstadoBoleto['-" . $n . "']"; 
	echo " = 'Erro na comunic. com a loja durante requisi&ccedil;&atilde;o dos dados da compra'";
	echo "</tr></td>\n";
}
echo "</table>";
*/

$linkboleto = "http://www.cscconsultoria.com.br/boletoteste27.txt";
$linhasboleto = fopen ($linkboleto, "r");
while (!feof ($linhasboleto))
{
$ponteiroboleto = fgets($linhasboleto, 4096);
$valoresboleto = explode("#",$ponteiroboleto);
	$ValorPago = $valoresboleto[6];
	$DataPago = $valoresboleto[7];
}
fclose ($linhasboleto);
echo $ValorPago;
echo $DataPago;
?>
</body>
</html>
