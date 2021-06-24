# build stage
FROM node:lts-alpine
WORKDIR /code
COPY app/package.json ./
RUN npm cache clean --force && npm install -g npm && npm install --production=false
ENV PATH /code/node_modules/.bin:$PATH

WORKDIR /code/app

#RUN npm cache clean --force && npm install -g npm && npm install

EXPOSE 8080
CMD ["/bin/sh", "entrypoint.sh"]
