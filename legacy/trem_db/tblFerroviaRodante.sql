# tblFerroviaRodante
#
# DESC:			Tabela de armazenamento do material rodante das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaRodante;
CREATE TABLE tblFerroviaRodante (
	CodFerroviaRodante			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	CodFerroviaModelo			INT(8)			NOT NULL								COMMENT 'Código do modelo',
	
	CodFerroviaFabricante		INT(8)			NULL									COMMENT 'Código do fabricante do modelo',
	CodFerroviaBitola			INT(8)			NULL									COMMENT 'Código da bitola do material rodante',
	


	NumeroSerieOriginal
	AnoFabricacao
	ModeloSigo					BOOLEAN			NOT NULL 	DEFAULT TRUE				COMMENT 'Se é um modelo SIGO ou não',
	NumeroModelo				INT(6)			NOT NULL								COMMENT 'Número do modelo',

	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento do material rodante das ferrovias';
