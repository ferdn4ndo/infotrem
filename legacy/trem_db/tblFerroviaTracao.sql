# tblFerroviaTracao
#
# DESC:			Tabela de armazenamento dos tipos dos tração das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaTracao;
CREATE TABLE tblFerroviaTracao (
	CodFerroviaTracao			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraFerroviaTracao			VARCHAR(1)		NULL									COMMENT 'Letra do tipo de carro',
	NomeFerroviaTracao			VARCHAR(255)	NULL									COMMENT 'Nome do tipo de carro',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos dos tração das ferrovias';

INSERT INTO tblFerroviaTracao (CodFerroviaTracao, LetraFerroviaTracao, NomeFerroviaTracao, Ativo) VALUES
	(1, 'V', 'Vapor', 1),
	(2, 'D', 'Diesel-elétrica', 1),
	(3, 'E', 'Elétrica', 1),
	(4, 'H', 'Diesel-hidráulica', 1);