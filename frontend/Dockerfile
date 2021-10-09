FROM node:lts-alpine
WORKDIR /code/app
COPY app/package.json ./
RUN apk update && \
    apk upgrade && \
    apk --no-cache add curl bash && \
    rm -rf /var/cache/apk/*
RUN curl --compressed -o- -L https://yarnpkg.com/install.sh | bash
ENV PATH "$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
RUN npm cache clean --force && yarn install && yarn audit
ENV PATH "/code/app/node_modules/.bin:$PATH"

CMD ["/bin/sh", "-f", "entrypoint.sh"]
