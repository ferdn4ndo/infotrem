export default (cpf) => {
  if (typeof cpf !== "number") {
    return cpf;
  }

  let formattedCpf = String(cpf).padStart(11, "0");

  return formattedCpf.replace(/^(\d{3})(\d{3})(\d{3})(\d{2}).*/, "$1.$2.$3-$4");
};
