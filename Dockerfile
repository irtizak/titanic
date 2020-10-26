FROM ubuntu:18.04

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y wget git

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    mkdir root/.conda && \
    sh Miniconda3-latest-Linux-x86_64.sh -b && \
    rm -f Miniconda3-latest-Linux-x86_64.sh

RUN git clone http://www.github.com/irtizak/titanic && \
    conda create --name titanic --file titanic/requirements1.txt && \
    conda install flask -y && \
    pip install flask_restful numpy joblib

RUN conda init bash

RUN /bin/bash -c "source activate titanic"

CMD python titanic/ml_api/api/app.py
