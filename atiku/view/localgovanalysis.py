from django.shortcuts import render

from atiku.models import LocalGovernment, ApplicantInfo


def page(request, state):
    localgov = LocalGovernment.objects.filter(country__name=state)
    from pprint import pprint
    pprint(state)
    applicant_number = [ApplicantInfo.objects.filter(local_government=state).count() for state in localgov]
    new = zip(localgov,applicant_number)
    from pprint import pprint
    pprint(new)
    return render(request, 'localgovernments.html',{'new':new} )