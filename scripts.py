from datacenter.models import *
import random
from django.core.exceptions import ObjectDoesNotExist,  MultipleObjectsReturned


def fix_marks(child):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
        Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
    except ObjectDoesNotExist:
        print("Школьник с таким именем отсутствует.")
    except MultipleObjectsReturned:
        print("С таким именем есть несколько школьников.")


def remove_chastisements(child):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
        Chastisement.objects.filter(schoolkid=schoolkid).delete()
    except ObjectDoesNotExist:
        print("Школьник с таким именем отсутствует.")
    except MultipleObjectsReturned:
        print("С таким именем есть несколько школьников.")


def create_commendation(child, subject):
    try:
        lessons = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title=subject)
        lesson = lessons.order_by('-date').first()
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
        commendation_text = random.choice(['Молодец!', 'Отлично!', 'Гораздо лучше, чем я ожидал!', 'Хорошо!',
                                           'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
                                           'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                                           'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
                                           'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!',
                                           'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
                                           'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
                                           'Это как раз то, что нужно!', 'Я тобой горжусь!',
                                           'С каждым разом у тебя получается всё лучше!',
                                           'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
                                           'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
                                           'Теперь у тебя точно все получится!'])
        Commendation.objects.create(text=commendation_text, created=lesson.date, schoolkid=schoolkid,
                                    subject=lesson.subject, teacher=lesson.teacher)
    except ObjectDoesNotExist:
        print("Школьник с таким именем отсутствует.")
    except MultipleObjectsReturned:
        print("С таким именем есть несколько школьников.")


fix_marks('Фролов Иван')
remove_chastisements('Фролов Иван')
create_commendation('Фролов Иван', 'Музыка')