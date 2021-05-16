# tblFerroviaSIGORegional
#
# DESC:			Tabela de armazenamento das regionais SIGO do módulo de ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaSIGORegional;
CREATE TABLE tblFerroviaSIGORegional (
	CodFerroviaSigoRegional		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraSigoRegional 			VARCHAR(1)		NOT NULL								COMMENT 'Código da entidade',
	CodFerroviaEmpresa			INT(8)			NULL									COMMENT 'Código da empresa administradora da ferrovia (tblFerroviaEmpresa)',
	DescricaoSigoRegional		VARCHAR(255)	NULL									COMMENT 'Descrição da regional',
	SiglaSigoRegional			VARCHAR(25)		NULL									COMMENT 'Sigla da regional',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das regionais SIGO do módulo de ferrovias';

INSERT INTO `tblFerroviaSIGORegional` (`CodFerroviaSigoRegional`,`LetraSigoRegional`,`CodFerroviaEmpresa`,`DescricaoSigoRegional`,`SiglaSigoRegional`,`Ativo`) VALUES
	(1, 'A', 2, 'Superintendência Regional São Luiz', 'SR-12', 1),
	(2, 'B', 2, 'Superintendência Regional Fortaleza', 'SR-11', 1),
	(3, 'C', 2, 'Superintendência Regional Recife', 'SR-1', 1),
	(4, 'D', 2, 'Superintendência Regional Salvador', 'SR-7', 1),
	(5, 'E', 2, 'Superintendência Regional Belo Horizonte', 'SR-2', 1),
	(6, 'F', 2, 'Superintendência Regional Juiz de Fora', 'SR-3', 1),
	(7, 'G', 2, 'Superintendência Regional Campos', 'SR-8', 1),
	(8, 'H', 5, 'Superintendência de Trens Urbanos RJ' , 'STU-RJ', 1),
	(9, 'I', 2, 'Superintendência Regional São Paulo' , 'SR-4', 1),
	(0, 'J', 2, 'Superintendência Regional Bauru', 'SR-10', 1),
	(8, 'K', 5, 'Metropolitano do Recife', 'Metrorec', 1),
	(8, 'L', 2, 'Superintendência Regional Curitiba', 'SR-5', 1),
	(8, 'M', 2, 'Superintendência Regional Tubarão', 'SR-9', 1),
	(8, 'N', 2, 'Superintendência Regional Porto Alegre', 'SR-6', 1),
	(8, 'O', 5, 'Superintendência de Trens Urbanos SP', 'STU-SP', 1),
	(8, 'P', 2, 'Superintendência de Patrimônio - Preservação', 'Preserfe', 1),
	(8, 'Q', 5, 'Belo Horizonte', 'Demetrô', 1),
	(8, 'R', 9, 'Ferrocarriles Argentinos', 'FA', 1),
	(8, 'S', 5, 'Porto Alegre', 'Trensurb', 1),
	(8, 'T', NULL, '(Reservado para estudos. Não alocado)', NULL, 1),
	(8, 'U', 8, 'Administracion de los Ferrocarriles del Estado – Uruguai', 'AFE', 1),
	(8, 'V', 6, 'EF Vitória a Minas', 'EFVM', 1),
	(8, 'W', 5, 'Superintendência de Trens Urbanos Fortaleza', 'STU-FOR', 1),
	(8, 'X', 7, 'Empresa Nacional de Ferrocarriles – Bolívia', 'ENFE', 1),
	(8, 'Y', 5, 'Superintendência de Trens Urbanos Recife', 'STU-REC', 1),
	(8, 'Z', 1, 'Ferrovia Paulista S/A', 'FEPASA', 1);