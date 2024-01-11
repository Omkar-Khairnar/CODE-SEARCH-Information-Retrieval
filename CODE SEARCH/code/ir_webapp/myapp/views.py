from django.shortcuts import render , redirect
from .forms import MyForm
from myapp.IRMODEL.Main import mainGetRankDocs
from myapp.IRMODEL.pr_curve import generate_pr_curve
import json

# Create your views here.
def index(request):
    form = MyForm()
    result_dict={}
    desc_dict={}
    feedback = {}

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'queryForm':
            user_input_query = request.POST.get('query')
            result_dict, desc_dict=mainGetRankDocs(user_input_query)
            feedback = {key: 1 for key in result_dict.keys()}
            with open('myapp/IRMODEL/pr/feedback.json', 'w') as json_file:
                json.dump(feedback, json_file, indent=2)

        if form_type == 'feedbackForm':
            with open('myapp/IRMODEL/pr/feedback.json') as json_file:
                feedback = json.load(json_file)

            user_feedback = request.POST.get('changes')
            user_feedback=json.loads(user_feedback)

            # Update new_dict based on user_feedback
            for key, value in user_feedback.items():
                if key in feedback:
                    feedback[key] = value

            generate_pr_curve(feedback)
            print("P-R Curve generated in myapp/IRMODEL/pr as PR_curve.png")
            result_dict={}
            desc_dict={}

    return render(request, 'myapp/index.html', {'form': form, 'query': 'Loops in C++', 'docs':result_dict, 'desc':desc_dict, 'feedback':feedback})

