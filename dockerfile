FROM python:3

RUN git clone https://github.com/PvonK/Sudoku
WORKDIR /Sudoku

RUN pip install -r requirements.txt

CMD [ "python3", "all_tests.py" ] && [ "python3", "Interfaz_Sudoku.py" ]
