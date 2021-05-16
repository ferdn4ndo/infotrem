# tblFerroviaModeloLocomotiva
#
# DESC:			Tabela de armazenamento dos modelos das locomotivas das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaModeloLocomotiva;
CREATE TABLE tblFerroviaModeloLocomotiva (
	CodFerroviaModeloLocomotiva	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeModelo					VARCHAR(20)		NULL									COMMENT 'Nome do modelo',
	CodFerroviaBitola			INT(8)			NULL									COMMENT 'Código da bitola da locomotiva',
	CodFerroviaClassificacao	INT(8)			NULL									COMMENT 'Código da classificação dos truques',
	CodFerroviaFabricante		INT(8)			NULL									COMMENT 'Código do fabricante da locomotiva',
	CodFerroviaTracao			INT(8)			NULL									COMMENT 'Código do tipo de tração da locomotiva',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos modelos das locomotivas das ferrovias';
