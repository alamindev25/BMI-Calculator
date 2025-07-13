from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.POST.get('weight'))
        feet = float(request.POST.get('feet'))
        inch = float(request.POST.get('inch'))

        
        total_inches = (feet * 12) + inch
        height = total_inches * 2.54 / 100  # convert to meters

        
        bmi = weight / (height ** 2)

        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render(request, 'calculator/index.html', {
        'bmi': bmi,
        'category': category
    })
