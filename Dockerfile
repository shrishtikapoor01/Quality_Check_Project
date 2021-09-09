FROM ayush122001/keras-flask-jenkins:v2
COPY app.py /
COPY final.h5 /
RUN mkdir /templates
COPY templates/index.html  /templates/index.html
COPY templates/good.html  /templates/good.html
COPY templates/bad.html  /templates/bad.html
COPY templates/form.html  /templates/form.html
COPY templates/bad.jpg  /templates/bad.jpg
COPY templates/black.jpg  /templates/black.jpg
COPY templates/good.jpg  /templates/good.jpg
COPY templates/img.jpg  /templates/img.jpg
COPY templates/quality_final.jpg  /templates/quality_final.jpg
COPY templates/wine.jpg  /templates/wine.jpg
COPY templates/wine_lying.jpg  /templates/wine_lying.jpg
CMD ["python3","/app.py"]
