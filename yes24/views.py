from django.shortcuts import render
import os
from glob import glob
import random
from django.conf import settings
from .models import Yes24Best200801202311

def yes24index(request):
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    img_dir = os.path.join(BASE_DIR, 'static', 'yes24', 'book_img')
    
    # glob을 사용하여 jpg 파일을 모두 가져옴
    book_cover_list = glob(os.path.join(img_dir, '*.jpg'))
    # list로 변환
    book_cover_list = list(book_cover_list)
    # print(book_cover_list)
    covers_10 = []
    for i in range(10):
        num = random.randrange(len(book_cover_list))
        img_url = book_cover_list[num].split("\\")[-1]
        covers_10.append(img_url)
    print(covers_10)
    context = {'covers_10' : covers_10}
    
    return render(request, 'yes24/yes24index.html', context)


