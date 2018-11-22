from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit
from ...crfs_requisitions import (
    crf_2000, crf_2010, crf_2020,
    crf_2060, crf_2180, crf_2240,
    crf_2300, crf_2360)
from ...crfs_requisitions import requisitions_followup


maternal_labour_schedule_v3 = Schedule(
    name='maternal_labour_schedule_v3',
    verbose_name='Day 1 to 36 months Follow-up v3',
    onschedule_model='td_maternal.onschedulematernallabourdel',
    offschedule_model='td_maternal.maternaloffstudy',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit2000 = Visit(
    code='2000M',
    title='Delivery Visit v3',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2000,
    facility_name='5-day clinic')

visit2010 = Visit(
    code='2010M',
    title='1 Months Visit v3',
    timepoint=1,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2010,
    facility_name='5-day clinic'
)

visit2020 = Visit(
    code='2020M',
    title='2 Months Visit v3',
    timepoint=2,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2020,
    facility_name='5-day clinic'
)

visit2060 = Visit(
    code='2060M',
    title='6 Months Visit v3',
    timepoint=6,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2060,
    facility_name='5-day clinic'
)

visit2120 = Visit(
    code='2120M',
    title='12 Months Visit v3',
    timepoint=12,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2060,
    facility_name='5-day clinic'
)

visit2180 = Visit(
    code='2120M',
    title='18 Months Visit v3',
    timepoint=18,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2180,
    facility_name='5-day clinic'
)

visit2240 = Visit(
    code='2240M',
    title='24 Months Visit v3',
    timepoint=24,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2240,
    facility_name='5-day clinic'
)

visit2300 = Visit(
    code='2300M',
    title='30 Months Visit v3',
    timepoint=30,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2300,
    facility_name='5-day clinic'
)

visit2360 = Visit(
    code='2360M',
    title='36 Months Visit v3',
    timepoint=36,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2360,
    facility_name='5-day clinic'
)

maternal_labour_schedule_v3.add_visit(visit2000)
maternal_labour_schedule_v3.add_visit(visit2010)
maternal_labour_schedule_v3.add_visit(visit2020)
maternal_labour_schedule_v3.add_visit(visit2060)
maternal_labour_schedule_v3.add_visit(visit2120)
maternal_labour_schedule_v3.add_visit(visit2180)
maternal_labour_schedule_v3.add_visit(visit2240)
maternal_labour_schedule_v3.add_visit(visit2300)
maternal_labour_schedule_v3.add_visit(visit2360)
