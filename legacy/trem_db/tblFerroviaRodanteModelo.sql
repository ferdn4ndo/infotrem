tblFerroviaRodanteModelo


CodFerroviaRodanteTipo
ModeloSigo


CodFerroviaVagaoSubTipo
CodFerroviaVagaoManga


# tblFerroviaRodanteModelo
#
# DESC:			Tabela de armazenamento dos subtipos dos vagões das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaRodanteModelo;
CREATE TABLE tblFerroviaRodanteModelo (
	CodFerroviaRodanteModelo	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	CodFerroviaRodanteTipo		INT(8)			NOT NULL								COMMENT 'Tipo de material rodante',
	ModeloSigo					BOOLEAN			NOT NULL 	DEFAULT TRUE				COMMENT 'Se é um modelo SIGO ou não',
	NomeModelo					

	CodFerroviaVagaoTipo 		INT(8)			NOT NULL								COMMENT 'Código do tipo que origina o subtipo',
	LetraVagaoSubTipo			VARCHAR(2)		NULL									COMMENT 'Conjunto de duas letras que formam o subtipo',
	DescricaoSubTipo			VARCHAR(255)	NULL									COMMENT 'Descrição do subtipo de vagão',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos dos vagões das ferrovias';
