import jpush
from app.models import Jgpush
from app.extensions import db
from flask import Blueprint, render_template
from app.forms import JgPush
from flask_login import login_required

jg = Blueprint('jg', __name__)

app_key = u'168135a19e4fae1414183d22'
master_secret = u'd25a54a591409078bcf9b003'


_jpush = jpush.JPush(app_key, master_secret)
# _jpush.set_logging("DEBUG")
report=_jpush.create_report()

@jg.route('/all/', methods=['GET', 'POST'])
@login_required
def all():
    form = JgPush()
    if form.validate_on_submit():
        content = form.content.data
        platform = form.platform.data
        print(content, platform)
        push = _jpush.create_push()
        push.audience = jpush.all_
        if platform == 'all':
            ios = jpush.ios(alert=content, sound="a.caf", extras={'k1': 'v1'})
            android = jpush.android(alert=content, priority=1, style=1, alert_type=1, big_text='jjjjjjjjjj', extras={'k1': 'v1'})
            push.notification = jpush.notification(alert=content, android=android, ios=ios)
            push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}
            push.platform = 'all'
        elif platform == 'ios开发':
            ios = jpush.ios(alert=content, sound="a.caf", extras={'k1': 'v1'})
            push.notification = jpush.notification(alert=content, ios=ios)
            push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}
            push.platform = 'ios'
        elif platform == 'ios生产':
            ios = jpush.ios(alert=content, sound="a.caf", extras={'k1': 'v1'})
            push.notification = jpush.notification(alert=content, ios=ios)
            push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": True}
            push.platform = 'ios'
        elif platform == 'android':
            android = jpush.android(alert=content, priority=1, style=1, alert_type=1, big_text='jjjjjjjjjj', extras={'k1': 'v1'})
            push.notification = jpush.notification(alert=content, android=android)
            push.platform = 'android'
        try:
            response=push.send()
            print(response)
            print(response.status_code)
            if response.status_code == 200:
                j = Jgpush(title=platform, message=content)
                db.session.add(j)
                print('222222222')
                return 'ok'
            else:
                print('11111111')
                return 'notok'
        except Exception as e:
            print(e)
    return render_template('common/jgpush.html', form=form)


# if __name__ == '__main__':
#     all()