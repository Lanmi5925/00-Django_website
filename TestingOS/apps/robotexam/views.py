from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from apps.robotexam.models import SingleSel, MultiSel, RightOrWrong, Answer
# Create your views here.


def index(request):
    paper = MultiSel.objects.filter(QuestionID=31)
    return render(request, "index.html", {"paper": paper})


def paper(request):
    # if request.method == "GET":
    date = request.GET.get('date', "20170225")
    date = int(date)
    template = loader.get_template("questionpaper.html")
    all_single = SingleSel.objects.filter(QuestionDate=date)
    all_multi = MultiSel.objects.filter(QuestionDate=date)
    all_ROW = RightOrWrong.objects.filter(QuestionDate=date)
    var_dict = {}
    if all_single:
        var_dict = dict(singlesels=all_single, multisels=all_multi, rows=all_ROW, date=date)
    return HttpResponse(template.render(var_dict))
    # return render(request, "questionpaper2.html", context={"numList": [1, 2, 3, 4, 5]})


def cal_grade(request):
    if request.method == "POST":
        date = request.POST.get('date')
        # print(date)
        date = int(date)
        grade = 0
        single_paper = SingleSel.objects.filter(QuestionDate=date).values("QuestionID", "Answer", "Score")
        multi_paper = MultiSel.objects.filter(QuestionDate=date).values("QuestionID", "Answer", "Score")
        row_paper = RightOrWrong.objects.filter(QuestionDate=date).values("QuestionID", "Answer", "Score")
        n = len(single_paper) + len(multi_paper) + len(row_paper)
        for s in single_paper:
            qid = str(s['QuestionID'])
            myans = request.POST.get(qid)
            answer = s['Answer'].strip()
            # print('第%s题，%s : %s' %(qid, myans, answer))
            if myans == answer:
                grade = grade + s['Score']
        for m in multi_paper:
            qid = str(m['QuestionID'])
            myans = request.POST.getlist(qid)
            myans = "".join(myans)
            answer = m['Answer'].strip()
            # print('第%s题，%s : %s' %(qid, myans, answer))
            if myans == answer:
                grade = grade + m['Score']
        for r in row_paper:
            qid = str(r['QuestionID'])
            myans = request.POST.get(qid)
            answer = r['Answer'].strip()
            # print('第%s题，%s : %s' %(qid, myans, answer))
            if myans == answer:
                grade = grade + r['Score']

        # s_answer = request.POST.get("radio")
        # answer = Answer()
        # answer.answer = s_answer
        # answer.save()
    return render(request, "grade.html", {"grade": grade})
