from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ...crfs_requisitions import crf_1000


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# TODO: Lab Requisitions for visits.
antenatal_schedule_1 = Schedule(
    name='antenatal_schedule_1',
    verbose_name='Antenatal Visits V1',
    onschedule_model='td_maternal.onscheduleantenatalenrollment',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit1000 = Visit(
    code='1000M',
    title='Antenatal Enrollment V1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1000,
    facility_name='5-day clinic')

antenatal_schedule_1.add_visit(visit=visit1000)
