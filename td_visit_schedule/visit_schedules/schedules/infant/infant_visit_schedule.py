from edc_visit_schedule import VisitSchedule, site_visit_schedules

from td_visit_schedule.visit_schedules.schedules.infant_followup_schedule import schedule

app_label = 'td_visit_schedules'

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Td Visit Schedule',
    offstudy_model='td_infant.infantoffstudy',
    death_report_model='td_infant.infantdeath',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule)
site_visit_schedules.register(visit_schedule)
