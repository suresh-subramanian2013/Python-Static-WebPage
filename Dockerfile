FROM python:alpine3.7
RUN mkdir /site
COPY . /site
WORKDIR /site
ENV ATC_USERNAME="hello" 
ENV ATC_PASSWORD="world"
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "serve.py" ]