FROM python:alpine3.7
RUN mkdir /site
COPY . /site
WORKDIR /site
ENV USERNAME="Hello World" 
ENV PASSWORD="Python Simple Static Website"
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "serve.py" ]