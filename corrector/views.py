from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import FormView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Correction
from .forms import TextCorrectionForm
from .utils import correct_text_with_ai


class TextCorrectionView(LoginRequiredMixin, FormView):
    template_name = 'corrector/correct_text.html'
    form_class = TextCorrectionForm

    def form_valid(self, form):
        original_text = form.cleaned_data['original_text']
        corrected_text, explanation = correct_text_with_ai(original_text)
        if corrected_text:
            Correction.objects.create(
                user=self.request.user,
                original_text=original_text,
                corrected_text=corrected_text,
                explanation=explanation
            )
        return self.render_to_response(self.get_context_data(
            form=form,
            corrected_text=corrected_text,
            explanation=explanation,
        ))


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

