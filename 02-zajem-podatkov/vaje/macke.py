import csv
import os
import requests
import re

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definirajte URL glavne strani bolhe za oglase z mačkami
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
# mapa, v katero bomo shranili podatke
cat_directory = 'zajeti_podatki'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'index.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'macke.csv'


def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url) 
    except requests.exceptions.ConnectionError: # Exceptions bi ulovil vse možne napake, npr. da koda ni dobro napisana, napake pri izvajanju, napačen html
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(f"Napaka pri povezovanju na {url}")
        return None
    # nadaljujemo s kodo če ni prišlo do napake

    # satus code nam pove kak je bil odgovor [200], [300] itd. 
    # requests.codes.ok so vsi tisti, ki so dobri
    if page_content.status_code == requests.codes.ok: 
        return page_content.text
    else:
        print(f"Napaka pri prenosu strani {url}")
        return None


def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""

    html = download_url_to_string(page)
    if html: # različno od None
        save_string_to_file(html, directory, filename)
    return None
    


###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
<<<<<<< HEAD
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    with open(os.path.join(directory, filename), encoding="utf-8") as f: #os.path... spravi na prav directory, Nastavit encoding
        return f.read()
=======
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
    raise NotImplementedError()
>>>>>>> profrepo/master


# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(page_content):
<<<<<<< HEAD
    """Funkcija poišče posamezne ogllase, ki se nahajajo v spletni strani in
    vrne njih seznam"""
    pattern = re.compile(r'<li class="EntityList-item EntityList-item--Regular(.*?)</article>', re.DOTALL)
    ads = re.findall(pattern, page_content)
    return ads
=======
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne seznam oglasov."""
    raise NotImplementedError()
>>>>>>> profrepo/master


# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, lokaciji, datumu objave in ceni v oglasu.


def get_dict_from_ad_block(block):
    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, ceni
<<<<<<< HEAD
    in opisu ter vrne slovar, ki vsebuje ustrezne podatke
    """
    pattern = r'alt="(?P<naslov_oglasa>(.*?))"' # groupdict
    result = re.search(pattern, block, re.DOTALL)
    return result.groupdict()

=======
    in opisu ter vrne slovar, ki vsebuje ustrezne podatke."""
    raise NotImplementedError()
>>>>>>> profrepo/master


# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    data = read_file_to_string(directory, filename)
    ad_blocks = page_to_ads(data)

    return [
        get_dict_from_ad_block(ad) for ad in ad_blocks
    ]

###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""
    # Stavek assert preveri da zahteva velja
    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju
    assert ads and (all(j.keys() == ads[0].keys() for j in ads)) # ads ni None in ključ ni None
    write_csv(ads[0].keys(), ads, directory, filename)


# Celoten program poženemo v glavni funkciji

def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    # Najprej v lokalno datoteko shranimo glavno stran # to rabimo shranit samo enkrat
            # save_frontpage(cats_frontpage_url, cat_directory, frontpage_filename)
    # Iz lokalne (html) datoteke preberemo podatke

<<<<<<< HEAD
    sez_ads = ads_from_file(frontpage_filename, cat_directory)
=======
    # Podatke preberemo v lepšo obliko (seznam slovarjev)
>>>>>>> profrepo/master

    # Podatke prebermo v lepšo obliko (seznam slovarjev)
        # Naret v ads_from_file
    # Podatke shranimo v csv datoteko
<<<<<<< HEAD
    write_cat_ads_to_csv(sez_ads, cat_directory, csv_filename)
    # Dodatno: S pomočjo parameteov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prense (četudi že obstaja)
=======

    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
>>>>>>> profrepo/master
    # in enako za pretvorbo


if __name__ == '__main__':
    main()
