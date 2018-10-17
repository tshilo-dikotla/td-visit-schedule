from edc_visit_schedule import FormsCollection, Crf

crf_1000 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalultrasoundinitial'),
    Crf(show_order=2, model='td_maternal.maternalobstericalhistory'),
    Crf(show_order=3, model='td_maternal.maternalmedicalhistory'),
    Crf(show_order=4, model='td_maternal.maternaldemographics'),
    Crf(show_order=5, model='td_maternal.maternallifetimearvhistory'),
    Crf(show_order=6, model='td_maternal.maternalarvpreg'),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementsone'),
    name='enrollment')

crf_1010 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalultrasoundinitial'),
    Crf(show_order=2, model='td_maternal.maternalrando'),
    Crf(show_order=3, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=4, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=5, model='td_maternal.rapidtestresult'),
    name='antenatal1')

crf_1020 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalarvpreg'),
    Crf(show_order=2, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=3, model='td_maternal.maternaldiagnoses'),
    Crf(show_order=4, model='td_maternal.maternalsubstanceusepriorpreg'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=6, model='td_maternal.rapidtestresult'),
    name='antenatal2')

crf_2000 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternaldiagnoses'),
    Crf(show_order=2, model='td_maternal.maternalhivinterimhx'),
    Crf(show_order=3, model='td_maternal.maternalarvpreg'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalsubstanceuseduringpreg'),
    Crf(show_order=6, model='td_maternal.rapidtestresult'),
    name='birth')

crf_2010 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost'),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=6, model='td_maternal.rapidtestresult'),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    Crf(show_order=9, model='td_maternal.maternalsrh'),
    name='followup1')

crf_2020 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost'),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=6, model='td_maternal.rapidtestresult'),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    Crf(show_order=9, model='td_maternal.maternalsrh'),
    name='followup2')

crf_2060 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost'),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=6, model='td_maternal.rapidtestresult'),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    Crf(show_order=9, model='td_maternal.maternalsrh'),
    name='followup3')

crf_2120 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost'),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=6, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=7, model='td_maternal.maternalcontraception'),
    Crf(show_order=8, model='td_maternal.rapidtestresult'),
    Crf(show_order=9, model='td_maternal.maternalsrh'),
    name='followup4')

crf_2180 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    name='followup5')

crf_2240 = crf_2180 + FormsCollection(
    Crf(show_order=6, model='td_maternal.maternalcontraception'),
    Crf(show_order=7, model='td_maternal.maternalsrh'),
    name='follow6')

crf_2300 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    name='followup7')

crf_2360 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    name='followup8')
