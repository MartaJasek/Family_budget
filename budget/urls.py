from rest_framework import routers

from budget.views import AccountsView, TransactionsView

router = routers.SimpleRouter()
router.register(r'account', AccountsView)
router.register(r'transaction', TransactionsView)
urlpatterns = router.urls