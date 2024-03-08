
import re
from rest_framework.serializers import ValidationError


class VideoValidator:
    """
    Валидатор для загрузки ссылок на видео
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if 'https://www.youtube.com/' not in tmp_val:
            raise ValidationError('Ссылки могут быть размещены только на платформу YouTube.')