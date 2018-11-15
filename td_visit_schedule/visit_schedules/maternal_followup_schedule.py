from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from .maternal_crfs import crf_2000
# TODO: Add PRN and Lab Requisitions for visits.

schedule = Schedule(
    name='schedule',
    verbose_name='Day 1 to 36 months Follow-up',
    onschedule_model='td_maternal.onschedule',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.maternalconsent',
    appointment_model='edc_appointment.appointment')

visit2000 = Visit(
    code='2000M',
    title='Delivery Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')
