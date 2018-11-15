from edc_visit_schedule import FormsCollection, Requisition
from td_labs import (infant_glucose_panel, infant_insulin, dna_pcr,
                     serum_panel, infant_pbmc_pl_panel, dbs_panel,
                     elisa_panel)
from edc_lab.aliquot_types import serum

infant_birth_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True,
        additional=True),
    Requisition(
        show_order=20, panel=serum_panel, required=True,
        additional=True),
    Requisition(
        show_order=30, panel=infant_glucose_panel, required=True,
        additional=True),
    Requisition(
        show_order=40, panel=dna_pcr, required=False,
        additional=True),
)

infant_1month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True,
        additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True,
        additional=True),
    Requisition(
        show_order=30, panel=dna_pcr, required=True,
        additional=True),
    Requisition(
        show_order=40, panel=infant_pbmc_pl_panel, required=False,
        additional=True),
    Requisition(
        show_order=50, panel=serum_panel, required=True,
        additional=True),
    Requisition(
        show_order=60, panel=dbs_panel, required=False,
        additional=True),
)

infant_followup_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=dna_pcr, required=False,
        additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=False,
        additional=True),
    Requisition(
        show_order=30, panel=infant_insulin, required=False,
        additional=True),
    Requisition(
        show_order=40, panel=elisa_panel, required=False,
        additional=True),
)

infant_18month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True,
        additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=False,
        additional=True),
    Requisition(
        show_order=30, panel=elisa_panel, required=False,
        additional=True),
    Requisition(
        show_order=40, panel=serum_panel, required=True,
        additional=True),
    Requisition(
        show_order=50, panel=infant_pbmc_pl_panel, required=True,
        additional=True),
    Requisition(
        show_order=60, panel=dna_pcr, required=False,
        additional=True),
)

infant_36month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True,
        additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True,
        additional=True),
    Requisition(
        show_order=30, panel=infant_pbmc_pl_panel, required=True,
        additional=True),
    Requisition(
        show_order=40, panel=serum_panel, required=True,
        additional=True),
    Requisition(
        show_order=50, panel=dna_pcr, required=False,
        additional=True),
    Requisition(
        show_order=60, panel=elisa_panel, required=False,
        additional=True),
)