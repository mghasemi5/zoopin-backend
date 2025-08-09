from django.shortcuts import render, redirect
from api.models import Partner
from django.contrib.admin.views.decorators import staff_member_required
from .forms import PartnerForm
from api.models import InfoBlock,logos, insights,testimonials,slider
from .forms import InfoBlockForm,logoForm,insightForm,testimonialForm,sliderForm


@staff_member_required
def slider_page(request):
    blocks = slider.objects.all()
    return render(request, 'dashboard/slider.html', {'blocks': blocks})

@staff_member_required
def add_slider(request):
    if request.method == 'POST':
        form = sliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slider')
    else:
        form = sliderForm()
    return render(request, 'dashboard/add_slider.html', {'form': form})

@staff_member_required
def edit_slider(request, pk):
    block = get_object_or_404(slider, pk=pk)
    if request.method == 'POST':
        form = sliderForm(request.POST, request.FILES, instance=block)
        if form.is_valid():
            form.save()
            return redirect('slider')
    else:
        form = sliderForm(instance=block)
    return render(request, 'dashboard/edit_testimonial.html', {'form': form, 'block': block})

@staff_member_required
def delete_slider(request, pk):
    block = get_object_or_404(slider, pk=pk)
    if request.method == 'POST':
        block.delete()
        return redirect('slider')
    return render(request, 'dashboard/delete_slider.html', {'block': block})

@staff_member_required
def testimonials_page(request):
    blocks = testimonials.objects.all()
    return render(request, 'dashboard/testimonials.html', {'blocks': blocks})

@staff_member_required
def add_testimonial(request):
    if request.method == 'POST':
        form = testimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = testimonialForm()
    return render(request, 'dashboard/add_testimonial.html', {'form': form})

@staff_member_required
def edit_testimonial(request, pk):
    block = get_object_or_404(testimonials, pk=pk)
    if request.method == 'POST':
        form = testimonialForm(request.POST, request.FILES, instance=block)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = testimonialForm(instance=block)
    return render(request, 'dashboard/edit_testimonial.html', {'form': form, 'block': block})

@staff_member_required
def delete_testimonial(request, pk):
    block = get_object_or_404(testimonials, pk=pk)
    if request.method == 'POST':
        block.delete()
        return redirect('testimonials')
    return render(request, 'dashboard/delete_testimonial.html', {'block': block})

@staff_member_required
def insights_page(request):
    blocks = insights.objects.all()
    return render(request, 'dashboard/insights.html', {'blocks': blocks})

@staff_member_required
def add_insight(request):
    if request.method == 'POST':
        form = insightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('insights')
    else:
        form = insightForm()
    return render(request, 'dashboard/add_insight.html', {'form': form})

@staff_member_required
def edit_insight(request, pk):
    block = get_object_or_404(insights, pk=pk)
    if request.method == 'POST':
        form = insightForm(request.POST, request.FILES, instance=block)
        if form.is_valid():
            form.save()
            return redirect('insights')
    else:
        form = insightForm(instance=block)
    return render(request, 'dashboard/edit_insight.html', {'form': form, 'block': block})

@staff_member_required
def delete_insight(request, pk):
    block = get_object_or_404(insights, pk=pk)
    if request.method == 'POST':
        block.delete()
        return redirect('insights')
    return render(request, 'dashboard/delete_insight.html', {'block': block})

@staff_member_required
def logos_page(request):
    logos_ch = logos.objects.all()
    return render(request, 'dashboard/logos.html', {'logos': logos_ch})

@staff_member_required
def add_logos(request):
    if request.method == 'POST':
        form = logoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logos')
    else:
        form = logoForm()
    return render(request, 'dashboard/add_logos.html', {'form': form})

@staff_member_required
def edit_logos(request, pk):
    logos_ch = get_object_or_404(logos, pk=pk)
    if request.method == 'POST':
        form = logoForm(request.POST, request.FILES, instance=logos_ch)
        if form.is_valid():
            form.save()
            return redirect('logos')
    else:
        form = InfoBlockForm(instance=logos_ch)
    return render(request, 'dashboard/edit_logos.html', {'form': form, 'logos': logos_ch})

@staff_member_required
def delete_logos(request, pk):
    logos_ch = get_object_or_404(logos, pk=pk)
    if request.method == 'POST':
        logos_ch.delete()
        return redirect('logos')
    return render(request, 'dashboard/delete_logos.html', {'logos': logos})


@staff_member_required
def infoblocks_page(request):
    blocks = InfoBlock.objects.all()
    return render(request, 'dashboard/infoblocks.html', {'blocks': blocks})

@staff_member_required
def add_infoblock(request):
    if request.method == 'POST':
        form = InfoBlockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('infoblocks')
    else:
        form = InfoBlockForm()
    return render(request, 'dashboard/add_infoblock.html', {'form': form})

@staff_member_required
def edit_infoblock(request, pk):
    block = get_object_or_404(InfoBlock, pk=pk)
    if request.method == 'POST':
        form = InfoBlockForm(request.POST, request.FILES, instance=block)
        if form.is_valid():
            form.save()
            return redirect('infoblocks')
    else:
        form = InfoBlockForm(instance=block)
    return render(request, 'dashboard/edit_infoblock.html', {'form': form, 'block': block})

@staff_member_required
def delete_infoblock(request, pk):
    block = get_object_or_404(InfoBlock, pk=pk)
    if request.method == 'POST':
        block.delete()
        return redirect('infoblocks')
    return render(request, 'dashboard/delete_infoblock.html', {'block': block})


@staff_member_required
def dashboard_home(request):
    partners = Partner.objects.all()
    return render(request, 'dashboard/home.html', {'partners': partners})

@staff_member_required
def partners_page(request):
    partners = Partner.objects.all()
    return render(request, 'dashboard/partners.html', {'partners': partners})



@staff_member_required
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = PartnerForm()
    return render(request, 'dashboard/add_partner.html', {'form': form})
from django.shortcuts import get_object_or_404

@staff_member_required
def edit_partner(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'dashboard/edit_partner.html', {'form': form, 'partner': partner})

@staff_member_required
def delete_partner(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        partner.delete()
        return redirect('dashboard_home')
    return render(request, 'dashboard/delete_partner.html', {'partner': partner})
