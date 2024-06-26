
FROM node:14.17.1-alpine

WORKDIR /app


COPY package*.json ./


RUN npm install --silent


COPY . .


RUN npm run build


EXPOSE 80


CMD ["npm", "run", "start"]
