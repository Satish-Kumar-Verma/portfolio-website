from django.shortcuts import render

# Create your views here.
def home(request):
    experiences = [
    {
        "company": "Cognizant, Mumbai",
        "period": "Sep 2016 - July 2020",
        "title": "Experience Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus nunc, posuere in justo vulputate, bibendum sodales."
    },
    {
        "company": "Cognizant, Mumbai",
        "period": "Sep 2016 - July 2020",
        "title": "Experience Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus nunc, posuere in justo vulputate, bibendum sodales."
    },
    {
        "company": "Cognizant, Mumbai",
        "period": "Sep 2016 - July 2020",
        "title": "Experience Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus nunc, posuere in justo vulputate, bibendum sodales."
    },
    {
        "company": "Cognizant, Mumbai",
        "period": "Sep 2016 - July 2020",
        "title": "Experience Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus nunc, posuere in justo vulputate, bibendum sodales."
    },
    {
        "company": "Cognizant, Mumbai Hla Min Naing",
        "period": "Sep 2016 - July 2020",
        "title": "Experience Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus nunc, posuere in justo vulputate, bibendum sodales."
    },
    ]
    testimonials = [
        {"name": "John Doe", "image": "client1.jpg", "message": "Amazing service!", "rating": 5},
        {"name": "Jane Smith", "image": "client2.jpg", "message": "Loved the attention to detail.", "rating": 4},
        {"name": "John Doe", "image": "client1.jpg", "message": "Amazing service!", "rating": 5},
        {"name": "Yoon Moh Moh Aung", "image": "client1.jpg", "message": "Amazing service!", "rating": 3},

    ]   
    for testimonial in testimonials:
        testimonial['rating_range'] = range(testimonial['rating'])
        testimonial['empty_range'] = range(5 - testimonial['rating'])

    context = {"experiences": experiences, "testimonials": testimonials}
    return render(request, "base.html", context)
