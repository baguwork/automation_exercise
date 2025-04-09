import requests

cookies = {
    'geo_ip': '2a09:bac1:5560::20a:29',
    'adidas_country': 'us',
    'geo_country': 'NL',
    'geo_state': '',
    'onesite_country': 'US',
    'gl-feat-enable': 'CHECKOUT_PAGES_ENABLED',
    'geo_coordinates': 'lat=52.35, long=4.92',
    'badab': 'true',
    'akacd_phased_PLP': '3921379539~rv=66~id=94ac7c08d99e4e9c23cf23c8bc9d4681',
    'bm_ss': 'ab8e18ef4e',
    'bm_so': 'D9074E3733B2BA015F07E52974F731E7BB2366D4B18E2C9D7C79F1BE2DB85AEF~YAAQSIoUAuTi7faVAQAAM0giCgPVAc5IBQx5TS+Lp74LEokfO5ZcfRVbaVAPP7zCeG3uSBoOCPLyeLOQBTP7BVJFtunNOF6lavIbkkvUszoRU06X4pCRjjRtacqqxdrhWVNOgO3MnReI8BmJvdrZ7YJS4tmD4HKgv6UZEB82NG6xGa+QCmp0v+Fod50Vr2CldQpy5jzO9aInzxShLewoacPbbFV/1xmcgGZASbKKxQPr1AFSyZLKmmfnyBbEhPYf9paBqNY7VK5RQnq2wZIxdukA+WHZZ/35rE+XE4SSrccVTKlAdhipmuaMmbaPgA8kpwu4rlM3vVnAJiVplQBFdJc3fofTONSi8RlOl/o1gpAvzn48Vf6obZuIa8Tdw3keO2eKZ+viIJhT4rZkzU5NcAQPYEldecNHhDKRvuxyshZ6B4f3djhvmjMNp7zczp/Zbg8h3F6HIO6/+rk3HVVUNI+A2dWLvWE=',
    'bm_sz': '1CD6AAECC711391686631DB77C0AAE3F~YAAQSIoUAuXi7faVAQAAM0giChvwi4tS12RDWMNgvBJRNtePcmDuXO5j9csa4JRolMb4wLexcMcN4jSCC+ML+0GOI/xpnVFi2r12yh8xuAxoHZM9NwxVjMf/HsG5+dXU2Q4Q8ONWlS6aLmhoEcSIVgXYuC2mrDdW3PM4gKTvyWAY64Ms0+BHVwvE0hH8sYzX4fdzaCXp6rNCnTtnuQ7IcywqFumNIUmR9MKElw4SgIVpdHYiAlqxUlENtJ++tFYqM/x21vyvDtjpV019kmAn5q+tARDIqqaYnift3f353I1OMfgVubN/BPsLLctEfXWt94Gw+Xv7sSFwNZylati8XTvEHCCOnws+/QtnHbg7ZvlCeSbA2yDMoFULFe8mOLO0R3bSW/8aIwe4GkinIkB2Ea3WV67Dz2h+zlnazpdkLM2Vo6eQOEtn~3294512~4408645',
    'akacd_Phased_www_adidas_com_Generic': '3921379540~rv=34~id=52bef9560979ed9240767d830ecc3e6e',
    'bm_lso': 'D9074E3733B2BA015F07E52974F731E7BB2366D4B18E2C9D7C79F1BE2DB85AEF~YAAQSIoUAuTi7faVAQAAM0giCgPVAc5IBQx5TS+Lp74LEokfO5ZcfRVbaVAPP7zCeG3uSBoOCPLyeLOQBTP7BVJFtunNOF6lavIbkkvUszoRU06X4pCRjjRtacqqxdrhWVNOgO3MnReI8BmJvdrZ7YJS4tmD4HKgv6UZEB82NG6xGa+QCmp0v+Fod50Vr2CldQpy5jzO9aInzxShLewoacPbbFV/1xmcgGZASbKKxQPr1AFSyZLKmmfnyBbEhPYf9paBqNY7VK5RQnq2wZIxdukA+WHZZ/35rE+XE4SSrccVTKlAdhipmuaMmbaPgA8kpwu4rlM3vVnAJiVplQBFdJc3fofTONSi8RlOl/o1gpAvzn48Vf6obZuIa8Tdw3keO2eKZ+viIJhT4rZkzU5NcAQPYEldecNHhDKRvuxyshZ6B4f3djhvmjMNp7zczp/Zbg8h3F6HIO6/+rk3HVVUNI+A2dWLvWE=^1743926741854',
    'akacd_phased_PDP': '3921379540~rv=92~id=e2a1c1dadce295152b5bf847635ecc8f',
    'mt.v': '2.032250148.1743926742058',
    'channelflow': 'nonpaid|other|1746518742330',
    'channeloriginator': 'nonpaid',
    'channelcloser': 'nonpaid',
    'x-browser-id': '96cab051-8997-4f23-abc1-941ff9913885',
    'x-session-id': '999aaffd-0a93-4c56-b742-284a552ff015',
    'ab_qm': 'b',
    'AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg': '1',
    'x-commerce-next-id': '7fbe0582-cd65-4869-bde4-565d83a6c10c',
    'AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20185%7CMCMID%7C88162336796767313862574451284687595910%7CMCAAMLH-1744531543%7C6%7CMCAAMB-1744531543%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1743933943s%7CNONE%7CMCAID%7CNONE',
    's_cc': 'true',
    'mt.sc': '%7B%22i%22%3A1743926744036%2C%22d%22%3A%5B%5D%7D',
    'RT': '"z=1&dm=adidas.com&si=150db5d0-77e0-498f-8765-cb9f4c38f30d&ss=m95cyd86&sl=1&tt=tq&bcn=%2F%2F684dd32e.akstat.io%2F&ld=39h"',
    'notice_preferences': '%5B0%5D',
    'RT': '"z=1&dm=adidas.com&si=150db5d0-77e0-498f-8765-cb9f4c38f30d&ss=m95cyd86&sl=1&tt=tq&bcn=%2F%2F684dd32e.akstat.io%2F&ld=39h"',
    'ak_bmsc': '54313F20D2D4908BE3613F48159EB053~000000000000000000000000000000~YAAQSIoUAoTn7faVAQAAH6ciChtP+vZYPSZuowdhNvko+F+yXqBccA4gmS8s9qi+ziX6ZEZhZG3Mev3cUobgduaZNvETWkOa7Tdo/l7r7thkyXTuuM8RgqXbaARnpt6kIZD+1Cxld0q9pdhg7HEh4oAt4e9elPyXYsygGMZiEnBzq93eMLlvBKkTJdwLChAfY9MCiLv0bFw3xzUoScKyno/aBUYaQlZgF3kXoFdVIrREQd+Fwkodtg3c+aHB73wVzN86h40PsG5VYPS0vXnj1yxB81ZF2LWN0a0TvrEwm3Ew4FDvetNUatOonWX/QwKq8OyS+snGMx89bw5bYCPq8IyJOpHLf0oOI8WOBI9/ij10TQyIgqk0vyafuhBbWksQkNBnFX7i89s741Hh09aZjWwzHQ==',
    'utag_main': 'v_id:01960a224d2e00000e2909563a260506f002606700978$_sn:1$_se:6%3Bexp-session$_ss:0%3Bexp-session$_st:1743928565485%3Bexp-session$ses_id:1743926742319%3Bexp-session$_pn:1%3Bexp-session$_vpn:2%3Bexp-session$_prevpage:PLP%7CG_MEN%7CPR_CLOTHING%7CPRI_10.0%3CPRICE%3C72.0%3Bexp-1743930365490',
    's_pers': '%20s_vnum%3D1746050400063%2526vn%253D1%7C1746050400063%3B%20pn%3D1%7C1746518754261%3B%20s_invisit%3Dtrue%7C1743928565493%3B',
    's_sess': '%5B%5BB%5D%5D',
    '_abck': '8707E4286C23BCE10A9BD6A2BC7F97E1~-1~YAAQSIoUArLn7faVAQAA8agiCg3oR8+ZJvES2WWcEABAXvFlPeypIOGnMMT605Uox2u2mxWsVpJz3ypjh3EF70hKD2h9iES5VzIocSWGdyxFI6lqNrLBY1sU0aFYhaYC+6qdhH3oOw25RGlLgQn6Afh/K+8hI5VyApuBIWQ+cByQFaiD2L93xDoDFUXeFtJta23FE/lSwr64bveo+6hNOZrc4zs/1r8Xc6jwbTY3BrKMZIQ5VcHPmg4OYlRwJ6o7byxHapiXB/BVbvSJnl0VBpw2kWX2zXwReTyMeWmX8LSghdzM/R2I5pgxgAQurBUxi9QsnSqkvnEjdZ5loRJPRJb/MJY0Pp5fnU/S+t5oLuXl5sYWcOaYau1SPgKor4tzre8T8BklbnoLqLGW1NKm4Il1np294/XFjwmyo34jDM8Mrf5XFn3HW/ji96wuA7FCwjkK+6DtUOUBZhBwRNXySVgyHhPQrFNXGrr/rhWM5+kcfiWHkcalIeS7PW4CCxpcAw8kmYCmYkiVevCqBfL5mNZhdl8vYAxnwIRlfvtDNBMmucF1ycXWk8t8WzM883hGnP4UBXZRx3FGWcR8CobA0si39MI8UPOYQUfZUcNl~-1~-1~1743930341',
    'bm_s': 'YAAQSIoUAtjn7faVAQAADKsiCgPxA9lv34HlLZbvD72706Qow9V+/gkOwqKcYLtSjBV55gud3DehLGBbDdVTWFUzeehDW2ZuyIGfKOIqueaGlpn9qKW5gSCBmIqNaJLiIO84uE50Dan9gEgk/TgyEmeXHgH6cTM2Flp38O+ErRvyZO2zxUwrJhKRVs9hunM/UO75bNx73ava4IgfcdXZJr4lpk9z6dpQb9qib3YtJB2E4hGmC3M+20+IBVwEQlsj23Xwr7VuZ+gSZKpoyW6rnab/Olwe8OcJHe1OhmIYafM7uW5+Acy5fS/1p1nKCpbvy3ETAJoYi4hJBSnWQmyCJhp3R/EA+csLoteuzo89UrYFfaH+lzEkn9hLMjqtmjPgp1oKaa9L+eT18qLcMsyaPYylR3tFIJVMFtJX3DaAnGNhvPX8YExLTrdt8GKjhnEqeYGK4RFkG/i6tOg=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'priority': 'u=1, i',
    'referer': 'https://www.adidas.com/us/men-clothing?price_max=72&price_min=10',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-instana-l': '1,correlationType=web;correlationId=16e7e5c3512fd05a',
    'x-instana-s': '16e7e5c3512fd05a',
    'x-instana-t': '16e7e5c3512fd05a',
    'x-nextjs-data': '1',
    # 'cookie': 'geo_ip=2a09:bac1:5560::20a:29; adidas_country=us; geo_country=NL; geo_state=; onesite_country=US; gl-feat-enable=CHECKOUT_PAGES_ENABLED; geo_coordinates=lat=52.35, long=4.92; badab=true; akacd_phased_PLP=3921379539~rv=66~id=94ac7c08d99e4e9c23cf23c8bc9d4681; bm_ss=ab8e18ef4e; bm_so=D9074E3733B2BA015F07E52974F731E7BB2366D4B18E2C9D7C79F1BE2DB85AEF~YAAQSIoUAuTi7faVAQAAM0giCgPVAc5IBQx5TS+Lp74LEokfO5ZcfRVbaVAPP7zCeG3uSBoOCPLyeLOQBTP7BVJFtunNOF6lavIbkkvUszoRU06X4pCRjjRtacqqxdrhWVNOgO3MnReI8BmJvdrZ7YJS4tmD4HKgv6UZEB82NG6xGa+QCmp0v+Fod50Vr2CldQpy5jzO9aInzxShLewoacPbbFV/1xmcgGZASbKKxQPr1AFSyZLKmmfnyBbEhPYf9paBqNY7VK5RQnq2wZIxdukA+WHZZ/35rE+XE4SSrccVTKlAdhipmuaMmbaPgA8kpwu4rlM3vVnAJiVplQBFdJc3fofTONSi8RlOl/o1gpAvzn48Vf6obZuIa8Tdw3keO2eKZ+viIJhT4rZkzU5NcAQPYEldecNHhDKRvuxyshZ6B4f3djhvmjMNp7zczp/Zbg8h3F6HIO6/+rk3HVVUNI+A2dWLvWE=; bm_sz=1CD6AAECC711391686631DB77C0AAE3F~YAAQSIoUAuXi7faVAQAAM0giChvwi4tS12RDWMNgvBJRNtePcmDuXO5j9csa4JRolMb4wLexcMcN4jSCC+ML+0GOI/xpnVFi2r12yh8xuAxoHZM9NwxVjMf/HsG5+dXU2Q4Q8ONWlS6aLmhoEcSIVgXYuC2mrDdW3PM4gKTvyWAY64Ms0+BHVwvE0hH8sYzX4fdzaCXp6rNCnTtnuQ7IcywqFumNIUmR9MKElw4SgIVpdHYiAlqxUlENtJ++tFYqM/x21vyvDtjpV019kmAn5q+tARDIqqaYnift3f353I1OMfgVubN/BPsLLctEfXWt94Gw+Xv7sSFwNZylati8XTvEHCCOnws+/QtnHbg7ZvlCeSbA2yDMoFULFe8mOLO0R3bSW/8aIwe4GkinIkB2Ea3WV67Dz2h+zlnazpdkLM2Vo6eQOEtn~3294512~4408645; akacd_Phased_www_adidas_com_Generic=3921379540~rv=34~id=52bef9560979ed9240767d830ecc3e6e; bm_lso=D9074E3733B2BA015F07E52974F731E7BB2366D4B18E2C9D7C79F1BE2DB85AEF~YAAQSIoUAuTi7faVAQAAM0giCgPVAc5IBQx5TS+Lp74LEokfO5ZcfRVbaVAPP7zCeG3uSBoOCPLyeLOQBTP7BVJFtunNOF6lavIbkkvUszoRU06X4pCRjjRtacqqxdrhWVNOgO3MnReI8BmJvdrZ7YJS4tmD4HKgv6UZEB82NG6xGa+QCmp0v+Fod50Vr2CldQpy5jzO9aInzxShLewoacPbbFV/1xmcgGZASbKKxQPr1AFSyZLKmmfnyBbEhPYf9paBqNY7VK5RQnq2wZIxdukA+WHZZ/35rE+XE4SSrccVTKlAdhipmuaMmbaPgA8kpwu4rlM3vVnAJiVplQBFdJc3fofTONSi8RlOl/o1gpAvzn48Vf6obZuIa8Tdw3keO2eKZ+viIJhT4rZkzU5NcAQPYEldecNHhDKRvuxyshZ6B4f3djhvmjMNp7zczp/Zbg8h3F6HIO6/+rk3HVVUNI+A2dWLvWE=^1743926741854; akacd_phased_PDP=3921379540~rv=92~id=e2a1c1dadce295152b5bf847635ecc8f; mt.v=2.032250148.1743926742058; channelflow=nonpaid|other|1746518742330; channeloriginator=nonpaid; channelcloser=nonpaid; x-browser-id=96cab051-8997-4f23-abc1-941ff9913885; x-session-id=999aaffd-0a93-4c56-b742-284a552ff015; ab_qm=b; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; x-commerce-next-id=7fbe0582-cd65-4869-bde4-565d83a6c10c; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20185%7CMCMID%7C88162336796767313862574451284687595910%7CMCAAMLH-1744531543%7C6%7CMCAAMB-1744531543%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1743933943s%7CNONE%7CMCAID%7CNONE; s_cc=true; mt.sc=%7B%22i%22%3A1743926744036%2C%22d%22%3A%5B%5D%7D; RT="z=1&dm=adidas.com&si=150db5d0-77e0-498f-8765-cb9f4c38f30d&ss=m95cyd86&sl=1&tt=tq&bcn=%2F%2F684dd32e.akstat.io%2F&ld=39h"; notice_preferences=%5B0%5D; RT="z=1&dm=adidas.com&si=150db5d0-77e0-498f-8765-cb9f4c38f30d&ss=m95cyd86&sl=1&tt=tq&bcn=%2F%2F684dd32e.akstat.io%2F&ld=39h"; ak_bmsc=54313F20D2D4908BE3613F48159EB053~000000000000000000000000000000~YAAQSIoUAoTn7faVAQAAH6ciChtP+vZYPSZuowdhNvko+F+yXqBccA4gmS8s9qi+ziX6ZEZhZG3Mev3cUobgduaZNvETWkOa7Tdo/l7r7thkyXTuuM8RgqXbaARnpt6kIZD+1Cxld0q9pdhg7HEh4oAt4e9elPyXYsygGMZiEnBzq93eMLlvBKkTJdwLChAfY9MCiLv0bFw3xzUoScKyno/aBUYaQlZgF3kXoFdVIrREQd+Fwkodtg3c+aHB73wVzN86h40PsG5VYPS0vXnj1yxB81ZF2LWN0a0TvrEwm3Ew4FDvetNUatOonWX/QwKq8OyS+snGMx89bw5bYCPq8IyJOpHLf0oOI8WOBI9/ij10TQyIgqk0vyafuhBbWksQkNBnFX7i89s741Hh09aZjWwzHQ==; utag_main=v_id:01960a224d2e00000e2909563a260506f002606700978$_sn:1$_se:6%3Bexp-session$_ss:0%3Bexp-session$_st:1743928565485%3Bexp-session$ses_id:1743926742319%3Bexp-session$_pn:1%3Bexp-session$_vpn:2%3Bexp-session$_prevpage:PLP%7CG_MEN%7CPR_CLOTHING%7CPRI_10.0%3CPRICE%3C72.0%3Bexp-1743930365490; s_pers=%20s_vnum%3D1746050400063%2526vn%253D1%7C1746050400063%3B%20pn%3D1%7C1746518754261%3B%20s_invisit%3Dtrue%7C1743928565493%3B; s_sess=%5B%5BB%5D%5D; _abck=8707E4286C23BCE10A9BD6A2BC7F97E1~-1~YAAQSIoUArLn7faVAQAA8agiCg3oR8+ZJvES2WWcEABAXvFlPeypIOGnMMT605Uox2u2mxWsVpJz3ypjh3EF70hKD2h9iES5VzIocSWGdyxFI6lqNrLBY1sU0aFYhaYC+6qdhH3oOw25RGlLgQn6Afh/K+8hI5VyApuBIWQ+cByQFaiD2L93xDoDFUXeFtJta23FE/lSwr64bveo+6hNOZrc4zs/1r8Xc6jwbTY3BrKMZIQ5VcHPmg4OYlRwJ6o7byxHapiXB/BVbvSJnl0VBpw2kWX2zXwReTyMeWmX8LSghdzM/R2I5pgxgAQurBUxi9QsnSqkvnEjdZ5loRJPRJb/MJY0Pp5fnU/S+t5oLuXl5sYWcOaYau1SPgKor4tzre8T8BklbnoLqLGW1NKm4Il1np294/XFjwmyo34jDM8Mrf5XFn3HW/ji96wuA7FCwjkK+6DtUOUBZhBwRNXySVgyHhPQrFNXGrr/rhWM5+kcfiWHkcalIeS7PW4CCxpcAw8kmYCmYkiVevCqBfL5mNZhdl8vYAxnwIRlfvtDNBMmucF1ycXWk8t8WzM883hGnP4UBXZRx3FGWcR8CobA0si39MI8UPOYQUfZUcNl~-1~-1~1743930341; bm_s=YAAQSIoUAtjn7faVAQAADKsiCgPxA9lv34HlLZbvD72706Qow9V+/gkOwqKcYLtSjBV55gud3DehLGBbDdVTWFUzeehDW2ZuyIGfKOIqueaGlpn9qKW5gSCBmIqNaJLiIO84uE50Dan9gEgk/TgyEmeXHgH6cTM2Flp38O+ErRvyZO2zxUwrJhKRVs9hunM/UO75bNx73ava4IgfcdXZJr4lpk9z6dpQb9qib3YtJB2E4hGmC3M+20+IBVwEQlsj23Xwr7VuZ+gSZKpoyW6rnab/Olwe8OcJHe1OhmIYafM7uW5+Acy5fS/1p1nKCpbvy3ETAJoYi4hJBSnWQmyCJhp3R/EA+csLoteuzo89UrYFfaH+lzEkn9hLMjqtmjPgp1oKaa9L+eT18qLcMsyaPYylR3tFIJVMFtJX3DaAnGNhvPX8YExLTrdt8GKjhnEqeYGK4RFkG/i6tOg=',
}

params = {
    'price_max': '21',
    'price_min': '10',
    'path': 'us',
    'taxonomy': 'men-clothing',
}

response = requests.get(
    'https://www.adidas.com/plp-app/_next/data/WSUPzTeC7Qvt2wDED1rI4/us/men-clothing.json',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(response.text)
