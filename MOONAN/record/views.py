from django.shortcuts import render
from django.http import JsonResponse
from .models import Record

# 오늘 하루 감정 업데이트
def record_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'record.html')
    
# 선택한 표정 버튼 강조
def expression_button_highlight(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        if request.user.is_authenticated:
            record = Record.objects.get_or_create(user=request.user)
            record.expression = expression
            record.save()
            
            return JsonResponse({'message': 'Success'})  # 응답 데이터 전송
        
    return JsonResponse({'message': 'Invalid request'}, status=400)