from fastapi import APIRouter


router = APIRouter()


@router.get("/{process_id}")
def get_process(process_id: str):
    '''Получение процесса по айди и отслеживание решения капчи'''

    return process_id


@router.post("/captcha")
def captcha_solution():
    '''Решение капчи и отправка ответа обратно'''

    return None