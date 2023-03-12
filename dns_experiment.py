import dns.name
import dns.resolver

# taking dnspython for a test drive:

# dns.name.Name test
def name_test():
# make domains
    base_domain = dns.name.from_text('python.org') # absolute domain
    blog_domain = dns.name.from_text('blog.python.org') # absolute domain
    specific_domain = dns.name.from_text('/2023/', origin=blog_domain) # absolute domain
    # relative_domain = dns.name.from_text('/2023/', origin=None)# relative domain (must specify origin=None)
    # print labels
    print(blog_domain.labels)
    print(specific_domain.labels)

    # is_subdomain / is_superdomain / parent
    print(blog_domain.is_subdomain(base_domain)) # true
    print(specific_domain.is_subdomain(blog_domain)) # true
    print(blog_domain.is_superdomain(base_domain)) # false
    print(base_domain.is_superdomain(blog_domain)) # true
    print(base_domain.parent())

    # relativize
    rel_domain = blog_domain.relativize(base_domain) # return name relative to given origin
    print(rel_domain)
    print(rel_domain.labels)

    # is absolute
    print(rel_domain.is_absolute())
    print(base_domain.is_absolute())

    # derelativize (concatenate relative name to origin)
    derel_domain = rel_domain.derelativize(origin=base_domain) # 
    print(derel_domain)

    # concatenate
    rel_domain2 = specific_domain.relativize(blog_domain)
    print(rel_domain2.labels) # '/2023/'
    print(rel_domain2.is_absolute())
    concat_domain = rel_domain2.concatenate(blog_domain) # '/2023/'.concatenate('blog.python.org')
    print(concat_domain.labels)
    print(concat_domain.is_absolute())

# rdata and rdataset

# dns messages

# dns queries over udp, tcp etc

# dns 

# dns stub resolver test
def resolver_test():
    url = "www.python.org"
    qtype = 'A' # alteratively 'A' 'CNAME' 'MX' 'NS' 'PTR' 
    result = dns.resolver.resolve(url, qtype, raise_on_no_answer=False) # returns dns.resolver.Answer
    if (result.rrset != None):
        for val in result.rrset:
            print(val) # ip's
    
    url = "www.python.org"
    qtype = 'CNAME' # alteratively 'A' 'CNAME' 'MX' 'NS' 'PTR' 
    result5 = dns.resolver.resolve(url, qtype, raise_on_no_answer=False) # returns dns.resolver.Answer
    if (result.rrset != None):
        for val in result5.rrset:
            print(val) # ip's

    result4 = dns.resolver.resolve("google.com", 'NS', raise_on_no_answer=False)
    if (result4.rrset != None):
        for val in result4.rrset:
            print(val)
    
    #result2 = dns.resolver.resolve('mail.google.com', 'MX', raise_on_no_answer=False)
    #for val in result2:
       #print(val)
    
    #result3 = dns.resolver.resolve 
if __name__ == "__main__":
    # name_test()
    resolver_test()

    