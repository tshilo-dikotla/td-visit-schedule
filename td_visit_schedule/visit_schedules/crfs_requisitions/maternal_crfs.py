from edc_visit_schedule import FormsCollection, Crf

crf_1000 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalultrasoundinitial'),
    Crf(show_order=2, model='td_maternal.maternalobstericalhistory',
        required=False),
    Crf(show_order=3, model='td_maternal.maternalmedicalhistory',
        required=False),
    Crf(show_order=4, model='td_maternal.maternaldemographics',
        required=False),
    Crf(show_order=5, model='td_maternal.maternallifetimearvhistory',
        required=False),
    Crf(show_order=6, model='td_maternal.maternalarvpreg', required=False),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementsone',
        required=False),
    name='enrollment')

crf_1010 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalrando', required=False),
    Crf(show_order=2, model='td_maternal.maternalinterimidcc', required=False),
    Crf(show_order=3, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=4, model='td_maternal.rapidtestresult', required=False),
    name='antenatal1')

crf_1020 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalarvpreg'),
    Crf(show_order=2, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=3, model='td_maternal.maternaldiagnoses'),
    Crf(show_order=4, model='td_maternal.maternalsubstanceusepriorpreg'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=6, model='td_maternal.rapidtestresult', required=False),
    name='antenatal2')

crf_2000 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternaldiagnoses'),
    Crf(show_order=2, model='td_maternal.maternalhivinterimhx',
        required=False),
    Crf(show_order=3, model='td_maternal.maternalarvpreg', required=False),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc', required=False),
    Crf(show_order=5, model='td_maternal.maternalsubstanceuseduringpreg'),
    Crf(show_order=6, model='td_maternal.rapidtestresult', required=False),
    name='birth')

crf_2010 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep',
        required=False),
    Crf(show_order=3, model='td_maternal.maternalarvpost', required=False),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh', required=False),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc', required=False),
    Crf(show_order=6, model='td_maternal.rapidtestresult', required=False),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    name='followup1')

crf_2020 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost', required=False),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh', required=False),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc', required=False),
    Crf(show_order=6, model='td_maternal.rapidtestresult', required=False),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    Crf(show_order=9, model='td_maternal.maternalsrh', required=False),
    name='followup2')

crf_2060 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost', required=False),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh', required=False),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc', required=False),
    Crf(show_order=6, model='td_maternal.rapidtestresult', required=False),
    Crf(show_order=7, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=8, model='td_maternal.maternalcontraception'),
    Crf(show_order=9, model='td_maternal.maternalsrh', required=False),
    name='followup3')

crf_2120 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalpostpartumdep'),
    Crf(show_order=3, model='td_maternal.maternalarvpost'),
    Crf(show_order=4, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=5, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=6, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=7, model='td_maternal.maternalcontraception'),
    Crf(show_order=8, model='td_maternal.rapidtestresult', required=False),
    Crf(show_order=9, model='td_maternal.maternalsrh', required=False),
    name='followup4')

crf_2180 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=6, model='td_maternal.maternalsrh', required=False),
    name='followup5')

crf_2240 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=6, model='td_maternal.maternalcontraception'),
    Crf(show_order=7, model='td_maternal.maternalsrh', required=False),
    name='follow6')

crf_2300 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    Crf(show_order=6, model='td_maternal.maternalsrh', required=False),
    name='followup7')

crf_2360 = FormsCollection(
    Crf(show_order=1, model='td_maternal.maternalpostpartumfu'),
    Crf(show_order=2, model='td_maternal.maternalarvpost'),
    Crf(show_order=3, model='td_maternal.maternalarvpostadh'),
    Crf(show_order=4, model='td_maternal.maternalinterimidcc'),
    Crf(show_order=5, model='td_maternal.maternalclinicalmeasurementstwo'),
    name='followup8')
