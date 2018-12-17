from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import (
    antenatal_schedule_1, antenatal_schedule_3,
    antenatal_membership_schedule_v3,
    antenatal_membership_schedule_1,
    maternal_labour_del_schedule_v1,
    maternal_labour_del_schedule_v3)

app_label = 'td_maternal'


# Anternatal Visit Schedules

antenatal_visit_schedule_v1 = VisitSchedule(
    name='anv_schedule_v1',
    verbose_name='Antenatal Visit Schedule 1',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v1.add_schedule(antenatal_schedule_1)

antenatal_visit_schedule_v3 = VisitSchedule(
    name='anv_schedule_v3',
    verbose_name='Antenatal Visit Schedule 3',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v3.add_schedule(antenatal_schedule_3)


# Anternatal Membership Visit Schedules

antenatal_membership_visit_schedule_v1 = VisitSchedule(
    name='anv_membership_v1',
    verbose_name='Antenatal Visit Membership Schedule 1',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_report.subjectlocator',
    previous_visit_schedule=None
)
antenatal_membership_visit_schedule_v1.add_schedule(
    antenatal_membership_schedule_1)

antenatal_membership_visit_schedule_v3 = VisitSchedule(
    name='anv_membership_v3',
    verbose_name='Antenatal Visit Membership v3',
    offstudy_model='td_maternal.maternaloffstudy',
    death_report_model='td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None
)
antenatal_membership_visit_schedule_v3.add_schedule(
    antenatal_membership_schedule_v3)


# Maternal Labour Visit Schedules
maternal_labour_visit_schedule_v1 = VisitSchedule(
    name='mtl_visit_schedule_v1',
    verbose_name='Maternal Labour Visit Schedule',
    offstudy_model=f'td_maternal.maternaloffstudy',
    death_report_model=f'td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None
)
maternal_labour_visit_schedule_v1.add_schedule(maternal_labour_del_schedule_v1)


maternal_labour_visit_schedule_v3 = VisitSchedule(
    name='mtl_visit_schedule_v3',
    verbose_name='Maternal Labour Visit Schedule',
    offstudy_model=f'td_maternal.maternaloffstudy',
    death_report_model=f'td_maternal.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None
)
<<<<<<< HEAD

antenatal_membership_visit_schedule_v3.add_schedule(
    antenatal_membership_schedule_v3)
=======
maternal_labour_visit_schedule_v3.add_schedule(maternal_labour_del_schedule_v3)
>>>>>>> a48543b313dab6ee0a241e4969b71c9c7b0dc0bc


# Registering Visit Schedules
site_visit_schedules.register(antenatal_visit_schedule_v1)
site_visit_schedules.register(antenatal_visit_schedule_v3)

site_visit_schedules.register(antenatal_membership_visit_schedule_v1)
site_visit_schedules.register(antenatal_membership_visit_schedule_v3)

site_visit_schedules.register(maternal_labour_visit_schedule_v1)
site_visit_schedules.register(maternal_labour_visit_schedule_v3)
