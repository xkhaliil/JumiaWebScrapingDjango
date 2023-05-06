from django.shortcuts import render
import requests 
from bs4 import BeautifulSoup  

def search(request):
    # Liste des options de marque
    brand_options = ["Apple", "Benco", "Evertek", "Huawei", "I-PLUS", "Iku", "Ila", "Infinix", "Inkax", "iPlus", "Itel", "Lenovo", "Logicom", "Nokia", "Oale", "One Plus", "OnePlus", "Oppo", "Oukitel", "Redmi", "Samsung", "Sans Marque", "Schneider", "Smart", "smartec", "TCL", "Techno", "Tecno", "Vivo", "XIAOMI"]
    
    # Récupérer la marque sélectionnée et le prix maximum
    selected_brand = request.POST.get('brand', 'Apple') 
    max_price = request.POST.get('max_price', '0') 
    
    # URL à partir de laquelle les données sont extraites
    url = f'https://www.jumia.com.tn/smartphones/{selected_brand}/?price=0-{max_price}#catalog-listing'
    
    # Récupération des données du site web
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    # Initialisation d'une liste pour stocker les informations des produits
    products = []
    
    # Extraction des données de chaque produit
    for product in soup.find_all('article', class_='prd _fb col c-prd'):
        name = product.find('h3', class_='name').get_text(strip=True)
        price = product.find('div', class_='prc').get_text(strip=True)
        link = product.find('a', class_='core')['href']
        brand = product.find('a', class_='core')['data-brand']
        image = product.find('img',class_='img')['data-src']
        products.append({'name': name, 'price': price, 'link': link, 'brand': brand, 'image': image})
    
    # Création d'un contexte pour transmettre les données à la vue
    context = {'products': products, 'brand_options': brand_options, 'selected_brand': selected_brand,'selected_max_price': max_price }
    
    # Rendu de la vue avec les données extraites
    return render(request, 'search.html', context)
