from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=1, model='td_infant.infantcovidscreening',
        required=False, additional=False),
    name='infant_crf_prn')

infant_crf_2000 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantbirthdata'),
    Crf(show_order=2, model='td_infant.infantbirthexam'),
    Crf(show_order=3, model='td_infant.infantbirthfeedingvaccine'),
    Crf(show_order=4, model='td_infant.infantbirtharv'),
    Crf(show_order=5, model='td_infant.infantcongenitalanomalies'),
    Crf(show_order=7, model='td_infant.infantnvpdispensing', required=False,
        additional=True),
    Crf(show_order=8, model='td_infant.infantcliniciannotes', required=False),
    name='Birth'
)

infant_crf_2010 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantarvproph'),
    Crf(show_order=6, model='td_infant.infantfeeding'),
    Crf(show_order=7, model='td_infant.solidfoodassessment', required=False),
    Crf(show_order=8, model='td_infant.infantnvpadjustment'),
    Crf(show_order=9, model='td_infant.infantfuimmunizations'),
    Crf(show_order=10, model='td_infant.karabotuberculosishistory',
        required=False),
    Crf(show_order=11, model='td_infant.karabooffstudy', required=False),
    Crf(show_order=12, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 1 Month Visit'
)

infant_crf_2020 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfuimmunizations'),
    Crf(show_order=6, model='td_infant.infantarvproph'),
    Crf(show_order=7, model='td_infant.infantfeeding'),
    Crf(show_order=8, model='td_infant.solidfoodassessment', required=False),
    Crf(show_order=9, model='td_infant.karabotuberculosishistory',
        required=False),
    Crf(show_order=10, model='td_infant.karabooffstudy', required=False),
    Crf(show_order=11, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 2 Month Visit '
)

infant_crf_2060 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=8, model='td_infant.karabotuberculosishistory',
        required=False),
    Crf(show_order=9, model='td_infant.karabooffstudy', required=False),
    Crf(show_order=10, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 6 Month Visit '
)

infant_crf_2120 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=9, model='td_infant.karabotuberculosishistory',
        required=False),
    Crf(show_order=10, model='td_infant.karabooffstudy', required=False),
    Crf(show_order=11, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 12 Month Visit'
)

infant_crf_2180 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=8, model='td_infant.karabotuberculosishistory',
        required=False),
    Crf(show_order=9, model='td_infant.karabooffstudy', required=False),
    Crf(show_order=10, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 18 Month Visit'
)

infant_crf_2240 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=8, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 24 Month Visit'
)

infant_crf_2300 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=8, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 30 Month Visit'
)

infant_crf_2360 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=6, model='td_infant.solidfoodassessment'),
    Crf(show_order=7, model='td_infant.infantfuimmunizations'),
    Crf(show_order=8, model='td_infant.infantcliniciannotes', required=False),
    name='Infant 36 Month Visit'
)
