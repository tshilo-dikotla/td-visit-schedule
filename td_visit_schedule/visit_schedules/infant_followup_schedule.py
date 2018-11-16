from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from .infant_requisitions import (infant_birth_requisitions, infant_1month_requisitions,
                                  infant_followup_requisitions,
                                  infant_18month_requisitions,
                                  infant_36month_requisitions)
from .infant_crfs import (crf_2000, crf_2010, crf_2020,
                          crf_2120, crf_2180, crf_2240,
                          crf_2300, crf_2360, crf_2060)

schedule = Schedule(
    name='schedule',
    verbose_name='Day 1 to 36 months Follow-up',
    onschedule_model='td_infant.onschedule',
    offschedule_model='td_infant.infantoffstudy',
    consent_model='td_infant.infantbirth',
    appointment_model='edc_appointment.appointment')

visit2000 = Visit(
    code='2000M',
    title='Birth',
    timepoint=0,
    rbase=relativedelta(months=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=infant_birth_requisitions,
    crfs=crf_2000,
    facility_name='5-day clinic')

visit2010 = Visit(
    code='2010M',
    title='Infant 1 Month Visit',
    timepoint=1,
    rbase=relativedelta(months=1),
    rlower=relativedelta(days=15),
    rupper=relativedelta(days=15),
    requisitions=infant_1month_requisitions,
    crfs=crf_2010,
    facility_name='5-day clinic')

visit2020 = Visit(
    code='2020M',
    title='Infant 2 Month Visit',
    timepoint=2,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=15),
    rupper=relativedelta(days=60),
    requisitions=infant_followup_requisitions,
    crfs=crf_2020,
    facility_name='5-day clinic')

visit2060 = Visit(
    code='2060M',
    title='Infant 6 Month Visit',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=89),
    rupper=relativedelta(days=60),
    requisitions=infant_followup_requisitions,
    crfs=crf_2060,
    facility_name='5-day clinic')

visit2120 = Visit(
    code='2120M',
    title='Infant 12 Month Visit',
    timepoint=12,
    rbase=relativedelta(months=12),
    rlower=relativedelta(months=4),
    rupper=relativedelta(months=3),
    requisitions=infant_followup_requisitions,
    crfs=crf_2120,
    facility_name='5-day clinic')

visit2180 = Visit(
    code='2180M',
    title='Infant 18 Month Visit',
    timepoint=18,
    rbase=relativedelta(months=18),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_18month_requisitions,
    crfs=crf_2180,
    facility_name='5-day clinic')

visit2240 = Visit(
    code='2240M',
    title='Infant 24 Month Visit',
    timepoint=30,
    rbase=relativedelta(months=24),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_followup_requisitions,
    crfs=crf_2240,
    facility_name='5-day clinic')

visit2300 = Visit(
    code='2300M',
    title='Infant 30 Month Visit',
    timepoint=30,
    rbase=relativedelta(months=30),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_followup_requisitions,
    crfs=crf_2300,
    facility_name='5-day clinic')

visit2360 = Visit(
    code='2360M',
    title='Infant 36 Month Visit',
    timepoint=36,
    rbase=relativedelta(months=36),
    rlower=relativedelta(months=3),
    rupper=relativedelta(months=3),
    requisitions=infant_36month_requisitions,
    crfs=crf_2360,
    facility_name='5-day clinic')

schedule.add_visit(visit=visit2000)
schedule.add_visit(visit=visit2010)
schedule.add_visit(visit=visit2020)
schedule.add_visit(visit=visit2120)
schedule.add_visit(visit=visit2180)
schedule.add_visit(visit=visit2240)
schedule.add_visit(visit=visit2300)
schedule.add_visit(visit=visit2360)
