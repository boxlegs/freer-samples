# Reverse Engineering the Free Sampler

There's the request/response for when we first scan the QR. There are three slugs that I assume are used to identify the machine.

```http
GET /TRSYULK8/WFXXJZ/5 HTTP/2
Host: burberry.freesamples.net.au
Cookie: bluedot=-1245608283.746D6F19F1ED5B9BAC4AE20A4A8526DB; __party-time=CfDJ8DQkpnqad6xNrYuEE_020kbaYQobrdRrJp72lSQb0uqlokwpX50LwrgPtP6oSxSfWejynylMMxNhvpkkSJi80HF0QZGTjFQlt2fLjaMQxxxe4VY6m487VXi2PQIRnHazdITctRUsq6HFjIB_Vl3zup4
Cache-Control: max-age=0
Sec-Ch-Ua: "Not.A/Brand";v="99", "Chromium";v="136"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
```

```http
GET /api/survey?qrKey=TRSYULK8&deviceKey=WFXXJZ&check=5 HTTP/2
Host: burberry.freesamples.net.au
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-GB,en;q=0.9
Accept: application/json, text/plain, */*
Sec-Ch-Ua: "Not.A/Brand";v="99", "Chromium";v="136"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Sec-Ch-Ua-Mobile: ?0
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://burberry.freesamples.net.au/TRSYULK8/WFXXJZ/5
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

/*--------------------------*/

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 26 May 2025 05:40:57 GMT
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
Cache-Control: no-cache, no-store
Pragma: no-cache
Set-Cookie: __party-time=CfDJ8DQkpnqad6xNrYuEE_020kbaYQobrdRrJp72lSQb0uqlokwpX50LwrgPtP6oSxSfWejynylMMxNhvpkkSJi80HF0QZGTjFQlt2fLjaMQxxxe4VY6m487VXi2PQIRnHazdITctRUsq6HFjIB_Vl3zup4; path=/; samesite=strict; httponly
X-Cache: Miss from cloudfront
Via: 1.1 b8886d1f3378e960d5929163eb160eee.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BNE50-P2
X-Amz-Cf-Id: NCA-UcOlWFd9TKEHhIpGtRSaFW1EmQm09CdmbTpmZmPfMKtmg5cQsw==

{"session":-1245608283,"yoke":"746D6F19F1ED5B9BAC4AE20A4A8526DB","template":"burberry","questions":[]}
```



```http
GET /api/survey?qrKey=TRSYULK8&deviceKey=WFXXJZ&check=5&session=-1245608283&yoke=746D6F19F1ED5B9BAC4AE20A4A8526DB HTTP/2
Host: burberry.freesamples.net.au
Cookie: __party-time=CfDJ8DQkpnqad6xNrYuEE_020kbaYQobrdRrJp72lSQb0uqlokwpX50LwrgPtP6oSxSfWejynylMMxNhvpkkSJi80HF0QZGTjFQlt2fLjaMQxxxe4VY6m487VXi2PQIRnHazdITctRUsq6HFjIB_Vl3zup4
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-GB,en;q=0.9
Accept: application/json, text/plain, */*
Sec-Ch-Ua: "Not.A/Brand";v="99", "Chromium";v="136"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Sec-Ch-Ua-Mobile: ?0
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://burberry.freesamples.net.au/TRSYULK8/WFXXJZ/5
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

/*------------------------------------------*/

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 26 May 2025 05:53:10 GMT
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
Cache-Control: no-cache, no-store
Pragma: no-cache
Set-Cookie: __party-time=CfDJ8JxIEog4o31FivUMt5_NVWskHOD7Uo7XsyMDDqU7Jurdhd7WNlbfbAlOiTsgGOzZz9mNkqH8ugCTXc-FVpvQVZYKTsv6tF3ZahO9WF8pGR35JtB1gLahRo7EDpLfuNrduoZldJlXK0A5FMicIt78UJU; path=/; samesite=strict; httponly
X-Cache: Miss from cloudfront
Via: 1.1 34a9164f42ba6fa44b5d26746860cf6e.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BNE50-P2
X-Amz-Cf-Id: V0esg_sZKZOXPJ9-ObDimAlNamgMY1SqIktomoBhYq5UlUWSiOMlJw==

{"session":-1245608283,"yoke":"746D6F19F1ED5B9BAC4AE20A4A8526DB","template":"burberry","questions":[]}
```


```http
POST /api/survey HTTP/2
Host: burberry.freesamples.net.au
Cookie: __party-time=CfDJ8JxIEog4o31FivUMt5_NVWskHOD7Uo7XsyMDDqU7Jurdhd7WNlbfbAlOiTsgGOzZz9mNkqH8ugCTXc-FVpvQVZYKTsv6tF3ZahO9WF8pGR35JtB1gLahRo7EDpLfuNrduoZldJlXK0A5FMicIt78UJU
Content-Length: 130
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-GB,en;q=0.9
Accept: application/json, text/plain, */*
Sec-Ch-Ua: "Not.A/Brand";v="99", "Chromium";v="136"
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Origin: https://burberry.freesamples.net.au
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://burberry.freesamples.net.au/TRSYULK8/WFXXJZ/5
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"qrKey":"TRSYULK8","deviceKey":"WFXXJZ","check":"5","session":-1245608283,"yoke":"746D6F19F1ED5B9BAC4AE20A4A8526DB","answers":[]}

---------------------------------------------------------------------

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 26 May 2025 05:53:46 GMT
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
X-Cache: Miss from cloudfront
Via: 1.1 34a9164f42ba6fa44b5d26746860cf6e.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BNE50-P2
X-Amz-Cf-Id: HcyzMGset23QZz3kqNu84wievlU7P9ww0PnsDHkj15rWW51-s_ADJg==

{"token":"01970b27-7ad5-4d45-b84f-bc1db2b34085"}
```



