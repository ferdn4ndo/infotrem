<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<title>Menu M&aacute;gico</title>
	<meta http-equiv="content-type" content="text/html;charset=iso-8859-1" />
	<meta name="generator" content="Geany 0.16" />
	<style>
		#menu-magico {
			position: absolute;
			top: 0;
			left: 0;
			text-align: right;
			padding: 3px 3px 3px 3px;
		}
		
		#menu-magico-button {
			background-color: red;
			float: right;
		}
		
		#teste1 {
			width:50px;
		}
		#subteste1 {
			width:80px;
			position:relative;
			left:50px;
			top:-20px;
		}
		#teste2 {
	width:50px;
	position:absolute;
	top: 73px;
		}
	</style>
	
<script language="javascript">
	
	function menu_magico(element){
		var links = document.getElementById(element);
		//var links = element;
		
		if(links.style.display == 'none'){
			links.style.display = 'inline';
		}else{
			links.style.display = 'none';
		}
	}
	</script>
</head>

<body>
<div id="menu-magico" onmouseover="menu_magico('menu-magico-links')" onmouseout="menu_magico('menu-magico-links')">
	<div id="menu-magico-links" style="display: none;">
		<a href="http://dotinfo.wordpress.com">.Info</a>
		<a href="http://dotlibrary.blogspot.com">.Library</a>
		<a href="http://codigofonte.uol.com.br">Código Fonte</a>
		<a href="http://www.vivaolinux.com.br">Viva o Linux</a>
	</div>
	<div id="menu-magico-button">
		<a href="javascript: menu_magico()">Menu</a>
	</div>
</div>
<p>&nbsp;</p>
<div id="teste1" onmouseover="menu_magico('subteste1')" onmouseout="menu_magico('subteste1')">Teste 1<div id="subteste1" style="display: none;"><table width="79" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td>Submenu 1</td>
  </tr>
  <tr>
    <td>Submenu 2</td>
  </tr>
  <tr>
    <td>Submenu 3</td>
  </tr>
</table></div></div>

<div id="teste2">Teste 2</div>
<p>&nbsp;</p>
<p>&nbsp;</p>

</body>
</html>
