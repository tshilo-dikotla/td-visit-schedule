from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ...crfs_requisitions import (requisitions_1010m,
                                  requisitions_1020m,
                                  requisitions_prn as default_requisitions_prn)
from ...crfs_requisitions import crf_1010, crf_1020

default_requisitions = None


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn or default_requisitions_prn,
            **kwargs)


# TODO: Add PRN for visits.
antenatal_membership_schedule_1 = Schedule(
    name='anv_membership_v1',
    verbose_name='Antenatal Visit Membership v1',
    onschedule_model='td_maternal.onscheduleantenatalvisitmembership',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit1010 = Visit(
    code='1010M',
    title='Antenatal Visit 1',
    timepoint=5,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1010m,
    crfs=crf_1010,
    facility_name='5-day clinic')

visit1020 = Visit(
    code='1020M',
    title='Antenatal Visit 2',
    timepoint=10,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_1020m,
    crfs=crf_1020,
    facility_name='5-day clinic')

antenatal_membership_schedule_1.add_visit(visit=visit1010)
antenatal_membership_schedule_1.add_visit(visit=visit1020)
