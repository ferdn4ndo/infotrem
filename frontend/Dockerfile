# build stage
FROM node:lts-alpine
WORKDIR /code
COPY app/package.json ./
RUN npm cache clean --force && npm install -g npm && npm install --save-dev --loglevel verbose
ENV PATH /code/node_modules/.bin:$PATH

WORKDIR /code/app/

EXPOSE 9906
CMD ["/bin/sh", "entrypoint.sh"]
