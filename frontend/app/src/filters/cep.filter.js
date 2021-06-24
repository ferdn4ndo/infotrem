export default (cep) => {
  if (typeof cep !== "number") {
    return cep;
  }

  let formattedCep = String(cep).padStart(8, "0");

  return formattedCep.replace(/^(\d{2})(\d{3})(\d{3}).*/, "$1.$2-$3");
};
