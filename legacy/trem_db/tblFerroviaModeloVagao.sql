# tblFerroviaModeloVagao
#
# DESC:			Tabela de armazenamento dos modelos dos vagões das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaModeloVagao;
CREATE TABLE tblFerroviaModeloVagao (
	CodFerroviaModeloVagao		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	ModeloSigo					BOOLEAN			NOT NULL 	DEFAULT TRUE				COMMENT 'Se é um modelo SIGO ou não',
	NomeModelo					VARCHAR(20)		NULL									COMMENT 'Nome do modelo (se não for SIGO)',
	CodFerroviaBitola			INT(8)			NULL									COMMENT 'Código da bitola do vagão',
	CodFerroviaVagaoSubTipo 	INT(8)			NOT NULL								COMMENT 'Código do tipo com subtipo do vagão',
	CodFerroviaVagaoManga 		INT(8)			NOT NULL								COMMENT 'Código da manga do vagão',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos modelos dos vagões das ferrovias';
