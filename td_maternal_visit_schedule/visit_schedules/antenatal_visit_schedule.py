from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from .maternal_requisitions import requisitions_1010m, requisitions_1020m
from .crfs import crf_1000, crf_1010, crf_1020

# TODO: Add PRN and Lab Requisitions for visits.

schedule = Schedule(
    name='schedule',
    verbose_name='Day 1 to 36 months Follow-up',
    onschedule_model='td_maternal.onschedule',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.maternalconsent',
    appointment_model='edc_appointment.appointment')

visit1000 = Visit(
    code='1000M',
    title='Antenatal Enrollment',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1000,
    facility_name='5-day clinic')

visit1010 = Visit(
    code='1010M',
    title='Antenatal Visit 1',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1010m,
    crfs=crf_1010,
    facility_name='5-day clinic')

visit1020 = Visit(
    code='1020M',
    title='Antenatal Visit 2',
    timepoint=2,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1020m,
    crfs=crf_1020,
    facility_name='5-day clinic')

schedule.add_visit(visit=visit1000)
schedule.add_visit(visit=visit1010)
schedule.add_visit(visit=visit1020)
