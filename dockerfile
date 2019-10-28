FROM python:3

RUN git clone https://github.com/PvonK/Sudoku
WORKDIR /Sudoku

RUN pip install -r requirements.txt
RUN pip install parameterized
