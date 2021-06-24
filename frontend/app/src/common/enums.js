export const RELATIONAL_STATUS_OPTIONS = [
  {
    text: "Solteiro(a)",
    value: "SINGLE",
  },
  {
    text: "União Estável",
    value: "STABLE_UNION",
  },
  {
    text: "Casado(a)",
    value: "MARRIED",
  },
  {
    text: "Divorciado(a)",
    value: "DIVORCED",
  },
  {
    text: "Viúvo(a)",
    value: "WIDOWED",
  },
];

export const SKIN_COLOUR_OPTIONS = [
  {
    text: "Caucasiano(a)",
    value: "WHITE",
  },
  {
    text: "Negro(a)",
    value: "BLACK",
  },
  {
    text: "Oriental",
    value: "YELLOW",
  },
  {
    text: "Pardo(a)",
    value: "BROWN",
  },
  {
    text: "Indígena",
    value: "INDIGENOUS",
  },
  {
    text: "Não declarado",
    value: "NOT_DECLARED",
  },
];

export const EDUCATION_LEVEL_OPTIONS = [
  {
    text: "Analfabeto(a)",
    value: "NONE",
  },
  {
    text: "Educação Infantil (1º ao 5º ano)",
    value: "INFANT_SCHOOL",
  },
  {
    text: "Educação Básica (6º ao 9º ano)",
    value: "JUNIOR_SCHOOL",
  },
  {
    text: "Ensino Médico",
    value: "HIGH_SCHOOL",
  },
  {
    text: "Escola Técnica",
    value: "TECHNICAL_SCHOOL",
  },
  {
    text: "Graduado(a)",
    value: "GRADUATION",
  },
  {
    text: "Especialista",
    value: "SPECIALIST",
  },
  {
    text: "Mestre",
    value: "MASTER",
  },
  {
    text: "Doutor(a)",
    value: "DOCTOR",
  },
  {
    text: "Pós-Doutor(a)",
    value: "POST_DOCTOR",
  },
];

export const HABITATION_LEVEL_OPTIONS = [
  {
    text: "Moro em casa ou apartamento, sozinho",
    value: "ALONE",
  },
  {
    text: "Moro em casa ou apartamento, com pais e/ou parentes",
    value: "PARENTS_RELATIVES",
  },
  {
    text: "Moro em casa ou apartamento, com cônjuge e/ou filhos",
    value: "PARTNER_CHILDREN",
  },
  {
    text:
      "Moro em casa ou apartamento, com outras pessoas (incluindo república)",
    value: "OTHER_PEOPLE",
  },
  {
    text: "Moro em um alojamento (público ou privado)",
    value: "ACCOMMODATION",
  },
  {
    text:
      "Moro em outros tipos de habitação individual ou coletiva (hotel, hospedaria, pensão ou outro)",
    value: "OTHER",
  },
];

export const FAMILY_INCOME_LEVEL_OPTIONS = [
  {
    text: "Até 1,5 salário mínimo (até R$ 1.497,00)",
    value: "UP_TO_ONE_AND_A_HALF",
  },
  {
    text: "De 1,5 a 3 salários mínimos (R$ 1.497,01 a R$ 2.994,00)",
    value: "FROM_ONE_AND_A_HALF_TO_THREE",
  },
  {
    text: "De 3 a 4,5 salários mínimos (R$ 2.994,01 a R$ 4.491,00)",
    value: "FROM_THREE_TO_FOUR_AND_A_HALF",
  },
  {
    text: "De 4,5 a 6 salários mínimos (R$ 4.491,01 a R$ 5.988,00)",
    value: "FROM_FOUR_AND_A_HALF_TO_SIX",
  },
  {
    text: "De 6 a 10 salários mínimos (R$ 5. 988,01 a R$ 9.980,00)",
    value: "FROM_SIX_TO_TEN",
  },
  {
    text: "De 10 a 30 salários mínimos (R$ 9.980,01 a R$ 29.940,00)",
    value: "FROM_TO_TEN_TO_THIRTY",
  },
  {
    text: "Acima de 30 salários mínimos (mais de R$ 29.940,00)",
    value: "ABOVE_THIRTY",
  },
];

export const FINANCIAL_STATUS_OPTIONS = [
  {
    text:
      "Não tenho renda e meus gastos são financiados por programas governamentais",
    value: "NO_INCOME_GOVERNMENT",
  },
  {
    text:
      "Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas",
    value: "NO_INCOME_FAMILY",
  },
  {
    text:
      "Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos",
    value: "INCOME_AND_FAMILY",
  },
  {
    text: "Tenho renda e não preciso de ajuda para financiar meus gastos",
    value: "INCOME_ONLY",
  },
  {
    text: "Tenho renda e contribuo com o sustento da família",
    value: "INCOME_AND_HELP_OTHERS",
  },
  {
    text: "Sou o principal responsável pelo sustento da família",
    value: "MAIN_INCOME",
  },
];

export const JOB_STATUS_OPTIONS = [
  {
    text: "Não estou trabalhando",
    value: "NOT_WORKING",
  },
  {
    text: "Trabalho eventualmente",
    value: "WORKING_EVENTUALLY",
  },
  {
    text: "Trabalho até 20 horas semanais",
    value: "WORKING_UP_TO_20_HOURS",
  },
  {
    text: "Trabalho de 21 a 39 horas semanais",
    value: "WORKING_FROM_21_TO_39_HOURS",
  },
  {
    text: "Trabalho 40 horas semanais ou mais",
    value: "WORKING_40_HOURS_OR_MORE",
  },
];

export const EVENT_TYPE_OPTIONS = [
  {
    text: "Concurso Público",
    value: "PUBLIC_TENDER",
  },
  {
    text: "Processo Seletivo",
    value: "SELECTION_PROCESS",
  },
];

export const EVENT_FILE_VISIBILITY_OPTIONS = [
  {
    text: "Todos (e o arquivo é listado no evento)",
    value: "EVERYONE",
  },
  {
    text: "Somente inscritos (e o arquivo só é visível para eles)",
    value: "SUBSCRIBED",
  },
  {
    text: "Não listado (o arquivo só é acessível com o link direto gerado no administrador)",
    value: "UNLISTED",
  },
];

export const EVENT_LINK_VISIBILITY_OPTIONS = [
  {
    text: "Todos (e o link é listado no evento)",
    value: "EVERYONE",
  },
  {
    text: "Somente inscritos (e o link só é visível para eles)",
    value: "SUBSCRIBED",
  },
  {
    text: "Não listado (o link só é visível por administradores)",
    value: "UNLISTED",
  },
];

export const EVENT_FILE_CATEGORY_OPTIONS = [
  {
    text: "Editoriais e documentos oficiais",
    value: "EDITORIAL",
  },
  {
    text: "Material de apoio",
    value: "STUDY",
  },
];
