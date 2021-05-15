<?
// Includes necessários para o funcionamento o website
//include("mysqlconecta.php");
//include("mysqlfuncao.php");
//include("listas.php");


//Arquivo de configurações da conexão com o banco de dados

$dbhost="localhost"; // Host do banco de dados
$dbname="infotrem"; // Indique o nome do banco de dados que será aberto
$usuario="root"; // Indique o nome do usuário que tem acesso
$password="ferd1994"; // Indique a senha do usuário

$versao="1.0.0 de 19-05-12";

//1º passo - Conecta ao servidor MySQL 
if(!($id = mysql_connect($dbhost,$usuario,$password))) {
    echo "N&atilde;o foi poss&iacute;vel estabelecer uma conex&atilde;o com o gerenciador MySQL. Favor Contactar o Administrador.";
    exit;
 } 
 
//2º passo - Seleciona o Banco de Dados 
if(!($con=mysql_select_db($dbname,$id))) { 
   echo "N&atilde;o foi poss&iacute;vel estabelecer uma conex&atilde;o com o gerenciador MySQL. Favor Contactar o Administrador.";
    exit; 
} 

//////////////////////////////////////////////////////////////////////////////////////////

/* 
$id - Ponteiro da Conexão 
$sql - Cláusula SQL a executar 
$erro - Especifica se a função exibe ou não(0=não, 1=sim) 
$res - Resposta 
*/ 

//Função para execução de um comando SQL no banco de dados MySQL
function mysqlexecuta($id,$sql,$erro = 1) { 
    if(empty($sql) OR !($id)) 
       return 0; //Erro na conexão ou no comando SQL   
    if (!($str = @mysql_query($sql,$id))) { 
      if($erro) 
        echo "Ocorreu um erro na execu&ccedil;&atilde;o do Comando SQL no banco de dados. Favor Contactar o Administrador.";
		return 0;
       exit;
    } 
    return $str; 
 }

//Função para contagem de itens que retornam daquela query
function mysqlcontar($id,$sql,$erro = 1) { 
    if(empty($sql) OR !($id)) 
       return 0; //Erro na conexão ou no comando SQL   
    if (!($str = @mysql_query($sql,$id))) { 
      if($erro) 
        echo "Ocorreu um erro na execu&ccedil;&atilde;o do Comando SQL no banco de dados. Favor Contactar o Administrador.";
		return 0;
       exit;
    } 
	$qtd = mysql_num_rows($str);
    return $qtd;
 } 
 
//Protege a entrada de dados contra SQL Injection
function AntiInjection($param){
 	$param = strip_tags($param); //  retirar as tags html 
	$param = mysql_escape_string($param); //Retirar todas tags referentes do mysql ex: select, insert, update drop etc... 
	return $param; 
}

//Verifica se uma string é data ou não
function ValidaData($dat){
	$data = explode("/","$dat"); // fatia a string $dat em pedados, usando / como referência
	$d = $data[0];
	$m = $data[1];
	$y = $data[2];

	// verifica se a data é válida!
	// 1 = true (válida)
	// 0 = false (inválida)
	$res = checkdate($m,$d,$y);
	if ($res == 1){
	   return true;
	} else {
	   return false;
	}
}

// Passando data do banco "AAAA-MM-DD" para "DD/MM/AAAA"
function mostraData ($data) {
if ($data!='') {
   return (substr($data,8,2).'/'.substr($data,5,2).'/'.substr($data,0,4));
}
else { return ''; }
}

// Passando data do text box "DD/MM/AAAA" para "AAAA-MM-DD"
function gravaData ($data) {
	if ($data != '') {
	   //return (substr($data,3,2).'/'.substr($data,0,2).'/'.substr($data,6,4));
	   return (implode("-", array_reverse(explode("/", $data))));
	}
	else { return ''; }
}

// Redirecionar URL
function redirecionar($url, $tempo)
{
    $url = str_replace('&amp;', '&', $url);
        
    if($tempo > 0)
    {
        header("Refresh: $tempo; URL=$url");
		return 0;
    }
    else
    {
        @ob_flush();
        @ob_end_clean();
        header("Location: $url");
        return 0;
    }
}

// Upload de arquivos
function upload($arquivo,$caminho){
	if(!(empty($arquivo))){
		$arquivo1 = $arquivo;
		$arquivo_minusculo = strtolower($arquivo1['name']);
		$caracteres = array("ç","~","^","]","[","{","}",";",":","´",",",">","<","-","/","|","@","$","%","ã","â","á","à","é","è","ó","ò","+","=","*","&","(",")","!","#","?","`","ã"," ","©");
		$arquivo_tratado = str_replace($caracteres,"_",$arquivo_minusculo);
		$destino = $caminho."/".$arquivo_tratado;
		if(move_uploaded_file($arquivo1['tmp_name'],$destino)){
			return $destino;
		}else{
			return 0;
		}
	}
}

// Função para retornar o estado do evento
function retornaestado($DatAbertura, $DatFimInsc, $DatProva){
	// Declara as variáveis
	$DAbertura = strtotime($DatAbertura);
	$DFimInsc = strtotime($DatFimInsc);
	$DProva = strtotime($DatProva);
	$DNow = strtotime(date("m.d.y"));
	
	// Faz a comparação e retorna o resultado
	if ($DAbertura > $DNow){
		return 0;
	} elseif ($DAbertura < $DNow && $DFimInsc > $DNow) {
		return 1;
	} elseif ($DFimInsc < $DNow && $DProva > $DNow) {
		return 2;
	} elseif ($DProva < $DNow) {
		return 3;
	} else {
		return 4;
	}
}

// Função que retorna o tipo de arquivo
// Pega a extensão do arquivo
function RetornaTipoArquivo($NomeArquivo){
	switch (strrchr(strtolower($NomeArquivo), ".")) {
		//PDF - 0
		case ".pdf":
			return 0;
			break;
		//TXT - 1
		case ".txt":
			return 1;
			break;
		//Documentos do WORD - 2
		case ".doc":
			return 2;
			break;
		case ".docx":
			return 2;
			break;
		//Documentos do EXCEL - 3
		case ".xls":
			return 3;
			break;
		case ".xlsx":
			return 3;
			break;
		//Documentos do POWER POINT - 4
		case ".ppt":
			return 4;
			break;
		case ".pptx":
			return 4;
			break;	
		case ".pps":
			return 4;
			break;	
		//Arquivos de Imagem - 5
		case ".gif":
			return 5;
			break;
		case ".bmp":
			return 5;
			break;
		case ".jpg":
			return 5;
			break;
		case ".jpeg":
			return 5;
			break;
		case ".png":
			return 5;
			break;
		//Arquivos do Corel Draw - 6
		case ".cdr":
			return 6;
			break;
		//Arquivos do AutoCAD - 7
		case ".dwg":
			return 7;
			break;
		//Arquivos ZIP - 8
		case ".zip":
			return 8;
			break;
		case ".rar":
			return 8;
			break;
		//Mensagens de e-mail - 9
		case ".eml":
			return 9;
			break;
		//Páginas da Web - 10
		case ".htm":
			return 10;
			break;
		case ".html":
			return 10;
			break;
		//Arquivos Executáveis - 11
		case ".exe":
			return 11;
			break;
	}
}



// Função que retorna o tipo de arquivo
// Pega a extensão do arquivo
function RetornaTipoArquivoString($TipoArquivo){
	switch ($TipoArquivo) {
		//PDF - 0
		case 0:
			return "Documento PDF";
			break;
		//TXT - 1
		case 1:
			return "Arquivo de Texto (TXT)";
			break;
		//Documentos do WORD - 2
		case 2:
			return "Documento do Word (DOC/DOCX)";
			break;
		//Documentos do EXCEL - 3
		case 3:
			return "Documento do Excel (XLS/XLSX)";
			break;
		//Documentos do POWER POINT - 4
		case 4:
			return "Documento do Power Point (PPT/PPTX/PPS)";
			break;	
		//Arquivos de Imagem - 5
		case 5:
			return "Arquivo de Imagem (BMP/GIF/JPEG/JPG/PNG)";
			break;
		//Arquivos do Corel Draw - 6
		case 6:
			return "Documento do Corel Draw (CDR)";
			break;
		//Arquivos do AutoCAD - 7
		case 7:
			return "Desenho do AutoCAD (DWG)";
			break;
		//Arquivos ZIP - 8
		case 8:
			return "Arquivo Compactado (ZIP/RAR)";
			break;
		//Mensagens de e-mail - 9
		case 9:
			return "Mensagem de E-mail (EML)";
			break;
		//Páginas da Web - 10
		case 10:
			return "Página da WEB (HTM/HTML)";
			break;
		//Arquivos Executáveis - 11
		case 11:
			return "Arquivo Executável (EXE)";
			break;
	}
}

// Função que valida o CPF
function validaCPF($cpf)
{	// Verifiva se o número digitado contém todos os digitos
    $cpf = str_pad(ereg_replace('[^0-9]', '', $cpf), 11, '0', STR_PAD_LEFT);
	
	// Verifica se nenhuma das sequências abaixo foi digitada, caso seja, retorna falso
    if (strlen($cpf) != 11 || $cpf == '00000000000' || $cpf == '11111111111' || $cpf == '22222222222' || $cpf == '33333333333' || $cpf == '44444444444' || $cpf == '55555555555' || $cpf == '66666666666' || $cpf == '77777777777' || $cpf == '88888888888' || $cpf == '99999999999')
	{
	return false;
    }
	else
	{   // Calcula os números para verificar se o CPF é verdadeiro
        for ($t = 9; $t < 11; $t++) {
            for ($d = 0, $c = 0; $c < $t; $c++) {
                $d += $cpf{$c} * (($t + 1) - $c);
            }

            $d = ((10 * $d) % 11) % 10;

            if ($cpf{$c} != $d) {
                return false;
            }
        }

        return true;
    }
}

function CalculaDV($Numero) {
	//Calculo do dígito verificador
	for ($i = 0; $i <= 5; $i++) {

		$x = substr($Numero, $i, 1);
		$num[$i] = (7 - $i) * $x;
		//$digito = $digito + $num;
		//echo $x;
		//echo $num;
	}
	$digito = $num[0] + $num[1] + $num[2] + $num[3] + $num[4] + $num[5];
	$verificado = 11 - ($digito % 11);
	
	if ($verificado==11) { $DV = 1; } 
	elseif ($verificado==10) { $DV = 0; }
	else { $DV = $verificado; }
	//$DV = substr($digito, -1)
	
	return $DV;
}

///////////////////////////////////////////////////////////////////////////////////////////////

//Arquivo de listas

//Estado do evento
$CategoriaRodante[1] = "Locomotiva";
$CategoriaRodante[2] = "Vagão";
$CategoriaRodante[3] = "Carro de Passageiros";
$CategoriaRodante[4] = "Auto de linha";
$CategoriaRodante[5] = "Outros";

//Categoria dos Locais
$CategoriaLocal[1] = "Estação";
$CategoriaLocal[2] = "Pátio";
$CategoriaLocal[3] = "Ramal";
$CategoriaLocal[4] = "Oficina";
$CategoriaLocal[5] = "Diversos";

//Tipo do evento
$EstadoRodante[1] = "Em Operação";
$EstadoRodante[2] = "Acidentado";
$EstadoRodante[3] = "Baixado";
$EstadoRodante[4] = "Cortado";
$EstadoRodante[5] = "Transformado";

//Tipo do evento
$EstadoLocal[1] = "Em Operação";
$EstadoLocal[2] = "Abandonado";
$EstadoLocal[3] = "Demolido/Removido";

///////////////////////////////////////////////////////////////////////////////////////////////

//Arquivo de listas

$Mensagem['erro'] = "<p><br><strong>Erro ao interpretar dados!</strong><br></p>";
$Mensagem['sucesso'] = "<p><center><strong>Cadastro concluído com sucesso!</strong><p><a href='index.php'> Clique Aqui para retornar &agrave; p&aacute;gina inicial!</a></p></center>";
$Mensagem['erromsg1'] = "<p>ERRO: <strong>";
$Mensagem['erromsg2'] = "</strong></p>";
$Mensagem['erroduplicado'] = "<center><strong>J&aacute; existe uma categoria id&ecirc;ntica cadastrada no sistema!</strong></center>";
?>