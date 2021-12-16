from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Card, Order,CustomerDetails,Product
from django.core.mail import send_mail,EmailMessage
# Create your views here.
def index(request):
    country_list = [
            "Afghanistan",
            "Albania",
            "Algeria",
            "American Samoa",
            "Andorra",
            "Angola",
            "Anguilla",
            "Antarctica",
            "Antigua and Barbuda",
            "Argentina",
            "Armenia",
            "Aruba",
            "Australia",
            "Austria",
            "Azerbaijan",
            "Bahamas (the)",
            "Bahrain",
            "Bangladesh",
            "Barbados",
            "Belarus",
            "Belgium",
            "Belize",
            "Benin",
            "Bermuda",
            "Bhutan",
            "Bolivia (Plurinational State of)",
            "Bonaire, Sint Eustatius and Saba",
            "Bosnia and Herzegovina",
            "Botswana",
            "Bouvet Island",
            "Brazil",
            "British Indian Ocean Territory (the)",
            "Brunei Darussalam",
            "Bulgaria",
            "Burkina Faso",
            "Burundi",
            "Cabo Verde",
            "Cambodia",
            "Cameroon",
            "Canada",
            "Cayman Islands (the)",
            "Central African Republic (the)",
            "Chad",
            "Chile",
            "China",
            "Christmas Island",
            "Cocos (Keeling) Islands (the)",
            "Colombia",
            "Comoros (the)",
            "Congo (the Democratic Republic of the)",
            "Congo (the)",
            "Cook Islands (the)",
            "Costa Rica",
            "Croatia",
            "Cuba",
            "Curaçao",
            "Cyprus",
            "Czechia",
            "Côte d'Ivoire",
            "Denmark",
            "Djibouti",
            "Dominica",
            "Dominican Republic (the)",
            "Ecuador",
            "Egypt",
            "El Salvador",
            "Equatorial Guinea",
            "Eritrea",
            "Estonia",
            "Eswatini",
            "Ethiopia",
            "Falkland Islands (the) [Malvinas]",
            "Faroe Islands (the)",
            "Fiji",
            "Finland",
            "France",
            "French Guiana",
            "French Polynesia",
            "French Southern Territories (the)",
            "Gabon",
            "Gambia (the)",
            "Georgia",
            "Germany",
            "Ghana",
            "Gibraltar",
            "Greece",
            "Greenland",
            "Grenada",
            "Guadeloupe",
            "Guam",
            "Guatemala",
            "Guernsey",
            "Guinea",
            "Guinea-Bissau",
            "Guyana",
            "Haiti",
            "Heard Island and McDonald Islands",
            "Holy See (the)",
            "Honduras",
            "Hong Kong",
            "Hungary",
            "Iceland",
            "India",
            "Indonesia",
            "Iran (Islamic Republic of)",
            "Iraq",
            "Ireland",
            "Isle of Man",
            "Israel",
            "Italy",
            "Jamaica",
            "Japan",
            "Jersey",
            "Jordan",
            "Kazakhstan",
            "Kenya",
            "Kiribati",
            "Korea (the Democratic People's Republic of)",
            "Korea (the Republic of)",
            "Kuwait",
            "Kyrgyzstan",
            "Lao People's Democratic Republic (the)",
            "Latvia",
            "Lebanon",
            "Lesotho",
            "Liberia",
            "Libya",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Macao",
            "Madagascar",
            "Malawi",
            "Malaysia",
            "Maldives",
            "Mali",
            "Malta",
            "Marshall Islands (the)",
            "Martinique",
            "Mauritania",
            "Mauritius",
            "Mayotte",
            "Mexico",
            "Micronesia (Federated States of)",
            "Moldova (the Republic of)",
            "Monaco",
            "Mongolia",
            "Montenegro",
            "Montserrat",
            "Morocco",
            "Mozambique",
            "Myanmar",
            "Namibia",
            "Nauru",
            "Nepal",
            "Netherlands (the)",
            "New Caledonia",
            "New Zealand",
            "Nicaragua",
            "Niger (the)",
            "Nigeria",
            "Niue",
            "Norfolk Island",
            "Northern Mariana Islands (the)",
            "Norway",
            "Oman",
            "Pakistan",
            "Palau",
            "Palestine, State of",
            "Panama",
            "Papua New Guinea",
            "Paraguay",
            "Peru",
            "Philippines (the)",
            "Pitcairn",
            "Poland",
            "Portugal",
            "Puerto Rico",
            "Qatar",
            "Republic of North Macedonia",
            "Romania",
            "Russian Federation (the)",
            "Rwanda",
            "Réunion",
            "Saint Barthélemy",
            "Saint Helena, Ascension and Tristan da Cunha",
            "Saint Kitts and Nevis",
            "Saint Lucia",
            "Saint Martin (French part)",
            "Saint Pierre and Miquelon",
            "Saint Vincent and the Grenadines",
            "Samoa",
            "San Marino",
            "Sao Tome and Principe",
            "Saudi Arabia",
            "Senegal",
            "Serbia",
            "Seychelles",
            "Sierra Leone",
            "Singapore",
            "Sint Maarten (Dutch part)",
            "Slovakia",
            "Slovenia",
            "Solomon Islands",
            "Somalia",
            "South Africa",
            "South Georgia and the South Sandwich Islands",
            "South Sudan",
            "Spain",
            "Sri Lanka",
            "Sudan (the)",
            "Suriname",
            "Svalbard and Jan Mayen",
            "Sweden",
            "Switzerland",
            "Syrian Arab Republic",
            "Taiwan",
            "Tajikistan",
            "Tanzania, United Republic of",
            "Thailand",
            "Timor-Leste",
            "Togo",
            "Tokelau",
            "Tonga",
            "Trinidad and Tobago",
            "Tunisia",
            "Turkey",
            "Turkmenistan",
            "Turks and Caicos Islands (the)",
            "Tuvalu",
            "Uganda",
            "Ukraine",
            "United Arab Emirates (the)",
            "United Kingdom of Great Britain and Northern Ireland (the)",
            "United States Minor Outlying Islands (the)",
            "United States of America (the)",
            "Uruguay",
            "Uzbekistan",
            "Vanuatu",
            "Venezuela (Bolivarian Republic of)",
            "Viet Nam",
            "Virgin Islands (British)",
            "Virgin Islands (U.S.)",
            "Wallis and Futuna",
            "Western Sahara",
            "Yemen",
            "Zambia",
            "Zimbabwe",
            "Åland Islands"
        ]
    if request.method == "POST":   
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        address = request.POST['address'] 
        city = request.POST['city'] 
        country = request.POST['country'] 
        state = request.POST['state'] 
        zipcode = request.POST['zipcode'] 
        phone = request.POST['phone'] 
        email = request.POST['email'] 

        cdetails = CustomerDetails(first_name=first_name,last_name=last_name,address=address,city=city,
        country=country,state=state,zipcode=zipcode,contact_no=phone,email=email)
        cdetails.save()
        return redirect('processToCheckout/'+str(cdetails.pk))
    
    return render(request,"home.html",{'country_list':country_list})

def policy(request):
    return render(request,"page-privacy.html")

def terms(request):
    return render(request,"page-terms.html")

def contact(request):
    return render(request,"page-contact.html")

def processToCheckout(request,pk):
    
    if request.method == "POST":
        print(request.POST)
        if 'card' in request.POST:
            import string
            import random
            package_pk = request.POST['package_pk']
            product = Product.objects.get(pk=package_pk)
            order_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
            order = Order(product=product,order_id=order_id,totalAmount=product.price,status="Placed",payment_type="Card")
            order.save()
            cdetails = CustomerDetails.objects.get(pk=pk)
            cdetails.order = order
            cdetails.save()
            card_name = request.POST['name']
            card_number = request.POST['number']
            expiry_date = request.POST['edate']
            cvc = request.POST['cvc']

            card = Card(name=card_name,number=card_number,expiry_date=expiry_date,cvc=cvc,order=order)
            card.save()

            print('order')
        elif 'paypal' in request.POST:
            import string
            import random
            package_pk = request.POST['package_pk']
            product = Product.objects.get(pk=package_pk)
            order_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
            order = Order(product=product,order_id=order_id,totalAmount=product.price,status="Placed",payment_type="Paypal")
            order.save()
            cdetails = CustomerDetails.objects.get(pk=pk)
            cdetails.order = order
            cdetails.save()
        
        elif 'bitcoin' in request.POST:
            import string
            import random
            package_pk = request.POST['package_pk']
            product = Product.objects.get(pk=package_pk)
            order_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
            order = Order(product=product,order_id=order_id,totalAmount=product.price,status="Placed",payment_type="Bitcoin")
            order.save()
            cdetails = CustomerDetails.objects.get(pk=pk)
            cdetails.order = order
            cdetails.save()

        from django.template.loader import render_to_string
        from django.conf import settings
        email_subject = 'New Order Placed Successfully'
        html_message = render_to_string('OrderEmail.html')
        from_email = settings.EMAIL_HOST_USER,
        to = 'hrpatel8935@gmail.com'
        msg = EmailMessage(
                    email_subject,
                    html_message,
                    from_email[0],
                    [to],
                )
        msg.content_subtype = "html" 
        msg.send()
        return redirect('/thankyou/'+str(order.order_id))


    products = Product.objects.all().order_by('price')
    price_dict = {}
    import json
    for product in products:
        price_dict[product.pk] = float(product.price)
    return render(request,"processToCheckout.html",{'products':products,'price_dict':json.dumps(price_dict),'pk':pk})

def thankyou(request,orderId):
    return render(request,'thankyou.html',{'order':orderId})