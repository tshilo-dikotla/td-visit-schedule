from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import (
    antenatal_schedule_1, antenatal_schedule_3, antenatal_membership_schedule_v3,
    antenatal_membership_schedule_1, maternal_labour_del_schedule_v1,
    maternal_labour_del_schedule_v3, infant_schedule_v1, infant_schedule_v3)

# Anternatal Visit Schedules

antenatal_visit_schedule_v1 = VisitSchedule(
    name='anv_schedule_v1',
    verbose_name='Antenatal Visit Schedule 1',
    offstudy_model='td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v1.add_schedule(antenatal_schedule_1)

antenatal_visit_schedule_v3 = VisitSchedule(
    name='anv_schedule_v3',
    verbose_name='Antenatal Visit Schedule 3',
    offstudy_model='td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None)

antenatal_visit_schedule_v3.add_schedule(antenatal_schedule_3)

# Anternatal Membership Visit Schedules

antenatal_membership_visit_schedule_v1 = VisitSchedule(
    name='anv_membership_v1',
    verbose_name='Antenatal Visit Membership Schedule 1',
    offstudy_model='td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
antenatal_membership_visit_schedule_v1.add_schedule(
    antenatal_membership_schedule_1)

antenatal_membership_visit_schedule_v3 = VisitSchedule(
    name='anv_membership_v3',
    verbose_name='Antenatal Visit Membership v3',
    offstudy_model='td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
antenatal_membership_visit_schedule_v3.add_schedule(
    antenatal_membership_schedule_v3)

# Maternal Labour Visit Schedules
maternal_labour_visit_schedule_v1 = VisitSchedule(
    name='mtl_visit_schedule_v1',
    verbose_name='Maternal Labour Visit Schedule',
    offstudy_model=f'td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
maternal_labour_visit_schedule_v1.add_schedule(maternal_labour_del_schedule_v1)

maternal_labour_visit_schedule_v3 = VisitSchedule(
    name='mtl_visit_schedule_v3',
    verbose_name='Maternal Labour Visit Schedule',
    offstudy_model=f'td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
maternal_labour_visit_schedule_v3.add_schedule(maternal_labour_del_schedule_v3)

# Infant Visit Schedule

infant_visit_schedule_v1 = VisitSchedule(
    name='infant_visit_schedule_v1',
    verbose_name='Infant Visit Schedule V1',
    offstudy_model='td_prn.infantoffstudy',
    death_report_model='td_prn.infantdeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
infant_visit_schedule_v1.add_schedule(infant_schedule_v1)

infant_visit_schedule_v3 = VisitSchedule(
    name='infant_visit_schedule_v3',
    verbose_name='Infant Visit Schedule V3',
    offstudy_model='td_prn.infantoffstudy',
    death_report_model='td_prn.infantdeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None
)
infant_visit_schedule_v3.add_schedule(infant_schedule_v3)
# Registering Visit Schedules
site_visit_schedules.register(antenatal_visit_schedule_v1)
site_visit_schedules.register(antenatal_visit_schedule_v3)

site_visit_schedules.register(antenatal_membership_visit_schedule_v1)
site_visit_schedules.register(antenatal_membership_visit_schedule_v3)

site_visit_schedules.register(maternal_labour_visit_schedule_v1)
site_visit_schedules.register(maternal_labour_visit_schedule_v3)

site_visit_schedules.register(infant_visit_schedule_v1)
site_visit_schedules.register(infant_visit_schedule_v3)
