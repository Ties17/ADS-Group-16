FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

HEALTHCHECK --interval=5m --timeout=3s CMD curl --fail http://nginx.host.com/ || exit 1