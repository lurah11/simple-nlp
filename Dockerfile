FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt -y update && apt -y upgrade
COPY ./requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt
COPY ./main.py ./main.py
# RUN python main.py 
EXPOSE 8000
COPY ./script.sh ./script.sh
CMD ["./script.sh"]