from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Correction
from .forms import TextCorrectionForm
from .utils import correct_text_with_ai

@login_required
def correct_text(request):
    if request.method == 'POST':
        form = TextCorrectionForm(request.POST)
        if form.is_valid():
            original_text = form.cleaned_data['original_text']
            corrected_text, explanation = correct_text_with_ai(original_text)
            if corrected_text:
                Correction.objects.create(
                    user=request.user,
                    original_text=original_text,
                    corrected_text=corrected_text,
                    explanation=explanation
                )
                return render(request, 'corrector/correct_text.html', {
                    'form': form,
                    'corrected_text': corrected_text,
                    'explanation': explanation,
                })
    else:
        form = TextCorrectionForm()

    return render(request, 'corrector/correct_text.html', {'form': form})


@login_required
def history(request):
    corrections = Correction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'corrector/history.html', {'corrections': corrections})


@login_required
def rate_correction(request, correction_id):
    correction = get_object_or_404(Correction, id=correction_id, user=request.user)
    if request.method == "POST":
        rating = request.POST.get("rating")
        if rating:
            correction.rating = int(rating)
            correction.save()
            return redirect("history")
    return render(request, 'corrector/rate_correction.html', {"correction": correction})
