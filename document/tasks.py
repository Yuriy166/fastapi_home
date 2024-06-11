from celery import Celery
import pytesseract
from PIL import Image
from document.models import session, DocumentsORM, Documents_textORM
from config import REDIS_HOST, REDIS_PORT


celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}') # broker=f'{BROKER_URL}/'


@celery.task
def doc_analyse(file_id: int):
    with session:
        query = session.get(DocumentsORM, file_id)
        name_file = query.psth
        img = Image.open(f'doc/{name_file}')
        text_doc = pytesseract.image_to_string(img)
        doc_text = Documents_textORM(id_doc=file_id, text=text_doc)
        session.add(doc_text)
        session.commit()
        return f'{file_id} обработана'
