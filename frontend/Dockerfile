FROM node:14.11-buster-slim

RUN apt-get update

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY ./ /app/

ARG FRONTEND_ENV=production

ENV VUE_APP_ENV=${FRONTEND_ENV}

RUN npm ci
RUN npm run build

ENV HOST 0.0.0.0
ENV PORT 80
