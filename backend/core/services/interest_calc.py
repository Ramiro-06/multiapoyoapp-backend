from datetime import date
from decimal import Decimal



def fixed_interest(principal: Decimal, monthly_rate_percent: Decimal) -> Decimal:
    """
    Interés mensual fijo (sin prorrateo).
    Base: capital pendiente * tasa mensual
    - principal: capital pendiente
    - monthly_rate_percent: ej 8.00
    """
    interest = principal * (monthly_rate_percent / Decimal("100.00"))
    return interest.quantize(Decimal("0.01"))
