from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta

from .crfs import crf_1000

schedule = Schedule(
    name='schedule',
    verbose_name='Day 1 to 36 months Follow-up',
    onschedule_model='td_maternal.onschedule',
    offschedule_model='td_maternal.studyterminationconclusion',
    consent_model='td_maternal.maternalconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000M',
    title='Antenatal Enrollment',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1000,
    #     requisitions_prn=FormsCollection(
    #         *[r for r in default_requisitions_prn if r.panel != chemistry_panel]),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1010M',
    title='Antenatal Visit 1',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1000,
    #     requisitions_prn=FormsCollection(
    #         *[r for r in default_requisitions_prn if r.panel != chemistry_panel]),
    facility_name='5-day clinic')

visit2 = Visit(
    code='1020M',
    title='Antenatal Visit 2',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1000,
    #     requisitions_prn=FormsCollection(
    #         *[r for r in default_requisitions_prn if r.panel != chemistry_panel]),
    facility_name='5-day clinic')
