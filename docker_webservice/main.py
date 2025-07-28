from fastapi import FastAPI
from fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
from prometheus_client import Counter

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# добавяем объект класса-обработчика
app.handler = FastApiHandler()

# main_app_predictions — объект метрики
main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    # описание метрики
    "Histogram of predictions",
    # указываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
) 

positive_predictions_counter = Counter(
    "positive_predictions_counter",
    "Counter of positive predictions"
)

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World",
            "info": "Это Веб-сервис для предсказания покупок продуктов банка.",
            "example": "http://ip:port/api/predict_products/657790"}

# обрабатываем запросы к специальному пути для получения предсказания модели
@app.get("/api/predict_products/{user_id}")
def get_prediction_for_item(user_id: str):
    all_params = {
        'user_id': user_id,
    }
    user_prediction = app.handler.handle(all_params)
    main_app_predictions.observe(1)
    if 1 in user_prediction.values:
        positive_predictions_counter.inc()
    return {"user_id": user_id, "predicted_products": user_prediction}