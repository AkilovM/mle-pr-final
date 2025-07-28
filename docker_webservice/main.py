from fastapi import FastAPI
from fast_api_handler import FastApiHandler

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# добавяем объект класса-обработчика
app.handler = FastApiHandler()
 
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
    return {"user_id": user_id, "predicted_products": user_prediction}