# squid-sundial

This is the Squid image I use to selectively redirect children's browsing through separate proxies.  I uploaded it here because it is apparently useful to my co-workers for other reasons.

## To just run a normal Squid proxy on port 3129, use...

* `docker run --name squid-sundial -p 3129:3129 gnomon/squid-sundial:1.0`

## To selectively send traffic for certain domains to other proxy servers...

* Create a *peerproxy.yml* file with your preferences (see below).

* `docker run --name squid-sundial -p 3129:3129 -v peerproxy.yml:/peerproxy.yml:ro gnomon/squid-sundial:1.0`

### Log file content

* Forwarded requests should look like this.

```1599206741.934 2020-09-04-0805.41    321 172.17.0.1:45512 TCP_MISS/301 455 GET http://www.dilbert.com/ - FIRSTUP_PARENT/proxy0.local.example.com:3128 text/html```

### YAML format for *peerproxy.yml*

```
---
neighbors:
  - name: neighborhood0
    proxy: proxy0.local.example.com
    proxyport: 3128
    destinations:
      - www.dilbert.com  # without a leading dot, it is a host
      - .acquisition.gov    # with a leading dot, it is a domain
  - name: neighborhood1
    proxy: proxy1.local.example.com
    proxyport: 3128
    destinations:
      - .local.mydomain.com
```

