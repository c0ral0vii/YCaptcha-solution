import base64
import json
import urllib

from PIL import Image
from io import BytesIO
from fastapi import APIRouter


router = APIRouter()


@router.get("/{process_id}")
def get_process(process_id: str):
    '''Получение процесса по айди и отслеживание решения капчи'''

    return process_id


@router.post("/captcha")
def captcha_solution(body: str, imginstructions: str, format: str = 'base64', json: int = 0):
    '''Решение капчи и отправка ответа обратно
        body - Изображение, закодированное в формат base64 или ссылка url. Содержит картинку для распознавания объектов на изображении.
        imginstructions - Изображение, закодированное в формат base64. Содержит картинку с последовательностью объектов.
        format - Актуально для параметра body.
            base64 — сервер будет принимать изображение в формате base64.
            url — сервер будет принимать изображение в формате прямой ссылки, взятой из тега <img src="...">. Не рекомендуется использовать данный метод, потому что будет повторный запрос с IP нашего сервера на скачивание картинки, что является подозрительной операцие
        json - 0 — сервер вернёт ответ в виде простого текста.
            1 — сервер вернёт ответ в формате JSON.
            Рекомендуется ставить 1.
    '''

    imageinstruction = base64.b64decode(imginstructions)

    if format != 'base64':
        image = base64.b64decode(imginstructions)


    return None