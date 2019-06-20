from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ...crfs_requisitions import (
    infant_birth_requisitions, infant_1month_requisitions,
    infant_followup_requisitions, infant_36month_requisitions,
    infant_18month_requisitions, infant_24month_requisitions,
    karabo_infant_requisitions_2060, karabo_infant_requisitions_2120)
from ...crfs_requisitions import (
    infant_crf_2000, infant_crf_2010, infant_crf_2020,
    infant_crf_2120, infant_crf_2180, infant_crf_2240,
    infant_crf_2300, infant_crf_2360, infant_crf_2060,
    infant_requisitions_prn)

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
            requisitions_prn=requisitions_prn or infant_requisitions_prn,
            **kwargs)


infant_schedule_v3 = Schedule(
    name='infant_schedule_v3',
    verbose_name='Day 1 to 36 months Follow-up V3',
    onschedule_model='td_infant.onscheduleinfantbirth',
    offschedule_model='td_infant.infantoffschedule',
    consent_model='td_infant.infantdummysubjectconsent',
    appointment_model='td_infant.appointment')

visit2000 = Visit(
    code='2000',
    title='Birth V3',
    timepoint=0,
    rbase=relativedelta(months=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=infant_birth_requisitions,
    crfs=infant_crf_2000,
    facility_name='5-day clinic')

visit2010 = Visit(
    code='2010',
    title='Infant 1 Month Visit V3',
    timepoint=10,
    rbase=relativedelta(months=1),
    rlower=relativedelta(days=15),
    rupper=relativedelta(days=15),
    requisitions=infant_1month_requisitions,
    crfs=infant_crf_2010,
    facility_name='5-day clinic')

visit2020 = Visit(
    code='2020',
    title='Infant 2 Month Visit V3',
    timepoint=20,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=15),
    rupper=relativedelta(days=60),
    requisitions=infant_followup_requisitions,
    crfs=infant_crf_2020,
    facility_name='5-day clinic')

visit2060 = Visit(
    code='2060',
    title='Infant 6 Month Visit V3',
    timepoint=60,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=89),
    rupper=relativedelta(days=60),
    requisitions=karabo_infant_requisitions_2060,
    crfs=infant_crf_2060,
    facility_name='5-day clinic')

visit2120 = Visit(
    code='2120',
    title='Infant 12 Month Visit V3',
    timepoint=120,
    rbase=relativedelta(months=12),
    rlower=relativedelta(months=4),
    rupper=relativedelta(months=3),
    requisitions=karabo_infant_requisitions_2120,
    crfs=infant_crf_2120,
    facility_name='5-day clinic')

visit2180 = Visit(
    code='2180',
    title='Infant 18 Month Visit V3',
    timepoint=180,
    rbase=relativedelta(months=18),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_18month_requisitions,
    crfs=infant_crf_2180,
    facility_name='5-day clinic')

visit2240 = Visit(
    code='2240',
    title='Infant 24 Month Visit V3',
    timepoint=240,
    rbase=relativedelta(months=24),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_24month_requisitions,
    crfs=infant_crf_2240,
    facility_name='5-day clinic')

visit2300 = Visit(
    code='2300',
    title='Infant 30 Month Visit V3',
    timepoint=300,
    rbase=relativedelta(months=30),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_followup_requisitions,
    crfs=infant_crf_2300,
    facility_name='5-day clinic')

visit2360 = Visit(
    code='2360',
    title='Infant 36 Month Visit V3',
    timepoint=360,
    rbase=relativedelta(months=36),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_36month_requisitions,
    crfs=infant_crf_2360,
    facility_name='5-day clinic')

infant_schedule_v3.add_visit(visit=visit2000)
infant_schedule_v3.add_visit(visit=visit2010)
infant_schedule_v3.add_visit(visit=visit2020)
infant_schedule_v3.add_visit(visit=visit2060)
infant_schedule_v3.add_visit(visit=visit2120)
infant_schedule_v3.add_visit(visit=visit2180)
infant_schedule_v3.add_visit(visit=visit2240)
infant_schedule_v3.add_visit(visit=visit2300)
infant_schedule_v3.add_visit(visit=visit2360)
