Яндекс Практикум, MLE, Спринт 6, Финальный проект.

Выбрал Кейс 1: Рекомендации банковских продуктов.

---

Скачиваем датасет:

```
mkdir dataset
cd dataset
wget https://getfile.dokpub.com/yandex/get/https://disk.yandex.com/d/Io0siOESo2RAaA
mv Io0siOESo2RAaA train_ver2.csv.zip
sudo apt install unzip
unzip train_ver2.csv.zip
cd ..
```

---

Настраиваем виртуальное окружение для Python:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

Проводим разведочный анализ данных в ноутбуке `Exploratory_Data_Analysis.ipynb`.

---

Развертывание MLFlow в скрипте `run_mlflow.sh`

TODO

---

Трансляция. Выберите метрики, на которые вы хотите повлиять, и решите, как будете решать задачу.



TODO

---

...