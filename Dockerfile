FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y git python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n titanic python=3.8

RUN git clone http://www.github.com/irtizak/titanic.git

RUN /bin/bash -c 'cd titanic \
    && source activate titanic \
    && pip install -r requirements.txt'

RUN streamlit run app/app.py
