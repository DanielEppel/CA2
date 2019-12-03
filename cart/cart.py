from vouchers.models import Voucher

__init__()
    self.voucher_id = self.session.get('voucher_id')


    @property
    def voucher(self):
        if self.voucher_id
            return Voucher.objects.get(id=self.voucher_id)
        return None

    def get_discount(self):
        if self.voucher:
            return(self.voucher.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount
