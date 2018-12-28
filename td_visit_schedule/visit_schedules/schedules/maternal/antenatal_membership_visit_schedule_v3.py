from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ...crfs_requisitions import crf_1010, crf_1020
from ...crfs_requisitions import requisitions_1010m, requisitions_1020m


# TODO: Add PRN and Lab Requisitions for visits.
antenatal_membership_schedule_v3 = Schedule(
    name='anv_membership_v3',
    verbose_name='Antenatal Visit Membership v3',
    onschedule_model='td_maternal.onscheduleantenatalvisitmembership',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit1010 = Visit(
    code='1010M',
    title='Antenatal Visit Membership 1 v3',
    timepoint=5,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1010m,
    crfs=crf_1010,
    facility_name='5-day clinic')

visit1020 = Visit(
    code='1020M',
    title='Antenatal Visit Membership 2 v3',
    timepoint=10,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1020m,
    crfs=crf_1020,
    facility_name='5-day clinic')

antenatal_membership_schedule_v3.add_visit(visit=visit1010)
antenatal_membership_schedule_v3.add_visit(visit=visit1020)
