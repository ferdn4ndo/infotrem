# tblFerroviaBitola
#
# DESC:			Tabela de armazenamento das bitolas das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaBitola;
CREATE TABLE tblFerroviaBitola (
	CodFerroviaBitola			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeFerroviaBitola 			VARCHAR(255)	NOT NULL								COMMENT 'Nome da bitola',
	DistanciaBitolaMM			INT(4)			NULL									COMMENT 'Distância da bitola',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das bitolas das ferrovias';

INSERT INTO tblFerroviaBitola (CodFerroviaBitola, NomeFerroviaBitola, DistanciaBitolaMM, Ativo) VALUES
	(1, 'Métrica', 1000, 1),
	(2, 'Larga', 1000, 1),
	(3, 'Standart', 1435, 1),
	(4, 'Bitolinha', 600, 1),
	(5, '76 cm', 760, 1);

