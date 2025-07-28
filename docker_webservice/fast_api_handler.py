"""Класс FastApiHandler, который обрабатывает запросы API."""
#from sklearn.linear_model import LogisticRegression
#from sklearn.multioutput import MultiOutputClassifier
import pickle

class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        # self.param_types = {
        #     "client_id": str,
        #     "model_params": dict
        # }

        self.model_path = "./model_baseline_LogReg.pkl"
        self.prod_obj_path = "./prod_obj.pkl"
        self.load_model(model_path=self.model_path)
        self.load_prod_obj(prod_obj_path=self.prod_obj_path)

    def load_model(self, model_path: str):
        """Загружаем обученную модель предсказания покупки банковских продуктов.
        
            Args:
            model_path (str): Путь до модели.
        """
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        except Exception as e:
            print(f"Failed to load model: {e}")
    
    def load_prod_obj(self, prod_obj_path: str):
        """Загружаем словарь, который содержит информацию о признаках, продуктах, переводы на русский.
        
            Args:
            model_path (str): Путь до prod_obj.
        """
        try:
            with open(prod_obj_path, 'rb') as f:
                self.prod_obj = pickle.load(f)
        except Exception as e:
            print(f"Failed to load prod_obj: {e}")

    def predict_products(self, user_id: int) -> float:
        """Предсказываем продукты для клиента.

        Args:
            user_id (int): id клиента банка.

        Returns:
            dict — предсказанные продукты.
        """
        self.prod_obj['products_spanish_to_ru_dict']
        self.prod_obj['user_id_order']
        self.prod_obj['products']
        self.prod_obj['features']

        user_index = self.prod_obj['user_id_order'].index(user_id)
        features = self.prod_obj['features'][user_index].reshape(1, -1)
        predicted_values = self.model.predict(features)[0]

        if len(predicted_values) != len(self.prod_obj['products']):
            raise Exception('Unexpected amount of targets!')
        
        predicted_products = dict()
        for i in range(len(self.prod_obj['products'])):
            product_prediction = predicted_values[i]
            spain_product_name = self.prod_obj['products'][i]
            russian_product_name = self.prod_obj['products_spanish_to_ru_dict'][spain_product_name]
            predicted_products[russian_product_name] = product_prediction
        return predicted_products

    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора.
        
                Args:
                    params (dict): Параметры запроса.
                
                Returns:
                    bool: True — если есть нужные параметры, False — иначе
                """
        if "user_id" not in query_params:
            return False
        if not isinstance(query_params["user_id"], str):
            return False
        return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры пользователя на наличие обязательного набора.
        Args:
            model_params (dict): Параметры пользователя для предсказания.
        Returns:
            bool: True — если есть нужные параметры, False — иначе
        """
        pass
    
    def validate_params(self, params: dict) -> bool:
        """Проверяем корректность параметров запроса и параметров модели.

        Args:
            params (dict): Словарь параметров запроса.

        Returns:
             bool: True — если проверки пройдены, False — иначе
        """
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        # if self.check_required_model_params(params["model_params"]):
        #     print("All model params exist")
        # else:
        #     print("Not all model params exist")
        #     return False
        return True

    def handle(self, params):
        """Функция для обработки запросов API.

        Args:
            params (dict): Словарь параметров запроса.

        Returns:
            dict: Словарь, содержащий результат выполнения запроса.
        """
        try:
            # валидируем запрос к API
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                user_id = params["user_id"]
                print(f"Predicting for user_id: {user_id}")
                # получаем предсказания модели
                predicted_products = self.predict_products(int(user_id))
                response = predicted_products
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response 