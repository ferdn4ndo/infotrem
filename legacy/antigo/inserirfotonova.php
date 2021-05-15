<?php
//Includes
include "includeslocalhost.php"; 

if (!isset($_SESSION)) {
  session_start();
}
?>

<?php
$colname_cfoto_rs = "-1";
if (isset($_SESSION['MM_Username'])) {
  $colname_cfoto_rs = (get_magic_quotes_gpc()) ? $_SESSION['MM_Username'] : addslashes($_SESSION['MM_Username']);
}
mysql_select_db($database_teste, $teste);
$query_cfoto_rs = sprintf("SELECT * FROM tblFotos WHERE CodFoto = %s", $colname_cfoto_rs);
$cfoto_rs = mysql_query($query_cfoto_rs, $teste) or die(mysql_error());
$row_cfoto_rs = mysql_fetch_assoc($cfoto_rs);
$totalRows_cfoto_rs = mysql_num_rows($cfoto_rs);
?>
<?php // upload/validação da foto e upload do path para a tabela
$erro = $config = array();

// Prepara a variável do arquivo
$arquivo = isset($_FILES["foto"]) ? $_FILES["foto"] : FALSE;

// Tamanho máximo do arquivo (em bytes)
$config["tamanho"] = 100000000;
// Largura máxima (pixels)
$config["largura"] = 100000000;
// Altura máxima (pixels)
$config["altura"]  = 10000000;

// Formulário postado... executa as ações
if($arquivo)
{  
    // Verifica se o mime-type do arquivo é de imagem
    if(!eregi("^image\/(pjpeg|jpeg|png|gif|bmp|jpg|png)$", $arquivo["type"]))
    {
        $erro[] = "Arquivo em formato inválido! A imagem deve ser jpg, jpeg,
            bmp, gif ou png. Envie outro arquivo";
    }
    else
    {
        // Verifica tamanho do arquivo
        if($arquivo["size"] > $config["tamanho"])
        {
            $erro[] = "Arquivo em tamanho muito grande!
        A imagem deve ser de no máximo " . $config["tamanho"] . " bytes.
        Envie outro arquivo";
        }
        
        // Para verificar as dimensões da imagem
        $tamanhos = getimagesize($arquivo["tmp_name"]);
        
        // Verifica largura
        if($tamanhos[0] > $config["largura"])
        {
            $erro[] = "Largura da imagem não deve
                ultrapassar " . $config["largura"] . " pixels";
        }

        // Verifica altura
        if($tamanhos[1] > $config["altura"])
        {
            $erro[] = "Altura da imagem não deve
                ultrapassar " . $config["altura"] . " pixels";
        }
    }
    
    // Imprime as mensagens de erro
    if(sizeof($erro))
    {
        foreach($erro as $err)
        {
            echo " - " . $err . "<BR>";
        }

            }

    // Verificação de dados OK, nenhum erro ocorrido, executa então o upload...
    else
    {
        // Pega extensão do arquivo
        preg_match("/\.(gif|bmp|png|jpg|jpeg){1}$/i", $arquivo["name"], $ext);

        // Gera um nome único para a imagem
        $imagem_nome = md5(uniqid(time())) . "." . $ext[1];

        // Caminho de onde a imagem ficará
        $imagem_dir = "fotos/" . $imagem_nome;
        
        //usuario a ser inserido no bd
        $usuariologado = $_SESSION['MM_Username'];
        
        // insere no banco de dados
  $insertSQL = sprintf("INSERT INTO tblFotos(Id, foto) VALUES ('$usuariologado', '$imagem_nome')");

  mysql_select_db($database_teste, $teste);
  $Result1 = mysql_query($insertSQL, $teste) or die(mysql_error());

       // Faz o upload da imagem
        move_uploaded_file($arquivo["tmp_name"], $imagem_dir);

        echo "Sua foto foi enviada com sucesso!";
        echo "<meta http-equiv='refresh' content='1' />";
        
}
}
// atualização/validação da foto e upload do path para a tabela
$erro = $config = array();

// Prepara a variável do arquivo
$arquivo = isset($_FILES["foto2"]) ? $_FILES["foto2"] : FALSE;

// Tamanho máximo do arquivo (em bytes)
$config["tamanho"] = 100000000;
// Largura máxima (pixels)
$config["largura"] = 100000000;
// Altura máxima (pixels)
$config["altura"]  = 10000000;

// Formulário postado... executa as ações
if($arquivo)
{  
    // Verifica se o mime-type do arquivo é de imagem
    if(!eregi("^image\/(pjpeg|jpeg|png|gif|bmp|jpg|png)$", $arquivo["type"]))
    {
        $erro[] = "Arquivo em formato inválido! A imagem deve ser jpg, jpeg,
            bmp, gif ou png. Envie outro arquivo";
    }
    else
    {
        // Verifica tamanho do arquivo
        if($arquivo["size"] > $config["tamanho"])
        {
            $erro[] = "Arquivo em tamanho muito grande!
        A imagem deve ser de no máximo " . $config["tamanho"] . " bytes.
        Envie outro arquivo";
        }
        
        // Para verificar as dimensões da imagem
        $tamanhos = getimagesize($arquivo["tmp_name"]);
        
        // Verifica largura
        if($tamanhos[0] > $config["largura"])
        {
            $erro[] = "Largura da imagem não deve
                ultrapassar " . $config["largura"] . " pixels";
        }

        // Verifica altura
        if($tamanhos[1] > $config["altura"])
        {
            $erro[] = "Altura da imagem não deve
                ultrapassar " . $config["altura"] . " pixels";
        }
    }
    
    // Imprime as mensagens de erro
    if(sizeof($erro))
    {
        foreach($erro as $err)
        {
            echo " - " . $err . "<br />";
        }

            }

    // Verificação de dados OK, nenhum erro ocorrido, executa então o upload...
    else
    {
        // Pega extensão do arquivo
        preg_match("/\.(gif|bmp|png|jpg|jpeg){1}$/i", $arquivo["name"], $ext);

        // Gera um nome único para a imagem
        $imagem_nome = $row_cfoto_rs['foto'];

        // Caminho de onde a imagem ficará
        $imagem_dir = "fotos/" . $imagem_nome;
        
        // Faz o upload da imagem
        move_uploaded_file($arquivo["tmp_name"], $imagem_dir);

        echo "Sua foto foi atualiza com sucesso!";
        echo "<meta http-equiv='refresh' content='1' />";
        
}
}
?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Inserir Foto</title>
<style type="text/css">
<!--
#Layer1 {
    position:absolute;
    z-index:4;
    left: 10px;
    top: 49px;
    background-color: #FF9900;
}
#Layer2 {
    position:absolute;
    width:386px;
    height:300px;
    z-index:2;
    left: 351px;
    top: 37px;

}
#Layer3 {
    position:absolute;
    width:324px;
    height:188px;
    z-index:3;
    left: 10px;
    top: 180px;
}
#Layer4 {
position:absolute;
    width:237px;
    height:67px;
    z-index:1;
    left: 10px;
    top: 49px;
    background-image:url(/eteca/fotos/fundo1.gif);
}
-->
</style>
</head>

<body>
<?php if ($totalRows_cfoto_rs == 0) { // Show if recordset empty ?>
  <div id="Layer1">
    <form  method="post"  enctype="multipart/form-data" name="uploadform">
  <input type="file" name="foto"><br />
  <input type="submit" value="Enviar Foto!">
  </form>
  </div>
  <?php } // Show if recordset empty ?>
  <div id="Layer2"></div>
  <?php if ($totalRows_cfoto_rs > 0) { // Show if recordset not empty ?>
  <div id="Layer3">
    <p>Foto atual : <img src="fotos/<?php echo $row_cfoto_rs['foto']; ?>" /> </p>
    <p>Atualizar foto :</p>
     <form  method="post"  enctype="multipart/form-data" name="uploadform2">
       <input type="file" name="foto2"><br />
       <input type="submit" value="Enviar Foto!">
    </form>
    <p><a href="deletar.php?foto=<?php echo $row_cfoto_rs['foto']; ?>">Deletar foto </a></p>
    <p> </p>
  </div>
    <?php } // Show if recordset not empty ?>
    <div id="Layer4"></div>
</body>
</html>
<?php
mysql_free_result($cfoto_rs);
?>