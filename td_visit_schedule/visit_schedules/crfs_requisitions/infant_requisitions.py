from edc_visit_schedule import FormsCollection, Requisition
from td_labs import (
    infant_insulin, serum_panel, infant_glucose_panel,
    infant_pbmc_pl_panel, dna_pcr, dbs_panel, infant_elisa_panel, infant_wb_panel)

infant_requisitions_prn = FormsCollection(
    Requisition(
        show_order=10,
        panel=infant_insulin, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=serum_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=infant_glucose_panel, required=False, additional=False),
    Requisition(
        show_order=40,
        panel=dna_pcr, required=False, additional=False),
    Requisition(
        show_order=50,
        panel=dbs_panel, required=False, additional=False),
    Requisition(
        show_order=60,
        panel=infant_elisa_panel, required=False, additional=False),
    name='infant_requisitions_prn')

infant_birth_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=serum_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=40, panel=infant_pbmc_pl_panel, required=True, additional=True),
    name='requisitions_2000'
)

infant_1month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=dna_pcr, required=True, additional=True),
    Requisition(
        show_order=40, panel=infant_pbmc_pl_panel, required=True, additional=True),
    Requisition(
        show_order=50, panel=serum_panel, required=True, additional=True),
    Requisition(
        show_order=60, panel=dbs_panel, required=False, additional=True),
    name='requisitions_2010'
)

infant_followup_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=dna_pcr, required=False, additional=True),
    name='requisitions_2020'
)

karabo_infant_requisitions_2060 = FormsCollection(
    Requisition(
        show_order=10, panel=dna_pcr, required=False, additional=True),
    Requisition(
        show_order=20, panel=infant_pbmc_pl_panel, required=False, additional=True),
    Requisition(
        show_order=30, panel=infant_wb_panel, required=False, additional=True),
    name='requisitions_2060'
)

karabo_infant_requisitions_2120 = FormsCollection(
    Requisition(
        show_order=10, panel=dna_pcr, required=False, additional=True),
    Requisition(
        show_order=20, panel=infant_pbmc_pl_panel, required=False, additional=True),
    name='requisitions_2120'
)

infant_18month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=infant_elisa_panel, required=False, additional=True),
    Requisition(
        show_order=40, panel=serum_panel, required=True, additional=True),
    Requisition(
        show_order=50, panel=infant_pbmc_pl_panel, required=True, additional=True),
    name='requisitions_2180'
)

# this list of requisitions applies to consent v3 infants only.
infant_24month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=serum_panel, required=True, additional=True),
    Requisition(
        show_order=40, panel=infant_pbmc_pl_panel, required=True, additional=True),
    name='requisitions_2240'
)

# this list of requisitions applies to consent v3 infants only.
infant_36month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=infant_pbmc_pl_panel, required=True, additional=True),
    Requisition(
        show_order=40, panel=serum_panel, required=True, additional=True),
    name='requisitions_2360'
)
