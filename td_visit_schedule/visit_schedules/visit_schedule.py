from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import antenatal_schedule_1, antenatal_schedule_3


app_label = 'td_maternal'

antenatal_visit_schedule_v1 = VisitSchedule(
    name='antenatal_visit_schedule_v1',
    verbose_name='Antenatal Visit Schedule 1',
    offstudy_model=f'',
    death_report_model='',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v1.add_schedule(antenatal_schedule_1)

antenatal_visit_schedule_v3 = VisitSchedule(
    name='antenatal_visit_schedule_v3',
    verbose_name='Antenatal Visit Schedule 3',
    offstudy_model='',
    death_report_model='',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v3.add_schedule(antenatal_schedule_3)

site_visit_schedules.register(antenatal_visit_schedule_v1)
site_visit_schedules.register(antenatal_visit_schedule_v3)
