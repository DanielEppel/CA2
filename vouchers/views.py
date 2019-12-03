from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import VoucherApplyForm

@require_POST
def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request_POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.object.get(code_iexact=code, valid_from_lte=now,
                                            valid_from_gte=now, active=True)

            request.session['voucher_id'] = voucher_id
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
    return redirect('cart:cart_detail')
# Create your views here.
