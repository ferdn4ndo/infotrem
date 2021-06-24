import moment from "moment";

const IN_DEV_MODE = process.env.ENV_MODE === "dev";

const LoggerService = {
  init() {
    // ToDo: check if may save somewhere
  },

  write(message, level= "info", stdOut = true) {
    const time = moment().format("YYYY-MM-DD hh:mm:ss");
    const formattedMessage = `[${time}] ${level.toUpperCase()} - ${message}`;

    if (stdOut) {
      console.log(formattedMessage);
    }

    return formattedMessage;
  },

  error(message) {
    return this.write(message, "error", true);
  },

  warning(message) {
    return this.write(message, "warning", true);
  },

  info(message) {
    return this.write(message, "info", IN_DEV_MODE);
  },

  debug(message) {
    return this.write(message, "debug", IN_DEV_MODE);
  },
};

export default LoggerService;
