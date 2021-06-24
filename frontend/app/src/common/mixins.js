import { FETCH_USER } from "@/store/actions.type";
import store from "@/store";

export const RequireAdminMixin = {
  beforeRouteEnter(to, from, next) {
    store
      .dispatch(FETCH_USER)
      .then((user) => {
        if (user.is_admin) {
          next();
        } else {
          next({ name: "home" });
        }
      })
      .catch(() => {
        next({ name: "home" });
      });
  },
};
