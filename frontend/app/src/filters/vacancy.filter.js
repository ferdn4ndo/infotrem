export default (vacancy) => {
  if (vacancy === 0) {
    return "Cadastro Reserva";
  }

  return vacancy.toString();
};
