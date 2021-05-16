# tblFerroviaCarroTipo
#
# DESC:			Tabela de armazenamento dos tipos dos carros das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaCarroTipo;
CREATE TABLE tblFerroviaCarroTipo (
	CodFerroviaCarroTipo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraCarroTipo				VARCHAR(1)		NULL									COMMENT 'Letra do tipo de carro',
	NomeCarroTipo				VARCHAR(255)	NULL									COMMENT 'Nome do tipo de carro',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos dos carros das ferrovias';

INSERT INTO tblFerroviaCarroTipo (CodFerroviaCarroTipo, LetraCarroTipo, NomeCarroTipo, Ativo) VALUES
	(1, 'A', 'Administração', 1),
	(2, 'B', 'Bagagem e/ou Correio', 1),
	(3, 'D', 'Dormitório com cabines', 1),
	(4, 'E', 'Pulmann(com poltronas especiais)', 1),
	(5, 'F', 'Buffet (com poltronas e bar)', 1),
	(6, 'L', 'Poltronas - leito', 1),
	(7, 'P', 'Poltronas de primeira classe', 1),
	(8, 'Q', 'Qualquer / outros', 1),
	(9, 'R', 'Restaurante', 1),
	(10, 'S', 'Segunda classe', 1),
	(11, 'T', 'Classe turística', 1),
	(12, 'U', 'Suburbano', 1);