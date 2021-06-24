export default (currency) => {
  if (typeof currency !== "number") {
    return currency;
  }
  var formatter = new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
    minimumFractionDigits: 2,
  });
  return formatter.format(currency);
};
