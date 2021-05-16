# tblFerroviaModelo
#
# DESC:			Tabela de armazenamento dos modelos de material rodante das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaModelo;
CREATE TABLE tblFerroviaModelo (
	CodFerroviaModelo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	CodFerroviaRodanteTipo		INT(8)			NOT NULL								COMMENT 'Tipo de material rodante',
	ModeloSigo					BOOLEAN			NOT NULL 	DEFAULT TRUE				COMMENT 'Se é um modelo SIGO ou não',
	NomeModelo					VARCHAR(20)		NULL									COMMENT 'Nome do modelo p/ locomotiva (e vagão/carro/tue se não for SIGO)',
	CodFerroviaFabricante		INT(8)			NULL									COMMENT 'Código do fabricante do modelo',
	CodFerroviaBitola			INT(8)			NULL									COMMENT 'Código da bitola do material rodante',

	CodTracaoClassificacao		INT(8)			NULL									COMMENT '[LOCO] Código da classificação dos truques',
	CodFerroviaTracao			INT(8)			NULL									COMMENT '[LOCO] Código do tipo de tração da locomotiva',
	
	CodFerroviaVagaoSubTipo 	INT(8)			NULL									COMMENT '[VAGÃO] Código do tipo com subtipo do vagão',
	CodFerroviaVagaoManga 		INT(8)			NULL									COMMENT '[VAGÃO] Código da manga do vagão',


	CodFerroviaAutoTipo			INT(8)			NULL									COMMENT '[AUTO] Código do tipo de auto de linha',

	CodFerroviaCarroMaterial	INT(8)			NULL									COMMENT '[CARRO] Código do material do carro',
	CodFerroviaCarroTipo		INT(8)			NULL									COMMENT '[CARRO] Código do tipo do carro',

	CodFerroviaTremUniTipo		INT(8)			NULL									COMMENT '[TUE] Código do tipo de trem unidade',

	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos modelos dos vagões das ferrovias';
