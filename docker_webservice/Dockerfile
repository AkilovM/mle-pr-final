FROM python:3.11-slim
# возьмём образ, который мы скачали ранее и в котором уже установлен Python

LABEL author="mle-student"
# инструкция LABEL задаёт метаданные для контейнера
# можно указать своё имя

COPY . ./my_super_dir
# инструкция COPY копирует содержимое текущей директории в директорию, 
# которую указали второй командой - в данном случае это my_super_dir
# если такой директории не было, docker её создаст

COPY ./prod_obj.pkl ./my_super_dir
COPY ./model_baseline_LogReg.pkl ./my_super_dir

WORKDIR my_super_dir
# изменяем рабочую директорию Docker 
# эта команда похожа на инструкцию RUN ["cd", "./my_super_dir"]
# в документации Docker рекомендуется использовать именно WORKDIR

RUN pip3 install -r requirements.txt

EXPOSE ${APP_PORT}

# эта инструкция указывает ту команду, которая должна выполниться при старте контейнера
CMD uvicorn main:app --host  0.0.0.0 --port ${APP_PORT}