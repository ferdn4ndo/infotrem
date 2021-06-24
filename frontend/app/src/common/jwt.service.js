const ID_TOKEN_KEY = "token_id";
const ID_TOKEN_EXP = "token_exp";

export const getToken = () => {
  return window.localStorage.getItem(ID_TOKEN_KEY);
};

export const getExp = () => {
  return window.localStorage.getItem(ID_TOKEN_EXP);
};

export const saveToken = (token) => {
  window.localStorage.setItem(ID_TOKEN_KEY, token);
};

export const saveExp = (exp) => {
  window.localStorage.setItem(ID_TOKEN_EXP, exp);
};

export const destroyToken = () => {
  window.localStorage.removeItem(ID_TOKEN_KEY);
  window.localStorage.removeItem(ID_TOKEN_EXP);
};

export default { getToken, getExp, saveToken, saveExp, destroyToken };
