export default (phone) => {
  if (typeof phone !== "number") {
    return phone;
  }

  let formattedPhone = String(phone);

  if (formattedPhone.length <= 10) {
    formattedPhone = formattedPhone.padStart(10, "0");

    return formattedPhone.replace(/^(\d{2})(\d{4})(\d{4}).*/, "($1) $2-$3");
  }

  formattedPhone = formattedPhone.padStart(11, "0");

  return formattedPhone.replace(/^(\d{2})(\d{5})(\d{4}).*/, "($1) $2-$3");
};
