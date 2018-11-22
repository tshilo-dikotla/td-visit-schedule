from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta
from ...crfs_requisitions import crf_1010, crf_1020
from ...crfs_requisitions import requisitions_1010m, requisitions_1020m

# TODO: Add PRN and Lab Requisitions for visits.

schedule = Schedule(
    name='schedule',
    verbose_name='Antenatal Visit Membership v3',
    onschedule_model='td_maternal.onscheduleantenatalvisitmembership',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit1010 = Visit(
    code='1010M',
    title='Antenatal Visit Membership v3',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1010m,
    crfs=crf_1010,
    facility_name='5-day clinic')

visit1020 = Visit(
    code='1020M',
    title='Antenatal Visit Membership v3',
    timepoint=2,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1020m,
    crfs=crf_1020,
    facility_name='5-day clinic')

schedule.add_visit(visit=visit1010)
schedule.add_visit(visit=visit1020)
