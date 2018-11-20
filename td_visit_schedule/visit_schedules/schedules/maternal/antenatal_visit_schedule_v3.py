from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from ...crfs_requisitions import crf_1000

# TODO: Add PRN and Lab Requisitions for visits.

antenatal_schedule_3 = Schedule(
    name='antenatal_schedule_3',
    verbose_name='Antenatal Visits V3',
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

antenatal_schedule_3.add_visit(visit=visit1000)
