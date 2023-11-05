# Use an official Node.js runtime as the base image
FROM node:18

WORKDIR /app

COPY package.json ./

RUN npm install -g vite
RUN npm install
COPY . .


CMD [ "npm", "run", "dev" ]