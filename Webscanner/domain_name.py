from tld import get_tld



def get_domain_name(url):
    get_domain = get_tld(url, as_object=True)
    domain_name = get_domain.fld
    return domain_name
    
#name= input('Enter domain name: ')
url = input('Enter url: ') 
print(get_domain_name(url))