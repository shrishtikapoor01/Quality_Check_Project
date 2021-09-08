FROM ayush122001/keras-flask-jenkins:v2
COPY app.py /
COPY final.h5 /
RUN mkdir /templates
COPY templates/index.html  /templates/index.html
COPY templates/good.html  /templates/good.html
COPY templates/bad.html  /templates/bad.html
COPY templates/form.html  /templates/form.html
CMD ["python3","/app.py"]
