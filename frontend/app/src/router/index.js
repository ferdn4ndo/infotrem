import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/Home"),
    meta: {
      title: "CSC Consultoria",
      metaTags: [
        {
          name: "description",
          content: "Página inicial da CSC Consultoria, Assessoria e Gestão.",
        },
        {
          property: "og:description",
          content: "Página inicial da CSC Consultoria, Assessoria e Gestão.",
        },
      ],
    },
  },
  // Handle child routes with a default, by giving the name to the
  // child.
  // SO: https://github.com/vuejs/vue-router/issues/777
  {
    path: "/perfil",
    component: () => import("@/views/Profile"),
    children: [
      {
        path: "",
        name: "profile",
        component: () => import("@/views/ProfileData"),
      },
      {
        name: "profile-registrations",
        path: "registrations",
        component: () => import("@/views/ProfileRegistrations"),
      },
    ],
  },
  {
    name: "events",
    path: "/eventos",
    component: () => import("@/views/EventsList"),
  },
  {
    name: "events-public-tenders",
    path: "/concursos",
    component: () => import("@/views/EventsPublicTender"),
    meta: {
      title: "Concursos Públicos - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "Concursos públicos com inscrições abertas, em andamento e finalizados da CSC Consultoria, Assessoria e Gestão.",
        },
        {
          property: "og:description",
          content:
            "Concursos públicos com inscrições abertas, em andamento e finalizados da CSC Consultoria, Assessoria e Gestão.",
        },
      ],
    },
  },
  {
    name: "events-selection-process",
    path: "/processos-seletivos",
    component: () => import("@/views/EventsSelectionProcess"),
    meta: {
      title: "Processos Seletivos - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "Processos seletivos com inscrições abertas, em andamento e finalizados da CSC Consultoria, Assessoria e Gestão.",
        },
        {
          property: "og:description",
          content:
            "Processos seletivos com inscrições abertas, em andamento e finalizados da CSC Consultoria, Assessoria e Gestão.",
        },
      ],
    },
  },
  {
    name: "event",
    path: "/eventos/:event_id",
    component: () => import("@/views/Event"),
  },
  {
    name: "services",
    path: "/servicos",
    component: () => import("@/views/Services"),
    meta: {
      title: "Serviços - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "A CSC oferece consultoria e assessoria em concursos públicos, processos seletivos e capacitações, além de promover a realizaçãode cursos. Saiba mais.",
        },
        {
          property: "og:description",
          content:
            "A CSC oferece consultoria e assessoria em concursos públicos, processos seletivos e capacitações, além de promover a realizaçãode cursos. Saiba mais.",
        },
      ],
    },
  },
  {
    name: "subscriptions",
    path: "/inscricoes",
    component: () => import("@/views/Subscriptions"),
    meta: {
      title: "Minhas Inscrições - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "A CSC oferece consultoria e assessoria em concursos públicos, processos seletivos e capacitações, além de promover a realizaçãode cursos. Saiba mais.",
        },
        {
          property: "og:description",
          content:
            "A CSC oferece consultoria e assessoria em concursos públicos, processos seletivos e capacitações, além de promover a realizaçãode cursos. Saiba mais.",
        },
      ],
    },
  },
  {
    name: "company",
    path: "/a-empresa",
    component: () => import("@/views/Company"),
    meta: {
      title: "A Empresa - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "Saiba mais sobre nós: quem somos, nossa missão, nossa visão, nossos valores, área de atuação. Também conheça alguns de nossos clientes e parceiros.",
        },
        {
          property: "og:description",
          content:
            "Saiba mais sobre nós: quem somos, nossa missão, nossa visão, nossos valores, área de atuação. Também conheça alguns de nossos clientes e parceiros.",
        },
      ],
    },
  },
  {
    name: "privacy-policy",
    path: "/politica-de-privacidade",
    component: () => import("@/views/PrivacyPolicy"),
    meta: {
      title: "Política de Privacidade - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "Leia nossa política de privacidade e uso de dados pessoais.",
        },
        {
          property: "og:description",
          content:
            "Leia nossa política de privacidade e uso de dados pessoais.",
        },
      ],
    },
  },
  {
    name: "contact",
    path: "/contato",
    component: () => import("@/views/Contact"),
    meta: {
      title: "Contato - CSC",
      metaTags: [
        {
          name: "description",
          content:
            "Entre em contato conosco através deste formulário. Retornaremos em breve!",
        },
        {
          property: "og:description",
          content:
            "Entre em contato conosco através deste formulário. Retornaremos em breve!",
        },
      ],
    },
  },
  {
    name: "email-validation",
    path: "/validate-email/:user_id/:validation_hash",
    component: () => import("@/views/EmailValidation"),
  },
  {
    name: "admin-home",
    path: "/administrador",
    component: () => import("@/views/AdminHome"),
  },
  {
    name: "admin-event-create",
    path: "/administrador/novo-evento",
    component: () => import("@/views/AdminEventCreate"),
  },
  {
    name: "admin-event-detail",
    path: "/administrador/editar-evento/:event_id",
    component: () => import("@/views/AdminEventDetail"),
  },
  {
    name: "admin-event-files",
    path: "/administrador/editar-evento/:event_id/arquivos",
    component: () => import("@/views/AdminEventFiles"),
  },
  {
    name: "admin-event-links",
    path: "/administrador/editar-evento/:event_id/links",
    component: () => import("@/views/AdminEventLinks"),
  },
  {
    name: "admin-event-subscriptions",
    path: "/administrador/editar-evento/:event_id/inscricoes",
    component: () => import("@/views/AdminEventSubscriptions"),
  },
  {
    name: "admin-event-list",
    path: "/administrador/listar-eventos",
    component: () => import("@/views/AdminEventList"),
  },
  {
    name: "404",
    path: "*",
    component: () => import("@/views/404"),
    meta: {
      title: "Página Não Encontrada - CSC",
      metaTags: [
        {
          name: "description",
          content: "A página que você está procurando não foi encontrada.",
        },
        {
          property: "og:description",
          content: "A página que você está procurando não foi encontrada.",
        },
      ],
    },
  },
];

const router = new VueRouter({
  routes: routes,
  mode: "history",
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
});

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  document.title = nearestWithTitle
    ? nearestWithTitle.meta.title
    : "CSC Consultoria";

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(
    document.querySelectorAll("[data-vue-router-controlled]")
  ).map((el) => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if (!nearestWithMeta) {
    return next();
  }

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags
    .map((tagDef) => {
      const tag = document.createElement("meta");

      Object.keys(tagDef).forEach((key) => {
        tag.setAttribute(key, tagDef[key]);
      });

      // We use this to track which meta tags we create, so we don't interfere with other ones.
      tag.setAttribute("data-vue-router-controlled", "");

      return tag;
    })
    // Add the meta tags to the document head.
    .forEach((tag) => document.head.appendChild(tag));

  next();
});

export default router;
