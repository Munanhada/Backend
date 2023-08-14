from django.shortcuts import render
from django.http import JsonResponse
from .models import Record

# 오늘 하루 감정 업데이트
def record_view(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        if request.user.is_authenticated:
            record, create = Record.objects.get_or_create(user=request.user)
            record.expression = expression
            record.save()
    
    # 무난하지 않았던 이유 카테고리 속 각각의 내용 불러오기
    context = {
        'eating_choices': Record.EATING_CHOICES, 
        'health_choices': Record.HEALTH_CHOICES,
        'sleep_choices': Record.SLEEP_CHOICES,
        'mood_choices': Record.MOOD_CHOICES,
        'accidents_choices': Record.ACCIDENTS_CHOICES,
    }

    return render(request, 'record.html', context)

# 오늘 하루 표정 표현
def submit_expression(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        if request.user.is_authenticated:
            record, created = Record.objects.get_or_create(user=request.user)
            record.expression = expression
            record.save()

        return JsonResponse({'message': '표정 전달 성공'}) 

    return JsonResponse({'message': '표정 전달 실패'}, status=400)

# 무난하지 않았던 이유 업데이트
def submit_reason(request):
    if request.method == 'POST':
        selected_category = request.POST.get('category')  # 선택한 카테고리 이름 가져오기
        selected_reason = request.POST.get('reason')

        if request.user.is_authenticated:
            record, created = Record.objects.get_or_create(user=request.user)

            # 선택한 카테고리에 따라서 해당 필드에 이유를 저장
            if selected_category == 'eating':
                record.eating = selected_reason if selected_reason in dict(Record.EATING_CHOICES) else None
            elif selected_category == 'health':
                record.health = selected_reason if selected_reason in dict(Record.HEALTH_CHOICES) else None
            elif selected_category == 'sleep':
                record.sleep = selected_reason if selected_reason in dict(Record.SLEEP_CHOICES) else None
            elif selected_category == 'mood':
                record.mood = selected_reason if selected_reason in dict(Record.MOOD_CHOICES) else None
            elif selected_category == 'accident':
                record.accident = selected_reason if selected_reason in dict(Record.ACCIDENTS_CHOICES) else None

            record.save()

        return JsonResponse({'message': '문안인사가 성공적으로 전송되었습니다!'}) 

    return JsonResponse({'message': '문안인사 전송에 실패하였습니다.'}, status=400)