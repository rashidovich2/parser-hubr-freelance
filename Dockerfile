FROM python
WORKDIR /usr/src/parser/
COPY . ./
EXPOSE 80
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]