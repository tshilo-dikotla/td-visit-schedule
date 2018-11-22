from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedules import antenatal_schedule_1, antenatal_schedule_3

from .schedules import maternal_labour_del_schedule_v1

app_label = 'td_maternal'

antenatal_visit_schedule_v1 = VisitSchedule(
    name='antenatal_visit_schedule_v1',
    verbose_name='Antenatal Visit Schedule 1',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v1.add_schedule(antenatal_schedule_1)

antenatal_visit_schedule_v3 = VisitSchedule(
    name='antenatal_visit_schedule_v3',
    verbose_name='Antenatal Visit Schedule 3',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v3.add_schedule(antenatal_schedule_3)

maternal_labour_visit_schedule_v1 = VisitSchedule(
    name='maternal_labour_visit_schedule_v1',
    verbose_name='Maternal Labour Visit Schedule',
    offstudy_model=f'td_maternal.maternaloffstudy',
    death_report_model=f'td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None
)

# maternal_labour_visit_schedule_v1.add_schedule(maternal_labour_del_schedule_v1)

site_visit_schedules.register(antenatal_visit_schedule_v1)
site_visit_schedules.register(antenatal_visit_schedule_v3)
# site_visit_schedules.register(maternal_labour_visit_schedule_v1)
