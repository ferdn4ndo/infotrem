# tblFerroviaFabricante
#
# DESC:			Tabela de armazenamento dos fabricantes de material rodante
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaFabricante;
CREATE TABLE tblFerroviaFabricante (
	CodFerroviaFabricante		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeFerroviaFabricante		VARCHAR(255)	NOT NULL								COMMENT 'Nome do fabricante',
	SiglaFerroviaFabricante		VARCHAR(255)	NOT NULL								COMMENT 'Sigla do fabricante',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos fabricantes de material rodante';
INSERT INTO `tblFerroviaFabricante` (`CodFerroviaFabricante`, `NomeFerroviaFabricante`, `SiglaFerroviaFabricante`, `Ativo`) VALUES
	(1, 'General Eletric', 'GE', 1),
	(2, 'General Motors', 'GM', 1),
	(3, 'American Locomotive Company', 'ALCO', 1);