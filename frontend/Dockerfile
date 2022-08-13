FROM node:lts-alpine

WORKDIR /code/

COPY package.json ./
COPY package-lock.json ./

RUN apk update && \
    apk upgrade && \
    apk --no-cache add curl bash git openssh && \
    rm -rf /var/cache/apk/*

#ENV PATH "$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

RUN npm cache clean --force && npm install
## && npm audit fix --force

ENV PATH "/code/node_modules/.bin:$PATH"

COPY entrypoint.sh ./

WORKDIR /code/app

CMD ["/bin/sh", "-f", "/code/entrypoint.sh"]
