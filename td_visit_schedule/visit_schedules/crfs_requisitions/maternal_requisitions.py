from edc_visit_schedule import FormsCollection, Requisition
from td_labs import cd4_panel, viral_load_panel, pbmc_vl_panel
from td_labs import fasting_glucose_panel, glucose_1h_panel, glucose_2h_panel
from td_labs import pbmc_pl_panel

requisitions_prn = FormsCollection(
    Requisition(
        show_order=10,
        panel=cd4_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=pbmc_pl_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=viral_load_panel, required=False, additional=False),
    Requisition(
        show_order=40,
        panel=fasting_glucose_panel, required=False, additional=False),
    Requisition(
        show_order=50,
        panel=glucose_1h_panel, required=False, additional=False),
    Requisition(
        show_order=60,
        panel=glucose_2h_panel, required=False, additional=False),
    name='requisitions_prn')

requisitions_1010m = FormsCollection(
    Requisition(
        show_order=10,
        panel=cd4_panel, required=False, additional=True),
    Requisition(
        show_order=20,
        panel=pbmc_vl_panel, required=False, additional=True),
    Requisition(
        show_order=30,
        panel=fasting_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=40,
        panel=glucose_1h_panel, required=True, additional=True),
    Requisition(
        show_order=50,
        panel=glucose_2h_panel, required=True, additional=True),
    Requisition(
        show_order=60,
        panel=pbmc_pl_panel, required=False, additional=True),
    Requisition(
        show_order=70,
        panel=viral_load_panel, required=False, additional=True),
    name='requisitions_1010m'
)

requisitions_1020m = FormsCollection(
    Requisition(
        show_order=10,
        panel=viral_load_panel, required=False, additional=True),
    Requisition(
        show_order=20,
        panel=cd4_panel, required=False, additional=True),
    Requisition(
        show_order=30,
        panel=fasting_glucose_panel, required=False, additional=True),
    Requisition(
        show_order=40,
        panel=glucose_1h_panel, required=False, additional=True),
    Requisition(
        show_order=50,
        panel=glucose_2h_panel, required=False, additional=True),
    name='requisitions_1020m'
)

requisitions_followup = FormsCollection(
    Requisition(
        show_order=10,
        panel=viral_load_panel, required=False, additional=True),
    Requisition(
        show_order=20,
        panel=cd4_panel, required=False, additional=True),
    Requisition(
        show_order=30,
        panel=fasting_glucose_panel, required=False, additional=True),
    Requisition(
        show_order=40,
        panel=glucose_1h_panel, required=False, additional=True),
    Requisition(
        show_order=50,
        panel=glucose_2h_panel, required=False, additional=True),
    name='requisitions_followup'
)
