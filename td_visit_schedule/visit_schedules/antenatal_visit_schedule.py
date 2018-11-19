from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from .maternal_crfs import crf_1000

# TODO: Add PRN and Lab Requisitions for visits.

schedule = Schedule(
    name='schedule',
    verbose_name='Antenatal Visits',
    onschedule_model='td_maternal.onscheduleantenatalenrollment',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
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

schedule.add_visit(visit=visit1000)
