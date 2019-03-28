FROM python:3.7-alpine
WORKDIR /app
COPY *.py ./
COPY run.sh ./

RUN apk --no-cache add dnsmasq && pip install requests

EXPOSE 53 53/udp
CMD ["./run.sh"]
