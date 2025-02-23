import os
from win11toast import toast
from win11toast import ToastNotification


icon = os.path.abspath('icon.ico')

toast(
    '自动打卡成功',
    app_id = 'Auto Clock In',
    icon = icon,
)
