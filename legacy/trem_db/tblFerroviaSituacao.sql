# tblFerroviaSituacao
#
# DESC:			Tabela de armazenamento das situações do módulo de ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaSituacao;
CREATE TABLE tblFerroviaSituacao (
	CodFerroviaSituacao			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeSituacao				VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de local',
	SiglaSituacao				VARCHAR(3)		NULL									COMMENT 'Sigla do tipo de local',
	ServeParaLocal				BOOLEAN 		NOT NULL	DEFAULT TRUE				COMMENT 'Se a situação serve para locais',
	ServeParaMatRod				BOOLEAN 		NOT NULL	DEFAULT TRUE				COMMENT 'Se a situação serve para materiais rodantes',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das situações do módulo de ferrovias';

INSERT INTO `tblFerroviaSituacao` (`CodFerroviaSituacao`, `ServeParaLocal`, `ServeParaMatRod`, `NomeSituacao`, `SiglaSituacao`, `Ativo`) VALUES
	(1, 1, 1, 'Ativo', 'A', 1),
	(2, 1, 1, 'Abandonado', 'O', 1),
	(3, 0, 1, 'Baixado', 'B', 1),
	(4, 0, 1, 'Cortado', 'C', 1),
	(5, 1, 0, 'Demolido', 'D', 1),
	(6, 1, 1, 'Transformado', 'T', 1);