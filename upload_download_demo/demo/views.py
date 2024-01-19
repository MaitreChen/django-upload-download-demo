from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from urllib.parse import quote
import os
from .forms import RecordForm  # 导入图片上传表单
from .models import Record  # 导入图片上传模型类


def upload_image(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = RecordForm()
    records = Record.objects.all()

    return render(request, 'upload_image.html', {'form': form, 'records': records})


def download_image(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'images', filename)

    # 获取文件扩展名
    _, file_extension = os.path.splitext(filename.lower())

    # 根据文件扩展名确定内容类型
    content_type_mapping = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
    }

    # 如果找不到扩展名，默认使用 'application/octet-stream'
    content_type = content_type_mapping.get(file_extension, 'application/octet-stream')

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type=content_type)

    # 设置 Content-Disposition 修改文件名
    response['Content-Disposition'] = f'attachment; filename={quote(filename)}'

    return response
