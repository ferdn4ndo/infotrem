<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Teste </title><br />
</head>

<body>
<?

//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

$sql = "SELECT * FROM tblRodante;";
$res = mysqlexecuta($id,$sql);

//echo "teste";

?>
<table width=100% cellpading=0 cellspacing=0>
<tr>
      <td>C&oacute;digo</td>
      <td>Categoria</td>
      <td>Modelo</td>
      <td>Numero</td> 
     <td>Ferrovia Atual</td> 
     <td>Ferrovia Origem</td>
     <td>Ultimo Local</td>
     <td>Ultima Data</td>
     <td>Estado</td>
     <td>Ultima Foto</td>
     <td>Detalhes</td>
     <td>CodPlanta</td>
  </tr>
 <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
 ?> 
  <tr>
      <td><? echo $row['CodReg'];?></td>
      <td><? echo $row['Categoria'];?></td>
      <td><? echo $row['Modelo'];?></td> 
      <td><? echo $row['Numero'];?></td> 
      <td><? echo $row['FerroviaAtual'];?></td> 
      <td><? echo $row['FerroviaOrigem'];?></td> 
      <td><? echo $row['UltimoLocal'];?></td> 
      <td><? echo $row['UltimaData'];?></td> 
      <td><? echo $row['Estado'];?></td> 
      <td><? echo $row['UltimaFoto'];?></td> 
      <td><? echo $row['Detalhes'];?></td> 
      <td><? echo $row['CodPlanta'];?></td> 
  </tr>

 <?
  }
  
 ?>
 </table> 
 
<p>
  <?
/*
//Teste de concatenação de strings
$a = "a";
$b = "b";
$c = $a . $b;
echo $c;
echo "<br>";
echo "teste";
*/
/*
//Teste de redirecionamento da página
echo "<br>Redir teste";
header("Location: 'http:\\localhost\index.php'");
*/

$teste = "SELECT * FROM tblRodante;";
echo "Total: " . mysqlcontar($id,$teste) . " registro(s).";

//Teste de download
/*
include "videodownload.php";
$a =  getYoutubeVideo('http://www.youtube.com/watch?v=nm42UBPnpxI&feature=mh_lolz&list=FLwT0FQqRkWv3Tni9SlrEQuw', 'video/', 'teste2', 'hd720', 'video/mp4');
echo $a; */

include "videodownload2.php";
$video_url = "http://www.youtube.com/watch?v=z-C-fTIRsd8";
$filename = "test.flv";
$youtube_video_grabber = new youtubegrabber($video_url, $filename);
echo "<p>done downloading... saved as: {$filename}</p>";

?>
</body>
</html>
