import sqlite3
import xml.etree.ElementTree as ET

def parse_product_catalog(xml_file):
    """Parse an XML product catalog and return a list of product dictionaries."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    products = []
    for product_element in root.findall('dokuments'):
        # Extract product data
        product = {
            'id': product_element.get('id'),
            'nosaukums': product_element.find('nosaukums').text,
            'apraksts': product_element.find('apraksts').text,
            'atbstr': product_element.find('atbstr').text,
            'datums': product_element.find('datums').text,
            'saite': product_element.find('saite').text,
            'fails': product_element.find('fails').text,
            'lasisana': product_element.find('lasisana').text,
            'svarigums': product_element.find('svarigums').text,
            'kategorija': product_element.find('kategorija').text,
            'aktivs': product_element.find('aktivs').text

        }
        products.append(product)
    #print(products)
    return products


products = parse_product_catalog('catalog.xml')
#print (products)
conn = sqlite3.connect('catalog.db')
cursor = conn.cursor()


for product in products:
    #print(f"\nProduct: {product['dokuments']}")
    print(f"\n  ID: {product['id']}")
    print(f"  Nosaukums: {product['nosaukums']}")
    print(f"  Apraksts: {product['apraksts']}")
    print(f"  Atbildīgā struktūrvienība: {product['atbstr']}")
    print(f"  Izveides datums: {product['datums']}")
    print(f"  Saite (URL) uz dokumentu: {product['saite']}")
    print(f"  Faila tips: {product['fails']}")
    print(f"  Aptuvenais lasīšanas laiks: {product['lasisana']}")
    print(f"  Svarīguma līmenis: {product['svarigums']}")
    print(f"  Kategorija: {product['kategorija']}")
    print(f"  Aktīvs statuss: {product['aktivs']}")
    cursor.execute("INSERT INTO CATALOG VALUES ('"+product['id']+"', '"+product['nosaukums']+"', '"+product['apraksts']+"', '"+product['atbstr']+"', '"+product['datums']+"', '"+product['saite']+"', '"+product['fails']+"', '"+product['lasisana']+"', '"+product['svarigums']+"', '"+product['kategorija']+"', '"+product['aktivs']+"')")



#conn = sqlite3.connect('catalog.db')
#cursor = conn.cursor()
#cursor.execute("INSERT INTO CATALOG VALUES ('')")
conn.commit()
conn.close()
