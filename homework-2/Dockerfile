FROM python:3.10

WORKDIR /app

COPY main.py .

COPY artifacts/data/. .

RUN apt-get update

RUN apt-get -y install texlive-latex-base

RUN pip install -i https://test.pypi.org/simple/ pdflatexsotnikovarkadiy==0.1.2

RUN python3 main.py

RUN pdflatex artifacts/task2.tex -output-directory=artifacts
