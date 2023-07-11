FROM python

WORKDIR https://github.com/Im-a-Degen/Nameless_Gardening_Game/tree/1633c030307430be113ebd1c1a31dd6b346e41bc

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "./main.py"]