FROM node:14.15.0-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

RUN apk update && \
    npm install && \
    npm install -g npm && \
    npm install -g vue-cli

RUN yarn global add @vue/cli
RUN yarn global add @vue/cli-init