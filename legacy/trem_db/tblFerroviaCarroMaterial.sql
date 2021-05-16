# tblFerroviaCarroMaterial
#
# DESC:			Tabela de armazenamento dos materiais dos carros das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaCarroMaterial;
CREATE TABLE tblFerroviaCarroMaterial (
	CodFerroviaCarroMaterial	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraCarroMaterial			VARCHAR(1)		NULL									COMMENT 'Letra do material do carro',
	NomeCarroMaterial			VARCHAR(255)	NULL									COMMENT 'Nome do material do carro',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos materiais dos carros das ferrovias';

INSERT INTO tblFerroviaCarroMaterial (CodFerroviaCarroMaterial, LetraCarroMaterial, NomeCarroMaterial, Ativo) VALUES
	(1, 'A', 'Alumínio'),
	(2, 'C', 'Aço carbono'),
	(3, 'D', 'Aço carbono e Madeira'),
	(4, 'E', 'Aço carbono e Inoxidável'),
	(5, 'I', 'Aço Inoxidável'),
	(6, 'L', 'Aço carbono e Alumínio'),
	(7, 'M', 'Madeira'),
	(8, 'Q', 'Qualquer / outros');