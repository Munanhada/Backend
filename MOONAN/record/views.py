from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Record
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q

# 오늘 하루 감정 업데이트
def record_view(request):
    
    # 로그인한 사용자가 오늘 작성한 레코드 조회
    today = timezone.now().date()
    user = request.user  # 로그인한 사용자

    today_records = Record.objects.filter(Q(created_date=today) & Q(user=user))

    
    # 무난하지 않았던 이유 카테고리 속 각각의 내용 불러오기
    context = {
        'eating_choices': Record.EATING_CHOICES, 
        'health_choices': Record.HEALTH_CHOICES,
        'sleep_choices': Record.SLEEP_CHOICES,
        'mood_choices': Record.MOOD_CHOICES,
        'accidents_choices': Record.ACCIDENTS_CHOICES,
        'today_records': today_records,
    }

    return render(request, 'record.html', context)

# 오늘 하루 표정 선택 & 무난하지 않았던 이유 저장
def submit_data(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        happyorsad = request.POST.get('happyorsad')
        selected_data_json = request.POST.get('selectedData', '')

        # JSON 데이터 파싱
        try:
            selected_data = json.loads(selected_data_json)
        except json.JSONDecodeError:
            selected_data = {}  # JSON 파싱 실패 시 빈 딕셔너리

        today = timezone.now().date()

        # 모델에 선택된 데이터 생성 또는 수정
        record, created = Record.objects.update_or_create(
            user=request.user,
            created_date=today,  # 현재 날짜
            defaults={
                'expression': expression,
                'eating': selected_data.get('eating'),
                'health': selected_data.get('health'),
                'sleep': selected_data.get('sleep'),
                'mood': selected_data.get('mood'),
                'accident': selected_data.get('accident'),
                'customContent': selected_data.get('customContent'),
                'happyorsad': happyorsad,
            }
        )

        print("표정:", expression)
        print("선택한 이유:", selected_data)

        return JsonResponse({'status': '문안 기록이 저장되었습니다.'})
    
    return JsonResponse({'status': 'error', 'message': '문안 기록 저장에 실패하였습니다.'})
