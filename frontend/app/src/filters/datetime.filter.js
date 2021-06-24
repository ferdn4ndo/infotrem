import moment from "moment";

export default (datetime) => {
  return moment(datetime).format("DD/MM/YY hh:mm:ss");
};
