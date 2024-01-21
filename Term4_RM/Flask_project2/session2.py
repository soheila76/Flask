from flask import Flask,jsonify

app=Flask(__name__)
@app.route("/")
def get_news():
    return "hello this is a test"

@app.route("/varzesh/")
def say_varzesh():
   return '''
    
<!DOCTYPE html>
<html lang="fa" prefix="og: http://ogp.me/ns#">
<head>
    <title>مرجع فوتبال و ورزش | ورزش سه</title>
    <meta charset="utf-8" />
    
    <meta name="viewport" content="width=1170" />
    
    <meta name="description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />





<link href="https://www.varzesh3.com/" rel="canonical" />

<meta property="og:site_name" content="ورزش سه">
<meta property="og:title" content="مرجع فوتبال و ورزش" />
<meta property="og:url" content="https://www.varzesh3.com/" />
<meta property="og:description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="fa_IR" />
<meta property="og:image" content="https://static.varzesh3.com/img/logo/vrz3-logo.svg" />

<meta name="twitter:site" content="ورزش سه">
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="مرجع فوتبال و ورزش" />
<meta name="twitter:image:src" content="https://static.varzesh3.com/img/logo/vrz3-logo.svg" />
<meta name="twitter:description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />
<meta name="twitter:url" content="https://www.varzesh3.com/" />



    

    <link href="https://www.varzesh3.com/fonts/iransans/woff2/IRANSansXFaNum-Regular.woff2" rel="preload" as="font" type="font/woff" crossorigin />
    <link href="https://www.varzesh3.com/fonts/iransans/woff2/IRANSansXFaNum-Medium.woff2" rel="preload" as="font" type="font/woff" crossorigin />
    <link href="https://www.varzesh3.com/fonts/iransans/woff2/IRANSansXFaNum-DemiBold.woff2" rel="preload" as="font" type="font/woff" crossorigin />
    <link href="https://www.varzesh3.com/fonts/iransans/woff2/IRANSansXFaNum-Bold.woff2" rel="preload" as="font" type="font/woff" crossorigin />

    <link rel="dns-prefetch" href="https://static.varzesh3.com" />
    <link rel="preconnect" href="https://static.varzesh3.com" />
    <link rel="dns-prefetch" href="https://biz-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://biz-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://match-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://match-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://news-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://news-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://newsw-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://newsw-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://newspaper-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://newspaper-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://newspaperw-cdn.varzesh3.com" />
    <link rel="preconnect" href="https://newspaperw-cdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://video-icdn.varzesh3.com" />
    <link rel="preconnect" href="https://video-icdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://video-vcdn.varzesh3.com" />
    <link rel="preconnect" href="https://video-vcdn.varzesh3.com" />
    <link rel="dns-prefetch" href="https://static2.farakav.com" />
    <link rel="preconnect" href="https://static2.farakav.com" />
    <link rel="dns-prefetch" href="https://static.farakav.com" />
    <link rel="preconnect" href="https://static.farakav.com" />

    <link rel="preload" as="style" href="https://static.varzesh3.com/css/global.vendor.css?v=1.99.12" />
    <link rel="preload" as="style" href="https://static.varzesh3.com/css/sharedLayout.css?v=1.99.12" />
    
    <link rel="preload" as="script" href="https://static.varzesh3.com/js/global.vendor.js?v=1.99.12" />
    <link rel="preload" as="script" href="https://static.varzesh3.com/js/sharedLayout.js?v=1.99.12" />
    
    <link rel="preload" as="style" href="https://static.varzesh3.com/css/home.css?v=1.99.12" />

    

  	<link rel="shortcut icon" href="/img/favicon.ico">
	<link rel="icon" sizes="16x16 32x32 64x64" href="/img/favicon.ico">
	<link rel="icon" type="image/png" sizes="196x196" href="/img/favicon-192.png">
	<link rel="icon" type="image/png" sizes="160x160" href="/img/favicon-160.png">
	<link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96.png">
	<link rel="icon" type="image/png" sizes="64x64" href="/img/favicon-64.png">
	<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="/img/favicon-16.png">
	<link rel="apple-touch-icon" href="/img/favicon-57.png">
	<link rel="apple-touch-icon" sizes="114x114" href="/img/favicon-114.png">
	<link rel="apple-touch-icon" sizes="72x72" href="/img/favicon-72.png">
	<link rel="apple-touch-icon" sizes="144x144" href="/img/favicon-144.png">
	<link rel="apple-touch-icon" sizes="60x60" href="/img/favicon-60.png">
	<link rel="apple-touch-icon" sizes="120x120" href="/img/favicon-120.png">
	<link rel="apple-touch-icon" sizes="76x76" href="/img/favicon-76.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/img/favicon-152.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/img/favicon-180.png">
	<meta name="msapplication-TileColor" content="#FFFFFF">
	<meta name="msapplication-TileImage" content="/img/favicon-144.png">
	<meta name="msapplication-config" content="/img/browserconfig.xml">

    <link rel="stylesheet" href="https://static.varzesh3.com/css/global.vendor.css?v=1.99.12" />
    <link rel="stylesheet" href="https://static.varzesh3.com/css/sharedLayout.css?v=1.99.12" />
    
    <link rel="stylesheet" href="https://static.varzesh3.com/css/home.css?v=1.99.12" />

    <script type="application/ld+json">
        {
            "@context": "http://schema.org/",
            "@type": "Organization",
            "name": "ورزش سه",
            "url": "http://www.varzesh3.com/",
            "logo": "https://static.varzesh3.com/img/logo/vrz3-logo.svg",
            "potentialAction": {
                "@type": "SearchAction",
                "target": "https://www.varzesh3.com/search?q={search_term_string}",
                "query-input": "required name=search_term_string"
            },
            "sameAs" : [
                "https://facebook.com/varzesh3",
                "https://twitter.com/varzesh3",
                "https://instagram.com/varzesh3"
            ]
        }
    </script>
    

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-5BWLB69');</script>
    <!-- End Google Tag Manager -->
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5BWLB69"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    <header>
        <section class="allhead">
    <div class="container">

        
<ul class="allhead-menu">
            <li class="">

                    <a target="_blank" href="https://www.anten.ir/?utm_source=varzesh3&amp;utm_medium=homepage_header&amp;utm_campaign=always">پخش زنده</a>
            </li>
            <li class="">

                    <a target="_blank" href="https://pishbini.varzesh3.com">پیش بینی </a>
            </li>
            <li class="">

                    <a href="https://www.varzesh3.com/news">اخبار ورزشی</a>
            </li>
            <li class="">

                    <a href="https://www.varzesh3.com/album">گزارش تصویری</a>
            </li>
            <li class="">

                    <a target="_blank" href="https://www.varzesh3.com/podcast">پادکست</a>
            </li>
            <li class="">

                    <a href="https://www.varzesh3.com/newspaper">روزنامه</a>
            </li>
            <li class="">

                    <a target="_blank" href="https://www.varzesh3.com/contact">ثبت نظر</a>
            </li>
            <li class="">

                    <a target="_blank" href="https://www.varzesh3.com/advertisement">تبلیغات</a>
            </li>
</ul>

        <div class="allhead-auth">
            <span class="allhead-date"><span class="today-time">
    <img alt="date-time" width="18" height="18" src="https://static.varzesh3.com/img/icons/icon-general-today.svg?w=18" />
    <span class="datetime"><span>دوشنبه 25 دی</span><span> - </span><span>15:33</span></span>
</span></span>
            <span class="search-btn"><img alt="جستجو" width="18" height="18" src="https://static.varzesh3.com/img/icons/search-icon-white.svg?w=18" /><span>جستجو </span></span>
            <div class="allhead-user-auth">
                <span class="login"> <span><img alt="ورود" width="9" height="9" src="https://static.varzesh3.com/img/shared/header/user.svg?w=9" /></span> ورود</span>
                <div class="user-is-loged-in">
                    <div class="dropdown" id="notfiDorpdown">
                        <span class="user-menu-data notification-menu-data" id="notificationMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" role="button">
                            <img alt="اعلا‌ن‌ها" width="24" height="24" src="https://static.varzesh3.com/img/default/default-notifications.svg?w=24" />
                        </span>                     
                        <div class="dropdown-menu notification-menu" aria-labelledby="notificationMenuButton">
                            <div class="data-list">
                                <div class="loading-inline">
                                    <img src="https://static.varzesh3.com/img/icons/circle-notch.svg" />
                                </div>
                            </div>
                            <a class="footer" href="/profile/notifications">
                                مشاهده همه اعلان‌ها
                            </a>
                        </div>                      
                    </div>
                    <div class="dropdown">
                        <span class="user-menu-data" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" role="button">
                            <img alt="حساب کاربری" width="24" height="24" src="https://static.varzesh3.com/img/default/default-user.svg?w=24" />
                        </span>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <a class="dropdown-item" href="/profile/info">
                                <span>
                                    <img alt="حساب کاربری" width="20" src="https://static.varzesh3.com/img/default/user-icon.jpg?w=20" class="user-profile-icon" />
                                </span>
                                مشاهده حساب کاربری
                            </a>
                            <a class="dropdown-item" href="/profile/favorites">
                                <span>
                                    <img alt="حساب کاربری" width="20" src="https://static.varzesh3.com/img/profile/favorites-outline.svg?w=20" class="user-profile-icon" />
                                </span>
                                علاقه‌مندی‌ها
                            </a>
                            <span class="dropdown-item logout">
                                <span>
                                    <img alt="خروج" width="20" src="https://static.varzesh3.com/img/icons/logout.svg?w=20" class="logout-icon" />
                                </span>
                                خروج
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<nav class="navbar navbar-expand-lg has-tb">
    <div class="container">
        <a class="navbar-brand" href="/">
            <h1>
                <svg width="98px" height="30px" viewBox="0 0 98 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                    <title>ورزش سه</title>
                    <g id="Branding-/-Logo-/-Varzesh3" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="Asset-1" transform="translate(73.000000, 3.000000)">
                            <path d="M18.1014151,20.2055288 L20.7323113,21.5396635 C24.6014151,13.1388221 18.8384434,6.59615385 15.5294811,5.19350962 C15.5294811,5.19350962 17.8909198,11.8641827 18.6615566,13.7433894 C19.4516509,15.672476 19.1379717,18.171875 18.1014151,20.2055288 Z" id="Path" fill="#E74436"></path>
                            <path d="M22.4941038,11.3305288 L25,9.76322115 C20.0571934,1.96754808 11.5595519,3.48557692 8.63974057,5.60096154 C8.63974057,5.60096154 15.4398585,7.09194712 17.4133255,7.42247596 C19.4375,7.76141827 21.3514151,9.35637019 22.4941038,11.3305288 Z" id="Path" fill="#2F363D"></path>
                            <path d="M16.7788915,2.99278846 L16.6745283,0 C7.58490566,0.540865385 4.68985849,8.82211538 5.05837264,12.4549279 C5.05837264,12.4549279 9.68337264,7.15985577 10.9380896,5.57211538 C12.2252358,3.94471154 14.5300708,3.03365385 16.7788915,2.99278846 Z" id="Path" fill="#4383F1"></path>
                            <path d="M6.58608491,3.515625 L3.96580189,2.15985577 C0.0300707547,10.5288462 5.74115566,17.1189904 9.03891509,18.5480769 C9.03891509,18.5480769 6.73054245,11.8605769 5.97287736,9.97295673 C5.19988208,8.03786058 5.53301887,5.54086538 6.58608491,3.515625 Z" id="Path" fill="#35A655"></path>
                            <path d="M2.47228774,12.8058894 L0,14.4230769 C5.09257075,22.1153846 13.5613208,20.4272837 16.4369104,18.250601 C16.4369104,18.250601 9.60849057,16.8984375 7.62912736,16.6081731 C5.60141509,16.311899 3.65566038,14.7566106 2.47228774,12.8058894 Z" id="Path" fill="#F8BA06"></path>
                            <ellipse id="Oval" fill="#757575" fill-rule="nonzero" cx="12.4068396" cy="11.9723558" rx="7.35082547" ry="7.4921875"></ellipse>
                            <path d="M7.71580189,21.0054087 L7.71580189,24 C16.8189858,23.7896635 20,15.6165865 19.7582547,11.9723558 C19.7582547,11.9723558 14.9516509,17.0973558 13.6426887,18.6382212 C12.3001179,20.21875 9.96462264,21.0456731 7.71580189,21.0054087 Z" id="Path" fill="#757575"></path>
                            <ellipse id="Oval" fill="#FFFFFF" fill-rule="nonzero" cx="12.4068396" cy="11.9723558" rx="4.3879717" ry="4.47235577"></ellipse>
                            <path d="M14.5518868,11.8623798 C14.5605255,12.1659935 14.4572339,12.4618867 14.2623821,12.6917067 C14.0681682,12.9221566 13.7819911,13.0505402 13.4840802,13.0408654 C13.2841986,13.0360525 13.089759,12.9735355 12.9233491,12.8605769 C12.7928094,12.7884355 12.6811862,12.6853832 12.5978774,12.5600962 C12.5380932,12.6762549 12.4553864,12.7785574 12.3549528,12.8605769 C12.2475131,12.9649993 12.1069745,13.0268147 11.9587264,13.0348558 C11.6835692,13.0348558 11.4943003,12.9767628 11.3909198,12.8605769 C11.4074292,13.0300481 11.4215802,13.3167067 11.4339623,13.71875 C11.4457547,14.1358173 11.4431997,14.4050481 11.4262972,14.5264423 L10.8012972,14.5264423 C10.8107311,14.40625 10.8160377,14.2680288 10.8160377,14.1057692 C10.8082707,13.4132187 10.7568678,12.7218917 10.6621462,12.0360577 C10.5509041,11.1834936 10.4176494,10.5108173 10.2623821,10.0180288 L10.8266509,9.76021635 C11.0434428,10.384712 11.1942567,11.0309965 11.276533,11.688101 C11.3358884,12.1268029 11.5216195,12.3461538 11.8337264,12.3461538 C11.952635,12.3445599 12.0605177,12.2748195 12.1126179,12.1658654 C12.172473,12.0636685 12.2032967,11.9465331 12.2016509,11.827524 C12.2012415,11.7822899 12.1965021,11.7372044 12.1875,11.6929087 L11.8626179,10.0012019 L12.4911557,9.79567308 L12.8266509,11.46875 C12.9390723,12.0296474 13.1385613,12.3100962 13.4251179,12.3100962 C13.7002752,12.3100962 13.8378538,12.1235978 13.8378538,11.750601 C13.8378538,11.5570913 13.771816,11.2738381 13.6397406,10.9008413 C13.549512,10.6203367 13.4263717,10.3519669 13.2729953,10.1015625 L13.8555425,9.81430288 C14.0572862,10.1189068 14.2160688,10.4508732 14.3272406,10.8004808 C14.4773978,11.2247596 14.5522799,11.578726 14.5518868,11.8623798 Z" id="Path" fill="#757575" fill-rule="nonzero"></path>
                        </g>
                        <path d="M59.1163634,8.63260026 L59.1163634,22.0666235 C59.1163634,23.8320397 58.4895044,25.3098318 57.2357865,26.5 L57.2357865,26.5 L55.5755897,25.0271669 C56.4571101,24.1841311 56.8978703,23.0435533 56.8978703,21.6054334 L56.8978703,21.6054334 L56.8978703,8.63260026 L59.1163634,8.63260026 Z M54.5618412,8.63260026 L54.5618412,22.0666235 C54.5618412,23.8320397 53.9349823,25.3098318 52.6812643,26.5 L52.6812643,26.5 L51.0210675,25.0271669 C51.9025879,24.1841311 52.3433482,23.0435533 52.3433482,21.6054334 L52.3433482,21.6054334 L52.3433482,8.63260026 L54.5618412,8.63260026 Z M68.9893921,8.64747736 L69.0040841,22.0517464 C69.0040841,23.7133146 68.4488042,25.1201016 67.3382444,26.2721075 L67.1235072,26.4851229 L65.4633104,25.0122898 C66.3448308,24.169254 66.7855911,23.0832255 66.7855911,21.7542044 C65.0323449,21.7542044 63.5435548,21.10953 62.3192209,19.8201811 C61.094887,18.5308323 60.48272,16.9935317 60.48272,15.2082794 C60.48272,13.403191 61.102233,11.8584519 62.3412589,10.5740621 C63.507401,9.36522462 64.9143089,8.72525183 66.5619828,8.65414374 L66.8737431,8.64747736 L68.9893921,8.64747736 Z M32.1712225,8.63260026 L32.1712225,18.1688228 C32.1712225,19.3589909 32.5801501,20.3681544 33.3980051,21.1963131 C34.2158602,22.0244718 35.212468,22.4385511 36.3878285,22.4385511 C37.6415465,22.4385511 38.6650896,21.98232 39.458458,21.0698577 C40.232237,20.1970677 40.6191266,19.1209573 40.6191266,17.8415265 L40.6191266,17.8415265 L40.6191266,8.63260026 L42.8376196,8.63260026 L42.8376196,18.3771022 C42.8376196,19.1705476 43.0677944,19.5672704 43.528144,19.5672704 C43.8611628,19.5672704 44.0717482,19.4631307 44.1599003,19.2548512 C44.2088736,19.1358344 44.2333603,18.8432514 44.2333603,18.3771022 L44.2333603,18.3771022 L44.2333603,8.63260026 L46.4518533,8.63260026 L46.4518533,18.3771022 C46.4518533,18.8234153 46.4812374,19.1159983 46.5400054,19.2548512 C46.6281574,19.4631307 46.8240509,19.5672704 47.1276857,19.5672704 C47.4900885,19.5672704 47.715366,19.4482536 47.803518,19.2102199 C47.8296371,19.1396914 47.8441477,18.9085147 47.8470499,18.5166898 L47.8470499,18.5166898 L47.847594,8.63260026 L50.0660871,8.63260026 L50.0660871,18.198577 C50.0660871,19.1903838 49.816323,20.0135834 49.3167947,20.6681759 C48.7682931,21.3921949 48.0190008,21.7542044 47.0689176,21.7542044 C46.2265759,21.7542044 45.643793,21.6252695 45.3205688,21.3673997 C44.8993979,21.6252695 44.3264097,21.7542044 43.601604,21.7542044 C42.8180303,21.7542044 42.2499393,21.6153514 41.8973312,21.3376455 C40.6338186,23.5692109 38.7973177,24.6849935 36.3878285,24.6849935 C34.6051984,24.6849935 33.0870243,24.0502372 31.8333064,22.7807245 C30.5795884,21.5112117 29.9527295,19.9739112 29.9527295,18.1688228 L29.9527295,18.1688228 L29.9527295,8.63260026 L32.1712225,8.63260026 Z M15.0403424,21.7542044 C13.188862,21.6955717 12.263553,20.565653 12.263553,18.3622251 L12.263553,18.3622251 L12.263553,15.2826649 C12.263553,14.1520052 11.8497282,13.1453213 11.0220784,12.2626132 C10.1944287,11.3799051 9.22720492,10.9385511 8.12040706,10.9385511 C6.92545716,10.9385511 5.91905468,11.365028 5.10119962,12.2179819 C4.28334457,13.0709357 3.87441704,14.1024148 3.87441704,15.3124191 C3.87441704,16.5323415 4.2808959,17.546464 5.09385362,18.3547865 C5.90681134,19.1631091 6.91566249,19.5672704 8.12040706,19.5672704 L8.12040706,19.5672704 L10.2213641,19.5672704 L10.2213641,21.7542044 L8.14979108,21.7542044 C6.35736622,21.7542044 4.83429483,21.119448 3.5805769,19.8499353 C2.32685897,18.5804226 1.7,17.038163 1.7,15.2231565 C1.7,13.398232 2.3244103,11.8460543 3.57323089,10.5666235 C4.82205149,9.28719276 6.34757155,8.64747736 8.14979108,8.64747736 C9.65817046,8.64747736 11.0294245,9.15825787 12.263553,10.1798189 L12.263553,10.1798189 L12.263553,8.63260026 L14.4673541,8.63260026 L14.4673541,18.5705045 C14.4673541,19.2350151 14.7073235,19.5672704 15.1872624,19.5672704 C15.6574067,19.5672704 15.8924788,19.3193187 15.8924788,18.8234153 L15.8924788,18.8234153 L15.8924788,8.63260026 L18.1109718,8.63260026 L18.1109718,18.3622251 C18.1109718,19.1655886 18.3362493,19.5672704 18.7868042,19.5672704 C19.266743,19.5672704 19.5067125,19.1705476 19.5067125,18.3771022 L19.5067125,18.3771022 L19.5067125,8.63260026 L21.7252056,8.63260026 L21.7252056,18.3771022 C21.7252056,19.1705476 21.950483,19.5672704 22.4010379,19.5672704 C22.8809768,19.5672704 23.1209462,19.1655886 23.1209462,18.3622251 L23.1209462,18.3622251 L23.1209462,8.63260026 L25.3394393,8.63260026 L25.3394393,18.198577 C25.3394393,19.1903838 25.0896752,20.0135834 24.5901469,20.6681759 C24.0416453,21.3921949 23.292353,21.7542044 22.3422698,21.7542044 C21.4999281,21.7542044 20.9171452,21.6252695 20.593921,21.3673997 C20.1727501,21.6252695 19.5752752,21.7542044 18.8014962,21.7542044 C18.1158692,21.7542044 17.5134969,21.5310479 16.9943793,21.0847348 C16.4752617,21.5310479 15.8728894,21.7542044 15.1872624,21.7542044 L15.334,21.748 L15.3341825,21.7542044 L15.0403424,21.7542044 Z M66.770899,10.8344114 C65.7130745,10.8344114 64.7629914,11.293122 63.9206497,12.2105433 C63.0783079,13.1279646 62.6571371,14.12721 62.6571371,15.2082794 C62.6571371,16.3984476 63.0489239,17.4150496 63.8324976,18.2580854 C64.5729748,19.0726894 65.4755646,19.5071448 66.5402672,19.5614518 L66.770899,19.5672704 L66.770899,10.8344114 Z M53.4452487,5.61254851 C53.7292942,5.61254851 53.9741609,5.71668823 54.179849,5.92496766 C54.3855371,6.13324709 54.4883812,6.38119879 54.4883812,6.66882277 C54.4883812,6.95644674 54.3855371,7.20191893 54.179849,7.40523933 C53.9741609,7.60855972 53.7292942,7.71021992 53.4452487,7.71021992 C53.1709979,7.71021992 52.9310284,7.60608021 52.7253403,7.39780078 C52.5196522,7.18952135 52.4168082,6.94652868 52.4168082,6.66882277 C52.4168082,6.38119879 52.5172036,6.13324709 52.7179943,5.92496766 C52.9187851,5.71668823 53.1612032,5.61254851 53.4452487,5.61254851 Z M46.6575414,5.59767141 C46.9415869,5.59767141 47.1864537,5.70181113 47.3921418,5.91009056 C47.5978299,6.11836999 47.7006739,6.36632169 47.7006739,6.65394567 C47.7006739,6.94156964 47.5978299,7.18704183 47.3921418,7.39036223 C47.1864537,7.59368262 46.9415869,7.69534282 46.6575414,7.69534282 C46.3832907,7.69534282 46.1433212,7.5912031 45.9376331,7.38292367 C45.731945,7.17464424 45.629101,6.93165157 45.629101,6.65394567 C45.629101,6.36632169 45.7294963,6.11836999 45.9302871,5.91009056 C46.1310779,5.70181113 46.373496,5.59767141 46.6575414,5.59767141 Z M44.1305162,5.59767141 C44.4145617,5.59767141 44.6594285,5.70181113 44.8651166,5.91009056 C45.0708047,6.11836999 45.1736487,6.36632169 45.1736487,6.65394567 C45.1736487,6.94156964 45.0708047,7.18704183 44.8651166,7.39036223 C44.6594285,7.59368262 44.4145617,7.69534282 44.1305162,7.69534282 C43.8562654,7.69534282 43.616296,7.5912031 43.4106079,7.38292367 C43.2049198,7.17464424 43.1020758,6.93165157 43.1020758,6.65394567 C43.1020758,6.36632169 43.2024711,6.11836999 43.4032619,5.91009056 C43.6040527,5.70181113 43.8464708,5.59767141 44.1305162,5.59767141 Z M45.3499528,3.5 C45.6339983,3.5 45.8788651,3.60413972 46.0845532,3.81241915 C46.2902413,4.02069858 46.3930853,4.26865028 46.3930853,4.55627426 C46.3930853,4.84389823 46.2902413,5.08937042 46.0845532,5.29269082 C45.8788651,5.49601121 45.6339983,5.59767141 45.3499528,5.59767141 C45.075702,5.59767141 44.8357326,5.49353169 44.6300445,5.28525226 C44.4243564,5.07697283 44.3215123,4.83398016 44.3215123,4.55627426 C44.3215123,4.26865028 44.4219077,4.02069858 44.6226985,3.81241915 C44.8234892,3.60413972 45.0659074,3.5 45.3499528,3.5 Z" id="Combined-Shape" fill="#757575" fill-rule="nonzero"></path>
                    </g>
                </svg>
            </h1>
        </a>
        <div class="navbar-collapse d-none  d-lg-inline-flex flex-lg-row-reverse">
            <ul class="navbar-nav flex-grow-1">
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/">
                    صفحه‌اصلی
                </a>
        </li>
<li class="nav-item first-parent-item highlight ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/%D8%AC%D8%A7%D9%85-%D9%85%D9%84%D8%AA-%D9%87%D8%A7%DB%8C-%D8%A2%D8%B3%DB%8C%D8%A7-2023"  target="_blank">
                    جام ملت‌های آسیا
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"  target="_blank">
                    جدول لیگ برتر
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://video.varzesh3.com"  target="_blank">
                    ویدیو
                </a>
        </li>
<li class="nav-item first-parent-item highlight ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/transfers/iran/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1"  target="_blank">
                    نقل‌ و‌ انتقالات
                </a>
        </li>
<li class="nav-item first-parent-item  live">
                <a class="menu-link-item" href="https://www.varzesh3.com/livescore">
                    نتایج زنده
                </a>
        </li>
</ul>
        </div>
        <div class="left-menu-box home-left-menu-box">
            <button class="navbar-toggler" type="button">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                    <g fill="none" fill-rule="evenodd">
                        <g>
                            <g>
                                <path d="M0 0L24 0 24 24 0 24z" transform="translate(-320 -16) translate(320 16)" />
                                <path fill="#757575" d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" transform="translate(-320 -16) translate(320 16)" />
                            </g>
                        </g>
                    </g>
                </svg>
            </button>

            <div class="tb-holder banner-zone justify-content-center header-ad">
                
        <div class="adbox" data-id="3459">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3459" rel="nofollow"
                    style="background-color: #f5f5f5;height:60px">
                        <img class="adimage" id="img-3459" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/14/65029f0a-caa8-4168-a46f-96751e36abe5.gif" 
                                                        width="468" 
                                                        height="60" alt="غول آسیا لایف استار" />
                </a>
    </div>

            </div>
        </div>
    </div>
</nav>


    </header>
    <section class="mainbody">
        <main role="main">
            



<div class="home-page">
    <div class="home-holder">
        
        <div class="right-side-big-col">
            <div class="v2-inner-col">
                <div class="v600-col">
                    
<div class="widget-holder">
    <div class="widget slider">
        <div class="homepage-slider v2 owl-carousel">
                    <div class="slider-item" data-index="0">
                        <div class="slider-image" data-video-preview="">
                                <img alt="پاسخ طعنه‌آمیز برانکو به سوال خبرنگار درباره پرسپولیس" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/C/tohmzggp.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994660/پاسخ-طعنه-آمیز-برانکو-به-سوال-خبرنگاران-درباره-پرسپولیس"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">عزیزم ما در جام ملت‌ها هستیم</p>
                                    <h2 class="headline">
                                    
                                        پاسخ طعنه‌آمیز برانکو به سوال خبرنگار درباره پرسپولیس
                                    </h2>
                                    <p class="lead">سرمربی تیم ملی عمان در پاسخ به سوال خبرنگاران ایرانی موضوع پرسپولیس را به آینده منوط کرد.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item" data-index="1">
                        <div class="slider-image" data-video-preview="">
                                <img alt="بحران تیم ملی عربستان در جنجالی‌ترین نشست جام ملت‌ها" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/C/pvwj0vge.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994652/بحران-تیم-ملی-عربستان-در-جنجالی-ترین-نشست-جام-ملتها"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">مانچینی: هر کس دوست ندارد فوری برود </p>
                                    <h2 class="headline">
                                    
                                        بحران تیم ملی عربستان در جنجالی‌ترین نشست جام ملت‌ها
                                    </h2>
                                    <p class="lead">روبرتو مانچینی در یک نشست خبری شلوغ و نسبتا طولانی، صحبت‌های عجیبی را درخصوص دلایل حذف چند ستاره مطرح تیم ملی عربستان به زبان آورد.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item" data-index="2">
                        <div class="slider-image" data-video-preview="">
                                <img alt="وای‌فای ضعیف، تنها راه متوقف کردن ایران در قطر!" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/B/kuehmuis.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994626/وای-فای-ضعیف-تنها-راه-متوقف-کردن-ایران-در-قطر"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">نیمکت ایران به آنالیز آنلاین مجهز شد</p>
                                    <h2 class="headline">
                                    
                                        وای‌فای ضعیف، تنها راه متوقف کردن ایران در قطر!
                                    </h2>
                                    <p class="lead">استفاده از دستگاه «آنالیز آنلاین» روی نیمکت، اتفاق ویژه‌ای است که کادرفنی تیم ملی در بازی با فلسطین رقم زد.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item" data-index="3">
                        <div class="slider-image" data-video-preview="">
                                <img alt="خداحافظی سپاهان با دو ستاره: Good Luck!" width="350" src="https://newsw-cdn.varzesh3.com/pictures/2023/12/10/D/xgsjt43k.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994608/جدایی-رسمی-دو-ستاره-از-سپاهان-عکس"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">پهلوان و آل‌کثیر اصفهان را ترک کردند</p>
                                    <h2 class="headline">
                                    
                                        خداحافظی سپاهان با دو ستاره: Good Luck!
                                    </h2>
                                    <p class="lead">باشگاه سپاهان به‌طور رسمی جدایی دو ستاره تاثیرگذار خود را اعلام کرد و  به نظر می‌رسد در آینده شاهد جدایی برخی نفرات دیگر هم باشیم.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item" data-index="4">
                        <div class="slider-image" data-video-preview="">
                                <img alt="جایزه The Best: مسی، امباپه یا هالند!" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/C/rm0opx2i.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994650/جایزه-the-best-مسی-امباپه-یا-هالند"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">امشب در لندن اهدا می‌شود</p>
                                    <h2 class="headline">
                                    
                                        جایزه The Best: مسی، امباپه یا هالند!
                                    </h2>
                                    <p class="lead">برندگان جوایز ارزشمند The Best که از سوی فیفا اهدا خواهد شد امشب معرفی می‌شوند. </p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item" data-index="5">
                        <div class="slider-image" data-video-preview="">
                                <img alt="فرش جادویی برای وینی: چهار تا خیلی کم بود!" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/A/myslsnxx.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1994568/فرش-جادویی-برای-وینی-چهار-تا-خیلی-کم-بود"  class="slider-item-link" data-nt-link>
                                    <p class="subhead">سلام بارسای ژاوی به بحران</p>
                                    <h2 class="headline">
                                    
                                        فرش جادویی برای وینی: چهار تا خیلی کم بود!
                                    </h2>
                                    <p class="lead">بارسلونا امشب را هرگز فراموش نخواهد کرد. شبی که سه گل از بهترین وینیسیوس تاریخ خورد و خوش شانس بود که در نهایت با چهار گل به رئال باخت.</p>
                                </a>
                        </div>
                    </div>
        </div>

    </div>
</div>

                    
<div class="widget-holder">
    <div class="widget slider-f">
        <div class="featured-news owl-carousel">
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="دیگر جنتلمنی مثل آنچلوتی وجود ندارد" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/C/n5kmn3xw.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994690/دیگر-جنتلمنی-مثل-آنچلوتی-وجود-ندارد" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>دیگر جنتلمنی مثل آنچلوتی وجود ندارد</h2>
                                <p class="featured-lead">رئال مادرید با کارلو آنچلوتی روندی پرافتخار را طی می‌کند و همه چیز نشان می‌دهد این روند ادامه‌دار خواهد بود. یک مربی باشخصیت که همه دوستش دارند.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="پهلوان به اهواز برگشت: سلام فولاد" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/B/djpeh0t3.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994616/اولین-خرید-فولاد-از-سپاهان-آمد-عکس" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>پهلوان به اهواز برگشت: سلام فولاد</h2>
                                <p class="featured-lead">احسان پهلوان با عقد قرارداد رسمی و 1.5 ساله به عضویت فولاد خوزستان در آمد.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="دستگیری و اخراج فوتبالیست رژیم اشغالگر در ترکیه" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/B/3em0ey5f.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994618/دستگیری-و-اخراج-فوتبالیست-رژیم-اشغالگر-در-ترکیه" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>دستگیری و اخراج فوتبالیست رژیم اشغالگر در ترکیه</h2>
                                <p class="featured-lead">شادی نژادپرستانه بازیکن اسراییلی آنتالیا اسپور جنجال بسیار زیادی در کشور ترکیه به وجود آورد.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="مانچینی و تصمیم شگفت‌انگیز: عربستان شماره یک ندارد" width="350" src="https://news-cdn.varzesh3.com/pictures/2023/09/09/B/2htx020o.jpeg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994597/این-تصمیم-مانچینی-را-اخراج-می-کند" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>مانچینی و تصمیم شگفت‌انگیز: عربستان شماره یک ندارد</h2>
                                <p class="featured-lead">همه در انتظار نشست خبری مانچینی پیش از مصاف با عمان هستند تا از او درباره تصمیمی که درباره العقیدی سنگربان تیمش اتخاذ کرده بپرسند.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="قربان‌زاده: فروپاشی شوروی در فوتبال ایران اتفاق می‌افتد!" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/13/C/pzy4pswx.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994594/قربان-زاده-فروپاشی-شوروی-در-فوتبال-ایران-اتفاق-می-افتد" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>قربان‌زاده: فروپاشی شوروی در فوتبال ایران اتفاق می‌افتد!</h2>
                                <p class="featured-lead">رئیس سابق سازمان خصوصی‌سازی توصیف جالبی از وضعیت مالی در فوتبال ایران دارد.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="ورود منصوریان با لپ‌تاپ: شغل جدید سرمربی معروف!" width="350" src="https://news-cdn.varzesh3.com/pictures/2024/01/15/A/pl2fx4lq.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994575/ورود-منصوریان-با-لپ-تاپ-شغل-جدید-سرمربی-معروف" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>ورود منصوریان با لپ‌تاپ: شغل جدید سرمربی معروف!</h2>
                                <p class="featured-lead">علیرضا منصوریان، کارشناس امروز برنامه فوتبال برتر بود که با تسلط کافی درباره تیم ملی اظهار نظر کرد.</p>
                            </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                            <img alt="پرسپولیس و سه خرید: یک امیدواری، دو ناامیدی!" width="350" src="https://news-cdn.varzesh3.com/pictures/2023/01/02/B/y0myh0lr.jpg?w=350" />
                        </div>

                        <div class="slider-info">
                            <a href="https://www.varzesh3.com/news/1994536/پرسپولیس-و-سه-خرید-زمستانی-یک-امیدواری-دو-ناامیدی" data-nt-link>
                                <h2 class="headline"><span class="second-title">تیتر دو</span>پرسپولیس و سه خرید: یک امیدواری، دو ناامیدی!</h2>
                                <p class="featured-lead">از سه گزینه نقل و انتقالات زمستانی پرسپولیس تنها یک گزینه نزدیک به قطعی شدن به نظر می‌رسد.</p>
                            </a>
                        </div>
                    </div>
        </div>
    </div>
</div>
                </div>
                <div class="v50-r-col widgets-parent-col">
                    <div class="forfix">
                        

            


        
        
        <div class="adbox" data-id="3351">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3351" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-3351" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/11/38443e74-6dc6-4612-b7bc-e97986f58780.gif" 
                                                        width="300" 
                                                        height="160" alt="آسیا تک" />
                </a>
    </div>

        
        <div class="adbox" data-id="2552">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2552" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-2552" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/13/8c36fa27-2271-42e4-b6e1-7477bb47bf2f.gif" 
                                                        width="300" 
                                                        height="160" alt="همراه اول طرح انتقال شارژ" />
                </a>
    </div>




            <div class="widget-holder">
                <div id="122" class="widget league schedual football">
                                


<div class="widget-header" style="background-image:url(&#x27;https://match-cdn.varzesh3.com/widget/2024/01/10/B/wcyceowl.png&#x27;);">
    <h2>
        <img src="https://match-cdn.varzesh3.com/widget/2024/01/10/B/ml5tgola.png" />
        <span style="color:#673ab7;">جام ملت های آسیا 2023</span>
    </h2>
    <div class="select-options">
        <select id="stage-122">
                    <option value="902307" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902307">گروه A </option>
                    <option value="902308" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902308">گروه B </option>
                    <option value="902309" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902309">گروه C </option>
                    <option value="902310" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902310">گروه D </option>
                    <option value="902311" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902311">گروه E </option>
                    <option value="902312" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/122/league/902312">گروه F </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:350px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#7f67f1"><h3>گروه E</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>دوشنبه 25 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355652/بازی-کره-جنوبی-بحرین"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    <a target="_blank" href="https://www.anten.ir/football/60969/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%DA%A9%D8%B1%D9%87-%D8%AC%D9%86%D9%88%D8%A8%DB%8C-%D8%A8%D8%AD%D8%B1%DB%8C%D9%86"><img alt="آنتن" width="17" height="17" src="https://static.varzesh3.com/img/icons/anten-icon.svg?w=17" /></a>
                                </div>
                                <a href="/football/match/355652/بازی-کره-جنوبی-بحرین" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کره جنوبی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بحرین</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355655/بازی-مالزی-اردن"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    <a target="_blank" href="https://www.anten.ir/football/60971/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%A7%D9%84%D8%B2%DB%8C-%D8%A7%D8%B1%D8%AF%D9%86"><img alt="آنتن" width="17" height="17" src="https://static.varzesh3.com/img/icons/anten-icon.svg?w=17" /></a>
                                </div>
                                <a href="/football/match/355655/بازی-مالزی-اردن" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مالزی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اردن</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>شنبه 30 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355660/بازی-اردن-کره-جنوبی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/355660/بازی-اردن-کره-جنوبی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اردن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>کره جنوبی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355658/بازی-بحرین-مالزی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/355658/بازی-بحرین-مالزی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بحرین</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مالزی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">18:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 5 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355663/بازی-کره-جنوبی-مالزی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/355663/بازی-کره-جنوبی-مالزی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کره جنوبی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مالزی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/355665/بازی-اردن-بحرین"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/355665/بازی-اردن-بحرین" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اردن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بحرین</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#7f67f1"><h3>جدول گروه E</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول گروه E</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><a href="/football/team/315/کره-جنوبی"> کره جنوبی</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><a href="/football/team/480/مالزی"> مالزی</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><a href="/football/team/321/اردن"> اردن</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><a href="/football/team/325/بحرین"> بحرین</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="https://www.varzesh3.com/football/%D8%AC%D8%A7%D9%85-%D9%85%D9%84%D8%AA-%D9%87%D8%A7%DB%8C-%D8%A2%D8%B3%DB%8C%D8%A7-2023?group=E" >جدول کامل جام ملت های آسیا گروه E</a></div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="344">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-3546"></div>
                </div>
    </div>

        
        <div class="adbox" data-id="2877">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2877" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-2877" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/12/10/a77a30cd-1670-4c6d-af8f-fd5744e71873.gif" 
                                                        width="300" 
                                                        height="160" alt="یابکس" />
                </a>
    </div>




            <div class="widget-holder">
                <div id="78" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">جدول لیگ های ایران</span>
    </h2>
    <div class="select-options">
        <select id="stage-78">
                    <option value="902337" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/78/league/902337">لیگ برتر ایران </option>
                    <option value="902404" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/78/league/902404">لیگ آزادگان </option>
                    <option value="901969" data-api="https://web-api.varzesh3.com/v1.0/futsal/widgets/78/league/901969">لیگ برتر فوتسال </option>
                    <option value="17" data-api="https://web-api.varzesh3.com/v1.0/beach-soccer/widgets/78/league/17">لیگ برتر فوتبال ساحلی </option>
                    <option value="902469" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/78/league/902469">لیگ برتر زنان </option>
                    <option value="901970" data-api="https://web-api.varzesh3.com/v1.0/futsal/widgets/78/league/901970">سوپرلیگ فوتسال زنان </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#f3b500"><h3>جدول لیگ برتر ایران</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول لیگ برتر ایران</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><a href="/football/team/4/استقلال"> استقلال</a></td>
                                <td>15</td>
                                <td>32</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><a href="/football/team/10/سپاهان"> سپاهان</a></td>
                                <td>15</td>
                                <td>31</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><a href="/football/team/6/پرسپولیس"> پرسپولیس</a></td>
                                <td>15</td>
                                <td>30</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><a href="/football/team/18/تراکتور"> تراکتور</a></td>
                                <td>15</td>
                                <td>28</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row"><a href="/football/team/1/ذوب-آهن"> ذوب آهن</a></td>
                                <td>15</td>
                                <td>25</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row"><a href="/football/team/14/ملوان"> ملوان</a></td>
                                <td>15</td>
                                <td>24</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row"><a href="/football/team/44/گل-گهرسیرجان"> گل گهرسیرجان</a></td>
                                <td>15</td>
                                <td>23</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row"><a href="/football/team/901631/آلومینیوم-اراک"> آلومینیوم اراک</a></td>
                                <td>15</td>
                                <td>22</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row"><a href="/football/team/902983/شمس-آذر-قزوین"> شمس آذر قزوین</a></td>
                                <td>15</td>
                                <td>20</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row"><a href="/football/team/28/مس-رفسنجان"> مس رفسنجان</a></td>
                                <td>15</td>
                                <td>15</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row"><a href="/football/team/9/فولاد"> فولاد</a></td>
                                <td>15</td>
                                <td>15</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row"><a href="/football/team/902565/هوادار"> هوادار</a></td>
                                <td>15</td>
                                <td>14</td>
                            </tr>
                            <tr>
                                <td>13</td>
                                <td scope="row"><a href="/football/team/11/پیکان"> پیکان</a></td>
                                <td>15</td>
                                <td>11</td>
                            </tr>
                            <tr>
                                <td>14</td>
                                <td scope="row"><a href="/football/team/21/صنعت-نفت-آبادان"> صنعت نفت آبادان</a></td>
                                <td>15</td>
                                <td>11</td>
                            </tr>
                            <tr>
                                <td>15</td>
                                <td scope="row"><a href="/football/team/37/نساجی-مازندران"> نساجی مازندران</a></td>
                                <td>15</td>
                                <td>10</td>
                            </tr>
                            <tr>
                                <td>16</td>
                                <td scope="row"><a href="/football/team/488/استقلال-خوزستان"> استقلال خوزستان</a></td>
                                <td>15</td>
                                <td>8</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/6/لیگ-برتر-ایران" >جدول کامل لیگ برتر ایران</a></div>
                </div>
            </div>
            


        



            <div class="widget-holder">
                <div id="79" class="widget news">
                                
<div class="widget-header"><h2>آخرین اخبار سایر ورزش‌ها</h2></div>
<div class="widget-body">
    <div class="news-tabs">
        <ul>
            <li data-type="Latest" class="active">جدیدترین‌ها   <span class="new-news-message"></span></li>
            <li data-type="MostVisited" data-url="https://web-api.varzesh3.com/v1.0/news/most-visited?excludeSports[0]=Football&amp;excludeSports[1]=Futsal&amp;excludeSports[2]=BeachSoccer">پربازدیدترین‌ها</li>
            <li data-type="MostCommented" data-url="https://web-api.varzesh3.com/v1.0/news/most-commented?excludeSports[0]=Football&amp;excludeSports[1]=Futsal&amp;excludeSports[2]=BeachSoccer">پربحث‌ترین‌ها</li>
        </ul>
    </div>
    <div class="news-content" data-type="Latest">
        
        <div class="alert-message">حداقل یکی از گزینه ها باید فعال باشد.</div>
        <div class="news-sport-filter">
            <select>
                    <option selected value="All">همه ورزش ها</option>
                    <optgroup label="پرطرفدارها">
                            <option value="3" data-url="/sport/getnews/volleyball">والیبال</option>
                            <option value="4" data-url="/sport/getnews/basketball">بسکتبال</option>
                            <option value="16" data-url="/sport/getnews/wrestling">کشتی</option>
                            <option value="5" data-url="/sport/getnews/handball">هندبال</option>
                            <option value="19" data-url="/sport/getnews/tennis">تنیس</option>
                    </optgroup>
                    <optgroup label="سایر">
                            <option value="25" data-url="/sport/getnews/autoracing">اتومبیل رانی</option>
                            <option value="43" data-url="/sport/getnews/squash">اسکواش</option>
                            <option value="42" data-url="/sport/getnews/skiing">اسکی</option>
                            <option value="27" data-url="/sport/getnews/skate">اسکیت</option>
                            <option value="21" data-url="/sport/getnews/badminton">بدمینتون</option>
                            <option value="23" data-url="/sport/getnews/wheelchairbasketball">بسکتبال با ویلچر</option>
                            <option value="12" data-url="/sport/getnews/boxing">بوکس</option>
                            <option value="30" data-url="/sport/getnews/bowling">بولینگ</option>
                            <option value="31" data-url="/sport/getnews/baseball">بیسبال</option>
                            <option value="29" data-url="/sport/getnews/billiards">بیلیارد</option>
                            <option value="17" data-url="/sport/getnews/taekwondo">تکواندو</option>
                            <option value="8" data-url="/sport/getnews/tabletennis">تنیس روی میز</option>
                            <option value="7" data-url="/sport/getnews/shooting">تیراندازی</option>
                            <option value="6" data-url="/sport/getnews/archery">تیراندازی با کمان</option>
                            <option value="45" data-url="/sport/getnews/jujutsu">جوجیتسو</option>
                            <option value="13" data-url="/sport/getnews/judo">جودو</option>
                            <option value="14" data-url="/sport/getnews/athletics">دو و میدانی</option>
                            <option value="9" data-url="/sport/getnews/cycling">دوچرخه سواری</option>
                            <option value="32" data-url="/sport/getnews/gymnastics">ژیمناستیک</option>
                            <option value="26" data-url="/sport/getnews/horseriding">سوارکاری</option>
                            <option value="33" data-url="/sport/getnews/chess">شطرنج</option>
                            <option value="11" data-url="/sport/getnews/fencing">شمشیربازی</option>
                            <option value="22" data-url="/sport/getnews/swim">شنا</option>
                            <option value="10" data-url="/sport/getnews/rowing">قایقرانی</option>
                            <option value="18" data-url="/sport/getnews/canoesprint">قایقرانی سرعتی (کنو)</option>
                            <option value="20" data-url="/sport/getnews/karate">کاراته</option>
                            <option value="34" data-url="/sport/getnews/kabaddi">کبدی</option>
                            <option value="44" data-url="/sport/getnews/kurash">کوراش</option>
                            <option value="35" data-url="/sport/getnews/mountaineering">کوهنوردی</option>
                            <option value="36" data-url="/sport/getnews/golf">گلف</option>
                            <option value="37" data-url="/sport/getnews/motorcycling">موتورسواری</option>
                            <option value="38" data-url="/sport/getnews/hockey">هاکی</option>
                            <option value="39" data-url="/sport/getnews/waterpolo">واترپلو</option>
                            <option value="24" data-url="/sport/getnews/sittingvolleyball">والیبال نشسته</option>
                            <option value="15" data-url="/sport/getnews/weightlifting">وزنه برداری</option>
                            <option value="40" data-url="/sport/getnews/wushu">ووشو</option>
                    </optgroup>
            </select>
        </div>
        <div class="news-main-list scrollable-box" data-height="1000" style="max-height: 1000px">
            <div class="scroll-list-content">
                <ul>
                            <li data-newsid="1994697" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="43">
                                <a title="تفاهم نامه اسکواش ایران با تایلند امضا شد" href="https://www.varzesh3.com/news/1994697/تفاهم-نامه-اسکواش-ایران-با-تایلند-امضا-شد" data-nt-link> <span class="news-type"></span>تفاهم نامه اسکواش ایران با تایلند امضا شد</a>
                            </li>
                            <li data-newsid="322038" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال پورتلند تریل بلیزرز - فنیکس سانز" href="https://video.varzesh3.com/video/322038/خلاصه-بسکتبال-پورتلند-تریل-بلیزرز-فنیکس-سانز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال پورتلند تریل بلیزرز - فنیکس سانز</a>
                            </li>
                            <li data-newsid="1994689" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="پر ستاره‌ترین تیم والیبال دنیا زیر و‌ رو‌ می‌شود!" href="https://www.varzesh3.com/news/1994689/پر-ستاره-ترین-تیم-والیبال-دنیا-زیر-و-رو-می-شود" data-nt-link> <span class="news-type"></span>پر ستاره‌ترین تیم والیبال دنیا زیر و‌ رو‌ می‌شود!</a>
                            </li>
                            <li data-newsid="550" class="album-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="پایان طلسم ۱۳ هفته‌ای هرمزگانی‌ها در لیگ برتر بسکتبال" href="https://www.varzesh3.com/album/550/پایان-طلسم-۱۳-هفته-ای-هرمزگانی-ها-در-لیگ-برتر-بسکتبال" data-nt-link> <span class="news-type"></span>پایان طلسم ۱۳ هفته‌ای هرمزگانی‌ها در لیگ برتر بسکتبال</a>
                            </li>
                            <li data-newsid="1994663" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="خیال تیم ملی از دروازه راحت است (عکس)" href="https://www.varzesh3.com/news/1994663/خیال-تیم-ملی-از-دروازه-راحت-است-عکس" data-nt-link> <span class="news-type"></span>خیال تیم ملی از دروازه راحت است (عکس)</a>
                            </li>
                            <li data-newsid="1994661" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="7">
                                <a title="نوجوان 15 ساله ایران در آستانه المپیکی شدن" href="https://www.varzesh3.com/news/1994661/نوجوان-15-ساله-ایران-در-آستانه-المپیکی-شدن" data-nt-link> <span class="news-type"></span>نوجوان 15 ساله ایران در آستانه المپیکی شدن</a>
                            </li>
                            <li data-newsid="1994653" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="تهاتر هفت ملک شهرداری با ورزشگاه تختی" href="https://www.varzesh3.com/news/1994653/تهاتر-هفت-ملک-شهرداری-با-ورزشگاه-تختی" data-nt-link> <span class="news-type"></span>تهاتر هفت ملک شهرداری با ورزشگاه تختی</a>
                            </li>
                            <li data-newsid="322037" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال مینه سوتا تیمبرولوز - لس آنجلس کلیپرز" href="https://video.varzesh3.com/video/322037/خلاصه-بسکتبال-مینه-سوتا-تیمبرولوز-لس-آنجلس-کلیپرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال مینه سوتا تیمبرولوز - لس آنجلس کلیپرز</a>
                            </li>
                            <li data-newsid="1994643" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="23">
                                <a title="ایران انتقام هانگژو را از ژاپن گرفت" href="https://www.varzesh3.com/news/1994643/ایران-انتقام-هانگژو-را-از-ژاپن-گرفت" data-nt-link> <span class="news-type"></span>ایران انتقام هانگژو را از ژاپن گرفت</a>
                            </li>
                            <li data-newsid="1994642" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="حال خراب و‌ اسف‌بار قهرمان والیبال اروپا" href="https://www.varzesh3.com/news/1994642/حال-خراب-و-اسف-بار-قهرمان-والیبال-اروپا" data-nt-link> <span class="news-type"></span>حال خراب و‌ اسف‌بار قهرمان والیبال اروپا</a>
                            </li>
                            <li data-newsid="322036" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال میامی هیت - شارلوت هورنتس" href="https://video.varzesh3.com/video/322036/خلاصه-بسکتبال-میامی-هیت-شارلوت-هورنتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال میامی هیت - شارلوت هورنتس</a>
                            </li>
                            <li data-newsid="1994636" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="سقوط پرافتخارترین تیم ایران به رده چهارم (عکس)" href="https://www.varzesh3.com/news/1994636/سقوط-پرافتخارترین-تیم-ایران-به-رده-چهارم-عکس" data-nt-link> <span class="news-type"></span>سقوط پرافتخارترین تیم ایران به رده چهارم (عکس)</a>
                            </li>
                            <li data-newsid="1994623" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="پیروزی باکس در ثانیه پایانی" href="https://www.varzesh3.com/news/1994623/پیروزی-باکس-در-ثانیه-پایانی" data-nt-link> <span class="news-type"></span>پیروزی باکس در ثانیه پایانی</a>
                            </li>
                            <li data-newsid="322041" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال میلواکی باکس - ساکرامنتو کینگز " href="https://video.varzesh3.com/video/322041/خلاصه-بسکتبال-میلواکی-باکس-ساکرامنتو-کینگز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال میلواکی باکس - ساکرامنتو کینگز </a>
                            </li>
                            <li data-newsid="1994619" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="تاسیس فدراسیون جهانی پهلوانی به ریاست وزیر ورزش!" href="https://www.varzesh3.com/news/1994619/تاسیس-فدراسیون-جهانی-پهلوانی-به-ریاست-وزیر-ورزش" data-nt-link> <span class="news-type"></span>تاسیس فدراسیون جهانی پهلوانی به ریاست وزیر ورزش!</a>
                            </li>
                            <li data-newsid="322035" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال دنور ناگتس - ایندیانا پیسرز" href="https://video.varzesh3.com/video/322035/خلاصه-بسکتبال-دنور-ناگتس-ایندیانا-پیسرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال دنور ناگتس - ایندیانا پیسرز</a>
                            </li>
                            <li data-newsid="1994615" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="11">
                                <a title="صعود پاکدامن و محمد رهبری در رنکینگ جهانی" href="https://www.varzesh3.com/news/1994615/صعود-پاکدامن-و-محمد-رهبری-در-رنکینگ-جهانی" data-nt-link> <span class="news-type"></span>صعود پاکدامن و محمد رهبری در رنکینگ جهانی</a>
                            </li>
                            <li data-newsid="1994607" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کشتی ایران هرکول تولید می‌کند! (عکس)" href="https://www.varzesh3.com/news/1994607/کشتی-ایران-هرکول-تولید-می-کند-عکس" data-nt-link> <span class="news-type"></span>کشتی ایران هرکول تولید می‌کند! (عکس)</a>
                            </li>
                            <li data-newsid="1994606" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="صعود آسان مدودف به مرحله دوم اوپن استرالیا" href="https://www.varzesh3.com/news/1994606/صعود-آسان-مدودف-به-مرحله-دوم-اوپن-استرالیا" data-nt-link> <span class="news-type"></span>صعود آسان مدودف به مرحله دوم اوپن استرالیا</a>
                            </li>
                            <li data-newsid="1994604" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="42">
                                <a title="جوان‌های المپیکی اسکی ایران وارد می‌شوند" href="https://www.varzesh3.com/news/1994604/جوان-های-المپیکی-اسکی-ایران-وارد-می-شوند" data-nt-link> <span class="news-type"></span>جوان‌های المپیکی اسکی ایران وارد می‌شوند</a>
                            </li>
                            <li data-newsid="1994603" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="15">
                                <a title="8 وزنه بردار پارالمپیکی ایران فراخوانده شدند" href="https://www.varzesh3.com/news/1994603/8-وزنه-بردار-پارالمپیکی-ایران-فراخوانده-شدند" data-nt-link> <span class="news-type"></span>8 وزنه بردار پارالمپیکی ایران فراخوانده شدند</a>
                            </li>
                            <li data-newsid="1994601" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="روسای سابق و فعلی والیبال ایران همسفر شدند" href="https://www.varzesh3.com/news/1994601/روسای-سابق-و-فعلی-والیبال-ایران-همسفر-شدند" data-nt-link> <span class="news-type"></span>روسای سابق و فعلی والیبال ایران همسفر شدند</a>
                            </li>
                            <li data-newsid="1994600" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="گزینه تیم ملی والیبال ایران در ایتالیا گل کاشت" href="https://www.varzesh3.com/news/1994600/گزینه-تیم-ملی-والیبال-ایران-در-ایتالیا-گل-کاشت" data-nt-link> <span class="news-type"></span>گزینه تیم ملی والیبال ایران در ایتالیا گل کاشت</a>
                            </li>
                            <li data-newsid="1994598" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="24">
                                <a title="ایران میزبان لیگ جهانی والیبال نشسته می‌شود" href="https://www.varzesh3.com/news/1994598/ایران-میزبان-لیگ-جهانی-والیبال-نشسته-می-شود" data-nt-link> <span class="news-type"></span>ایران میزبان لیگ جهانی والیبال نشسته می‌شود</a>
                            </li>
                            <li data-newsid="1994591" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="ادعای بزرگ از رقیب: جوکوویچ بهترین ورزشکار تاریخ" href="https://www.varzesh3.com/news/1994591/ادعای-بزرگ-از-رقیب-جوکوویچ-بهترین-ورزشکار-تاریخ" data-nt-link> <span class="news-type"></span>ادعای بزرگ از رقیب: جوکوویچ بهترین ورزشکار تاریخ</a>
                            </li>
                            <li data-newsid="1994537" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="نیمکت‌نشینی امین علیه‌ شگفتی‌سازی ورونا" href="https://www.varzesh3.com/news/1994537/نیمکت-نشینی-امین-علیه-شگفتی-سازی-ورونا" data-nt-link> <span class="news-type"></span>نیمکت‌نشینی امین علیه‌ شگفتی‌سازی ورونا</a>
                            </li>
                            <li data-newsid="1994516" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="پایان کار تیم چهار نفره فرنگی با یک طلا و یک نقره" href="https://www.varzesh3.com/news/1994516/پایان-کار-تیم-چهار-نفره-فرنگی-با-یک-طلا-و-یک-نقره" data-nt-link> <span class="news-type"></span>پایان کار تیم چهار نفره فرنگی با یک طلا و یک نقره</a>
                            </li>
                            <li data-newsid="1994511" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="فردين براى قهرمان جهان خط و نشان كشيد!" href="https://www.varzesh3.com/news/1994511/فردين-براى-قهرمان-جهان-خط-و-نشان-كشيد" data-nt-link> <span class="news-type"></span>فردين براى قهرمان جهان خط و نشان كشيد!</a>
                            </li>
                            <li data-newsid="321990" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="مدال طلای هدایتی در رقابت‌های اوپن کرواسی" href="https://video.varzesh3.com/video/321990/مدال-طلای-هدایتی-در-رقابت-های-اوپن-کرواسی" data-nt-link> <span class="news-type"></span>مدال طلای هدایتی در رقابت‌های اوپن کرواسی</a>
                            </li>
                            <li data-newsid="1994484" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="روز&#xA0;اول&#xA0;رقابت‌های&#xA0;اوپن&#xA0;استرالیا: بدون شگفتی!" href="https://www.varzesh3.com/news/1994484/روز-اول-رقابت-های-اوپن-استرالیا-بدون-شگفتی" data-nt-link> <span class="news-type"></span>روز&#xA0;اول&#xA0;رقابت‌های&#xA0;اوپن&#xA0;استرالیا: بدون شگفتی!</a>
                            </li>
                            <li data-newsid="1994474" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="فيروزجا، برنده دوئل بزرگ ايرانى‌ها در تاتااستايل" href="https://www.varzesh3.com/news/1994474/فيروزجا-برنده-دوئل-بزرگ-ايرانى-ها-در-تاتااستايل" data-nt-link> <span class="news-type"></span>فيروزجا، برنده دوئل بزرگ ايرانى‌ها در تاتااستايل</a>
                            </li>
                            <li data-newsid="1994470" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="قدرت‌نمايى گرگان و شكست مهرام در بازى حساس هفته" href="https://www.varzesh3.com/news/1994470/قدرتنمايى-گرگان-و-شكست-مهرام-در-بازى-حساس-هفته" data-nt-link> <span class="news-type"></span>قدرت‌نمايى گرگان و شكست مهرام در بازى حساس هفته</a>
                            </li>
                            <li data-newsid="1994467" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="صعود هندبال ايران با عبور از ديوار چين قطعى شد" href="https://www.varzesh3.com/news/1994467/صعود-هندبال-ايران-با-عبور-از-ديوار-چين-قطعى-شد" data-nt-link> <span class="news-type"></span>صعود هندبال ايران با عبور از ديوار چين قطعى شد</a>
                            </li>
                            <li data-newsid="321981" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="خلاصه هندبال ایران 24 - چین 22" href="https://video.varzesh3.com/video/321981/خلاصه-هندبال-ایران-24-چین-22" data-nt-link> <span class="news-type"></span>خلاصه هندبال ایران 24 - چین 22</a>
                            </li>
                            <li data-newsid="1994451" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="تمام رقبای ستاره جوان برای فتح سکوی پاریس" href="https://www.varzesh3.com/news/1994451/تمام-رقبای-ستاره-جوان-برای-سکوی-فتح-پاریس" data-nt-link> <span class="news-type"></span>تمام رقبای ستاره جوان برای فتح سکوی پاریس</a>
                            </li>
                            <li data-newsid="321953" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="ویسی: مقابل تیم قلدری موفق به کسب پیروزی شدیم" href="https://video.varzesh3.com/video/321953/ویسی-مقابل-تیم-قلدری-موفق-به-کسب-پیروزی-شدیم" data-nt-link> <span class="news-type"></span>ویسی: مقابل تیم قلدری موفق به کسب پیروزی شدیم</a>
                            </li>
                            <li data-newsid="321952" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="سامری: شعارهای روی سکو آزاردهنده شده است " href="https://video.varzesh3.com/video/321952/سامری-شعارهای-روی-سکو-آزاردهنده-شده-است" data-nt-link> <span class="news-type"></span>سامری: شعارهای روی سکو آزاردهنده شده است </a>
                            </li>
                            <li data-newsid="321950" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="ویدئو چک مهر تاییدی بر پیروزی آورتا در آمل" href="https://video.varzesh3.com/video/321950/ویدئو-چک-مهر-تاییدی-بر-پیروزی-آورتا-در-آمل" data-nt-link> <span class="news-type"></span>ویدئو چک مهر تاییدی بر پیروزی آورتا در آمل</a>
                            </li>
                            <li data-newsid="1994413" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="عجیب‌ترین حکم ممکن: این خودش یک بی‌قانونی است!" href="https://www.varzesh3.com/news/1994413/عجیب-ترین-حکم-ممکن-این-خودش-یک-بی-قانونی-است" data-nt-link> <span class="news-type"></span>عجیب‌ترین حکم ممکن: این خودش یک بی‌قانونی است!</a>
                            </li>
                            <li data-newsid="321943" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="حضور حامد حدادی در سالن‌ پیامبراعظم آمل" href="https://video.varzesh3.com/video/321943/حضور-حامد-حدادی-در-سالن-پیامبراعظم-آمل" data-nt-link> <span class="news-type"></span>حضور حامد حدادی در سالن‌ پیامبراعظم آمل</a>
                            </li>
                            <li data-newsid="321940" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="هدایتی با پیروزی قاطع راهی فینال کشتی زاگرب شد" href="https://video.varzesh3.com/video/321940/هدایتی-با-پیروزی-قاطع-راهی-فینال-کشتی-زاگرب-شد" data-nt-link> <span class="news-type"></span>هدایتی با پیروزی قاطع راهی فینال کشتی زاگرب شد</a>
                            </li>
                            <li data-newsid="321936" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="هدایتی با غلبه بر حریف کوبایی به نیمه‌نهایی رسید" href="https://video.varzesh3.com/video/321936/هدایتی-با-غلبه-بر-حریف-کوبایی-به-نیمه-نهایی-رسید" data-nt-link> <span class="news-type"></span>هدایتی با غلبه بر حریف کوبایی به نیمه‌نهایی رسید</a>
                            </li>
                            <li data-newsid="321935" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="برد هدایتی مقابل حریف چینی در مرحله یک هشتم" href="https://video.varzesh3.com/video/321935/برد-هدایتی-مقابل-حریف-چینی-در-مسابقات-کرواسی" data-nt-link> <span class="news-type"></span>برد هدایتی مقابل حریف چینی در مرحله یک هشتم</a>
                            </li>
                            <li data-newsid="1994387" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="پدیده اوپن استرالیا جوکوویچ را به زحمت انداخت!" href="https://www.varzesh3.com/news/1994387/پدیده-اوپن-استرالیا-جوکوویچ-را-به-زحمت-انداخت" data-nt-link> <span class="news-type"></span>پدیده اوپن استرالیا جوکوویچ را به زحمت انداخت!</a>
                            </li>
                            <li data-newsid="321906" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="10 حرکت برتر بسکتبال حرفه‌ای NBA در شب گذشته" href="https://video.varzesh3.com/video/321906/10-حرکت-برتر-بسکتبال-حرفه-ای-nba-در-شب-گذشته" data-nt-link> <span class="news-type"></span>10 حرکت برتر بسکتبال حرفه‌ای NBA در شب گذشته</a>
                            </li>
                            <li data-newsid="1994369" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="8">
                                <a title="شکست دختر پینگ‌پنگ‌باز ایران در مسابقات قطر" href="https://www.varzesh3.com/news/1994369/شکست-دختر-پینگ-پنگ-باز-ایران-در-مسابقات-قطر" data-nt-link> <span class="news-type"></span>شکست دختر پینگ‌پنگ‌باز ایران در مسابقات قطر</a>
                            </li>
                            <li data-newsid="1994366" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="دومین کشتی‌گیر المپیکی ایران هم معرفی شد" href="https://www.varzesh3.com/news/1994366/دومین-کشتی-گیر-المپیکی-ایران-هم-معرفی-شد" data-nt-link> <span class="news-type"></span>دومین کشتی‌گیر المپیکی ایران هم معرفی شد</a>
                            </li>
                            <li data-newsid="321927" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="برگزاری سمینار جهانی ورزش زورخانه‌ای و پهلوانی" href="https://video.varzesh3.com/video/321927/برگزاری-سمینار-جهانی-ورزش-زورخانه-ای-و-پهلوانی" data-nt-link> <span class="news-type"></span>برگزاری سمینار جهانی ورزش زورخانه‌ای و پهلوانی</a>
                            </li>
                            <li data-newsid="1994365" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="کامبوج، میزبان یک رویداد بزرگ آسیایی" href="https://www.varzesh3.com/news/1994365/کامبوج-میزبان-یک-رویداد-بزرگ-آسیایی" data-nt-link> <span class="news-type"></span>کامبوج، میزبان یک رویداد بزرگ آسیایی</a>
                            </li>
                            <li data-newsid="1994364" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="15">
                                <a title="حرف‌های تکان دهنده خروس طلایی ایران" href="https://www.varzesh3.com/news/1994364/حرف-های-تکان-دهنده-خروس-طلایی-ایران" data-nt-link> <span class="news-type"></span>حرف‌های تکان دهنده خروس طلایی ایران</a>
                            </li>
                            <li data-newsid="321903" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال دالاس ماوریکس - نیو اورلینز پلیکانز" href="https://video.varzesh3.com/video/321903/خلاصه-بسکتبال-دالاس-ماوریکس-نیو-اورلینز-پلیکانز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال دالاس ماوریکس - نیو اورلینز پلیکانز</a>
                            </li>
                            <li data-newsid="321902" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال ممفیس گریزلیز - نیویورک نیکس" href="https://video.varzesh3.com/video/321902/خلاصه-بسکتبال-ممفیس-گریزلیز-نیویورک-نیکس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال ممفیس گریزلیز - نیویورک نیکس</a>
                            </li>
                            <li data-newsid="321901" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال اوکلاهاما سیتی تاندر - اورلاندو مجیک" href="https://video.varzesh3.com/video/321901/خلاصه-بسکتبال-اوکلاهاما-سیتی-تاندر-اورلاندو-مجیک" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال اوکلاهاما سیتی تاندر - اورلاندو مجیک</a>
                            </li>
                            <li data-newsid="321900" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال آتلانتا هاوکس - واشینگتن ویزاردز" href="https://video.varzesh3.com/video/321900/خلاصه-بسکتبال-آتلانتا-هاوکس-واشینگتن-ویزاردز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال آتلانتا هاوکس - واشینگتن ویزاردز</a>
                            </li>
                            <li data-newsid="1994335" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کشتی‌گیر ایرانی عضو تیم ملی کانادا شد!" href="https://www.varzesh3.com/news/1994335/کشتی-گیر-ایرانی-عضو-تیم-ملی-کانادا-شد" data-nt-link> <span class="news-type"></span>کشتی‌گیر ایرانی عضو تیم ملی کانادا شد!</a>
                            </li>
                            <li data-newsid="1994333" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="تساوی مقصودلو در دور اول تاتا استیل" href="https://www.varzesh3.com/news/1994333/تساوی-مقصودلو-در-دور-اول-تاتا-استیل" data-nt-link> <span class="news-type"></span>تساوی مقصودلو در دور اول تاتا استیل</a>
                            </li>
                            <li data-newsid="1994325" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="زارع - تنها صدرنشین رنکینگ کشتی آزاد UWW" href="https://www.varzesh3.com/news/1994325/زارع-تنها-صدرنشین-رنکینگ-کشتی-آزاد-uww" data-nt-link> <span class="news-type"></span>زارع - تنها صدرنشین رنکینگ کشتی آزاد UWW</a>
                            </li>
                            <li data-newsid="321905" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال یوتا جاز - لس آنجلس لیکرز" href="https://video.varzesh3.com/video/321905/خلاصه-بسکتبال-یوتا-جاز-لس-آنجلس-لیکرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال یوتا جاز - لس آنجلس لیکرز</a>
                            </li>
                            <li data-newsid="321904" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال سن آنتونیو اسپرز - شیکاگو بولز" href="https://video.varzesh3.com/video/321904/خلاصه-بسکتبال-سن-آنتونیو-اسپرز-شیکاگو-بولز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال سن آنتونیو اسپرز - شیکاگو بولز</a>
                            </li>
                            <li data-newsid="1994307" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="روزهای تلخ نایب‌قهرمان ویمبلدون: انصراف از استرالیا" href="https://www.varzesh3.com/news/1994307/روزهای-تلخ-نایب-قهرمان-ویمبلدون-انصراف-از-استرالیا" data-nt-link> <span class="news-type"></span>روزهای تلخ نایب‌قهرمان ویمبلدون: انصراف از استرالیا</a>
                            </li>
                            <li data-newsid="1994302" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="23">
                                <a title="دومين برد تیم ملی بسکتبال با ویلچر برابر تایلند" href="https://www.varzesh3.com/news/1994302/دومين-برد-تیم-ملی-بسکتبال-با-ویلچر-برابر-تایلند" data-nt-link> <span class="news-type"></span>دومين برد تیم ملی بسکتبال با ویلچر برابر تایلند</a>
                            </li>
                            <li data-newsid="1994299" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="دفاع کوبنده محمد موسوی: این‌بار نه در زمین والیبال!" href="https://www.varzesh3.com/news/1994299/دفاع-کوبنده-محمد-موسوی-این-بار-نه-در-زمین-والیبال" data-nt-link> <span class="news-type"></span>دفاع کوبنده محمد موسوی: این‌بار نه در زمین والیبال!</a>
                            </li>
                            <li data-newsid="1994292" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="آلکاراس: می‌خواهم جوکوویچ را در فینال ببینم" href="https://www.varzesh3.com/news/1994292/آلکاراس-می-خواهم-جوکوویچ-را-در-فینال-ببینم" data-nt-link> <span class="news-type"></span>آلکاراس: می‌خواهم جوکوویچ را در فینال ببینم</a>
                            </li>
                            <li data-newsid="1994291" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="الکلاسیکو اینجاست: گلادیاتور روبه‌روی نابغه" href="https://www.varzesh3.com/news/1994291/الکلاسیکو-اینجاست-گلادیاتور-روبروی-نابغه" data-nt-link> <span class="news-type"></span>الکلاسیکو اینجاست: گلادیاتور روبه‌روی نابغه</a>
                            </li>
                            <li data-newsid="321899" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال بوستون سلتیکس - هیوستون راکتس" href="https://video.varzesh3.com/video/321899/خلاصه-بسکتبال-بوستون-سلتیکس-هیوستون-راکتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال بوستون سلتیکس - هیوستون راکتس</a>
                            </li>
                            <li data-newsid="1994286" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="شکست سنگین هیوستون مقابل بوستون" href="https://www.varzesh3.com/news/1994286/شکست-سنگین-هیوستون-مقابل-بوستون" data-nt-link> <span class="news-type"></span>شکست سنگین هیوستون مقابل بوستون</a>
                            </li>
                            <li data-newsid="321898" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال میلواکی باکس - گلدن استیت واریرز" href="https://video.varzesh3.com/video/321898/خلاصه-بسکتبال-میلواکی-باکس-گلدن-استیت-واریرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال میلواکی باکس - گلدن استیت واریرز</a>
                            </li>
                            <li data-newsid="1994280" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="خدا بهترین قاضی است، باید جواب‌گوی یک استان باشید" href="https://www.varzesh3.com/news/1994280/خدا-بهترین-قاضی-است-باید-جوابگوی-یک-استان-باشید" data-nt-link> <span class="news-type"></span>خدا بهترین قاضی است، باید جواب‌گوی یک استان باشید</a>
                            </li>
                            <li data-newsid="1994276" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="در انتظار حل معمای پیچیده والیبال ایران" href="https://www.varzesh3.com/news/1994276/بلاتکلیفی-نگران-کننده-هیچکس-هم-دلش-نمی-سوزد" data-nt-link> <span class="news-type"></span>در انتظار حل معمای پیچیده والیبال ایران</a>
                            </li>
                            <li data-newsid="1994275" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="پاسخ سربالا النی به فدراسیون بسکتبال" href="https://www.varzesh3.com/news/1994275/پاسخ-سربالا-النی-به-فدراسیون-بسکتبال" data-nt-link> <span class="news-type"></span>پاسخ سربالا النی به فدراسیون بسکتبال</a>
                            </li>
                            <li data-newsid="1994274" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="تساوی مرد شماره یک شطرنج ایران در تاتا استیل" href="https://www.varzesh3.com/news/1994274/تساوی-مرد-شماره-یک-شطرنج-ایران-مقابل-تاتا-استیل" data-nt-link> <span class="news-type"></span>تساوی مرد شماره یک شطرنج ایران در تاتا استیل</a>
                            </li>
                            <li data-newsid="1994273" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="6">
                                <a title="شبانی: برای رسیدن به سهمیه المپیک چیزی کم نداریم" href="https://www.varzesh3.com/news/1994273/شبانی-برای-رسیدن-به-سهمیه-المپیک-چیزی-کم-نداریم" data-nt-link> <span class="news-type"></span>شبانی: برای رسیدن به سهمیه المپیک چیزی کم نداریم</a>
                            </li>
                            <li data-newsid="1994272" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="یک ایرانی دومین ستاره ارزشمند لیگ پرستاره والیبال" href="https://www.varzesh3.com/news/1994272/یک-ایرانی-دومین-ستاره-ارزشمند-لیگ-پرستاره-والیبال" data-nt-link> <span class="news-type"></span>یک ایرانی دومین ستاره ارزشمند لیگ پرستاره والیبال</a>
                            </li>
                            <li data-newsid="1994271" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="مدیر تیم قهرمان ایران و‌ چند خواسته خیلی مهم!" href="https://www.varzesh3.com/news/1994271/مدیر-تیم-قهرمان-ایران-و-چند-خواسته-خیلی-مهم" data-nt-link> <span class="news-type"></span>مدیر تیم قهرمان ایران و‌ چند خواسته خیلی مهم!</a>
                            </li>
                            <li data-newsid="1994270" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="گلبال مردان ایران در پارالمپیک پاریس" href="https://www.varzesh3.com/news/1994270/گلبال-مردان-ایران-در-پارالمپیک-پاریس" data-nt-link> <span class="news-type"></span>گلبال مردان ایران در پارالمپیک پاریس</a>
                            </li>
                            <li data-newsid="1994155" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="امین اسماعیل‌نژاد به قهرمان و صدرنشین سری‌آ رسید" href="https://www.varzesh3.com/news/1994155/امین-اسماعیل-نژاد-به-قهرمان-و-صدرنشین-سری-آ-رسید" data-nt-link> <span class="news-type"></span>امین اسماعیل‌نژاد به قهرمان و صدرنشین سری‌آ رسید</a>
                            </li>
                            <li data-newsid="1994145" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="۱۵ بازی ۱۵ برد: غول مهارنشدنی و‌ شکست‌ناپذیر" href="https://www.varzesh3.com/news/1994145/۱۵-بازی-۱۵-برد-غول-مهارنشدنی-و-شکست-ناپذیر" data-nt-link> <span class="news-type"></span>۱۵ بازی ۱۵ برد: غول مهارنشدنی و‌ شکست‌ناپذیر</a>
                            </li>
                            <li data-newsid="1994147" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="شگفتی بزرگ در ترکیه: مدافع عنوان قهرمانی تحقیر شد" href="https://www.varzesh3.com/news/1994147/شگفتی-بزرگ-در-ترکیه-مدافع-عنوان-قهرمانی-تحقیر-شد" data-nt-link> <span class="news-type"></span>شگفتی بزرگ در ترکیه: مدافع عنوان قهرمانی تحقیر شد</a>
                            </li>
                            <li data-newsid="321798" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال یوتا جاز - تورنتو رپترز" href="https://video.varzesh3.com/video/321798/خلاصه-بسکتبال-یوتا-جاز-تورنتو-رپترز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال یوتا جاز - تورنتو رپترز</a>
                            </li>
                            <li data-newsid="1994213" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="داستان تراژیک ستاره محبوب کشتی ایران!" href="https://www.varzesh3.com/news/1994213/داستان-تراژیک-ستاره-محبوب-کشتی-ایران" data-nt-link> <span class="news-type"></span>داستان تراژیک ستاره محبوب کشتی ایران!</a>
                            </li>
                            <li data-newsid="1994196" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="ستاره‌های ایرانی عاملان خوشبختی تیم رومانیایی" href="https://www.varzesh3.com/news/1994196/ستاره-های-ایرانی-عاملان-خوشبختی-تیم-رومانیایی" data-nt-link> <span class="news-type"></span>ستاره‌های ایرانی عاملان خوشبختی تیم رومانیایی</a>
                            </li>
                            <li data-newsid="1994193" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="پایان روز سوم مسابقات هندبال قهرمانی آسیا" href="https://www.varzesh3.com/news/1994193/پایان-روز-سوم-مسابقات-هندبال-قهرمانی-آسیا" data-nt-link> <span class="news-type"></span>پایان روز سوم مسابقات هندبال قهرمانی آسیا</a>
                            </li>
                            <li data-newsid="1994186" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="پنجمی و هشتمی یخ‌نوردان ایران در جام جهانی کره‌جنوبی" href="https://www.varzesh3.com/news/1994186/پنجمی-و-هشتمی-یخ-نوردان-ایران-در-جام-جهانی-کره-جنوبی" data-nt-link> <span class="news-type"></span>پنجمی و هشتمی یخ‌نوردان ایران در جام جهانی کره‌جنوبی</a>
                            </li>
                            <li data-newsid="321839" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="راه نجات لیگ والیبال ایران از اینجا می‌گذرد" href="https://video.varzesh3.com/video/321839/راه-نجات-لیگ-والیبال-ایران-از-اینجا-می-گذرد" data-nt-link> <span class="news-type"></span>راه نجات لیگ والیبال ایران از اینجا می‌گذرد</a>
                            </li>
                            <li data-newsid="1994157" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="قدردان حمایت رئیس جمهور ایران از کشتی هستم" href="https://www.varzesh3.com/news/1994157/قدردان-حمایت-رییس-جمهور-ایران-از-کشتی-هستم" data-nt-link> <span class="news-type"></span>قدردان حمایت رئیس جمهور ایران از کشتی هستم</a>
                            </li>
                            <li data-newsid="1994154" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="خواسته‌های وزیر ورزش ایران از نناد لالوویچ" href="https://www.varzesh3.com/news/1994154/خواسته-های-وزیر-ورزش-ایران-از-نناد-لالوویچ" data-nt-link> <span class="news-type"></span>خواسته‌های وزیر ورزش ایران از نناد لالوویچ</a>
                            </li>
                            <li data-newsid="1994150" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="مطمئن بودم اسنایدر جلوی من کم می‌آورد!" href="https://www.varzesh3.com/news/1994150/مطمئن-بودم-اسنایدر-جلوی-من-کم-می-آورد" data-nt-link> <span class="news-type"></span>مطمئن بودم اسنایدر جلوی من کم می‌آورد!</a>
                            </li>
                            <li data-newsid="1994149" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="11">
                                <a title="صعود محمد رهبری به جدول اصلی گرندپری تونس" href="https://www.varzesh3.com/news/1994149/صعود-محمد-رهبری-به-جدول-اصلی-گرندپری-تونس" data-nt-link> <span class="news-type"></span>صعود محمد رهبری به جدول اصلی گرندپری تونس</a>
                            </li>
                            <li data-newsid="1994144" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="ماراتن نفس‌گیر روسیه به سود یاران عبادی‌پور" href="https://www.varzesh3.com/news/1994144/ماراتن-نفس-گیر-روسیه-به-سود-یاران-عبادی-پور" data-nt-link> <span class="news-type"></span>ماراتن نفس‌گیر روسیه به سود یاران عبادی‌پور</a>
                            </li>
                            <li data-newsid="1994140" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="کامبک با شکوه با سوپر استاری به نام بردیا سعادت" href="https://www.varzesh3.com/news/1994140/کامبک-با-شکوه-با-سوپر-استاری-به-نام-بردیا-سعادت" data-nt-link> <span class="news-type"></span>کامبک با شکوه با سوپر استاری به نام بردیا سعادت</a>
                            </li>
                            <li data-newsid="1994129" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="رویاهای رقیب گرایی خیلی زود رنگ باخت" href="https://www.varzesh3.com/news/1994129/رویاهای-رقیب-گرایی-خیلی-زود-رنگ-باخت" data-nt-link> <span class="news-type"></span>رویاهای رقیب گرایی خیلی زود رنگ باخت</a>
                            </li>
                            <li data-newsid="1994122" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="25">
                                <a title="پایان حضور آلکس پالو در فرمول یک" href="https://www.varzesh3.com/news/1994122/پایان-حضور-آلکس-پالو-در-فرمول-یک" data-nt-link> <span class="news-type"></span>پایان حضور آلکس پالو در فرمول یک</a>
                            </li>
                            <li data-newsid="1994116" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="وزير ورزش با رييس كشتى جهان ديدار كرد" href="https://www.varzesh3.com/news/1994116/وزير-ورزش-با-رييس-كشتى-جهان-ديدار-كرد" data-nt-link> <span class="news-type"></span>وزير ورزش با رييس كشتى جهان ديدار كرد</a>
                            </li>
                            <li data-newsid="321796" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال دیترویت پیستونز - هیوستون راکتس" href="https://video.varzesh3.com/video/321796/خلاصه-بسکتبال-دیترویت-پیستونز-هیوستون-راکتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال دیترویت پیستونز - هیوستون راکتس</a>
                            </li>
                            <li data-newsid="1994112" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="فنرباغچه و تحقیر رقیب با کمک ملی‌پوش ایرانی" href="https://www.varzesh3.com/news/1994112/فنرباغچه-و-تحقیر-رقیب-با-کمک-ملی-پوش-ایرانی" data-nt-link> <span class="news-type"></span>فنرباغچه و تحقیر رقیب با کمک ملی‌پوش ایرانی</a>
                            </li>
                            <li data-newsid="1994109" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="فدراسیون والیبال امروز یک مهمان ویژه داشت (عکس)" href="https://www.varzesh3.com/news/1994109/فدراسیون-والیبال-امروز-یک-مهمان-ویژه-داشت-عکس" data-nt-link> <span class="news-type"></span>فدراسیون والیبال امروز یک مهمان ویژه داشت (عکس)</a>
                            </li>
                            <li data-newsid="321817" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شکست سهرابی در مقابل اسلیوا از لیتوانی 67kg" href="https://video.varzesh3.com/video/321817/شکست-سهرابی-در-مقابل-اسلیوا-از-لیتوانی-67kg" data-nt-link> <span class="news-type"></span>شکست سهرابی در مقابل اسلیوا از لیتوانی 67kg</a>
                            </li>
                            <li data-newsid="1994098" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="35">
                                <a title="صفدریان قهرمان جام جهانی یخ‌نوردی" href="https://www.varzesh3.com/news/1994098/صفدریان-قهرمان-جام-جهانی-یخ-نوردی" data-nt-link> <span class="news-type"></span>صفدریان قهرمان جام جهانی یخ‌نوردی</a>
                            </li>
                            <li data-newsid="321816" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="قهرمانی تیم دونفره ایران در فیوچرز مردان" href="https://video.varzesh3.com/video/321816/قهرمانی-تیم-دونفره-ایران-در-فیوچرز-مردان" data-nt-link> <span class="news-type"></span>قهرمانی تیم دونفره ایران در فیوچرز مردان</a>
                            </li>
                            <li data-newsid="321795" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال آتلانتا هاوکس - ایندیانا پیسرز" href="https://video.varzesh3.com/video/321795/خلاصه-بسکتبال-آتلانتا-هاوکس-ایندیانا-پیسرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال آتلانتا هاوکس - ایندیانا پیسرز</a>
                            </li>
                            <li data-newsid="1994069" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="جدیدترین لژیونر والیبال ایرانی یک سرمربی است" href="https://www.varzesh3.com/news/1994069/جدیدترین-لژیونر-والیبال-ایرانی-یک-سرمربی-است" data-nt-link> <span class="news-type"></span>جدیدترین لژیونر والیبال ایرانی یک سرمربی است</a>
                            </li>
                            <li data-newsid="1994067" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کامبک شگفت‌انگیز فرنگی کار ایرانی" href="https://www.varzesh3.com/news/1994067/کامبک-شگفت-انگیز-فرنگی-کار-ایرانی" data-nt-link> <span class="news-type"></span>کامبک شگفت‌انگیز فرنگی کار ایرانی</a>
                            </li>
                            <li data-newsid="1994054" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="قهرمانی دلچسب تیم ایران در فیوچرز مردان" href="https://www.varzesh3.com/news/1994054/قهرمانی-دلچسب-تیم-ایران-در-فیوچرز-مردان" data-nt-link> <span class="news-type"></span>قهرمانی دلچسب تیم ایران در فیوچرز مردان</a>
                            </li>
                            <li data-newsid="321808" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="برد سهرابی در مقابل یورگنسن از نروژ در وزن 67 kg" href="https://video.varzesh3.com/video/321808/برد-سهرابی-در-مقابل-یورگنسن-از-نروژ-در-وزن-67kg" data-nt-link> <span class="news-type"></span>برد سهرابی در مقابل یورگنسن از نروژ در وزن 67 kg</a>
                            </li>
                            <li data-newsid="321792" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال سن آنتونیو اسپرز - شارلوت هورنتس" href="https://video.varzesh3.com/video/321792/خلاصه-بسکتبال-سن-آنتونیو-اسپرز-شارلوت-هورنتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال سن آنتونیو اسپرز - شارلوت هورنتس</a>
                            </li>
                            <li data-newsid="1994042" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="23">
                                <a title="پیروزی تیم ملی بسکتبال با ویلچر ایران مقابل کره‌جنوبی" href="https://www.varzesh3.com/news/1994042/پیروزی-تیم-ملی-بسکتبال-با-ویلچر-ایران-مقابل-کره-جنوبی" data-nt-link> <span class="news-type"></span>پیروزی تیم ملی بسکتبال با ویلچر ایران مقابل کره‌جنوبی</a>
                            </li>
                            <li data-newsid="1994038" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="استارت تیم ملی گلبال برای پارالمپیک پاریس" href="https://www.varzesh3.com/news/1994038/استارت-تیم-ملی-گلبال-برای-پارالمپیک-پاریس" data-nt-link> <span class="news-type"></span>استارت تیم ملی گلبال برای پارالمپیک پاریس</a>
                            </li>
                            <li data-newsid="1994031" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="7">
                                <a title="برزیل، آخرین فرصت مرد طلایی توکیو و رفقا!" href="https://www.varzesh3.com/news/1994031/برزیل-آخرین-فرصت-مرد-طلایی-توکیو-و-رفقا" data-nt-link> <span class="news-type"></span>برزیل، آخرین فرصت مرد طلایی توکیو و رفقا!</a>
                            </li>
                            <li data-newsid="1994029" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="8">
                                <a title="جمعه متفاوت تنیس روی میز ایران (عکس)" href="https://www.varzesh3.com/news/1994029/جمعه-متفاوت-تنیس-روی-میز-ایران-عکس" data-nt-link> <span class="news-type"></span>جمعه متفاوت تنیس روی میز ایران (عکس)</a>
                            </li>
                            <li data-newsid="321793" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال میامی هیت - اورلاندو مجیک" href="https://video.varzesh3.com/video/321793/خلاصه-بسکتبال-میامی-هیت-اورلاندو-مجیک" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال میامی هیت - اورلاندو مجیک</a>
                            </li>
                            <li data-newsid="1994026" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="استرالیا-هند، جنگ اصلی جای دیگری است! (عکس)" href="https://www.varzesh3.com/news/1994026/استرالیا-هند-جنگ-اصلی-جای-دیگری-است-عکس" data-nt-link> <span class="news-type"></span>استرالیا-هند، جنگ اصلی جای دیگری است! (عکس)</a>
                            </li>
                            <li data-newsid="1994024" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="استیونس آمریکایی امتیازآورترین بازیکن لیگ بسکتبال" href="https://www.varzesh3.com/news/1994024/استیونس-آمریکایی-امتیازآورترین-بازیکن-لیگ-بسکتبال" data-nt-link> <span class="news-type"></span>استیونس آمریکایی امتیازآورترین بازیکن لیگ بسکتبال</a>
                            </li>
                            <li data-newsid="1994027" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="25">
                                <a title="پایان مسابقه سافاری قزوین با قهرمانی آذربایجان شرقی" href="https://www.varzesh3.com/news/1994027/پایان-مسابقه-سافاری-قزوین-با-قهرمانی-آذربایجان-شرقی" data-nt-link> <span class="news-type"></span>پایان مسابقه سافاری قزوین با قهرمانی آذربایجان شرقی</a>
                            </li>
                            <li data-newsid="1994019" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="بحران جدی 77 کیلوگرم در غیاب کاپیتان" href="https://www.varzesh3.com/news/1994019/بحران-جدی-77-کیلوگرم-در-غیاب-کاپیتان" data-nt-link> <span class="news-type"></span>بحران جدی 77 کیلوگرم در غیاب کاپیتان</a>
                            </li>
                            <li data-newsid="1994017" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="17">
                                <a title="مقانلو: تکواندوی مصر شرایط مطلوبی دارد " href="https://www.varzesh3.com/news/1994017/مقانلو-تکواندو-مصر-شرایط-مطلوبی-دارد" data-nt-link> <span class="news-type"></span>مقانلو: تکواندوی مصر شرایط مطلوبی دارد </a>
                            </li>
                            <li data-newsid="1994014" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="حل مشکل انتخاباتی شطرنج با یک انتصاب" href="https://www.varzesh3.com/news/1994014/حل-مشکل-انتخاباتی-شطرنج-با-یک-انتصاب" data-nt-link> <span class="news-type"></span>حل مشکل انتخاباتی شطرنج با یک انتصاب</a>
                            </li>
                            <li data-newsid="321800" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال دنور ناگتس - نیو اورلینز پلیکانز (گزارش اختصاصی)" href="https://video.varzesh3.com/video/321800/خلاصه-بسکتبال-دنور-ناگتس-نیو-اورلینز-پلیکانز-گزارش-اختصاصی" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال دنور ناگتس - نیو اورلینز پلیکانز (گزارش اختصاصی)</a>
                            </li>
                            <li data-newsid="1994013" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="دیدار مهم هاشمی و دبیر با رییس اتحادیه جهانی" href="https://www.varzesh3.com/news/1994013/دیدار-مهم-هاشمی-و-دبیر-با-رییس-اتحادیه-جهانی" data-nt-link> <span class="news-type"></span>دیدار مهم هاشمی و دبیر با رییس اتحادیه جهانی</a>
                            </li>
                            <li data-newsid="1994012" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="شانس جوکوویچ برای قهرمانی در اوپن استرالیا" href="https://www.varzesh3.com/news/1994012/شانس-جوکوویچ-برای-قهرمانی-در-اوپن-استرالیا" data-nt-link> <span class="news-type"></span>شانس جوکوویچ برای قهرمانی در اوپن استرالیا</a>
                            </li>
                            <li data-newsid="1994011" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="یک ایرانی سوژه جدید فدراسیون جهانی والیبال (عکس)" href="https://www.varzesh3.com/news/1994011/یک-ایرانی-سوژه-جدید-فدراسیون-جهانی-والیبال-عکس" data-nt-link> <span class="news-type"></span>یک ایرانی سوژه جدید فدراسیون جهانی والیبال (عکس)</a>
                            </li>
                            <li data-newsid="321799" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال فیلادلفیا - ساکرامنتو کینگز (گزارش اختصاصی)" href="https://video.varzesh3.com/video/321799/خلاصه-بسکتبال-فیلادلفیا-ساکرامنتو-کینگز-گزارش-اختصاصی" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال فیلادلفیا - ساکرامنتو کینگز (گزارش اختصاصی)</a>
                            </li>
                            <li data-newsid="321788" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="حلاصه بسکتبال ممفیس گریزلیز - لس‌آنجلس کلیپرز" href="https://video.varzesh3.com/video/321788/حلاصه-بسکتبال-ممفیس-گریزلیز-لس-آنجلس-کلیپرز" data-nt-link> <span class="news-type"></span>حلاصه بسکتبال ممفیس گریزلیز - لس‌آنجلس کلیپرز</a>
                            </li>
                            <li data-newsid="1994006" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="ستاره ایرانی ششمین بازیکن برتر سخت‌ترین لیگ ‌دنیا" href="https://www.varzesh3.com/news/1994006/ستاره-ایرانی-ششمین-بازیکن-برتر-سخت-ترین-لیگ-دنیا" data-nt-link> <span class="news-type"></span>ستاره ایرانی ششمین بازیکن برتر سخت‌ترین لیگ ‌دنیا</a>
                            </li>
                            <li data-newsid="1994005" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="35">
                                <a title="خطر سقوط بهمن در کمین کوهنوردان" href="https://www.varzesh3.com/news/1994005/خطر-سقوط-بهمن-در-کمین-کوهنوردان" data-nt-link> <span class="news-type"></span>خطر سقوط بهمن در کمین کوهنوردان</a>
                            </li>
                            <li data-newsid="1994004" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="والیبالیست پاکستانی لیگ کره جنوبی را به آتش کشید!" href="https://www.varzesh3.com/news/1994004/والیبالیست-پاکستانی-لیگ-کره-جنوبی-را-به-آتش-کشید" data-nt-link> <span class="news-type"></span>والیبالیست پاکستانی لیگ کره جنوبی را به آتش کشید!</a>
                            </li>
                            <li data-newsid="1994002" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="33">
                                <a title="آخرین وضعیت بدهی ۱۴ میلیاردی شطرنج" href="https://www.varzesh3.com/news/1994002/آخرین-وضعیت-بدهی-۱۴میلیاردی-شطرنج" data-nt-link> <span class="news-type"></span>آخرین وضعیت بدهی ۱۴ میلیاردی شطرنج</a>
                            </li>
                            <li data-newsid="1994001" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="15">
                                <a title="رقابت سخت معتمدی و کرمی برای سهمیه" href="https://www.varzesh3.com/news/1994001/رقابت-سخت-معتمدی-و-کرمی-برای-سهمیه" data-nt-link> <span class="news-type"></span>رقابت سخت معتمدی و کرمی برای سهمیه</a>
                            </li>
                            <li data-newsid="1994000" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="7">
                                <a title="نجمه خدمتی در تفنگ سه وضعیت هشتم شد" href="https://www.varzesh3.com/news/1994000/نجمه-خدمتی-در-تفنگ-سه-وضعیت-هشتم-شد" data-nt-link> <span class="news-type"></span>نجمه خدمتی در تفنگ سه وضعیت هشتم شد</a>
                            </li>
                            <li data-newsid="321787" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال شیکاگو بولز - گلدن استیت واریرز" href="https://video.varzesh3.com/video/321787/خلاصه-بسکتبال-شیکاگو-بولز-گلدن-استیت-واریرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال شیکاگو بولز - گلدن استیت واریرز</a>
                            </li>
                            <li data-newsid="1993999" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="10">
                                <a title="بلاتکلیفی قایقرانان پارا با نامشخص بودن کادر فنی!" href="https://www.varzesh3.com/news/1993999/بلاتکلیفی-قایقرانان-پارا-با-نامشخص-بودن-کادر-فنی" data-nt-link> <span class="news-type"></span>بلاتکلیفی قایقرانان پارا با نامشخص بودن کادر فنی!</a>
                            </li>
                            <li data-newsid="1993998" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="7">
                                <a title="نجمه خدمتی در تفنگ سه وضعیت فینالیست شد" href="https://www.varzesh3.com/news/1993998/نجمه-خدمتی-در-تفنگ-سه-وضعیت-فینالیست-شد" data-nt-link> <span class="news-type"></span>نجمه خدمتی در تفنگ سه وضعیت فینالیست شد</a>
                            </li>
                            <li data-newsid="321780" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="0">
                                <a title="اسطوره‌‌های ایرانی میهمان ویژه جام ملت‌های آسیا" href="https://video.varzesh3.com/video/321780/اسطوره-های-ایرانی-میهمان-ویژه-جام-ملت-های-آسیا" data-nt-link> <span class="news-type"></span>اسطوره‌‌های ایرانی میهمان ویژه جام ملت‌های آسیا</a>
                            </li>
                            <li data-newsid="1993951" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="روز پر استرس لژیونرهای والیبال ایران در ترکیه" href="https://www.varzesh3.com/news/1993951/روز-پر-استرس-لژیونرهای-والیبال-ایران-در-ترکیه" data-nt-link> <span class="news-type"></span>روز پر استرس لژیونرهای والیبال ایران در ترکیه</a>
                            </li>
                            <li data-newsid="1993928" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="کاپیتانی برای ملی‌پوش سابق والیبال خوش‌یمن بود" href="https://www.varzesh3.com/news/1993928/کاپیتانی-برای-ملی-پوش-سابق-والیبال-خوش-یمن-بود" data-nt-link> <span class="news-type"></span>کاپیتانی برای ملی‌پوش سابق والیبال خوش‌یمن بود</a>
                            </li>
                            <li data-newsid="1993997" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="شکست مدعی قهرمانی لیگ برتر هندبال زنان" href="https://www.varzesh3.com/news/1993997/شکست-مدعی-قهرمانی-لیگ-برتر-هندبال-زنان" data-nt-link> <span class="news-type"></span>شکست مدعی قهرمانی لیگ برتر هندبال زنان</a>
                            </li>
                            <li data-newsid="1993996" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="مکالمه خاص جوکوویچ و روبلف در استرالیا" href="https://www.varzesh3.com/news/1993996/مکالمه-خاص-جوکوویچ-و-روبلف-در-استرالیا" data-nt-link> <span class="news-type"></span>مکالمه خاص جوکوویچ و روبلف در استرالیا</a>
                            </li>
                            <li data-newsid="1993995" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="25">
                                <a title="همکاری تیم آمریکایی فرمول یک با فراری" href="https://www.varzesh3.com/news/1993995/همکاری-تیم-آمریکایی-فرمول-یک-با-فراری" data-nt-link> <span class="news-type"></span>همکاری تیم آمریکایی فرمول یک با فراری</a>
                            </li>
                            <li data-newsid="321784" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title=" رضایی: با این پیروزی امیدمان برای صعود بیشتر شد" href="https://video.varzesh3.com/video/321784/رضایی-با-این-پیروزی-امیدمان-برای-صعود-بیشتر-شد" data-nt-link> <span class="news-type"></span> رضایی: با این پیروزی امیدمان برای صعود بیشتر شد</a>
                            </li>
                            <li data-newsid="321782" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="نیما بابازاده: آمل شهر والیبال خیز است" href="https://video.varzesh3.com/video/321782/نیما-بابازاده-آمل-شهر-والیبال-خیز-است" data-nt-link> <span class="news-type"></span>نیما بابازاده: آمل شهر والیبال خیز است</a>
                            </li>
                            <li data-newsid="321781" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="ایرج حسینخانی: فعل خواستن را صرف کردند" href="https://video.varzesh3.com/video/321781/ایرج-حسینخانی-فعل-خواستن-را-صرف-کردند" data-nt-link> <span class="news-type"></span>ایرج حسینخانی: فعل خواستن را صرف کردند</a>
                            </li>
                            <li data-newsid="321778" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="موقتی: تیم‌ ما از میانگین سنی پایین برخوردار است" href="https://video.varzesh3.com/video/321778/موقتی-تیم-ما-از-میانگین-سنی-پایین-برخوردار-است" data-nt-link> <span class="news-type"></span>موقتی: تیم‌ ما از میانگین سنی پایین برخوردار است</a>
                            </li>
                            <li data-newsid="321777" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="پدرام‌فلاح: برای کسب تجربه در لیگ‌یک‌حضور داریم" href="https://video.varzesh3.com/video/321777/پدرام-فلاح-برای-کسب-تجربه-در-لیگ-یک-حضور-داریم" data-nt-link> <span class="news-type"></span>پدرام‌فلاح: برای کسب تجربه در لیگ‌یک‌حضور داریم</a>
                            </li>
                            <li data-newsid="321776" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="ایمان‌ والی زاده: متاسفانه بازی را وا دادیم" href="https://video.varzesh3.com/video/321776/ایمان-والی-زاده-متاسفانه-بازی-را-وا-دادیم" data-nt-link> <span class="news-type"></span>ایمان‌ والی زاده: متاسفانه بازی را وا دادیم</a>
                            </li>
                            <li data-newsid="1993957" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="نقره مهمدى سكانس پايانى روز اول فرنگى زاگرب" href="https://www.varzesh3.com/news/1993957/نقره-مهمدى-سكانس-پايانى-روز-اول-فرنگى-زاگرب" data-nt-link> <span class="news-type"></span>نقره مهمدى سكانس پايانى روز اول فرنگى زاگرب</a>
                            </li>
                            <li data-newsid="321770" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="مهمدی از رسیدن به طلا مسابقات کرواسی بازماند" href="https://video.varzesh3.com/video/321770/مهمدی-از-رسیدن-به-طلا-مسابقات-کرواسی-بازماند" data-nt-link> <span class="news-type"></span>مهمدی از رسیدن به طلا مسابقات کرواسی بازماند</a>
                            </li>
                            <li data-newsid="321740" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="10 حرکت برتر بسکتبال حرفه‌ای NBA در شب گذشته" href="https://video.varzesh3.com/video/321740/10-حرکت-برتر-بسکتبال-حرفه-ای-nba-در-شب-گذشته" data-nt-link> <span class="news-type"></span>10 حرکت برتر بسکتبال حرفه‌ای NBA در شب گذشته</a>
                            </li>
                            <li data-newsid="321755" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="صعود مهمدی به فینال رقابت‌های کشتی اوپن کرواسی" href="https://video.varzesh3.com/video/321755/صعود-مهمدی-به-فینال-رقابت-های-کشتی-اوپن-کرواسی" data-nt-link> <span class="news-type"></span>صعود مهمدی به فینال رقابت‌های کشتی اوپن کرواسی</a>
                            </li>
                            <li data-newsid="1993905" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="19">
                                <a title="آرزوی من گفتگوی طولانی با مسی است" href="https://www.varzesh3.com/news/1993905/آرزوی-من-گفتگوی-طولانی-با-مسی-است" data-nt-link> <span class="news-type"></span>آرزوی من گفتگوی طولانی با مسی است</a>
                            </li>
                            <li data-newsid="321743" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="خلاصه هندبال ایران 40 - نیوزلند 13" href="https://video.varzesh3.com/video/321743/خلاصه-هندبال-ایران-40-نیوزلند-13" data-nt-link> <span class="news-type"></span>خلاصه هندبال ایران 40 - نیوزلند 13</a>
                            </li>
                            <li data-newsid="321739" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="پیروزی مهمدی در مقابل ویو وانگ از چین در وزن (87kg)" href="https://video.varzesh3.com/video/321739/پیروزی-مهمدی-در-مقابل-ویو-وانگ-از-چین-در-وزن-87kg" data-nt-link> <span class="news-type"></span>پیروزی مهمدی در مقابل ویو وانگ از چین در وزن (87kg)</a>
                            </li>
                            <li data-newsid="1993877" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="باشگاه ایتالیایی بی‌خیال گزینه هدایت ایران شد" href="https://www.varzesh3.com/news/1993877/باشگاه-ایتالیایی-بی-خیال-گزینه-هدایت-ایران-شد" data-nt-link> <span class="news-type"></span>باشگاه ایتالیایی بی‌خیال گزینه هدایت ایران شد</a>
                            </li>
                            <li data-newsid="1993845" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="بهترین استفاده ممکن از شکست مدافع قهرمانی" href="https://www.varzesh3.com/news/1993845/بهترین-استفاده-ممکن-از-شکست-مدافع-قهرمانی" data-nt-link> <span class="news-type"></span>بهترین استفاده ممکن از شکست مدافع قهرمانی</a>
                            </li>
                            <li data-newsid="321727" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال لس‌آنجلس لیکرز - فینیکس سانز" href="https://video.varzesh3.com/video/321727/خلاصه-بسکتبال-لس-آنجلس-لیکرز-فینیکس-سانز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال لس‌آنجلس لیکرز - فینیکس سانز</a>
                            </li>
                            <li data-newsid="1993833" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="صورت‌زخمی سکوی المپیک را شبیه‌سازی کرد!" href="https://www.varzesh3.com/news/1993833/صورت-زخمی-سکوی-المپیک-را-شبیه-سازی-کرد" data-nt-link> <span class="news-type"></span>صورت‌زخمی سکوی المپیک را شبیه‌سازی کرد!</a>
                            </li>
                            <li data-newsid="1993828" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="17">
                                <a title="ناهید کیانی رسما به المپیک پاریس رسید" href="https://www.varzesh3.com/news/1993828/ناهید-کیانی-رسما-به-المپیک-پاریس-رسید" data-nt-link> <span class="news-type"></span>ناهید کیانی رسما به المپیک پاریس رسید</a>
                            </li>
                            <li data-newsid="1993829" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شکست سنگین عبدی در مبارزه اول" href="https://www.varzesh3.com/news/1993829/شکست-سنگین-عبدی-در-مبارزه-اول" data-nt-link> <span class="news-type"></span>شکست سنگین عبدی در مبارزه اول</a>
                            </li>
                            <li data-newsid="321732" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شکست عبدی در مقابل کامنجاسویچ در وزن (77kg)" href="https://video.varzesh3.com/video/321732/شکست-عبدی-در-مقابل-کامنجاسویچ-در-وزن-77kg" data-nt-link> <span class="news-type"></span>شکست عبدی در مقابل کامنجاسویچ در وزن (77kg)</a>
                            </li>
                            <li data-newsid="1993816" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="این بدترین ورژن یک مدافع عنوان قهرمانی است" href="https://www.varzesh3.com/news/1993816/این-بدترین-ورژن-یک-مدافع-عنوان-قهرمانی-است" data-nt-link> <span class="news-type"></span>این بدترین ورژن یک مدافع عنوان قهرمانی است</a>
                            </li>
                            <li data-newsid="1993810" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="رسمی: والیبال در المپیک پاریس با یک قانون جدید" href="https://www.varzesh3.com/news/1993810/رسمی-والیبال-در-المپیک-پاریس-با-یک-قانون-جدید" data-nt-link> <span class="news-type"></span>رسمی: والیبال در المپیک پاریس با یک قانون جدید</a>
                            </li>
                            <li data-newsid="321725" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال اوکلاهاما سیتی تاندر - پورتلند تریل بلیزرز" href="https://video.varzesh3.com/video/321725/خلاصه-بسکتبال-اوکلاهاما-سیتی-تاندر-پورتلند-تریل-بلیزرز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال اوکلاهاما سیتی تاندر - پورتلند تریل بلیزرز</a>
                            </li>
                            <li data-newsid="1993796" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="فوق ستاره والیبال دنیا در آستانه انتقال به ژاپن!" href="https://www.varzesh3.com/news/1993796/فوق-ستاره-والیبال-دنیا-در-آستانه-انتقال-به-ژاپن" data-nt-link> <span class="news-type"></span>فوق ستاره والیبال دنیا در آستانه انتقال به ژاپن!</a>
                            </li>
                            <li data-newsid="1993789" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="تیم هفته: رونمایی از عوامل خلق شگفتی" href="https://www.varzesh3.com/news/1993789/تیم-هفته-رونمایی-از-عوامل-خلق-شگفتی" data-nt-link> <span class="news-type"></span>تیم هفته: رونمایی از عوامل خلق شگفتی</a>
                            </li>
                            <li data-newsid="321724" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال کلیولند کاوالیرز - بروکلین نتس" href="https://video.varzesh3.com/video/321724/خلاصه-بسکتبال-کلیولند-کاوالیرز-بروکلین-نتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال کلیولند کاوالیرز - بروکلین نتس</a>
                            </li>
                            <li data-newsid="1993786" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="شوک به والیبال لهستان: پادشاه در آستانه حذف!" href="https://www.varzesh3.com/news/1993786/شوک-به-والیبال-لهستان-پادشاه-در-آستانه-حذف" data-nt-link> <span class="news-type"></span>شوک به والیبال لهستان: پادشاه در آستانه حذف!</a>
                            </li>
                            <li data-newsid="1993783" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="7">
                                <a title="تیراندازان در تفنگ سه وضعیت به فینال نرسیدند" href="https://www.varzesh3.com/news/1993783/تیراندازان-در-تفنگ-سه-وضعیت-به-فینال-نرسیدند" data-nt-link> <span class="news-type"></span>تیراندازان در تفنگ سه وضعیت به فینال نرسیدند</a>
                            </li>
                            <li data-newsid="1993784" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="10">
                                <a title="خاطره تلخ دختر قایقران ایران از المپیک توکیو" href="https://www.varzesh3.com/news/1993784/خاطره-تلخ-دختر-قایقران-ایران-از-المپیک-توکیو" data-nt-link> <span class="news-type"></span>خاطره تلخ دختر قایقران ایران از المپیک توکیو</a>
                            </li>
                            <li data-newsid="1993785" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="23">
                                <a title="آغاز جدال بسکتبال با ویلچر برای پارالمپیکی شدن" href="https://www.varzesh3.com/news/1993785/آغاز-جدال-بسکتبال-با-ویلچر-برای-پارالمپیکی-شدن" data-nt-link> <span class="news-type"></span>آغاز جدال بسکتبال با ویلچر برای پارالمپیکی شدن</a>
                            </li>
                            <li data-newsid="321723" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال دالاس ماوریکس - نیویورک نیکس" href="https://video.varzesh3.com/video/321723/خلاصه-بسکتبال-دالاس-ماوریکس-نیویورک-نیکس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال دالاس ماوریکس - نیویورک نیکس</a>
                            </li>
                            <li data-newsid="1993782" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="13">
                                <a title="مربی تیم‌ملی جودو: از کار اخراج شدم" href="https://www.varzesh3.com/news/1993782/مربی-تیم-ملی-جودو-از-کار-اخراج-شدم" data-nt-link> <span class="news-type"></span>مربی تیم‌ملی جودو: از کار اخراج شدم</a>
                            </li>
                            <li data-newsid="321721" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال میلواکی باکس - بوستون سلتیکس" href="https://video.varzesh3.com/video/321721/خلاصه-بسکتبال-میلواکی-باکس-بوستون-سلتیکس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال میلواکی باکس - بوستون سلتیکس</a>
                            </li>
                            <li data-newsid="546" class="album-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="درخشش نماینده بسکتبال ایران در آسیا" href="https://www.varzesh3.com/album/546/درخشش-نماینده-بسکتبال-ایران-در-آسیا" data-nt-link> <span class="news-type"></span>درخشش نماینده بسکتبال ایران در آسیا</a>
                            </li>
                            <li data-newsid="321709" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال یوتا جاز - دنور ناگتس" href="https://video.varzesh3.com/video/321709/خلاصه-بسکتبال-یوتا-جاز-دنور-ناگتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال یوتا جاز - دنور ناگتس</a>
                            </li>
                            <li data-newsid="1993746" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="طوفان در زاگرب، غول آمريكايى در خاک نشست!" href="https://www.varzesh3.com/news/1993746/طوفان-در-زاگرب-غول-آمريكايى-در-خاک-نشست" data-nt-link> <span class="news-type"></span>طوفان در زاگرب، غول آمريكايى در خاک نشست!</a>
                            </li>
                            <li data-newsid="321710" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کسب مدال طلای زارع در رقابت‌های اوپن کرواسی" href="https://video.varzesh3.com/video/321710/کسب-مدال-طلای-زارع-در-رقابت-های-اوپن-کرواسی" data-nt-link> <span class="news-type"></span>کسب مدال طلای زارع در رقابت‌های اوپن کرواسی</a>
                            </li>
                            <li data-newsid="1993731" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="هرکول کشتی ایران بلیت پاریس را رزرو کرد" href="https://www.varzesh3.com/news/1993731/هرکول-کشتی-ایران-بلیت-پاریس-را-رزرو-کرد" data-nt-link> <span class="news-type"></span>هرکول کشتی ایران بلیت پاریس را رزرو کرد</a>
                            </li>
                            <li data-newsid="321708" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کسب مدال طلای آذرپیرا در اوپن کرواسی " href="https://video.varzesh3.com/video/321708/کسب-مدال-طلای-آذرپیرا-در-اوپن-کرواسی" data-nt-link> <span class="news-type"></span>کسب مدال طلای آذرپیرا در اوپن کرواسی </a>
                            </li>
                            <li data-newsid="1993721" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شگفتى بزرگ: غول آمريكايى برابر جوان ايرانى زانو زد" href="https://www.varzesh3.com/news/1993721/شگفتى-بزرگ-غول-آمريكايى-برابر-جوان-ايرانى-زانو-زد" data-nt-link> <span class="news-type"></span>شگفتى بزرگ: غول آمريكايى برابر جوان ايرانى زانو زد</a>
                            </li>
                            <li data-newsid="1993719" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="برنز سهم كامران قاسمپور از كرواسى" href="https://www.varzesh3.com/news/1993719/برنز-سهم-كامران-قاسمپور-از-كرواسى" data-nt-link> <span class="news-type"></span>برنز سهم كامران قاسمپور از كرواسى</a>
                            </li>
                            <li data-newsid="1993718" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="ساجس در تهران هم برابر گرگانى‌ها زانو زد" href="https://www.varzesh3.com/news/1993718/ساجس-در-تهران-هم-برابر-گرگانى-ها-زانو-زد" data-nt-link> <span class="news-type"></span>ساجس در تهران هم برابر گرگانى‌ها زانو زد</a>
                            </li>
                            <li data-newsid="1993712" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="اولين طلاى ايران در زاگرب به نام محمد نخودى" href="https://www.varzesh3.com/news/1993712/اولين-طلاى-ايران-در-زاگرب-به-نام-محمد-نخودى" data-nt-link> <span class="news-type"></span>اولين طلاى ايران در زاگرب به نام محمد نخودى</a>
                            </li>
                            <li data-newsid="321706" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="کسب مدال طلای مسابقات اوپن کرواسی توسط نخودی" href="https://video.varzesh3.com/video/321706/کسب-مدال-طلای-مسابقات-اوپن-کرواسی-توسط-نخودی" data-nt-link> <span class="news-type"></span>کسب مدال طلای مسابقات اوپن کرواسی توسط نخودی</a>
                            </li>
                            <li data-newsid="321705" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="ضربه‌فنی شیخ‌حسنی مقابل حریف آمریکایی (79 KG)" href="https://video.varzesh3.com/video/321705/ضربه-فنی-شیخ-حسنی-مقابل-حریف-آمریکایی-79-kg" data-nt-link> <span class="news-type"></span>ضربه‌فنی شیخ‌حسنی مقابل حریف آمریکایی (79 KG)</a>
                            </li>
                            <li data-newsid="1993691" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="همشهریان سردار آزمون کولاک کردند(عکس)" href="https://www.varzesh3.com/news/1993691/همشهریان-سردار-آزمون-کولاک-کردند-عکس" data-nt-link> <span class="news-type"></span>همشهریان سردار آزمون کولاک کردند(عکس)</a>
                            </li>
                            <li data-newsid="321654" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال لس آنجلس کلیپرز - تورنتو رپترز" href="https://video.varzesh3.com/video/321654/خلاصه-بسکتبال-لس-آنجلس-کلیپرز-تورنتو-رپترز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال لس آنجلس کلیپرز - تورنتو رپترز</a>
                            </li>
                            <li data-newsid="1993690" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="گران‌قیمت‌ترین والیبالیست دنیا: من می‌روم، خداحافظ!" href="https://www.varzesh3.com/news/1993690/گرانقیمت-ترین-والیبالیست-دنیا-من-می-روم-خداحافظ" data-nt-link> <span class="news-type"></span>گران‌قیمت‌ترین والیبالیست دنیا: من می‌روم، خداحافظ!</a>
                            </li>
                            <li data-newsid="321680" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="37">
                                <a title="برترین لحظات موتو 2 در ژاپن " href="https://video.varzesh3.com/video/321680/برترین-لحظات-موتو-2-در-ژاپن" data-nt-link> <span class="news-type"></span>برترین لحظات موتو 2 در ژاپن </a>
                            </li>
                            <li data-newsid="321652" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال شارلوت هورنتس - ساکرامنتو کینگز" href="https://video.varzesh3.com/video/321652/خلاصه-بسکتبال-شارلوت-هورنتس-ساکرامنتو-کینگز" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال شارلوت هورنتس - ساکرامنتو کینگز</a>
                            </li>
                            <li data-newsid="1993681" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="اعلام تیم منتخب لیگ پرستاره والیبال دنیا" href="https://www.varzesh3.com/news/1993681/اعلام-تیم-منتخب-لیگ-پرستاره-والیبال-دنیا" data-nt-link> <span class="news-type"></span>اعلام تیم منتخب لیگ پرستاره والیبال دنیا</a>
                            </li>
                            <li data-newsid="1993679" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="يک طلای قطعی و ۶ مدال در انتظار آزادکاران ایرانی" href="https://www.varzesh3.com/news/1993679/يک-طلای-قطعی-و-۶-مدال-در-انتظار-آزادکاران-ایرانی" data-nt-link> <span class="news-type"></span>يک طلای قطعی و ۶ مدال در انتظار آزادکاران ایرانی</a>
                            </li>
                            <li data-newsid="1993678" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="5">
                                <a title="ایران-نیوزلند: گام اول از يک ماموریت دشوار" href="https://www.varzesh3.com/news/1993678/ایران-نیوزلند-گام-اول-از-يک-ماموریت-دشوار" data-nt-link> <span class="news-type"></span>ایران-نیوزلند: گام اول از يک ماموریت دشوار</a>
                            </li>
                            <li data-newsid="1993674" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="تیم مریضی که انگار درمان‌پذیر نیست!" href="https://www.varzesh3.com/news/1993674/تیم-مریضی-که-انگار-درمان-پذیر-نیست" data-nt-link> <span class="news-type"></span>تیم مریضی که انگار درمان‌پذیر نیست!</a>
                            </li>
                            <li data-newsid="321648" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="4">
                                <a title="خلاصه بسکتبال شیکاگو بولز - هیوستون راکتس" href="https://video.varzesh3.com/video/321648/خلاصه-بسکتبال-شیکاگو-بولز-هیوستون-راکتس" data-nt-link> <span class="news-type"></span>خلاصه بسکتبال شیکاگو بولز - هیوستون راکتس</a>
                            </li>
                            <li data-newsid="1993667" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="کامبک به لیگ با فرهاد قائمی و بقیه " href="https://www.varzesh3.com/news/1993667/کامبک-به-لیگ-با-فرهاد-قائمی-و-بقیه" data-nt-link> <span class="news-type"></span>کامبک به لیگ با فرهاد قائمی و بقیه </a>
                            </li>
                            <li data-newsid="1993662" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="3">
                                <a title="بغض تیم محبوب والیبال ایران شکست" href="https://www.varzesh3.com/news/1993662/بغض-تیم-محبوب-والیبال-ایران-شکست" data-nt-link> <span class="news-type"></span>بغض تیم محبوب والیبال ایران شکست</a>
                            </li>
                            <li data-newsid="1993658" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="زور سلطان زيرهاى ناب ايرانى به اسنايدر نرسيد" href="https://www.varzesh3.com/news/1993658/زور-سلطان-زيرهاى-ناب-ايرانى-به-اسنايدر-نرسيد" data-nt-link> <span class="news-type"></span>زور سلطان زيرهاى ناب ايرانى به اسنايدر نرسيد</a>
                            </li>
                            <li data-newsid="321679" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شکست قاسم‌پور مقابل اسنایدر از آمریکا در وزن (97Kg)" href="https://video.varzesh3.com/video/321679/شکست-قاسم-پور-مقابل-اسنایدر-از-آمریکا-در-وزن-97kg" data-nt-link> <span class="news-type"></span>شکست قاسم‌پور مقابل اسنایدر از آمریکا در وزن (97Kg)</a>
                            </li>
                            <li data-newsid="321678" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="پیروزی نخودی مقابل ویک از آمریکا در وزن (79Kg)" href="https://video.varzesh3.com/video/321678/پیروزی-نخودی-مقابل-ویک-از-آمریکا-در-وزن-79kg" data-nt-link> <span class="news-type"></span>پیروزی نخودی مقابل ویک از آمریکا در وزن (79Kg)</a>
                            </li>
                            <li data-newsid="321677" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="پیروزی معصومی مقابل میسون از آمریکا  (125Kg)" href="https://video.varzesh3.com/video/321677/پیروزی-معصومی-مقابل-میسون-از-آمریکا-125kg" data-nt-link> <span class="news-type"></span>پیروزی معصومی مقابل میسون از آمریکا  (125Kg)</a>
                            </li>
                            <li data-newsid="321676" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="شکست شیخ اعظمی مقابل کنتچادزه گرجستانی (79Kg)" href="https://video.varzesh3.com/video/321676/شکست-شیخ-اعظمی-مقابل-کنتچادزه-گرجستانی-79kg" data-nt-link> <span class="news-type"></span>شکست شیخ اعظمی مقابل کنتچادزه گرجستانی (79Kg)</a>
                            </li>
                            <li data-newsid="1993650" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="16">
                                <a title="كامران باز هم حريف كايل اسنايدر نشد" href="https://www.varzesh3.com/news/1993650/كامران-بازهم-حريف-كايل-اسنايدر-نشد" data-nt-link> <span class="news-type"></span>كامران باز هم حريف كايل اسنايدر نشد</a>
                            </li>
                </ul>
            </div>
        </div>
    </div>
</div>
                </div>
            </div>
            


        



            <div class="widget-holder">
                <div id="131" class="widget multi-sport league">
                                
<div class="widget-header">
    <h2>توپ و تور</h2>
</div>
<div class="widget-body">
    <ul class="nav nav-tabs vrz-tab" id="multiSportLeagueTab#131" role="tablist">

                <li role="tab" class="nav-item"> <a href="#Volleyball-tab-content" id="Volleyball-tab" data-toggle="tab" aria-controls="Volleyball" class="nav-link active">والیبال</a></li>
                <li role="tab" class="nav-item"> <a href="#Basketball-tab-content" id="Basketball-tab" data-toggle="tab" aria-controls="Basketball" class="nav-link">بسکتبال</a></li>
                <li role="tab" class="nav-item"> <a href="#Handball-tab-content" id="Handball-tab" data-toggle="tab" aria-controls="Handball" class="nav-link">هندبال</a></li>
    </ul>
    <div class="tab-content" id="multiSportLeagueTabContentb#131">
            <div id="Volleyball-tab-content" role="tabpanel" aria-labelledby="Volleyball-tab" class="tab-pane fade volleyball active show">
                        <div class="widget-header">
    <h2></h2>
    <div class="select-options">
        <select id="stage-131">
                    <option value="902075" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/volleyball/widgets/131/league/902075">
                        لیگ برتر والیبال
                    </option>
        </select>
        <select id="round-131">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15">هفته 15</option>
                    <option value="16" selected="selected">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21">هفته 21</option>
                    <option value="22">هفته 22</option>
                    <option value="23">هفته 23</option>
                    <option value="24">هفته 24</option>
                    <option value="25">هفته 25</option>
                    <option value="26">هفته 26</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="widget-volleyball">
        <div class="widget-subtitle" style="background-color:#47a0c2"><h3>لیگ برتر والیبال</h3></div>
        <div class="table-holder setnum-box ">
            <div class="setnum">
            
                    <div>
                        <div></div>
                        <div>
                            <div></div>
                            <div>1st</div>
                            <div>2nd</div>
                            <div>3rd</div>
                            <div>4th</div>
                            <div>5th</div>
                            <div></div>
                        </div>
                        <div></div>
                    </div>
              
            </div>
        </div>
    </div>
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
            <div class="widget-volleyball">
                        <div class="date-seprator"><h4>چهارشنبه 27 دی</h4></div>
                        <div class="table-holder ">
                            <div class="game-table">
                              
                                        <div class="even">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105388/بازی-ایفاسرام-اردکان-هورسان-رامسر"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105388/بازی-ایفاسرام-اردکان-هورسان-رامسر">
                                                    <div>ایفاسرام اردکان<br />هورسان رامسر</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="odd">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105389/بازی-نیان-الکترونیک-طبیعت"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105389/بازی-نیان-الکترونیک-طبیعت">
                                                    <div>نیان الکترونیک<br />طبیعت</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="even">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105390/بازی-شهرداری-ارومیه-شهرداری-گنبد"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105390/بازی-شهرداری-ارومیه-شهرداری-گنبد">
                                                    <div>شهرداری ارومیه<br />شهرداری گنبد</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="odd">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105391/بازی-شهداب-یزد-مس-رفسنجان"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105391/بازی-شهداب-یزد-مس-رفسنجان">
                                                    <div>شهداب یزد<br />مس رفسنجان</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="even">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105392/بازی-فولاد-سیرجان-چادرملو-اردکان"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105392/بازی-فولاد-سیرجان-چادرملو-اردکان">
                                                    <div>فولاد سیرجان<br />چادرملو اردکان</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="odd">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105393/بازی-پیکان-تهران-پاس-گرگان"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105393/بازی-پیکان-تهران-پاس-گرگان">
                                                    <div>پیکان تهران<br />پاس گرگان</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                                        <div class="even">
                                     
                                            <div>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/105394/بازی-سایپا-گیتی-پسند"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                                </div>
                                            </div>
                                            <div>
                                                <a class="match-link" href="/volleyball/match/105394/بازی-سایپا-گیتی-پسند">
                                                    <div>سایپا<br />گیتی پسند</div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div><br /></div>
                                                    <div class="result"><br /></div>
                                                </a>
                                            </div>
                                            <div>
                                                
                                                <span>16:00</span>
                                                <span class="match-status"></span>
                                            </div>
                                          
                                        </div>
                            </div>
                        </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#47a0c2"><h3>جدول لیگ برتر والیبال</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول لیگ برتر والیبال</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">برد</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row">فولاد سیرجان</td>
                                <td>15</td>
                                <td>13</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row">شهداب یزد</td>
                                <td>15</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row">ایفاسرام اردکان</td>
                                <td>15</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row">پاس گرگان</td>
                                <td>15</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row">هورسان رامسر</td>
                                <td>15</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row">گیتی پسند</td>
                                <td>15</td>
                                <td>8</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row">پیکان تهران</td>
                                <td>15</td>
                                <td>8</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row">چادرملو اردکان</td>
                                <td>15</td>
                                <td>8</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row">طبیعت</td>
                                <td>15</td>
                                <td>8</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row">مس رفسنجان</td>
                                <td>15</td>
                                <td>7</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row">نیان الکترونیک</td>
                                <td>15</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row">شهرداری ارومیه</td>
                                <td>15</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>13</td>
                                <td scope="row">شهرداری گنبد</td>
                                <td>15</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>14</td>
                                <td scope="row">سایپا</td>
                                <td>15</td>
                                <td>1</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"><a href="/volleyball/league/33/لیگ-برتر-والیبال">جدول کامل لیگ برتر والیبال</a></div>
            </div>
            <div id="Basketball-tab-content" role="tabpanel" aria-labelledby="Basketball-tab" class="tab-pane fade basketball">
                        

<div class="widget-header">
    <h2></h2>
    <div class="select-options">
        <select id="stage-131">
                    <option value="902059" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/basketball/widgets/131/league/902059">لیگ برتر بسکتبال</option>
        </select>
        <select id="round-131">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15" selected="selected">هفته 15</option>
                    <option value="16">هفته 16</option>
        </select>
    </div>
</div>

<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
            <div class="widget-subtitle" style="background-color:#47a0c2"><h3>لیگ برتر بسکتبال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>پنج شنبه 28 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107833/بازی-مس-کرمان-ذوب-آهن"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107833/بازی-مس-کرمان-ذوب-آهن" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">مس کرمان</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">ذوب آهن</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107834/بازی-مهرام-لیموندیس-فارس"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107834/بازی-مهرام-لیموندیس-فارس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">مهرام</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">لیموندیس فارس</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107835/بازی-فولاد-هرمزگان-مس-رفسنجان"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107835/بازی-فولاد-هرمزگان-مس-رفسنجان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">فولاد هرمزگان</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">مس رفسنجان</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107836/بازی-پالایش-نفت-آبادان-طبیعت"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107836/بازی-پالایش-نفت-آبادان-طبیعت" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">پالایش نفت آبادان</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">طبیعت</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107837/بازی-کاله-شهرداری-گرگان"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107837/بازی-کاله-شهرداری-گرگان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">کاله</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">شهرداری گرگان</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    
                                    <a href="/basketball/match/107838/بازی-رعد-پدافند-مشهد-آورتا-ساری"><img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                </div>
                                <a href="/basketball/match/107838/بازی-رعد-پدافند-مشهد-آورتا-ساری" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host">رعد پدافند مشهد</div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest">آورتا ساری</div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span>16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#47a0c2"><h3>جدول لیگ برتر بسکتبال</h3></div>
        <div class="table-holder">
            <table class="league-standing widget-standing">
                <caption>جدول لیگ برتر بسکتبال</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتیاز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row">شهرداری گرگان</td>
                                <td>14</td>
                                <td>27</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row">ذوب آهن</td>
                                <td>14</td>
                                <td>26</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row">طبیعت</td>
                                <td>14</td>
                                <td>23</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row">مهرام</td>
                                <td>14</td>
                                <td>23</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row">کاله</td>
                                <td>14</td>
                                <td>22</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row">پالایش نفت آبادان</td>
                                <td>14</td>
                                <td>22</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row">مس کرمان</td>
                                <td>14</td>
                                <td>21</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row">آورتا ساری</td>
                                <td>14</td>
                                <td>21</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row">مس رفسنجان</td>
                                <td>14</td>
                                <td>19</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row">لیموندیس فارس</td>
                                <td>14</td>
                                <td>18</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row">فولاد هرمزگان</td>
                                <td>14</td>
                                <td>15</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row">رعد پدافند مشهد</td>
                                <td>14</td>
                                <td>15</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"><a href="/basketball/league/32/لیگ-برتر-بسکتبال" >جدول کامل لیگ برتر بسکتبال</a></div>
            </div>
            <div id="Handball-tab-content" role="tabpanel" aria-labelledby="Handball-tab" class="tab-pane fade handball">
                        

<div class="widget-header">
    <h2></h2>
    <div class="select-options">
        <select id="stage-131">
                    <option value="1" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/handball/widgets/131/league/1 ">لیگ برتر هندبال </option>
                    <option value="2" data-api="https://web-api.varzesh3.com/v1.0/handball/widgets/131/league/2 ">لیگ برتر هندبال زنان </option>
        </select>
        <select id="round-131">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9" selected="selected">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15">هفته 15</option>
                    <option value="16">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21">هفته 21</option>
                    <option value="22">هفته 22</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#47a0c2"><h3>لیگ برتر هندبال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 20 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/41/بازی-آلومینیوم-اراک-پرواز-هوانیروز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/41/بازی-آلومینیوم-اراک-پرواز-هوانیروز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آلومینیوم اراک</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پرواز هوانیروز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/42/بازی-مس-کرمان-پلیمر-خرم-آباد"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/42/بازی-مس-کرمان-پلیمر-خرم-آباد" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مس کرمان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پلیمر خرم آباد</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/43/بازی-نفت-و-گاز-گچساران-زغال-سنگ-طبس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/43/بازی-نفت-و-گاز-گچساران-زغال-سنگ-طبس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نفت و گاز گچساران</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>زغال سنگ طبس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/45/بازی-شهید-شاملی-کازرون-گیتی-پسند"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/45/بازی-شهید-شاملی-کازرون-گیتی-پسند" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>شهید شاملی کازرون</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>گیتی پسند</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/85/بازی-سپاهان-نوین-پیکان-سبزوار"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/85/بازی-سپاهان-نوین-پیکان-سبزوار" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سپاهان نوین</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پیکان سبزوار</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/handball/match/44/بازی-سپاهان-فراز-بام-دهدشت"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/handball/match/44/بازی-سپاهان-فراز-بام-دهدشت" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سپاهان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>فراز بام دهدشت</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">18:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#47a0c2"><h3>جدول لیگ برتر هندبال</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول لیگ برتر هندبال</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row">مس کرمان</td>
                                <td>7</td>
                                <td>14</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row">گیتی پسند</td>
                                <td>7</td>
                                <td>13</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row">شهید شاملی کازرون</td>
                                <td>7</td>
                                <td>12</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row">پلیمر خرم آباد</td>
                                <td>7</td>
                                <td>10</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row">زغال سنگ طبس</td>
                                <td>7</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row">سپاهان</td>
                                <td>7</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row">نفت و گاز گچساران</td>
                                <td>7</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row">پیکان سبزوار</td>
                                <td>7</td>
                                <td>5</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row">پرواز هوانیروز</td>
                                <td>7</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row">آلومینیوم اراک</td>
                                <td>7</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row">سپاهان نوین</td>
                                <td>7</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row">فراز بام دهدشت</td>
                                <td>7</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/handball/league/4/لیگ-برتر-هندبال" >جدول کامل لیگ برتر هندبال</a></div>
            </div>
    </div>

</div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="343">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-4200"></div>
                </div>
    </div>




            <div class="widget-holder">
                <div id="67" class="widget broadcast">
                                


<div class="widget-header">
    <h2>جدول پخش زنده مسابقات ورزشی</h2>
</div>
<div class="widget-body">
    <div class="conductor-filter">
        <div class="conductor-filter-item anten">
            <input id="anten-coductor" type="checkbox" data-type="1" checked="checked">
            <label for="anten-coductor">آنتن</label>
        </div>
        <div class="conductor-filter-item">
            <input id="tv-coductor" type="checkbox" data-type="2" checked="">
            <label for="tv-coductor">شبکه‌های تلویزیونی</label>
        </div>
    </div>
    <div class="conductor-alert-message">حداقل یکی از گزینه ها باید فعال باشد.</div>
    <div class="conductor-main-list scrollable-box" data-desktop-max="5" data-mobile-max="5" data-height="500" style="max-height: 500px">
        <div class="scroll-list-content">
                    <div class="conductor-day">
                        <div class="date-seprator"><h3>دوشنبه 25 دی</h3></div>
                            <div data-type="3" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">15:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">کره جنوبی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> بحرین</div>
                                        <div class="broadcast-info">جام ملت های آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه سه</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60969/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%DA%A9%D8%B1%D9%87-%D8%AC%D9%86%D9%88%D8%A8%DB%8C-%D8%A8%D8%AD%D8%B1%DB%8C%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">15:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">قزاقستان</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> هنگ کنگ</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/60980/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%D9%82%D8%B2%D8%A7%D9%82%D8%B3%D8%AA%D8%A7%D9%86-%D9%87%D9%86%DA%AF-%DA%A9%D9%86%DA%AF?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">17:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">سنگال</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> گامبیا</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60972/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%B3%D9%86%DA%AF%D8%A7%D9%84-%DA%AF%D8%A7%D9%85%D8%A8%DB%8C%D8%A7?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">17:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">عراق</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> عربستان</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/60981/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%D8%B9%D8%B1%D8%A7%D9%82-%D8%B9%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="3" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">18:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">اندونزی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> عراق</div>
                                        <div class="broadcast-info">جام ملت های آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه ورزش</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60970/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A7%D9%86%D8%AF%D9%88%D9%86%D8%B2%DB%8C-%D8%B9%D8%B1%D8%A7%D9%82?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">19:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">بحرین</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> امارات</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/60982/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%D8%A8%D8%AD%D8%B1%DB%8C%D9%86-%D8%A7%D9%85%D8%A7%D8%B1%D8%A7%D8%AA?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">20:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">کامرون</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> گینه</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60973/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%DA%A9%D8%A7%D9%85%D8%B1%D9%88%D9%86-%DA%AF%DB%8C%D9%86%D9%87?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="3" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">21:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">مالزی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> اردن</div>
                                        <div class="broadcast-info">جام ملت های آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه ورزش</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60971/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%A7%D9%84%D8%B2%DB%8C-%D8%A7%D8%B1%D8%AF%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">21:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">فیلادلفیا</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> هیوستون راکتس</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/60976/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%81%DB%8C%D9%84%D8%A7%D8%AF%D9%84%D9%81%DB%8C%D8%A7-%D8%B3%D9%88%D9%86%D8%AA%DB%8C-%D8%B3%DB%8C%DA%A9%D8%B3%D8%B1%D8%B2-%D9%87%DB%8C%D9%88%D8%B3%D8%AA%D9%88%D9%86-%D8%B1%D8%A7%DA%A9%D8%AA%D8%B3?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">دالاس ماوریکس</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> نیو اورلینز پلیکانز</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/60977/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D8%AF%D8%A7%D9%84%D8%A7%D8%B3-%D9%85%D8%A7%D9%88%D8%B1%DB%8C%DA%A9%D8%B3-%D9%86%DB%8C%D9%88-%D8%A7%D9%88%D8%B1%D9%84%DB%8C%D9%86%D8%B2-%D9%BE%D9%84%DB%8C%DA%A9%D8%A7%D9%86%D8%B2?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:15</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">آتالانتا</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> فروزینونه</div>
                                        <div class="broadcast-info">سری آ ایتالیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60968/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A2%D8%AA%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D8%A7-%D9%81%D8%B1%D9%88%D8%B2%DB%8C%D9%86%D9%88%D9%86%D9%87?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">الجزایر</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> آنگولا</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/60974/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%DB%8C%D8%B1-%D8%A2%D9%86%DA%AF%D9%88%D9%84%D8%A7?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">نیویورک نیکس</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> اورلاندو مجیک</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/60978/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%86%DB%8C%D9%88%DB%8C%D9%88%D8%B1%DA%A9-%D9%86%DB%8C%DA%A9%D8%B3-%D8%A7%D9%88%D8%B1%D9%84%D8%A7%D9%86%D8%AF%D9%88-%D9%85%D8%AC%DB%8C%DA%A9?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div class="conductor-day">
                        <div class="date-seprator"><h3>سه شنبه 26 دی</h3></div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">00:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">آتلانتا هاکس</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> سن آنتونیو اسپرز</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/61093/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D8%A2%D8%AA%D9%84%D8%A7%D9%86%D8%AA%D8%A7-%D9%87%D8%A7%DA%A9%D8%B3-%D8%B3%D9%86-%D8%A2%D9%86%D8%AA%D9%88%D9%86%DB%8C%D9%88-%D8%A7%D8%B3%D9%BE%D8%B1%D8%B2?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">02:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">ممفیس گریزلیز</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> گلدن استیت واریرز</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/61094/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D9%85%D9%81%DB%8C%D8%B3-%DA%AF%D8%B1%DB%8C%D8%B2%D9%84%DB%8C%D8%B2-%DA%AF%D9%84%D8%AF%D9%86-%D8%A7%D8%B3%D8%AA%DB%8C%D8%AA-%D9%88%D8%A7%D8%B1%DB%8C%D8%B1%D8%B2?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">07:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">لس آنجلس لیکرز</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> اوکلاهاما سیتی تاندر</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/61095/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%84%D8%B3-%D8%A2%D9%86%D8%AC%D9%84%D8%B3-%D9%84%DB%8C%DA%A9%D8%B1%D8%B2-%D8%A7%D9%88%DA%A9%D9%84%D8%A7%D9%87%D8%A7%D9%85%D8%A7-%D8%B3%DB%8C%D8%AA%DB%8C-%D8%AA%D8%A7%D9%86%D8%AF%D8%B1?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="3" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">13:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">نیوزیلند</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> چین</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه ورزش</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/61021/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%D9%86%DB%8C%D9%88%D8%B2%DB%8C%D9%84%D9%86%D8%AF-%DA%86%DB%8C%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">15:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">چین تایپه</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> عمان</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/61022/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%DA%86%DB%8C%D9%86-%D8%AA%D8%A7%DB%8C%D9%BE%D9%87-%D8%B9%D9%85%D8%A7%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">17:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">بورکینافاسو</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> موریتانی</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61013/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A8%D9%88%D8%B1%DA%A9%DB%8C%D9%86%D8%A7%D9%81%D8%A7%D8%B3%D9%88-%D9%85%D9%88%D8%B1%DB%8C%D8%AA%D8%A7%D9%86%DB%8C?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">17:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">کویت</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> قطر</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/61023/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%DA%A9%D9%88%DB%8C%D8%AA-%D9%82%D8%B7%D8%B1?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">18:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">تایلند</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> قرقیزستان</div>
                                        <div class="broadcast-info">جام ملت های آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61009/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%AA%D8%A7%DB%8C%D9%84%D9%86%D8%AF-%D9%82%D8%B1%D9%82%DB%8C%D8%B2%D8%B3%D8%AA%D8%A7%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="3" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">19:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">کره جنوبی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> ایران</div>
                                        <div class="broadcast-info">هندبال قهرمانی آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه ورزش</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/handball/61024/%D9%87%D9%86%D8%AF%D8%A8%D8%A7%D9%84-%DA%A9%D8%B1%D9%87-%D8%AC%D9%86%D9%88%D8%A8%DB%8C-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">20:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">تونس</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> نامیبیا</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61014/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%AA%D9%88%D9%86%D8%B3-%D9%86%D8%A7%D9%85%DB%8C%D8%A8%DB%8C%D8%A7?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="3" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">21:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">عربستان</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> عمان</div>
                                        <div class="broadcast-info">جام ملت های آسیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        <span> شبکه سه</span>
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61010/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%B9%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86-%D8%B9%D9%85%D8%A7%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">22:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">ختافه</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> سویا</div>
                                        <div class="broadcast-info">جام حذفی اسپانیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61011/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%AE%D8%AA%D8%A7%D9%81%D9%87-%D8%B3%D9%88%DB%8C%D8%A7?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">ولورهمپتون</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> برنتفورد</div>
                                        <div class="broadcast-info">جام حذفی انگلیس</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61008/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D9%88%D9%84%D9%88%D8%B1%D9%87%D9%85%D9%BE%D8%AA%D9%88%D9%86-%D8%A8%D8%B1%D9%86%D8%AA%D9%81%D9%88%D8%B1%D8%AF?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:15</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">یوونتوس</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> ساسولو</div>
                                        <div class="broadcast-info">سری آ ایتالیا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61004/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%DB%8C%D9%88%D9%88%D9%86%D8%AA%D9%88%D8%B3-%D8%B3%D8%A7%D8%B3%D9%88%D9%84%D9%88?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:15</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">بیرمنگام</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> هال سیتی</div>
                                        <div class="broadcast-info">جام حذفی انگلیس</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61005/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A8%DB%8C%D8%B1%D9%85%D9%86%DA%AF%D8%A7%D9%85-%D9%87%D8%A7%D9%84-%D8%B3%DB%8C%D8%AA%DB%8C?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:15</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">بولتون</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> لوتون</div>
                                        <div class="broadcast-info">جام حذفی انگلیس</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61006/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A8%D9%88%D9%84%D8%AA%D9%88%D9%86-%D9%84%D9%88%D8%AA%D9%88%D9%86-%D8%AA%D8%A7%D9%88%D9%86?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:15</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">بریستول سیتی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> وستهم</div>
                                        <div class="broadcast-info">جام حذفی انگلیس</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61007/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D8%A8%D8%B1%DB%8C%D8%B3%D8%AA%D9%88%D9%84-%D8%B3%DB%8C%D8%AA%DB%8C-%D9%88%D8%B3%D8%AA%D9%87%D9%85?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">23:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">مالی</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> آفریقای جنوبی</div>
                                        <div class="broadcast-info">جام ملت های آفریقا</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/football/61015/%D9%81%D9%88%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%A7%D9%84%DB%8C-%D8%A2%D9%81%D8%B1%DB%8C%D9%82%D8%A7%DB%8C-%D8%AC%D9%86%D9%88%D8%A8%DB%8C?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div class="conductor-day">
                        <div class="date-seprator"><h3>چهارشنبه 27 دی</h3></div>
                            <div data-type="1" class="broadcast-match even">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">04:00</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">فیلادلفیا</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> دنور ناگتس</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/61096/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%81%DB%8C%D9%84%D8%A7%D8%AF%D9%84%D9%81%DB%8C%D8%A7-%D8%B3%D9%88%D9%86%D8%AA%DB%8C-%D8%B3%DB%8C%DA%A9%D8%B3%D8%B1%D8%B2-%D8%AF%D9%86%D9%88%D8%B1-%D9%86%D8%A7%DA%AF%D8%AA%D8%B3?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                            <div data-type="1" class="broadcast-match odd">
                                <div class="broadcast-match-bottom-row">
                                    <div class="broadcast-match-time">06:30</div>
                                    
                                    <div class="broadcast-match-teams">
                                        <div class="broadcast-match-host">لس آنجلس کلیپرز</div>
                                        <div class="broadcast-match-sep"><span> - </span></div>
                                        <div class="broadcast-match-guest"> اوکلاهاما سیتی تاندر</div>
                                        <div class="broadcast-info">بسکتبال حرفه‌ای NBA</div>
                                    </div>
                                    <div class="broadcast-tvs">
                                        
                                        <span><a class="anten-text" target="_blank" href="https://www.anten.ir/basketball/61097/%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%84%D8%B3-%D8%A2%D9%86%D8%AC%D9%84%D8%B3-%DA%A9%D9%84%DB%8C%D9%BE%D8%B1%D8%B2-%D8%A7%D9%88%DA%A9%D9%84%D8%A7%D9%87%D8%A7%D9%85%D8%A7-%D8%B3%DB%8C%D8%AA%DB%8C-%D8%AA%D8%A7%D9%86%D8%AF%D8%B1?utm_source=varzesh3&utm_medium=home_Live_schedule&utm_campaign=always"> آنتن</a></span>
                                    </div>
                                </div>
                            </div>
                    </div>
        </div>
    </div>
    
</div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="2641">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2641" rel="nofollow"
                    style="background-color: #f5f5f5;height:133px">
                        <img class="adimage" id="img-2641" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/12/24/929fde33-e7c8-43a6-b0ac-e143fa38bf2d.gif" 
                                                        width="300" 
                                                        height="133" alt="اوانو" />
                </a>
    </div>






                    </div>
                </div>
                <div class="v50-l-col widgets-parent-col">
                    <div class="forfix">
                        

            


        
        
        <div class="adbox" data-id="2181">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2181" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-2181" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/14/bc0eeeb2-cb7d-426b-8ed9-2880cd03a0af.gif" 
                                                        width="300" 
                                                        height="160" alt="بنر جا باما " />
                </a>
    </div>

        
        <div class="adbox" data-id="3431">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3431" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-3431" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/11/fb947a7e-db8f-44f3-aa05-f0d3633a1515.gif" 
                                                        width="300" 
                                                        height="160" alt="رونیکس" />
                </a>
    </div>




            
            <div class="widget-holder">
                <div id="68" class="widget video">
                                

<div class="widget-header"><h2>ویدیو</h2></div>
<div class="widget-body">
    <ul class="nav nav-tabs vrz-tab" id="videoTab" role="tablist">
        
        <li role="tab" class="nav-item"><a id="new-tab" data-toggle="tab" href="#new" aria-controls="new" class="nav-link active">جدیدترین</a></li>
        <li role="tab" class="nav-item"><a class="nav-link" id="featured-tab" data-toggle="tab" href="#featured" aria-controls="featured">ویژه</a></li>
        <li role="tab" class="nav-item"><a class="nav-link" id="live-tab" data-toggle="tab" href="#live" aria-controls="live"><img alt="پخش زنده" width="10" height="10" src="https://static.varzesh3.com/img/icons/live-video-widget.svg?w=10" />پخش زنده</a></li>
    </ul>
    <div class="tab-content" id="videoTabContent">

        
        <div id="new" role="tabpanel" aria-labelledby="new-tab" class="tab-pane fade show active">
            <div class="video-new-holder">
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322038/خلاصه-بسکتبال-پورتلند-تریل-بلیزرز-فنیکس-سانز">
    <div class="video-cover-image">
            <img alt="خلاصه بسکتبال پورتلند تریل بلیزرز - فنیکس سانز" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/B/exvg2yeo.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">09:14</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 18 دقیقه پیش - </span>
    <span class="view">33 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322038/خلاصه-بسکتبال-پورتلند-تریل-بلیزرز-فنیکس-سانز">
    <h3>خلاصه بسکتبال پورتلند تریل بلیزرز - فنیکس سانز</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322048/برانکو-از-ایران-ژاپن-و-کره-انتظار-بیشتری-برای-قهرمانی-هست">
    <div class="video-cover-image">
            <img alt="برانکو: از ایران، ژاپن و کره انتظار بیشتری برای قهرمانی هست" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/jkfevw52.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:55</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 50 دقیقه پیش - </span>
    <span class="view">831 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322048/برانکو-از-ایران-ژاپن-و-کره-انتظار-بیشتری-برای-قهرمانی-هست">
    <h3>برانکو: از ایران، ژاپن و کره انتظار بیشتری برای قهرمانی هست</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322047/آخرین-وضعیت-مصدومان-از-زبان-پزشک-تیم-ملی-ایران">
    <div class="video-cover-image">
            <img alt="آخرین وضعیت مصدومان از زبان پزشک تیم ملی ایران" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/wli045ux.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:50</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 1 ساعت پیش - </span>
    <span class="view">2.1K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322047/آخرین-وضعیت-مصدومان-از-زبان-پزشک-تیم-ملی-ایران">
    <h3>آخرین وضعیت مصدومان از زبان پزشک تیم ملی ایران</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322046/پاسخ-برانکو-به-سؤال-جنجالی-عزیزم">
    <div class="video-cover-image">
            <img alt="پاسخ برانکو به سؤال جنجالی: عزیزم!" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/isc3y1o5.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">01:25</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 1 ساعت پیش - </span>
    <span class="view">5.8K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322046/پاسخ-برانکو-به-سؤال-جنجالی-عزیزم">
    <h3>پاسخ برانکو به سؤال جنجالی: عزیزم!</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322045/رونمایی-از-دومین-دوره-مسابقات-جام-پرچم-توسط-دکتر-کلهر">
    <div class="video-cover-image">
            <img alt="رونمایی از دومین دوره مسابقات جام پرچم توسط دکتر کلهر" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/nsas3ngo.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">08:07</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 2 ساعت پیش - </span>
    <span class="view">279 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322045/رونمایی-از-دومین-دوره-مسابقات-جام-پرچم-توسط-دکتر-کلهر">
    <h3>رونمایی از دومین دوره مسابقات جام پرچم توسط دکتر کلهر</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322044/شجاع-قهرمان-شویم-ریش-روزبه-را-می-زنم">
    <div class="video-cover-image">
            <img alt="شجاع: قهرمان شویم، ریش روزبه را می‌زنم" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/0p1rsuby.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:53</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 2 ساعت پیش - </span>
    <span class="view">12.3K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322044/شجاع-قهرمان-شویم-ریش-روزبه-را-می-زنم">
    <h3>شجاع: قهرمان شویم، ریش روزبه را می‌زنم</h3>
</a>
</div>
                        <div class="videobox"> 

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322043/پیام-سم-کر-اسطوره-فوتبال-زنان-برای-درگذشت-ملیکا">
    <div class="video-cover-image">
            <img alt="پیام سم کر اسطوره فوتبال زنان برای درگذشت ملیکا" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/C/132g4k23.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:14</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 2 ساعت پیش - </span>
    <span class="view">15.1K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322043/پیام-سم-کر-اسطوره-فوتبال-زنان-برای-درگذشت-ملیکا">
    <h3>پیام سم کر اسطوره فوتبال زنان برای درگذشت ملیکا</h3>
</a>
</div>
            </div>
        </div>
        <div class="tab-pane fade show" id="featured" role="tabpanel" aria-labelledby="featured-tab">
            <div class="video-new-holder">
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322031/خلاصه-بازی-کالیاری-2-بولونیا-1">
    <div class="video-cover-image">
            <img alt="خلاصه بازی کالیاری 2 - بولونیا 1" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/B/givkcwfe.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">01:56</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 5 ساعت پیش - </span>
    <span class="view">781 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322031/خلاصه-بازی-کالیاری-2-بولونیا-1">
    <h3>خلاصه بازی کالیاری 2 - بولونیا 1</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322027/خلاصه-بازی-آلمریا-0-خیرونا-0">
    <div class="video-cover-image">
            <img alt="خلاصه بازی آلمریا 0 - خیرونا 0" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/A/abzyfdpg.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">02:43</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 7 ساعت پیش - </span>
    <span class="view">1.1K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322027/خلاصه-بازی-آلمریا-0-خیرونا-0">
    <h3>خلاصه بازی آلمریا 0 - خیرونا 0</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322028/تیتر-از-شکایت-پرسپولیس-از-afc-تا-پیروزی-پر-گل-تیم-ملی">
    <div class="video-cover-image">
            <img alt="از شکایت پرسپولیس از afc تا پیروزی پر گل تیم ملی" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/B/voq0cmz5.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">01:02</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 7 ساعت پیش - </span>
    <span class="view">15.5K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322028/تیتر-از-شکایت-پرسپولیس-از-afc-تا-پیروزی-پر-گل-تیم-ملی">
    <h3>از شکایت پرسپولیس از afc تا پیروزی پر گل تیم ملی</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322024/خلاصه-بازی-غنا-1-کیپ-ورد-2">
    <div class="video-cover-image">
            <img alt="خلاصه بازی غنا 1 - کیپ ورد 2" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/A/vlepkeea.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">06:52</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 13 ساعت پیش - </span>
    <span class="view">5.5K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322024/خلاصه-بازی-غنا-1-کیپ-ورد-2">
    <h3>خلاصه بازی غنا 1 - کیپ ورد 2</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322023/خلاصه-بازی-آث-میلان-3-آاس-رم-1">
    <div class="video-cover-image">
            <img alt="خلاصه بازی آث میلان 3 - آاس رم 1" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/15/A/kjwwwyao.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">08:45</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 14 ساعت پیش - </span>
    <span class="view">35K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322023/خلاصه-بازی-آث-میلان-3-آاس-رم-1">
    <h3>خلاصه بازی آث میلان 3 - آاس رم 1</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/322014/خلاصه-بازی-رئال-مادرید-4-بارسلونا-1">
    <div class="video-cover-image">
            <img alt="خلاصه بازی رئال مادرید 4 - بارسلونا 1" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/14/A/sltx1lsz.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">09:37</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 15 ساعت پیش - </span>
    <span class="view">331.3K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/322014/خلاصه-بازی-رئال-مادرید-4-بارسلونا-1">
    <h3>خلاصه بازی رئال مادرید 4 - بارسلونا 1</h3>
</a>
</div>
                        <div class="videobox">

<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/321996/خلاصه-بازی-ایران-4-فلسطین-1">
    <div class="video-cover-image">
            <img alt="خلاصه بازی ایران 4 - فلسطین 1" width="300" height="155" src="https://video-icdn.varzesh3.com/covers/2024/01/14/D/r50njty5.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">06:14</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 16 ساعت پیش - </span>
    <span class="view">379.2K بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/321996/خلاصه-بازی-ایران-4-فلسطین-1">
    <h3>خلاصه بازی ایران 4 - فلسطین 1</h3>
</a>
</div>
            </div>
        </div>
        <div class="tab-pane fade show" id="live" role="tabpanel" aria-labelledby="live-tab">
            <div class="video-new-holder">
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/football/60969/فوتبال-کره-جنوبی-بحرین/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="فوتبال کره جنوبی - بحرین" width="300" height="155" src="https://r1-edge-v2.s3mer.net/hls/stream/thumbs/stream851.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش زنده" width="18" height="18" src="https://static.varzesh3.com/img/icons/live-video-widget.svg?w=18" />
        </span>

        <span class="duration">زنده</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 14:51</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/football/60969/فوتبال-کره-جنوبی-بحرین/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>فوتبال کره جنوبی - بحرین</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/tennis/61127/تنیس-فلیکس-اوژه-آلیاسیم-دومینیک-تیم/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="تنیس فلیکس اوژه آلیاسیم - دومینیک تیم" width="300" height="155" src="https://r1-edge-v2.s3mer.net/hls/stream/thumbs/stream853.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش زنده" width="18" height="18" src="https://static.varzesh3.com/img/icons/live-video-widget.svg?w=18" />
        </span>

        <span class="duration">زنده</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 13:05</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/tennis/61127/تنیس-فلیکس-اوژه-آلیاسیم-دومینیک-تیم/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>تنیس فلیکس اوژه آلیاسیم - دومینیک تیم</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/futsal/61130/مسابقات-فوتسال-کارگری-کشور/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="مسابقات فوتسال کارگری کشور" width="300" height="155" src="https://static.r1-edge-v2.s3mer.net/images/e0612fa6-16f1-4cda-a743-4f2bf38137a1/e0612fa6-16f1-4cda-a743-4f2bf38137a1.jpeg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش زنده" width="18" height="18" src="https://static.varzesh3.com/img/icons/live-video-widget.svg?w=18" />
        </span>

        <span class="duration">زنده</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 15:15</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/futsal/61130/مسابقات-فوتسال-کارگری-کشور/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>مسابقات فوتسال کارگری کشور</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/handball/60980/هندبال-قزاقستان-هنگ-کنگ/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="هندبال قزاقستان - هنگ کنگ" width="300" height="155" src="https://r1-edge-v2.s3mer.net/hls/stream/thumbs/stream855.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش زنده" width="18" height="18" src="https://static.varzesh3.com/img/icons/live-video-widget.svg?w=18" />
        </span>

        <span class="duration">زنده</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 15:30</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/handball/60980/هندبال-قزاقستان-هنگ-کنگ/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>هندبال قزاقستان - هنگ کنگ</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/football/60972/فوتبال-سنگال-گامبیا/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="فوتبال سنگال - گامبیا" width="300" height="155" src="https://static.r1-edge-v2.s3mer.net/images/2023/6/14/C/6376d74c-71cc-4142-b10d-8d6b48f26aea.jpg?w=300" />
    </div>
    
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 17:30</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/football/60972/فوتبال-سنگال-گامبیا/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>فوتبال سنگال - گامبیا</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/handball/60981/هندبال-عراق-عربستان/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="هندبال عراق - عربستان" width="300" height="155" src="https://static.r1-edge-v2.s3mer.net/images/2023/11/2/B/40210c81-d142-44cb-9539-a73450849abd.jpg?w=300" />
    </div>
    
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 17:30</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/handball/60981/هندبال-عراق-عربستان/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>هندبال عراق - عربستان</h3>
</a>
</div>
                        <div class="videobox">
<a class="video-cover-box is-anten" target="_blank" href="https://www.anten.ir/football/60970/فوتبال-اندونزی-عراق/?utm_source=varzesh3&amp;utm_medium=live-row">
    <div class="video-cover-image">
        <img alt="فوتبال اندونزی - عراق" width="300" height="155" src="https://static.r1-edge-v2.s3mer.net/images/2023/10/30/B/66c0f7f0-044c-446b-8d95-ecc9e6b185cb.jpg?w=300" />
    </div>
    
</a>
<div class="video-data">
    <span class="date"> 25 دی 1402 ساعت 18:00</span>
</div>
<a class="title" target="_blank" href="https://www.anten.ir/football/60970/فوتبال-اندونزی-عراق/?utm_source=varzesh3&amp;utm_medium=live-row">
    <h3>فوتبال اندونزی - عراق</h3>
</a>
</div>
            </div>
        </div>

    </div>
</div>
<div class="widget-footer">
    <a href="https://video.varzesh3.com/" target="_blank">مشاهده ویدیوها</a>
</div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="2294">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2294" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-2294" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/01/e1ade8c2-6aab-40e2-a698-f777df0e05ef.gif" 
                                                        width="300" 
                                                        height="160" alt="لست سکند " />
                </a>
    </div>




            <div class="widget-holder">
                <div id="69" class="widget newspaper">
                                
<div class="widget-header">
    <h2>گیشه روزنامه ورزشی</h2>
</div>
<div class="widget-body">
    <div class="newspaper-carousel-holder">
        <div class="newspaper-carousel owl-carousel">
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/8/1402-10-25/%D8%AE%D8%A8%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <div class="newspaper-image-holder">
                                    <img alt="خبر ورزشی دوشنبه 25 دی" width="450" src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/A/dehjop3g.jpg?w=450" />
                                </div>

                            <p>خبر ورزشی دوشنبه 25 دی</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/11/1402-10-25/%DA%AF%D9%84">
                                <div class="newspaper-image-holder">
                                    <img alt="گل  دوشنبه 25 دی" width="450" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/A/gtr50d2i.jpg?w=450" class="owl-lazy lazy" />
                                </div>

                            <p>گل  دوشنبه 25 دی</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/1/1402-10-25/%D8%A7%D8%A8%D8%B1%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <div class="newspaper-image-holder">
                                    <img alt="ابرار ورزشی دوشنبه 25 دی" width="450" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/A/qj1kv0kb.jpg?w=450" class="owl-lazy lazy" />
                                </div>

                            <p>ابرار ورزشی دوشنبه 25 دی</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/4/1402-10-25/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <div class="newspaper-image-holder">
                                    <img alt="ایران ورزشی دوشنبه 25 دی" width="450" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/A/prkqmsur.jpg?w=450" class="owl-lazy lazy" />
                                </div>

                            <p>ایران ورزشی دوشنبه 25 دی</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/2/1402-10-25/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84">
                                <div class="newspaper-image-holder">
                                    <img alt="استقلال دوشنبه 25 دی" width="450" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/B/tbr53iqw.jpg?w=450" class="owl-lazy lazy" />
                                </div>

                            <p>استقلال دوشنبه 25 دی</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/24/1402-10-25/%D9%81%D8%B1%D9%87%DB%8C%D8%AE%D8%AA%DA%AF%D8%A7%D9%86-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <div class="newspaper-image-holder">
                                    <img alt="فرهیختگان ورزشی دوشنبه 25 دی" width="450" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaperw-cdn.varzesh3.com/newspapers/2024/01/15/A/jkgjmaeo.jpg?w=450" class="owl-lazy lazy" />
                                </div>

                            <p>فرهیختگان ورزشی دوشنبه 25 دی</p>
                        </a>
                    </div>
        </div>
    </div>
</div>
<div class="widget-footer"><a href="/newspaper">مشاهده روزنامه ها</a></div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="3406">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3406" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-3406" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/11/ee087a54-88fb-44a5-8233-5fcd0bf437e5.gif" 
                                                        width="300" 
                                                        height="160" alt="بیت" />
                </a>
    </div>




            <div class="widget-holder">
                <div id="115" class="widget top-players">
                                
<div class="widget-header">
    <h2>بازیکنان برتر</h2>
    <div class="select-options">
        <select id="league">
                    <option value="900709" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900709" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900709" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900709" selected="selected">لیگ برتر ایران</option>
                    <option value="900734" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900734" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900734" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900734">لیگ قهرمانان آسیا</option>
                    <option value="900728" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900728" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900728" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900728">لیگ قهرمانان اروپا</option>
                    <option value="900704" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900704" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900704" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900704">لیگ برتر انگلیس</option>
                    <option value="900707" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900707" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900707" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900707">لالیگا اسپانیا</option>
                    <option value="900710" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900710" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900710" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900710">بوندسلیگا آلمان</option>
                    <option value="900706" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900706" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900706" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900706">سری آ ایتالیا</option>
                    <option value="900708" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900708" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900708" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900708">لیگ یک فرانسه</option>
                    <option value="900711" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900711" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900711" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900711">لیگ برتر پرتغال</option>
                    <option value="900714" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900714" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900714" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900714">اردیویسه هلند</option>
                    <option value="900720" data-score-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-scorers/900720" data-assist-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-assisters/900720" data-clean-sheet-api="https://web-api.varzesh3.com/v1.0/football/widgets/115/top-goalkeepers/900720">لیگ حرفه‌ای عربستان</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="top-player-tabs">
        <ul>
            <li data-type="score" class="active">
                گلزنان
            </li>
            <li data-type="assist">
                پاسورها
            </li>
            <li data-type="clean-sheet">
                کلین شیت
            </li>
        </ul>
    </div>
    <div class="table-holder">
        <table class="topscorers">
            <tbody>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img alt="شهریار مغانلو" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/05/18/C/o5cf1v3k.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/39150/شهریار-مغانلو">شهریار مغانلو</a> -</span>
                                    <span>سپاهان</span>
                                </div>
                            </td>
                            <td>9</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img alt="رضا اسدی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/06/29/C/4vfqqmbw.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/105453/رضا-اسدی">رضا اسدی</a> -</span>
                                    <span>سپاهان</span>
                                </div>
                            </td>
                            <td>8</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img alt="رضا جعفری" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/02/26/B/1e0ytiec.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/4265/رضا-جعفری">رضا جعفری</a> -</span>
                                    <span>ملوان</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="شهاب زاهدی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/07/01/B/wfimg0he.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/37054/شهاب-زاهدی">شهاب زاهدی</a> -</span>
                                    <span>پرسپولیس</span>
                                </div>
                            </td>
                            <td>6</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img alt="مهدی عبدی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/06/29/C/fp4qowcn.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/39348/مهدی-عبدی">مهدی عبدی</a> -</span>
                                    <span>تراکتور</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="رحمان جعفری" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/05/30/C/rpzkpwzo.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/94241/رحمان-جعفری">رحمان جعفری</a> -</span>
                                    <span>شمس آذر قزوین</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="پوریا سرآبادانی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/08/09/C/3xyltlnn.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/166450/پوریا-سرآبادانی">پوریا سرآبادانی</a> -</span>
                                    <span>شمس آذر قزوین</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="لوسیانو پریرا" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/02/12/C/khhn3fyh.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/6571/لوسیانو-پریرا">لوسیانو پریرا</a> -</span>
                                    <span>مس رفسنجان</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="محمدجواد محمدی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/02/26/B/cjpvkuae.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/112212/محمدجواد-محمدی">محمدجواد محمدی</a> -</span>
                                    <span>ذوب آهن</span>
                                </div>
                            </td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img alt="گیورگی گولسیانی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/04/28/B/a4klrqaz.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/119939/گیورگی-گولسیانی">گیورگی گولسیانی</a> -</span>
                                    <span>پرسپولیس</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="رامین رضائیان" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/05/23/C/zqrszhcp.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/128712/رامین-رضائیان">رامین رضائیان</a> -</span>
                                    <span>سپاهان</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="کوین یامگا" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/06/29/C/0t315xex.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/139248/کوین-یامگا">کوین یامگا</a> -</span>
                                    <span>استقلال</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="آریا یوسفی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/05/07/C/o1abssu3.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/165585/آریا-یوسفی">آریا یوسفی</a> -</span>
                                    <span>سپاهان</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="طالب ریکانی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/02/14/C/ckbjssu0.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/557/طالب-ریکانی">طالب ریکانی</a> -</span>
                                    <span>صنعت نفت آبادان</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="امین قاسمی نژاد" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2022/05/31/B/zmzu5iuj.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/714/امین-قاسمی-نژاد">امین قاسمی نژاد</a> -</span>
                                    <span>هوادار</span>
                                </div>
                                    <div class="player">
                                        <figure><img alt="مهرداد محمدی" width="45" height="45" src="https://match-cdn.varzesh3.com/football-player/2023/03/18/B/o5tqya1n.jpg?w=45" /></figure>
                                    <span class="player-name"> <a href="/football/person/180717/مهرداد-محمدی">مهرداد محمدی</a> -</span>
                                    <span>استقلال</span>
                                </div>
                            </td>
                            <td>4</td>
                        </tr>
            </tbody>
        </table>
    </div>
</div>
<div class="widget-footer">
    <a href="/football/league/6/لیگ-برتر-ایران/بازیکنان-برتر" >مشاهده لیست کامل برترین ها</a>
</div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="345">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-2922"></div>
                </div>
    </div>




            


        



            <div class="widget-holder">
                <div id="123" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ قهرمانان آسیا</span>
    </h2>
    <div class="select-options">
        <select id="stage-123">
                    <option value="902381" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902381">مقدماتی </option>
                    <option value="902412" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902412">گروه A </option>
                    <option value="902413" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902413">گروه B </option>
                    <option value="902414" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902414">گروه C </option>
                    <option value="902415" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902415">گروه D </option>
                    <option value="902416" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902416">گروه E </option>
                    <option value="902417" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902417">گروه F </option>
                    <option value="902418" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902418">گروه G </option>
                    <option value="902419" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902419">گروه I </option>
                    <option value="902420" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902420">گروه H </option>
                    <option value="902421" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902421">گروه J </option>
                    <option value="902518" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/123/league/902518">یک هشتم نهایی </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:350px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#ea4336"><h3>یک هشتم نهایی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>سه شنبه 24 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399428/بازی-شاندونگ-تایشان-کاوازاکی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399428/بازی-شاندونگ-تایشان-کاوازاکی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>شاندونگ تایشان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>کاوازاکی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 25 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399427/بازی-چونبوک-موتورز-پوهانگ-استیلرز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399427/بازی-چونبوک-موتورز-پوهانگ-استیلرز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>چونبوک موتورز</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پوهانگ استیلرز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">13:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399430/بازی-بانکوک-یونایتد-یوکوهاما-مارینوس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399430/بازی-بانکوک-یونایتد-یوکوهاما-مارینوس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بانکوک یونایتد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>یوکوهاما مارینوس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399423/بازی-نسف-قارشی-العین-امارات"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399423/بازی-نسف-قارشی-العین-امارات" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نسف قارشی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>العین امارات</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">17:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399424/بازی-الفیحا-النصر"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399424/بازی-الفیحا-النصر" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>الفیحا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>النصر</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 26 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399429/بازی-اولسان-هیوندای-ونتفورت-کوفو"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399429/بازی-اولسان-هیوندای-ونتفورت-کوفو" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اولسان هیوندای</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ونتفورت کوفو</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">13:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399426/بازی-نوبهار-نمنگان-الاتحاد"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399426/بازی-نوبهار-نمنگان-الاتحاد" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نوبهار نمنگان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>الاتحاد</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">17:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399425/بازی-سپاهان-الهلال"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399425/بازی-سپاهان-الهلال" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سپاهان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>الهلال</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">19:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 1 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399435/بازی-پوهانگ-استیلرز-چونبوک-موتورز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399435/بازی-پوهانگ-استیلرز-چونبوک-موتورز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پوهانگ استیلرز</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>چونبوک موتورز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">12:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399436/بازی-کاوازاکی-شاندونگ-تایشان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399436/بازی-کاوازاکی-شاندونگ-تایشان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کاوازاکی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>شاندونگ تایشان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 2 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399438/بازی-ونتفورت-کوفو-اولسان-هیوندای"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399438/بازی-ونتفورت-کوفو-اولسان-هیوندای" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ونتفورت کوفو</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اولسان هیوندای</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">12:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399437/بازی-یوکوهاما-مارینوس-بانکوک-یونایتد"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399437/بازی-یوکوهاما-مارینوس-بانکوک-یونایتد" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>یوکوهاما مارینوس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بانکوک یونایتد</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399431/بازی-العین-امارات-نسف-قارشی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399431/بازی-العین-امارات-نسف-قارشی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>العین امارات</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نسف قارشی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">19:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399432/بازی-النصر-الفیحا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399432/بازی-النصر-الفیحا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>النصر</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>الفیحا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 3 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399434/بازی-الاتحاد-نوبهار-نمنگان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399434/بازی-الاتحاد-نوبهار-نمنگان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>الاتحاد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نوبهار نمنگان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">19:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399433/بازی-الهلال-سپاهان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399433/بازی-الهلال-سپاهان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>الهلال</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>سپاهان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/26/لیگ-قهرمانان-آسیا/نمودار-حذفی" >نمودار حذفی لیگ قهرمانان آسیا</a></div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="347">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-10354"></div>
                </div>
    </div>




            <div class="widget-holder">
                <div id="104" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ قهرمانان اروپا</span>
    </h2>
    <div class="select-options">
        <select id="stage-104">
                    <option value="902423" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902423">گروه A </option>
                    <option value="902424" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902424">گروه B </option>
                    <option value="902425" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902425">گروه C </option>
                    <option value="902426" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902426">گروه D </option>
                    <option value="902427" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902427">گروه E </option>
                    <option value="902428" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902428">گروه F </option>
                    <option value="902429" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902429">گروه G </option>
                    <option value="902430" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902430">گروه H </option>
                    <option value="902507" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/104/league/902507">یک هشتم نهایی </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#00439c"><h3>یک هشتم نهایی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>سه شنبه 24 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399165/بازی-کپنهاگن-منچسترسیتی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399165/بازی-کپنهاگن-منچسترسیتی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کپنهاگن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>منچسترسیتی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399166/بازی-لایپزیش-رئال-مادرید"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399166/بازی-لایپزیش-رئال-مادرید" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>لایپزیش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>رئال مادرید</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 25 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399161/بازی-پاری-سن-ژرمن-رئال-سوسیداد"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399161/بازی-پاری-سن-ژرمن-رئال-سوسیداد" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پاری سن ژرمن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>رئال سوسیداد</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399164/بازی-لاتزیو-بایرن-مونیخ"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399164/بازی-لاتزیو-بایرن-مونیخ" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>لاتزیو</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بایرن مونیخ</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 1 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399162/بازی-اینتر-اتلتیکومادرید"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399162/بازی-اینتر-اتلتیکومادرید" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اینتر</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اتلتیکومادرید</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399163/بازی-آیندهوون-دورتموند"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399163/بازی-آیندهوون-دورتموند" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آیندهوون</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>دورتموند</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 2 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399159/بازی-پورتو-آرسنال"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399159/بازی-پورتو-آرسنال" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پورتو</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آرسنال</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399160/بازی-ناپولی-بارسلونا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399160/بازی-ناپولی-بارسلونا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ناپولی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بارسلونا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 15 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399169/بازی-رئال-سوسیداد-پاری-سن-ژرمن"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399169/بازی-رئال-سوسیداد-پاری-سن-ژرمن" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>رئال سوسیداد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پاری سن ژرمن</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399173/بازی-بایرن-مونیخ-لاتزیو"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399173/بازی-بایرن-مونیخ-لاتزیو" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بایرن مونیخ</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لاتزیو</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 16 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399172/بازی-منچسترسیتی-کپنهاگن"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399172/بازی-منچسترسیتی-کپنهاگن" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>منچسترسیتی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>کپنهاگن</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399174/بازی-رئال-مادرید-لایپزیش"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399174/بازی-رئال-مادرید-لایپزیش" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>رئال مادرید</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لایپزیش</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 22 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399167/بازی-آرسنال-پورتو"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399167/بازی-آرسنال-پورتو" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آرسنال</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پورتو</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399168/بازی-بارسلونا-ناپولی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399168/بازی-بارسلونا-ناپولی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بارسلونا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ناپولی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 23 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399170/بازی-اتلتیکومادرید-اینتر"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399170/بازی-اتلتیکومادرید-اینتر" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اتلتیکومادرید</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اینتر</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399171/بازی-دورتموند-آیندهوون"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399171/بازی-دورتموند-آیندهوون" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>دورتموند</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آیندهوون</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/25/لیگ-قهرمانان-اروپا/نمودار-حذفی" >نمودار حذفی لیگ قهرمانان اروپا</a></div>
                </div>
            </div>
            <div class="widget-holder">
                <div id="74" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ اروپا</span>
    </h2>
    <div class="select-options">
        <select id="stage-74">
                    <option value="902432" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902432">گروه A </option>
                    <option value="902433" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902433">گروه B </option>
                    <option value="902434" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902434">گروه C </option>
                    <option value="902435" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902435">گروه D </option>
                    <option value="902436" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902436">گروه E </option>
                    <option value="902437" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902437">گروه F </option>
                    <option value="902438" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902438">گروه G </option>
                    <option value="902439" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902439">گروه H </option>
                    <option value="902508" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/74/league/902508">پلی آف حذفی </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#ff6a00"><h3>پلی آف حذفی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>پنج شنبه 26 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399175/بازی-فاینورد-آاس-رم"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399175/بازی-فاینورد-آاس-رم" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>فاینورد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آاس رم</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399178/بازی-یانگ-بویز-اسپورتینگ"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399178/بازی-یانگ-بویز-اسپورتینگ" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>یانگ بویز</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اسپورتینگ</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399181/بازی-گالاتاسرای-اسپارتا-پراگ"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399181/بازی-گالاتاسرای-اسپارتا-پراگ" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>گالاتاسرای</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اسپارتا پراگ</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399182/بازی-شاختار-مارسی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399182/بازی-شاختار-مارسی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>شاختار</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مارسی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399176/بازی-آث-میلان-رن"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399176/بازی-آث-میلان-رن" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آث میلان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>رن</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399177/بازی-لانس-فرایبورگ"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399177/بازی-لانس-فرایبورگ" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>لانس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>فرایبورگ</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399179/بازی-بنفیکا-تولوز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399179/بازی-بنفیکا-تولوز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بنفیکا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>تولوز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399180/بازی-براگا-قره-باغ"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399180/بازی-براگا-قره-باغ" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>براگا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>قره باغ</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 3 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399184/بازی-رن-آث-میلان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399184/بازی-رن-آث-میلان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>رن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آث میلان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399185/بازی-فرایبورگ-لانس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399185/بازی-فرایبورگ-لانس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>فرایبورگ</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لانس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399187/بازی-تولوز-بنفیکا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399187/بازی-تولوز-بنفیکا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>تولوز</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بنفیکا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399188/بازی-قره-باغ-براگا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399188/بازی-قره-باغ-براگا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>قره باغ</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>براگا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399183/بازی-آاس-رم-فاینورد"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399183/بازی-آاس-رم-فاینورد" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آاس رم</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>فاینورد</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399186/بازی-اسپورتینگ-یانگ-بویز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399186/بازی-اسپورتینگ-یانگ-بویز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسپورتینگ</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>یانگ بویز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399189/بازی-اسپارتا-پراگ-گالاتاسرای"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399189/بازی-اسپارتا-پراگ-گالاتاسرای" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسپارتا پراگ</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>گالاتاسرای</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399190/بازی-مارسی-شاختار"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399190/بازی-مارسی-شاختار" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مارسی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>شاختار</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/29/لیگ-اروپا/بازی-ها" >برنامه بازی های لیگ اروپا</a></div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="348">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-10718"></div>
                </div>
    </div>




            <div class="widget-holder">
                <div id="75" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ کنفرانس اروپا</span>
    </h2>
    <div class="select-options">
        <select id="stage-75">
                    <option value="902440" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902440">گروه A </option>
                    <option value="902441" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902441">گروه B </option>
                    <option value="902442" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902442">گروه C </option>
                    <option value="902443" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902443">گروه D </option>
                    <option value="902444" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902444">گروه E </option>
                    <option value="902445" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902445">گروه F </option>
                    <option value="902446" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902446">گروه G </option>
                    <option value="902447" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902447">گروه H </option>
                    <option value="902509" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/75/league/902509">پلی آف حذفی </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#00c650"><h3>پلی آف حذفی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>پنج شنبه 26 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399191/بازی-اشتورم-گراتس-اسلوان-براتیسلاوا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399191/بازی-اشتورم-گراتس-اسلوان-براتیسلاوا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اشتورم گراتس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اسلوان براتیسلاوا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399193/بازی-سن-ژیلواز-آینتراخت-فرانکفورت"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399193/بازی-سن-ژیلواز-آینتراخت-فرانکفورت" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سن ژیلواز</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آینتراخت فرانکفورت</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399195/بازی-المپیاکوس-فرنتس-واروش"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399195/بازی-المپیاکوس-فرنتس-واروش" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>المپیاکوس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>فرنتس واروش</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399197/بازی-مولده-لژیا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399197/بازی-مولده-لژیا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مولده</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لژیا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399192/بازی-سروت-لودوگورتس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399192/بازی-سروت-لودوگورتس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سروت</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لودوگورتس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399194/بازی-رئال-بتیس-دیناموزاگرب"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399194/بازی-رئال-بتیس-دیناموزاگرب" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>رئال بتیس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>دیناموزاگرب</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399196/بازی-آژاکس-بوده"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399196/بازی-آژاکس-بوده" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آژاکس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>بوده</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399198/بازی-مکابی-خنت"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399198/بازی-مکابی-خنت" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مکابی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>خنت</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 2 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399206/بازی-خنت-مکابی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399206/بازی-خنت-مکابی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>خنت</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مکابی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 3 اسفند</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399200/بازی-لودوگورتس-سروت"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399200/بازی-لودوگورتس-سروت" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>لودوگورتس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>سروت</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399202/بازی-دیناموزاگرب-رئال-بتیس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399202/بازی-دیناموزاگرب-رئال-بتیس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>دیناموزاگرب</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>رئال بتیس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399204/بازی-بوده-آژاکس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399204/بازی-بوده-آژاکس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بوده</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آژاکس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399199/بازی-اسلوان-براتیسلاوا-اشتورم-گراتس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399199/بازی-اسلوان-براتیسلاوا-اشتورم-گراتس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسلوان براتیسلاوا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اشتورم گراتس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399201/بازی-آینتراخت-فرانکفورت-سن-ژیلواز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399201/بازی-آینتراخت-فرانکفورت-سن-ژیلواز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آینتراخت فرانکفورت</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>سن ژیلواز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399203/بازی-فرنتس-واروش-المپیاکوس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399203/بازی-فرنتس-واروش-المپیاکوس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>فرنتس واروش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>المپیاکوس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399205/بازی-لژیا-مولده"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399205/بازی-لژیا-مولده" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>لژیا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مولده</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/67/لیگ-کنفرانس-اروپا/بازی-ها" >برنامه بازی های لیگ کنفرانس اروپا</a></div>
                </div>
            </div>
            <div class="widget-holder">
                <div id="85" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">جام ملت‌های اروپا 2024</span>
    </h2>
    <div class="select-options">
        <select id="stage-85">
                    <option value="902489" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902489">گروه A </option>
                    <option value="902490" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902490">گروه B </option>
                    <option value="902491" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902491">گروه C </option>
                    <option value="902492" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902492">گروه D </option>
                    <option value="902493" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902493">گروه E </option>
                    <option value="902494" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/85/league/902494">گروه F </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:300px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#33ab54"><h3>گروه A</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 25 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399032/بازی-آلمان-اسکاتلند"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399032/بازی-آلمان-اسکاتلند" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آلمان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>اسکاتلند</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>شنبه 26 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399033/بازی-مجارستان-سوئیس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399033/بازی-مجارستان-سوئیس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مجارستان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>سوئیس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 30 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399035/بازی-آلمان-مجارستان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399035/بازی-آلمان-مجارستان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آلمان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مجارستان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">19:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399034/بازی-اسکاتلند-سوئیس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399034/بازی-اسکاتلند-سوئیس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسکاتلند</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>سوئیس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 3 تیر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399036/بازی-سوئیس-آلمان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399036/بازی-سوئیس-آلمان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سوئیس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آلمان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399037/بازی-اسکاتلند-مجارستان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399037/بازی-اسکاتلند-مجارستان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسکاتلند</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مجارستان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#33ab54"><h3>جدول گروه A</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول گروه A</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><a href="/football/team/348/آلمان"> آلمان</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><a href="/football/team/449/اسکاتلند"> اسکاتلند</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><span> مجارستان</span></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><a href="/football/team/373/سوئیس"> سوئیس</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/23/جام-ملت-های-اروپا?group=902489" >جدول کامل جام ملت های اروپا گروه A</a></div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <div class="v300-col widgets-parent-col">
                <div class="forfix">
                    

            


        
        
        <div class="adbox" data-id="3178">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3178" rel="nofollow"
                    style="background-color: #f5f5f5;height:160px">
                        <img class="adimage" id="img-3178" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/12/19/11fb0ea6-36a9-4c9f-96cb-7273fea0dddb.gif" 
                                                        width="300" 
                                                        height="160" alt="ایران هتل" />
                </a>
    </div>

        
        <div class="adbox" data-id="2839">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2839" rel="nofollow"
                    style="background-color: #f5f5f5;height:80px">
                        <img class="adimage" id="img-2839" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/14/f5eee269-9778-4922-b000-4220dbd70089.gif" 
                                                        width="300" 
                                                        height="80" alt="لایف استار" />
                </a>
    </div>




            <div class="widget-holder">
                <div id="66" class="widget news">
                                
<div class="widget-header"><h2>آخرین اخبار فوتبال</h2></div>
<div class="widget-body">
    <div class="news-tabs">
        <ul>
            <li data-type="Latest" class="active">جدیدترین‌ها   <span class="new-news-message"></span></li>
            <li data-type="MostVisited" data-url="https://web-api.varzesh3.com/v1.0/news/most-visited?includeSports[0]=Football&amp;includeSports[1]=Futsal&amp;includeSports[2]=BeachSoccer">پربازدیدترین‌ها</li>
            <li data-type="MostCommented" data-url="https://web-api.varzesh3.com/v1.0/news/most-commented?includeSports[0]=Football&amp;includeSports[1]=Futsal&amp;includeSports[2]=BeachSoccer">پربحث‌ترین‌ها</li>
        </ul>
    </div>
    <div class="news-content" data-type="Latest">
        <div class="news-filter" data-sports="1,2,41">

                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-origin-1" checked value="1" data-filter-type="origin" />
                    <label for="66-origin-1">داخلی</label>
                </div>
                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-origin-2" checked value="2" data-filter-type="origin" />
                    <label for="66-origin-2">خارجی</label>
                </div>
                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-media-2" checked value="2" data-filter-type="media" />
                    <label for="66-media-2">ویدیو</label>
                </div>
        </div>
        <div class="alert-message">حداقل یکی از گزینه ها باید فعال باشد.</div>
        
        <div class="news-main-list scrollable-box" data-height="1500" style="max-height: 1500px">
            <div class="scroll-list-content">
                <ul>
                            <li data-newsid="1994696" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مطهری و نکونام هیچ مشکلی با هم ندارند" href="https://www.varzesh3.com/news/1994696/مطهری-و-نکونام-هیچ-مشکلی-با-هم-ندارند" data-nt-link> <span class="news-type"></span>مطهری و نکونام هیچ مشکلی با هم ندارند</a>
                            </li>
                            <li data-newsid="1994695" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="باانگیزه ترین ورژن امیری 1402&#x2B;عکس" href="https://www.varzesh3.com/news/1994695/باانگیزه-ترین-ورژن-امیری-1402-عکس" data-nt-link> <span class="news-type"></span>باانگیزه ترین ورژن امیری 1402&#x2B;عکس</a>
                            </li>
                            <li data-newsid="1994694" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="برنده توپ طلا، راه حل فوری برای چلسی!" href="https://www.varzesh3.com/news/1994694/برنده-توپ-طلا-راه-حل-فوری-برای-چلسی" data-nt-link> <span class="news-type"></span>برنده توپ طلا، راه حل فوری برای چلسی!</a>
                            </li>
                            <li data-newsid="1994693" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرسپولیس سرانجام مسافر خارج شد" href="https://www.varzesh3.com/news/1994693/پرسپولیس-سرانجام-مسافر-خارج-شد" data-nt-link> <span class="news-type"></span>پرسپولیس سرانجام مسافر خارج شد</a>
                            </li>
                            <li data-newsid="1994690" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دیگر جنتلمنی مثل آنچلوتی وجود ندارد" href="https://www.varzesh3.com/news/1994690/دیگر-جنتلمنی-مثل-آنچلوتی-وجود-ندارد" data-nt-link> <span class="news-type"></span>دیگر جنتلمنی مثل آنچلوتی وجود ندارد</a>
                            </li>
                            <li data-newsid="1994692" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="VAR نگذاشت پیش‌بینی منصوریان درست در بیاید!" href="https://www.varzesh3.com/news/1994692/var-نگذاشت-پیش-بینی-منصوریان-درست-در-بیاید" data-nt-link> <span class="news-type"></span>VAR نگذاشت پیش‌بینی منصوریان درست در بیاید!</a>
                            </li>
                            <li data-newsid="1994691" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تعجب اوسمار از شرایط بدنی پرسپولیسی‌ها" href="https://www.varzesh3.com/news/1994691/تعجب-اوسمار-از-شرایط-بدنی-پرسپولیسی-ها" data-nt-link> <span class="news-type"></span>تعجب اوسمار از شرایط بدنی پرسپولیسی‌ها</a>
                            </li>
                            <li data-newsid="1994688" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بیرانوند از بازی در بلغارستان عبرت گرفت (عکس)" href="https://www.varzesh3.com/news/1994688/بیرانوند-از-بازی-در-بلغارستان-عبرت-گرفت-عکس" data-nt-link> <span class="news-type"></span>بیرانوند از بازی در بلغارستان عبرت گرفت (عکس)</a>
                            </li>
                            <li data-newsid="1994687" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رکورد ویژه امید ابراهیمی با چند دقیقه بازی" href="https://www.varzesh3.com/news/1994687/رکورد-ویژه-امید-ابراهیمی-با-چند-دقیقه-بازی" data-nt-link> <span class="news-type"></span>رکورد ویژه امید ابراهیمی با چند دقیقه بازی</a>
                            </li>
                            <li data-newsid="1994685" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شاگردان قلعه‌نویی از چمن دور شدند" href="https://www.varzesh3.com/news/1994685/شاگردان-قلعه-نویی-از-چمن-دور-شدند" data-nt-link> <span class="news-type"></span>شاگردان قلعه‌نویی از چمن دور شدند</a>
                            </li>
                            <li data-newsid="1994681" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اتلتیکو احترام رئال را نگه نمی‌دارد" href="https://www.varzesh3.com/news/1994681/اتلتیکو-احترام-رئال-را-نگه-نمی-دارد" data-nt-link> <span class="news-type"></span>اتلتیکو احترام رئال را نگه نمی‌دارد</a>
                            </li>
                            <li data-newsid="1994684" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="زاهدی: بی‌معرفتی است پرسپولیس را تنها بگذارم" href="https://www.varzesh3.com/news/1994684/زاهدی-بی-معرفتی-است-در-این-شرایط-پرسپولیس-را-تنها-بگذارم" data-nt-link> <span class="news-type"></span>زاهدی: بی‌معرفتی است پرسپولیس را تنها بگذارم</a>
                            </li>
                            <li data-newsid="1994683" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="2">
                                <a title="راز موفقیت فوتسال: چگونگی کشف هزار بازیکن" href="https://www.varzesh3.com/news/1994683/راز-موفقیت-فوتسال-چگونگی-کشف-8-هزار-استعداد" data-nt-link> <span class="news-type"></span>راز موفقیت فوتسال: چگونگی کشف هزار بازیکن</a>
                            </li>
                            <li data-newsid="1994682" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="عزم جدی استقلال برای بازگشت به لیگ قهرمانان آسیا" href="https://www.varzesh3.com/news/1994682/عزم-جدی-استقلال-برای-بازگشت-به-لیگ-قهرمانان-آسیا" data-nt-link> <span class="news-type"></span>عزم جدی استقلال برای بازگشت به لیگ قهرمانان آسیا</a>
                            </li>
                            <li data-newsid="1994680" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شروع جسورانه بحرینی‌ها مقابل کره جنوبی" href="https://www.varzesh3.com/news/1994680/شروع-جسورانه-بحرینی-ها-مقابل-کره-جنوبی" data-nt-link> <span class="news-type"></span>شروع جسورانه بحرینی‌ها مقابل کره جنوبی</a>
                            </li>
                            <li data-newsid="1994679" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="برانکو و حذف یک مدعی از جریان قهرمانی آسیا!" href="https://www.varzesh3.com/news/1994679/برانکو-و-حذف-یک-مدعی-از-جریان-قهرمانی-آسیا" data-nt-link> <span class="news-type"></span>برانکو و حذف یک مدعی از جریان قهرمانی آسیا!</a>
                            </li>
                            <li data-newsid="1994678" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کل‌کل شدید روی آنتن زنده: عکس با لباس ورزشی نداری!" href="https://www.varzesh3.com/news/1994678/کل-کل-شدید-روی-آنتن-زنده-عکس-با-لباس-ورزشی-نداری" data-nt-link> <span class="news-type"></span>کل‌کل شدید روی آنتن زنده: عکس با لباس ورزشی نداری!</a>
                            </li>
                            <li data-newsid="1994677" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="17 روز فرصت برای نقل و انتقالات لیگ برتر زنان" href="https://www.varzesh3.com/news/1994677/17-روز-فرصت-برای-نقل-و-انتقالات-لیگ-برتر-زنان" data-nt-link> <span class="news-type"></span>17 روز فرصت برای نقل و انتقالات لیگ برتر زنان</a>
                            </li>
                            <li data-newsid="322047" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="آخرین وضعیت مصدومان از زبان پزشک تیم ملی ایران" href="https://video.varzesh3.com/video/322047/آخرین-وضعیت-مصدومان-از-زبان-پزشک-تیم-ملی-ایران" data-nt-link> <span class="news-type"></span>آخرین وضعیت مصدومان از زبان پزشک تیم ملی ایران</a>
                            </li>
                            <li data-newsid="1994675" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دور افتخار مثلث مخوف رئال با بنر عجیب (عکس)" href="https://www.varzesh3.com/news/1994675/دور-افتخار-مثلث-مخوف-رئال-با-بنر-عجیب-عکس" data-nt-link> <span class="news-type"></span>دور افتخار مثلث مخوف رئال با بنر عجیب (عکس)</a>
                            </li>
                            <li data-newsid="1994676" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شروع بحران: بارسلونا در جست‌‍‌وجوی جانشین ژاوی!" href="https://www.varzesh3.com/news/1994676/شروع-بحران-بارسلونا-در-جستجوی-جانشین-ژاوی" data-nt-link> <span class="news-type"></span>شروع بحران: بارسلونا در جست‌‍‌وجوی جانشین ژاوی!</a>
                            </li>
                            <li data-newsid="1994674" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مهاجم تراکتور از تیم ملی انصراف داد" href="https://www.varzesh3.com/news/1994674/مهاجم-تراکتور-از-تیم-ملی-انصراف-داد" data-nt-link> <span class="news-type"></span>مهاجم تراکتور از تیم ملی انصراف داد</a>
                            </li>
                            <li data-newsid="1994673" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="حسرت مانچینی: می‌توانستم 10 سال دیگر در ایتالیا بمانم" href="https://www.varzesh3.com/news/1994673/حسرت-مانچینی-می-توانستم-10-سال-دیگر-در-ایتالیا-بمانم" data-nt-link> <span class="news-type"></span>حسرت مانچینی: می‌توانستم 10 سال دیگر در ایتالیا بمانم</a>
                            </li>
                            <li data-newsid="1994671" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ترکیب پرستاره کره جنوبی مقابل بحرین" href="https://www.varzesh3.com/news/1994671/ترکیب-پرستاره-کره-جنوبی-مقابل-بحرین" data-nt-link> <span class="news-type"></span>ترکیب پرستاره کره جنوبی مقابل بحرین</a>
                            </li>
                            <li data-newsid="1994672" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="2">
                                <a title="کفش طلا آقای‌گلی ایران فقط به پای این بازیکن می‌خورد" href="https://www.varzesh3.com/news/1994672/کفش-طلا-آقای-گلی-ایران-فقط-به-پای-این-بازیکن-می-خورد" data-nt-link> <span class="news-type"></span>کفش طلا آقای‌گلی ایران فقط به پای این بازیکن می‌خورد</a>
                            </li>
                            <li data-newsid="1994669" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ببر برزیلی بارسا روی نیمکت خشک شد" href="https://www.varzesh3.com/news/1994669/ببر-برزیلی-بارسا-روی-نیمکت-خشک-شد" data-nt-link> <span class="news-type"></span>ببر برزیلی بارسا روی نیمکت خشک شد</a>
                            </li>
                            <li data-newsid="1994670" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اعتراف مدافع رئال مادرید: کمی دیوانه هستم" href="https://www.varzesh3.com/news/1994670/اعتراف-مدافع-رئال-مادرید-کمی-دیوانه-هستم" data-nt-link> <span class="news-type"></span>اعتراف مدافع رئال مادرید: کمی دیوانه هستم</a>
                            </li>
                            <li data-newsid="322046" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پاسخ برانکو به سؤال جنجالی: عزیزم!" href="https://video.varzesh3.com/video/322046/پاسخ-برانکو-به-سؤال-جنجالی-عزیزم" data-nt-link> <span class="news-type"></span>پاسخ برانکو به سؤال جنجالی: عزیزم!</a>
                            </li>
                            <li data-newsid="1994667" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خرید 20 میلیون یورویی برای مقابله با سپاهان!" href="https://www.varzesh3.com/news/1994667/خرید-20-میلیون-یورویی-برای-مقابله-با-سپاهان" data-nt-link> <span class="news-type"></span>خرید 20 میلیون یورویی برای مقابله با سپاهان!</a>
                            </li>
                            <li data-newsid="1994668" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تکمیل شب کابوس‌وار: ستاره بارسا لنگ‌زنان رفت" href="https://www.varzesh3.com/news/1994668/تکمیل-شب-کابوس-وار-ستاره-بارسا-لنگ-زنان-رفت" data-nt-link> <span class="news-type"></span>تکمیل شب کابوس‌وار: ستاره بارسا لنگ‌زنان رفت</a>
                            </li>
                            <li data-newsid="1994666" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرونده بازگشت شفر به ایران بسته شد" href="https://www.varzesh3.com/news/1994666/پرونده-بازگشت-شفر-به-ایران-بسته-شد" data-nt-link> <span class="news-type"></span>پرونده بازگشت شفر به ایران بسته شد</a>
                            </li>
                            <li data-newsid="1994665" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ژاوی بهترین مدافعش را از دست داد" href="https://www.varzesh3.com/news/1994665/ژاوی-بهترین-مدافعش-را-از-دست-داد" data-nt-link> <span class="news-type"></span>ژاوی بهترین مدافعش را از دست داد</a>
                            </li>
                            <li data-newsid="1994664" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="نیمکت‌نشین‌ها بیش از گذشته آماده باشند" href="https://www.varzesh3.com/news/1994664/نیمکت-نشینها-بیش-از-گذشته-آماده-باشند" data-nt-link> <span class="news-type"></span>نیمکت‌نشین‌ها بیش از گذشته آماده باشند</a>
                            </li>
                            <li data-newsid="1994662" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تمجید ویژه اسطوره پرسپولیس از جواد نکونام " href="https://www.varzesh3.com/news/1994662/تمجید-ویژه-اسطوره-پرسپولیس-از-جواد-نکونام" data-nt-link> <span class="news-type"></span>تمجید ویژه اسطوره پرسپولیس از جواد نکونام </a>
                            </li>
                            <li data-newsid="1994658" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دو بازیکن بارسا همه را ناامید کردند" href="https://www.varzesh3.com/news/1994658/دو-بازیکن-بارسا-همه-را-ناامید-کردند" data-nt-link> <span class="news-type"></span>دو بازیکن بارسا همه را ناامید کردند</a>
                            </li>
                            <li data-newsid="1994659" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شگفتی باشگاه انگلیسی از درخشش قدوس (عکس)" href="https://www.varzesh3.com/news/1994659/شگفتی-باشگاه-انگلیسی-از-درخشش-قدوس-عکس" data-nt-link> <span class="news-type"></span>شگفتی باشگاه انگلیسی از درخشش قدوس (عکس)</a>
                            </li>
                            <li data-newsid="1994660" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پاسخ طعنه‌آمیز برانکو به سوال خبرنگار درباره پرسپولیس" href="https://www.varzesh3.com/news/1994660/پاسخ-طعنه-آمیز-برانکو-به-سوال-خبرنگاران-درباره-پرسپولیس" data-nt-link> <span class="news-type"></span>پاسخ طعنه‌آمیز برانکو به سوال خبرنگار درباره پرسپولیس</a>
                            </li>
                            <li data-newsid="1994657" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ادعای ستاره منچسترسیتی: بهتر از مسی ندیدم!" href="https://www.varzesh3.com/news/1994657/ادعای-ستاره-منچسترسیتی-بهتر-از-مسی-ندیدم" data-nt-link> <span class="news-type"></span>ادعای ستاره منچسترسیتی: بهتر از مسی ندیدم!</a>
                            </li>
                            <li data-newsid="1994656" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بازگشت آقا بیژن: سرپرست سابق استقلال در کویر" href="https://www.varzesh3.com/news/1994656/بازگشت-آقا-بیژن-سرپرست-سابق-استقلال-در-کویر" data-nt-link> <span class="news-type"></span>بازگشت آقا بیژن: سرپرست سابق استقلال در کویر</a>
                            </li>
                            <li data-newsid="322044" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شجاع: قهرمان شویم، ریش روزبه را می‌زنم" href="https://video.varzesh3.com/video/322044/شجاع-قهرمان-شویم-ریش-روزبه-را-می-زنم" data-nt-link> <span class="news-type"></span>شجاع: قهرمان شویم، ریش روزبه را می‌زنم</a>
                            </li>
                            <li data-newsid="1994655" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کاپیتان رئال جواب آرائوخو را داد" href="https://www.varzesh3.com/news/1994655/کاپیتان-رئال-جواب-آرائوخو-را-داد" data-nt-link> <span class="news-type"></span>کاپیتان رئال جواب آرائوخو را داد</a>
                            </li>
                            <li data-newsid="1994654" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ناراحتی ستاره ایتالیایی: حق ما این نیست" href="https://www.varzesh3.com/news/1994654/ناراحتی-ستاره-ایتالیایی-حق-ما-این-نیست" data-nt-link> <span class="news-type"></span>ناراحتی ستاره ایتالیایی: حق ما این نیست</a>
                            </li>
                            <li data-newsid="322043" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پیام سم کر اسطوره فوتبال زنان برای درگذشت ملیکا" href="https://video.varzesh3.com/video/322043/پیام-سم-کر-اسطوره-فوتبال-زنان-برای-درگذشت-ملیکا" data-nt-link> <span class="news-type"></span>پیام سم کر اسطوره فوتبال زنان برای درگذشت ملیکا</a>
                            </li>
                            <li data-newsid="1994652" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بحران تیم ملی عربستان در جنجالی‌ترین نشست جام ملت‌ها" href="https://www.varzesh3.com/news/1994652/بحران-تیم-ملی-عربستان-در-جنجالی-ترین-نشست-جام-ملتها" data-nt-link> <span class="news-type"></span>بحران تیم ملی عربستان در جنجالی‌ترین نشست جام ملت‌ها</a>
                            </li>
                            <li data-newsid="1994651" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="امید در اردوی پرسپولیس، امیری به بازی حذفی می‌رسد" href="https://www.varzesh3.com/news/1994651/امید-در-اردوی-پرسپولیس-امیری-به-بازی-حذفی-می-رسد" data-nt-link> <span class="news-type"></span>امید در اردوی پرسپولیس، امیری به بازی حذفی می‌رسد</a>
                            </li>
                            <li data-newsid="1994648" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بارسلونا را باید خراب کرد و از نو ساخت!" href="https://www.varzesh3.com/news/1994648/بارسلونا-را-باید-خراب-کرد-و-از-نو-ساخت" data-nt-link> <span class="news-type"></span>بارسلونا را باید خراب کرد و از نو ساخت!</a>
                            </li>
                            <li data-newsid="1994649" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بازگشت لیث نوبری به صحنه رسانه‌های قطری" href="https://www.varzesh3.com/news/1994649/بازگشت-لیث-نوبری-به-صحنه-رسانه-های-قطری" data-nt-link> <span class="news-type"></span>بازگشت لیث نوبری به صحنه رسانه‌های قطری</a>
                            </li>
                            <li data-newsid="1994646" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="محرمی-رضاییان: رقابت در این پست بالا گرفت" href="https://www.varzesh3.com/news/1994646/محرمی-رضاییان-رقابت-در-این-پست-بالا-گرفت" data-nt-link> <span class="news-type"></span>محرمی-رضاییان: رقابت در این پست بالا گرفت</a>
                            </li>
                            <li data-newsid="1994647" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پیغام دومین بازیکن برتر جهان برای ملیکا محمدی" href="https://www.varzesh3.com/news/1994647/پیغام-دومین-بازیکن-برتر-جهان-برای-ملیکا-محمدی" data-nt-link> <span class="news-type"></span>پیغام دومین بازیکن برتر جهان برای ملیکا محمدی</a>
                            </li>
                            <li data-newsid="1994650" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="جایزه The Best: مسی، امباپه یا هالند!" href="https://www.varzesh3.com/news/1994650/جایزه-the-best-مسی-امباپه-یا-هالند" data-nt-link> <span class="news-type"></span>جایزه The Best: مسی، امباپه یا هالند!</a>
                            </li>
                            <li data-newsid="1994645" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="متاسفم به ایران باختیم، برای مردم غزه جبران می‌کنیم" href="https://www.varzesh3.com/news/1994645/متاسفم-به-ایران-باختیم-برای-مردم-غزه-جبران-می-کنیم" data-nt-link> <span class="news-type"></span>متاسفم به ایران باختیم، برای مردم غزه جبران می‌کنیم</a>
                            </li>
                            <li data-newsid="1994644" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مربی تیم ملی درباره گل فلسطین: غافلگیر شدیم" href="https://www.varzesh3.com/news/1994644/مربی-تیم-ملی-درباره-گل-فلسطین-غافلگیر-شدیم" data-nt-link> <span class="news-type"></span>مربی تیم ملی درباره گل فلسطین: غافلگیر شدیم</a>
                            </li>
                            <li data-newsid="1994641" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رکورد تاریخی لواندوفسکی در شب تلخ بارسا" href="https://www.varzesh3.com/news/1994641/رکورد-تاریخی-لواندوفسکی-در-شب-تلخ-بارسا" data-nt-link> <span class="news-type"></span>رکورد تاریخی لواندوفسکی در شب تلخ بارسا</a>
                            </li>
                            <li data-newsid="1994640" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گزینه استقلال با تیم اصفهانی استارت زد!" href="https://www.varzesh3.com/news/1994640/گزینه-استقلال-با-تیم-اصفهانی-استارت-زد" data-nt-link> <span class="news-type"></span>گزینه استقلال با تیم اصفهانی استارت زد!</a>
                            </li>
                            <li data-newsid="1994639" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرز: به وینیسیوس گفتم باید بیشتر از سه تا می‌زدی!" href="https://www.varzesh3.com/news/1994639/پرز-به-وینیسیوس-گفتم-باید-بیشتر-از-سه-تا-می-زدی" data-nt-link> <span class="news-type"></span>پرز: به وینیسیوس گفتم باید بیشتر از سه تا می‌زدی!</a>
                            </li>
                            <li data-newsid="1994638" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="وضعیت پیچیده مس رفسنجان و ساکت الهامی" href="https://www.varzesh3.com/news/1994638/وضعیت-پیچیده-مس-رفسنجان-و-ساکت-الهامی" data-nt-link> <span class="news-type"></span>وضعیت پیچیده مس رفسنجان و ساکت الهامی</a>
                            </li>
                            <li data-newsid="1994637" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اتهام جعل امضا به مدیران استقلال رد شد" href="https://www.varzesh3.com/news/1994637/اتهام-جعل-امضا-به-مدیران-استقلال-رد-شد" data-nt-link> <span class="news-type"></span>اتهام جعل امضا به مدیران استقلال رد شد</a>
                            </li>
                            <li data-newsid="1994635" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="طعنه مربی الهلال به نیمار در مقایسه با رونالدو" href="https://www.varzesh3.com/news/1994635/طعنه-مربی-الهلال-به-نیمار-در-مقایسه-با-رونالدو" data-nt-link> <span class="news-type"></span>طعنه مربی الهلال به نیمار در مقایسه با رونالدو</a>
                            </li>
                            <li data-newsid="1994633" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="این عادت زشت بارسا در ال‌کلاسیکو هم تکرار شد" href="https://www.varzesh3.com/news/1994633/این-عادت-زشت-بارسا-در-ال-کلاسیکو-هم-تکرار-شد" data-nt-link> <span class="news-type"></span>این عادت زشت بارسا در ال‌کلاسیکو هم تکرار شد</a>
                            </li>
                            <li data-newsid="1994634" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تمجید ستاره رئال از بازیکنان بارسا: چه با جنبه!" href="https://www.varzesh3.com/news/1994634/تمجید-ستاره-رئال-از-بازیکنان-بارسا-چه-با-جنبه" data-nt-link> <span class="news-type"></span>تمجید ستاره رئال از بازیکنان بارسا: چه با جنبه!</a>
                            </li>
                            <li data-newsid="322042" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دیدار ایران و فلسطین از زاویه‌ای متفاوت" href="https://video.varzesh3.com/video/322042/دیدار-ایران-و-فلسطین-از-زاویه-ای-متفاوت" data-nt-link> <span class="news-type"></span>دیدار ایران و فلسطین از زاویه‌ای متفاوت</a>
                            </li>
                            <li data-newsid="1994631" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بارسا را در کاتالونیا به صلیب کشیدند! (عکس)" href="https://www.varzesh3.com/news/1994631/بارسا-را-در-کاتالونیا-به-صلیب-کشیدند-عکس" data-nt-link> <span class="news-type"></span>بارسا را در کاتالونیا به صلیب کشیدند! (عکس)</a>
                            </li>
                            <li data-newsid="1994632" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ناراحتی ستاره بارسا: این شکست قابل قبول نیست" href="https://www.varzesh3.com/news/1994632/ناراحتی-ستاره-بارسا-این-شکست-قابل-قبول-نیست" data-nt-link> <span class="news-type"></span>ناراحتی ستاره بارسا: این شکست قابل قبول نیست</a>
                            </li>
                            <li data-newsid="322040" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کُری خوانی یک پرسپولیسی در شبکۀ الکاس " href="https://video.varzesh3.com/video/322040/کُری-خوانی-یک-پرسپولیسی-در-شبکٔ-الکاس" data-nt-link> <span class="news-type"></span>کُری خوانی یک پرسپولیسی در شبکۀ الکاس </a>
                            </li>
                            <li data-newsid="1994630" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پیام ستاره رئال برای بلینگام: این تازه اولی بود" href="https://www.varzesh3.com/news/1994630/پیام-ستاره-رئال-برای-بلینگام-این-تازه-اولی-بود" data-nt-link> <span class="news-type"></span>پیام ستاره رئال برای بلینگام: این تازه اولی بود</a>
                            </li>
                            <li data-newsid="1994627" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پزشک تیم ملی خیال همه را راحت کرد" href="https://www.varzesh3.com/news/1994627/پزشک-تیم-ملی-خیال-همه-را-راحت-کرد" data-nt-link> <span class="news-type"></span>پزشک تیم ملی خیال همه را راحت کرد</a>
                            </li>
                            <li data-newsid="1994626" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="وای‌فای ضعیف، تنها راه متوقف کردن ایران در قطر!" href="https://www.varzesh3.com/news/1994626/وای-فای-ضعیف-تنها-راه-متوقف-کردن-ایران-در-قطر" data-nt-link> <span class="news-type"></span>وای‌فای ضعیف، تنها راه متوقف کردن ایران در قطر!</a>
                            </li>
                            <li data-newsid="1994629" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اولین تصویر از سنگ مزار قیصر فوتبال (عکس)" href="https://www.varzesh3.com/news/1994629/اولین-تصویر-از-سنگ-مزار-قیصر-فوتبال-عکس" data-nt-link> <span class="news-type"></span>اولین تصویر از سنگ مزار قیصر فوتبال (عکس)</a>
                            </li>
                            <li data-newsid="1994625" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="برهانی: دیگر نباید اینطور گل بخوریم" href="https://www.varzesh3.com/news/1994625/برهانی-دیگر-نباید-اینطور-گل-بخوریم" data-nt-link> <span class="news-type"></span>برهانی: دیگر نباید اینطور گل بخوریم</a>
                            </li>
                            <li data-newsid="1994624" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="برانکو: دوست دارم با عمان صعود کنم" href="https://www.varzesh3.com/news/1994624/برانکو-دوست-دارم-با-عمان-صعود-کنم" data-nt-link> <span class="news-type"></span>برانکو: دوست دارم با عمان صعود کنم</a>
                            </li>
                            <li data-newsid="1994621" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="غیبت دو مهره تهاجمی تراکتور در ترکیه" href="https://www.varzesh3.com/news/1994621/غیبت-دو-مهره-تهاجمی-تراکتور-در-ترکیه" data-nt-link> <span class="news-type"></span>غیبت دو مهره تهاجمی تراکتور در ترکیه</a>
                            </li>
                            <li data-newsid="1994620" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="یادداشت: قلعه‌نویی، وارث بياتى، رنجبر و مهاجرانى" href="https://www.varzesh3.com/news/1994620/یادداشت-قلعه-نویی-وارث-بياتى-رنجبر-و-مهاجرانى" data-nt-link> <span class="news-type"></span>یادداشت: قلعه‌نویی، وارث بياتى، رنجبر و مهاجرانى</a>
                            </li>
                            <li data-newsid="1994617" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دو فریم از گگن‌پرسینگ سنگین ایران" href="https://www.varzesh3.com/news/1994617/دو-فریم-از-گگن-پرسینگ-سنگین-ایران" data-nt-link> <span class="news-type"></span>دو فریم از گگن‌پرسینگ سنگین ایران</a>
                            </li>
                            <li data-newsid="1994622" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تلاش لوا برای ضربه به وینی: چه پنالتی‌زنی!" href="https://www.varzesh3.com/news/1994622/تلاش-لوا-برای-ضربه-به-وینی-چه-پنالتی-زنی" data-nt-link> <span class="news-type"></span>تلاش لوا برای ضربه به وینی: چه پنالتی‌زنی!</a>
                            </li>
                            <li data-newsid="1994616" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پهلوان به اهواز برگشت: سلام فولاد" href="https://www.varzesh3.com/news/1994616/اولین-خرید-فولاد-از-سپاهان-آمد-عکس" data-nt-link> <span class="news-type"></span>پهلوان به اهواز برگشت: سلام فولاد</a>
                            </li>
                            <li data-newsid="1994618" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دستگیری و اخراج فوتبالیست رژیم اشغالگر در ترکیه" href="https://www.varzesh3.com/news/1994618/دستگیری-و-اخراج-فوتبالیست-رژیم-اشغالگر-در-ترکیه" data-nt-link> <span class="news-type"></span>دستگیری و اخراج فوتبالیست رژیم اشغالگر در ترکیه</a>
                            </li>
                            <li data-newsid="1994614" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گلر ژاپن: کاملا می‌دانم من مقصر هستم" href="https://www.varzesh3.com/news/1994614/گلر-ژاپن-کاملا-می-دانم-من-مقصر-هستم" data-nt-link> <span class="news-type"></span>گلر ژاپن: کاملا می‌دانم من مقصر هستم</a>
                            </li>
                            <li data-newsid="1994597" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مانچینی و تصمیم شگفت‌انگیز: عربستان شماره یک ندارد" href="https://www.varzesh3.com/news/1994597/این-تصمیم-مانچینی-را-اخراج-می-کند" data-nt-link> <span class="news-type"></span>مانچینی و تصمیم شگفت‌انگیز: عربستان شماره یک ندارد</a>
                            </li>
                            <li data-newsid="1994613" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="برنامه ویژه فلسطینی‌ها: مهار دسته جمعی طارمی" href="https://www.varzesh3.com/news/1994613/برنامه-ویژه-فلسطینی-ها-مهار-دسته-جمعی-طارمی" data-nt-link> <span class="news-type"></span>برنامه ویژه فلسطینی‌ها: مهار دسته جمعی طارمی</a>
                            </li>
                            <li data-newsid="1994612" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بزرگ‌ترین شگفتی جام ملت‌های آفریقا رقم خورد" href="https://www.varzesh3.com/news/1994612/بزرگترین-شگفتی-جام-ملتهای-آفربقا-رقم-خورد" data-nt-link> <span class="news-type"></span>بزرگ‌ترین شگفتی جام ملت‌های آفریقا رقم خورد</a>
                            </li>
                            <li data-newsid="1994611" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خالص‌ترین خوشحالی گل قایدی در تمام دوران! (عکس)" href="https://www.varzesh3.com/news/1994611/خالص-ترین-خوشحالی-گل-قایدی-در-تمام-دوران-عکس" data-nt-link> <span class="news-type"></span>خالص‌ترین خوشحالی گل قایدی در تمام دوران! (عکس)</a>
                            </li>
                            <li data-newsid="1994610" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خبر درگذشت برادر ملی‌پوش الجزایر در دل اردو" href="https://www.varzesh3.com/news/1994610/خبر-درگذشت-برادر-ملی-پوش-الجزایر-در-دل-اردو" data-nt-link> <span class="news-type"></span>خبر درگذشت برادر ملی‌پوش الجزایر در دل اردو</a>
                            </li>
                            <li data-newsid="1994609" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سردار گل زد، طارمی از او خوشحال‌تر بود (عکس)" href="https://www.varzesh3.com/news/1994609/سردار-گل-زد-طارمی-از-او-خوشحال-تر-بود-عکس" data-nt-link> <span class="news-type"></span>سردار گل زد، طارمی از او خوشحال‌تر بود (عکس)</a>
                            </li>
                            <li data-newsid="1994608" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خداحافظی سپاهان با دو ستاره: Good Luck!" href="https://www.varzesh3.com/news/1994608/جدایی-رسمی-دو-ستاره-از-سپاهان-عکس" data-nt-link> <span class="news-type"></span>خداحافظی سپاهان با دو ستاره: Good Luck!</a>
                            </li>
                            <li data-newsid="322031" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی کالیاری 2 - بولونیا 1" href="https://video.varzesh3.com/video/322031/خلاصه-بازی-کالیاری-2-بولونیا-1" data-nt-link> <span class="news-type"></span>خلاصه بازی کالیاری 2 - بولونیا 1</a>
                            </li>
                            <li data-newsid="1994605" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رکورد دست نیافتنی: پرز جای برنابئو نشست" href="https://www.varzesh3.com/news/1994605/رکورد-دست-نیافتنی-پرز-جای-برنابئو-نشست" data-nt-link> <span class="news-type"></span>رکورد دست نیافتنی: پرز جای برنابئو نشست</a>
                            </li>
                            <li data-newsid="1994602" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="انریکه: پاری سن ژرمن متخصص رقابت است" href="https://www.varzesh3.com/news/1994602/انریکه-پاری-سن-ژرمن-متخصص-رقابت-است" data-nt-link> <span class="news-type"></span>انریکه: پاری سن ژرمن متخصص رقابت است</a>
                            </li>
                            <li data-newsid="322034" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="آنالیز دیدار تیم ملی برابر فلسطین توسط ستار همدانی" href="https://video.varzesh3.com/video/322034/آنالیز-دیدار-تیم-ملی-برابر-فلسطین-توسط-ستار-همدانی" data-nt-link> <span class="news-type"></span>آنالیز دیدار تیم ملی برابر فلسطین توسط ستار همدانی</a>
                            </li>
                            <li data-newsid="1994599" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پیولی: میلان را از کورس قهرمانی بیرون بکشید" href="https://www.varzesh3.com/news/1994599/پیولی-میلان-را-از-کورس-قهرمانی-بیرون-بکشید" data-nt-link> <span class="news-type"></span>پیولی: میلان را از کورس قهرمانی بیرون بکشید</a>
                            </li>
                            <li data-newsid="1994594" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قربان‌زاده: فروپاشی شوروی در فوتبال ایران اتفاق می‌افتد!" href="https://www.varzesh3.com/news/1994594/قربان-زاده-فروپاشی-شوروی-در-فوتبال-ایران-اتفاق-می-افتد" data-nt-link> <span class="news-type"></span>قربان‌زاده: فروپاشی شوروی در فوتبال ایران اتفاق می‌افتد!</a>
                            </li>
                            <li data-newsid="322030" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="از برد تیم ملی ایران تا شکایت پرسپولیس از AFC" href="https://video.varzesh3.com/video/322030/از-برد-تیم-ملی-ایران-تا-شکایت-پرسپولیس-از-afc" data-nt-link> <span class="news-type"></span>از برد تیم ملی ایران تا شکایت پرسپولیس از AFC</a>
                            </li>
                            <li data-newsid="1994593" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="جای طارمی را در پورتو گرفتند!" href="https://www.varzesh3.com/news/1994593/جای-طارمی-را-در-پورتو-گرفتند" data-nt-link> <span class="news-type"></span>جای طارمی را در پورتو گرفتند!</a>
                            </li>
                            <li data-newsid="1994590" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سرمربی فلسطین: فکر می‌کردیم مقابل ایران نتیجه بگیریم" href="https://www.varzesh3.com/news/1994590/سرمربی-فلسطین-فکر-می-کردیم-مقابل-ایران-نتیجه-بگیریم" data-nt-link> <span class="news-type"></span>سرمربی فلسطین: فکر می‌کردیم مقابل ایران نتیجه بگیریم</a>
                            </li>
                            <li data-newsid="1994589" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مایکل اوون: برای ایران آرزوی موفقیت دارم" href="https://www.varzesh3.com/news/1994589/مایکل-اوون-برای-ایران-آرزوی-موفقیت-دارم" data-nt-link> <span class="news-type"></span>مایکل اوون: برای ایران آرزوی موفقیت دارم</a>
                            </li>
                            <li data-newsid="322029" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی اورتون 0 - استون ویلا 0" href="https://video.varzesh3.com/video/322029/خلاصه-بازی-اورتون-0-استون-ویلا-0" data-nt-link> <span class="news-type"></span>خلاصه بازی اورتون 0 - استون ویلا 0</a>
                            </li>
                            <li data-newsid="1994586" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شایان مصلح: سپاهان شانس اول قهرمانی است" href="https://www.varzesh3.com/news/1994586/شایان-مصلح-سپاهان-شانس-اول-قهرمانی-است" data-nt-link> <span class="news-type"></span>شایان مصلح: سپاهان شانس اول قهرمانی است</a>
                            </li>
                            <li data-newsid="1994582" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سوارز فاش کرد: دلیل جالب پیوستن به اینترمیامی!" href="https://www.varzesh3.com/news/1994582/سوارز-فاش-کرد-دلیل-اصلی-پیوستن-به-اینترمیامی" data-nt-link> <span class="news-type"></span>سوارز فاش کرد: دلیل جالب پیوستن به اینترمیامی!</a>
                            </li>
                            <li data-newsid="1994596" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کاپیتان فلسطین: هدف ما و ایران فرق دارد" href="https://www.varzesh3.com/news/1994596/کاپیتان-فلسطین-هدف-ما-و-ایران-فرق-دارد" data-nt-link> <span class="news-type"></span>کاپیتان فلسطین: هدف ما و ایران فرق دارد</a>
                            </li>
                            <li data-newsid="1994595" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="واکنش پلتفرم کاریابی به شایعه اخراج: سلام ژاوی!" href="https://www.varzesh3.com/news/1994595/واکنش-پلتفرم-کاریابی-به-شایعه-اخراج-سلام-ژاوی" data-nt-link> <span class="news-type"></span>واکنش پلتفرم کاریابی به شایعه اخراج: سلام ژاوی!</a>
                            </li>
                            <li data-newsid="1994587" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سرمربی الجزایر قبل از جام ملت‌ها گفت راحت می‌رود!" href="https://www.varzesh3.com/news/1994587/سرمربی-الجزایر-قبل-از-جام-ملتها-گفت-راحت-می-رود" data-nt-link> <span class="news-type"></span>سرمربی الجزایر قبل از جام ملت‌ها گفت راحت می‌رود!</a>
                            </li>
                            <li data-newsid="1994585" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اتفاق شگفت‌انگیز با ایگناسیو و برتری صدمی!" href="https://www.varzesh3.com/news/1994585/اتفاق-شگفت-انگیز-با-ایگناسیو-و-برتری-صدمی" data-nt-link> <span class="news-type"></span>اتفاق شگفت‌انگیز با ایگناسیو و برتری صدمی!</a>
                            </li>
                            <li data-newsid="322027" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی آلمریا 0 - خیرونا 0" href="https://video.varzesh3.com/video/322027/خلاصه-بازی-آلمریا-0-خیرونا-0" data-nt-link> <span class="news-type"></span>خلاصه بازی آلمریا 0 - خیرونا 0</a>
                            </li>
                            <li data-newsid="1994583" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="فلسطین طلسم ۱۳ ساله ایران را شکست (عکس)" href="https://www.varzesh3.com/news/1994583/فلسطین-طلسم-۱۳-ساله-ایران-را-شکست-عکس" data-nt-link> <span class="news-type"></span>فلسطین طلسم ۱۳ ساله ایران را شکست (عکس)</a>
                            </li>
                            <li data-newsid="1994584" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="حدادی‌فر: هواداران ایرانی تشنه گل هستند" href="https://www.varzesh3.com/news/1994584/حدادی-فر-هواداران-ایرانی-تشنه-گل-هستند" data-nt-link> <span class="news-type"></span>حدادی‌فر: هواداران ایرانی تشنه گل هستند</a>
                            </li>
                            <li data-newsid="1994579" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قاتلان سرزن لیگ بیست و سوم: رحمان بی‌رحم" href="https://www.varzesh3.com/news/1994579/قاتلان-سرزن-لیگ-بیست-و-سوم-رحمان-بی-رحم" data-nt-link> <span class="news-type"></span>قاتلان سرزن لیگ بیست و سوم: رحمان بی‌رحم</a>
                            </li>
                            <li data-newsid="322028" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="از شکایت پرسپولیس از afc تا پیروزی پر گل تیم ملی" href="https://video.varzesh3.com/video/322028/تیتر-از-شکایت-پرسپولیس-از-afc-تا-پیروزی-پر-گل-تیم-ملی" data-nt-link> <span class="news-type"></span>از شکایت پرسپولیس از afc تا پیروزی پر گل تیم ملی</a>
                            </li>
                            <li data-newsid="1994578" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اتفاق عجیب برای هم‌بازی مسی: ریکلمه رودست خورد!" href="https://www.varzesh3.com/news/1994578/اتفاق-عجیب-برای-همبازی-سابق-مسی-ریکلمه-رو-دست-خورد" data-nt-link> <span class="news-type"></span>اتفاق عجیب برای هم‌بازی مسی: ریکلمه رودست خورد!</a>
                            </li>
                            <li data-newsid="1994577" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بعد از بدشانسی آسیایی: پای امیری به توپ خورد " href="https://www.varzesh3.com/news/1994577/بعد-از-بدشانسی-آسیایی-پای-امیری-به-توپ-خورد" data-nt-link> <span class="news-type"></span>بعد از بدشانسی آسیایی: پای امیری به توپ خورد </a>
                            </li>
                            <li data-newsid="1994575" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ورود منصوریان با لپ‌تاپ: شغل جدید سرمربی معروف!" href="https://www.varzesh3.com/news/1994575/ورود-منصوریان-با-لپ-تاپ-شغل-جدید-سرمربی-معروف" data-nt-link> <span class="news-type"></span>ورود منصوریان با لپ‌تاپ: شغل جدید سرمربی معروف!</a>
                            </li>
                            <li data-newsid="1994571" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سید مجید چشم از توپ برنمی دارد! (عکس)" href="https://www.varzesh3.com/news/1994571/سید-مجید-چشم-از-توپ-برنمی-دارد-عکس" data-nt-link> <span class="news-type"></span>سید مجید چشم از توپ برنمی دارد! (عکس)</a>
                            </li>
                            <li data-newsid="1994566" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شب درخشان دو شاگرد فرهاد مجیدی در جام ملت‌ها" href="https://www.varzesh3.com/news/1994566/شب-درخشان-دو-شاگرد-فرهاد-مجیدی-در-جام-ملت-ها" data-nt-link> <span class="news-type"></span>شب درخشان دو شاگرد فرهاد مجیدی در جام ملت‌ها</a>
                            </li>
                            <li data-newsid="1994565" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="هزارمین گل تاریخ جام ملت‌ها پیش از بازی ایران" href="https://www.varzesh3.com/news/1994565/هزارمین-گل-تاریخ-جام-ملت-ها-پیش-از-بازی-ایران" data-nt-link> <span class="news-type"></span>هزارمین گل تاریخ جام ملت‌ها پیش از بازی ایران</a>
                            </li>
                            <li data-newsid="1994557" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مجوزی که تا جمعه می‌آید: ورود طبل به ورزشگاه!" href="https://www.varzesh3.com/news/1994557/مجوزی-که-تا-جمعه-می-آید-ورود-طبل-به-ورزشگاه" data-nt-link> <span class="news-type"></span>مجوزی که تا جمعه می‌آید: ورود طبل به ورزشگاه!</a>
                            </li>
                            <li data-newsid="1994555" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شایعه تکذیب شد: کاپیتان انگلیس همچنان در عربستان" href="https://www.varzesh3.com/news/1994555/شایعه-تکذیب-شد-کاپیتان-انگلیس-همچنان-در-عربستان" data-nt-link> <span class="news-type"></span>شایعه تکذیب شد: کاپیتان انگلیس همچنان در عربستان</a>
                            </li>
                            <li data-newsid="1994554" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="حال و هوای نیمکت ایران: همه‌ چیز عالی!" href="https://www.varzesh3.com/news/1994554/حال-و-هوای-نیمکت-ایران-همه-چیز-عالی" data-nt-link> <span class="news-type"></span>حال و هوای نیمکت ایران: همه‌ چیز عالی!</a>
                            </li>
                            <li data-newsid="1994567" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رامین خونگرم‌ترین بازیکن ایران! (عکس) " href="https://www.varzesh3.com/news/1994567/رامین-خونگرم-ترین-بازیکن-ایران" data-nt-link> <span class="news-type"></span>رامین خونگرم‌ترین بازیکن ایران! (عکس) </a>
                            </li>
                            <li data-newsid="1994553" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تکلی که سردار از آن جان سالم به در برد!" href="https://www.varzesh3.com/news/1994553/تکلی-که-سردار-از-آن-جان-سالم-به-در-برد-عکس" data-nt-link> <span class="news-type"></span>تکلی که سردار از آن جان سالم به در برد!</a>
                            </li>
                            <li data-newsid="1994551" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قهرمان‌های سال‌های دور هواداران ویژه تیم ملی (عکس)" href="https://www.varzesh3.com/news/1994551/قهرمان-های-سال-های-دور-هواداران-وِیژه-تیم-ملی-عکس" data-nt-link> <span class="news-type"></span>قهرمان‌های سال‌های دور هواداران ویژه تیم ملی (عکس)</a>
                            </li>
                            <li data-newsid="1994550" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سرلک امیدوار به اتفاق مشابه با پیام نیازمند" href="https://www.varzesh3.com/news/1994550/سرلک-امیدوار-به-اتفاق-مشابه-با-پیام-نیازمند" data-nt-link> <span class="news-type"></span>سرلک امیدوار به اتفاق مشابه با پیام نیازمند</a>
                            </li>
                            <li data-newsid="1994539" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مرتضی: نزدیک‌ترین یار دوازدهم تیم ملی و قلعه‌نویی" href="https://www.varzesh3.com/news/1994539/مرتضی-نزدیک-ترین-یار-دوازدهم-تیم-ملی-و-قلعه-نویی" data-nt-link> <span class="news-type"></span>مرتضی: نزدیک‌ترین یار دوازدهم تیم ملی و قلعه‌نویی</a>
                            </li>
                            <li data-newsid="1994549" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سردار یک قدم تا یک رکورد تاریخی دیگر " href="https://www.varzesh3.com/news/1994549/سردار-یک-قدم-تا-یک-رکورد-تاریخی-دیگر" data-nt-link> <span class="news-type"></span>سردار یک قدم تا یک رکورد تاریخی دیگر </a>
                            </li>
                            <li data-newsid="1994547" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرسپوليس به یحیی نزدیک می‌شود" href="https://www.varzesh3.com/news/1994547/پرسپوليس-به-یحیی-نزدیک-می-شود" data-nt-link> <span class="news-type"></span>پرسپوليس به یحیی نزدیک می‌شود</a>
                            </li>
                            <li data-newsid="1994546" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رکورد تاریخی محمد صلاح در جام ملت‌ها" href="https://www.varzesh3.com/news/1994546/رکورد-تاریخی-محمد-صلاح-در-جام-ملت-ها" data-nt-link> <span class="news-type"></span>رکورد تاریخی محمد صلاح در جام ملت‌ها</a>
                            </li>
                            <li data-newsid="1994544" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ستاره استقلال دوباره شاگرد اول شد!" href="https://www.varzesh3.com/news/1994544/ستاره-استقلال-دوباره-شاگرد-اول-شد" data-nt-link> <span class="news-type"></span>ستاره استقلال دوباره شاگرد اول شد!</a>
                            </li>
                            <li data-newsid="1994542" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ستاره سابق رئال هم‌تیمی سامان قدوس می‌شود" href="https://www.varzesh3.com/news/1994542/ستاره-سابق-رئال-هم-تیمی-سامان-قدوس-می-شود" data-nt-link> <span class="news-type"></span>ستاره سابق رئال هم‌تیمی سامان قدوس می‌شود</a>
                            </li>
                            <li data-newsid="1994541" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کاپیتان عراق: 2007 انگیزه قهرمانی ماست" href="https://www.varzesh3.com/news/1994541/کاپیتان-عراق-2007-انگیزه-قهرمانی-ماست" data-nt-link> <span class="news-type"></span>کاپیتان عراق: 2007 انگیزه قهرمانی ماست</a>
                            </li>
                            <li data-newsid="1994540" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سعید به جای امارات، در قطر حضور زد" href="https://www.varzesh3.com/news/1994540/سعید-به-جای-امارات-در-قطر-حضور-زد" data-nt-link> <span class="news-type"></span>سعید به جای امارات، در قطر حضور زد</a>
                            </li>
                            <li data-newsid="1994536" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرسپولیس و سه خرید: یک امیدواری، دو ناامیدی!" href="https://www.varzesh3.com/news/1994536/پرسپولیس-و-سه-خرید-زمستانی-یک-امیدواری-دو-ناامیدی" data-nt-link> <span class="news-type"></span>پرسپولیس و سه خرید: یک امیدواری، دو ناامیدی!</a>
                            </li>
                            <li data-newsid="1994534" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شانزدهمین کاپیتان تیم ملی در آسیا " href="https://www.varzesh3.com/news/1994534/شانزدهمین-کاپیتان-تیم-ملی-در-آسیا" data-nt-link> <span class="news-type"></span>شانزدهمین کاپیتان تیم ملی در آسیا </a>
                            </li>
                            <li data-newsid="1994530" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کاتانچ: مسی در تیم ما غایب بود!" href="https://www.varzesh3.com/news/1994530/کاتانچ-مسی-در-تیم-ما-غایب-بود" data-nt-link> <span class="news-type"></span>کاتانچ: مسی در تیم ما غایب بود!</a>
                            </li>
                            <li data-newsid="1994528" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ننکا بعد از استعفای یحیی گفته بود برنمی‌گردم!" href="https://www.varzesh3.com/news/1994528/ننکا-بعد-از-استعفای-یحیی-گفته-بود-برنمی-گردم" data-nt-link> <span class="news-type"></span>ننکا بعد از استعفای یحیی گفته بود برنمی‌گردم!</a>
                            </li>
                            <li data-newsid="1994493" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رئیس آفریقا: هر اتفاقی رخ دهد، تقصیر من است" href="https://www.varzesh3.com/news/1994493/رئیس-آفریقا-هر-اتفاقی-رخ-دهد-تقصیر-من-است" data-nt-link> <span class="news-type"></span>رئیس آفریقا: هر اتفاقی رخ دهد، تقصیر من است</a>
                            </li>
                            <li data-newsid="1994440" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خطرناک‌ترین خطوط هوایی آسمان اروپا در نیم فصل" href="https://www.varzesh3.com/news/1994440/خطرناک-ترین-خطوط-هوایی-آسمان-اروپا-در-نیم-فصل" data-nt-link> <span class="news-type"></span>خطرناک‌ترین خطوط هوایی آسمان اروپا در نیم فصل</a>
                            </li>
                            <li data-newsid="1994427" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="نکونام در تمرین اول بازیکن کم آورد! (عکس)" href="https://www.varzesh3.com/news/1994427/نکونام-در-تمرین-اول-بازیکن-کم-آورد-عکس" data-nt-link> <span class="news-type"></span>نکونام در تمرین اول بازیکن کم آورد! (عکس)</a>
                            </li>
                            <li data-newsid="1994391" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دعوای رئال، لیورپول و پی‌اس‌جی برای این بازیکن" href="https://www.varzesh3.com/news/1994391/دعوای-رئال-لیورپول-و-پی-اس-جی-برای-این-بازیکن" data-nt-link> <span class="news-type"></span>دعوای رئال، لیورپول و پی‌اس‌جی برای این بازیکن</a>
                            </li>
                            <li data-newsid="1994357" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تاثیر قهرمانی جهان با مسی: مردم عاشق‌تر شدند" href="https://www.varzesh3.com/news/1994357/تاثیر-قهرمانی-جهان-با-مسی-مردم-عاشق-تر-شدند" data-nt-link> <span class="news-type"></span>تاثیر قهرمانی جهان با مسی: مردم عاشق‌تر شدند</a>
                            </li>
                            <li data-newsid="1994319" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="فغانی یکی از سه داور مورد اعتماد کشور اندونزی" href="https://www.varzesh3.com/news/1994319/فغانی-یکی-از-سه-داور-مورد-اعتماد-کشور-اندونزی" data-nt-link> <span class="news-type"></span>فغانی یکی از سه داور مورد اعتماد کشور اندونزی</a>
                            </li>
                            <li data-newsid="322026" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی کادیز 1 - والنسیا 4" href="https://video.varzesh3.com/video/322026/خلاصه-بازی-کادیز-1-والنسیا-4" data-nt-link> <span class="news-type"></span>خلاصه بازی کادیز 1 - والنسیا 4</a>
                            </li>
                            <li data-newsid="1994592" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دکو تایید کرد: قرار نیست ژاوی را اخراج کنیم" href="https://www.varzesh3.com/news/1994592/دکو-تایید-کرد-قرار-نیست-ژاوی-را-اخراج-کنیم" data-nt-link> <span class="news-type"></span>دکو تایید کرد: قرار نیست ژاوی را اخراج کنیم</a>
                            </li>
                            <li data-newsid="1994588" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پروین برای علی دایی سنگ‌ تمام گذاشت" href="https://www.varzesh3.com/news/1994588/پروین-برای-علی-دایی-سنگ-تمام-گذاشت" data-nt-link> <span class="news-type"></span>پروین برای علی دایی سنگ‌ تمام گذاشت</a>
                            </li>
                            <li data-newsid="1994581" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="وینیسیوس: همه می‌خواهند با من دعوا کنند!" href="https://www.varzesh3.com/news/1994581/وینیسیوس-همه-می-خواهند-با-من-دعوا-کنند" data-nt-link> <span class="news-type"></span>وینیسیوس: همه می‌خواهند با من دعوا کنند!</a>
                            </li>
                            <li data-newsid="1994580" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پرز: امشب وقت شادی است، از امباپه حرف نزنید!" href="https://www.varzesh3.com/news/1994580/پرز-امشب-وقت-شادی-است-از-امباپه-حرف-نزنید" data-nt-link> <span class="news-type"></span>پرز: امشب وقت شادی است، از امباپه حرف نزنید!</a>
                            </li>
                            <li data-newsid="322024" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی غنا 1 - کیپ ورد 2" href="https://video.varzesh3.com/video/322024/خلاصه-بازی-غنا-1-کیپ-ورد-2" data-nt-link> <span class="news-type"></span>خلاصه بازی غنا 1 - کیپ ورد 2</a>
                            </li>
                            <li data-newsid="322025" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی لانس 0 - پاری سن ژرمن 2" href="https://video.varzesh3.com/video/322025/خلاصه-بازی-لانس-0-پاری-سن-ژرمن-2" data-nt-link> <span class="news-type"></span>خلاصه بازی لانس 0 - پاری سن ژرمن 2</a>
                            </li>
                            <li data-newsid="1994576" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ژاوی: تیم امشب اصلا بارسلونا نبود!" href="https://www.varzesh3.com/news/1994576/ژاوی-تیم-امشب-اصلا-بارسلونا-نبود" data-nt-link> <span class="news-type"></span>ژاوی: تیم امشب اصلا بارسلونا نبود!</a>
                            </li>
                            <li data-newsid="1994574" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="جدایی احتمالی فروزان از تیم دوست‌داشتنی" href="https://www.varzesh3.com/news/1994574/جدایی-احتمالی-فروزان-از-تیم-دوست-داشتنی" data-nt-link> <span class="news-type"></span>جدایی احتمالی فروزان از تیم دوست‌داشتنی</a>
                            </li>
                            <li data-newsid="322023" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی آث میلان 3 - آاس رم 1" href="https://video.varzesh3.com/video/322023/خلاصه-بازی-آث-میلان-3-آاس-رم-1" data-nt-link> <span class="news-type"></span>خلاصه بازی آث میلان 3 - آاس رم 1</a>
                            </li>
                            <li data-newsid="1994573" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="میلان 3-1 رم: روزهای سیاه مورینیو ادامه دارد!" href="https://www.varzesh3.com/news/1994573/میلان-3-1-رم-روزهای-سیاه-مورینیو-ادامه-دارد" data-nt-link> <span class="news-type"></span>میلان 3-1 رم: روزهای سیاه مورینیو ادامه دارد!</a>
                            </li>
                            <li data-newsid="1994572" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="لانس ۰-۲ پی‌اس‌جی: پیروزی بی‌دردسر تیم انریکه" href="https://www.varzesh3.com/news/1994572/لانس-۰-۲-پی-اس-جی-پیروزی-بی-دردسر-تیم-انریکه" data-nt-link> <span class="news-type"></span>لانس ۰-۲ پی‌اس‌جی: پیروزی بی‌دردسر تیم انریکه</a>
                            </li>
                            <li data-newsid="322022" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گل سوم آث میلان به آاس رم توسط هرناندز" href="https://video.varzesh3.com/video/322022/گل-سوم-آث-میلان-به-آاس-رم-توسط-هرناندز" data-nt-link> <span class="news-type"></span>گل سوم آث میلان به آاس رم توسط هرناندز</a>
                            </li>
                            <li data-newsid="1994568" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="فرش جادویی برای وینی: چهار تا خیلی کم بود!" href="https://www.varzesh3.com/news/1994568/فرش-جادویی-برای-وینی-چهار-تا-خیلی-کم-بود" data-nt-link> <span class="news-type"></span>فرش جادویی برای وینی: چهار تا خیلی کم بود!</a>
                            </li>
                            <li data-newsid="1994570" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="مصدومیت مچ، شجاع را از پا درآورد (عکس)" href="https://www.varzesh3.com/news/1994570/پاشنه-شجاع-را-از-پا-درآورد-عکس" data-nt-link> <span class="news-type"></span>مصدومیت مچ، شجاع را از پا درآورد (عکس)</a>
                            </li>
                            <li data-newsid="1994569" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قایدی و انصاری‌فرد به این دلیل بازی کردند" href="https://www.varzesh3.com/news/1994569/قایدی-و-انصاری-فرد-به-این-دلیل-بازی-کردند" data-nt-link> <span class="news-type"></span>قایدی و انصاری‌فرد به این دلیل بازی کردند</a>
                            </li>
                            <li data-newsid="322021" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="انصاری‌فرد: هرکسی حق انتقاد کردن دارد" href="https://video.varzesh3.com/video/322021/انصاری-فرد-هرکسی-حق-انتقاد-کردن-دارد" data-nt-link> <span class="news-type"></span>انصاری‌فرد: هرکسی حق انتقاد کردن دارد</a>
                            </li>
                            <li data-newsid="322019" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="طارمی: ان‌شاءالله با همین روند پیش می‌رویم" href="https://video.varzesh3.com/video/322019/طارمی-انشالله-با-همین-روند-پیش-می-رویم" data-nt-link> <span class="news-type"></span>طارمی: ان‌شاءالله با همین روند پیش می‌رویم</a>
                            </li>
                            <li data-newsid="322020" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گل اول آاس رم به آث میلان (پاردس)" href="https://video.varzesh3.com/video/322020/گل-اول-آاس-رم-به-آث-میلان-پاردس" data-nt-link> <span class="news-type"></span>گل اول آاس رم به آث میلان (پاردس)</a>
                            </li>
                            <li data-newsid="322018" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کنفرانس خبری قلعه‌نویی پس از برد مقابل فلسطین" href="https://video.varzesh3.com/video/322018/کنفرانس-خبری-قلعه-نویی-پس-از-برد-مقابل-فلسطین" data-nt-link> <span class="news-type"></span>کنفرانس خبری قلعه‌نویی پس از برد مقابل فلسطین</a>
                            </li>
                            <li data-newsid="1994563" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="آنچلوتی: بازی نزدیک‌تر از این نتیجه بود!" href="https://www.varzesh3.com/news/1994563/آنچلوتی-بازی-نزدیکتر-از-این-نتیجه-بود" data-nt-link> <span class="news-type"></span>آنچلوتی: بازی نزدیک‌تر از این نتیجه بود!</a>
                            </li>
                            <li data-newsid="1994564" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بنتو: آرزو داشتم پرگل ببریم" href="https://www.varzesh3.com/news/1994564/بنتو-آرزو-داشتم-پرگل-ببریم" data-nt-link> <span class="news-type"></span>بنتو: آرزو داشتم پرگل ببریم</a>
                            </li>
                            <li data-newsid="1994562" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="محبی: ژاپن به زور ویتنام را شکست داد" href="https://www.varzesh3.com/news/1994562/محبی-ژاپن-به-زور-ویتنام-را-شکست-داد" data-nt-link> <span class="news-type"></span>محبی: ژاپن به زور ویتنام را شکست داد</a>
                            </li>
                            <li data-newsid="322017" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گل دوم آث میلان به آاس رم توسط ژیرو" href="https://video.varzesh3.com/video/322017/گل-دوم-آث-میلان-به-آاس-رم-توسط-ژیرو" data-nt-link> <span class="news-type"></span>گل دوم آث میلان به آاس رم توسط ژیرو</a>
                            </li>
                            <li data-newsid="1994561" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="باختن به رئال بدترین اتفاق ممکن است" href="https://www.varzesh3.com/news/1994561/باختن-به-رئال-بدترین-اتفاق-ممکن-است" data-nt-link> <span class="news-type"></span>باختن به رئال بدترین اتفاق ممکن است</a>
                            </li>
                            <li data-newsid="1994560" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="آزمون از حالا فقط به رکورد دایی فکر می‌کند" href="https://www.varzesh3.com/news/1994560/آزمون-از-حالا-فقط-به-رکورد-دایی-فکر-می-کند" data-nt-link> <span class="news-type"></span>آزمون از حالا فقط به رکورد دایی فکر می‌کند</a>
                            </li>
                            <li data-newsid="1994559" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قایدی: اولین گل در اولین تورنمنت، خوشحالم" href="https://www.varzesh3.com/news/1994559/قایدی-اولین-گل-در-اولین-تورنمنت-خوشحالم" data-nt-link> <span class="news-type"></span>قایدی: اولین گل در اولین تورنمنت، خوشحالم</a>
                            </li>
                            <li data-newsid="1994556" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="بیرانوند: 10 بر یک هم ببریم، ناراحت می‌شوم" href="https://www.varzesh3.com/news/1994556/بیرانوند-10-بر-یک-هم-ببریم-ناراحت-می-شوم" data-nt-link> <span class="news-type"></span>بیرانوند: 10 بر یک هم ببریم، ناراحت می‌شوم</a>
                            </li>
                            <li data-newsid="1994558" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="وینسیوس روی اعصاب بارسایی: سلطان کُری! (عکس)" href="https://www.varzesh3.com/news/1994558/وینسیوس-روی-اعصاب-بارسایی-سلطان-کُری-عکس" data-nt-link> <span class="news-type"></span>وینسیوس روی اعصاب بارسایی: سلطان کُری! (عکس)</a>
                            </li>
                            <li data-newsid="1994497" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="نمایش خاص رئال برای در هم کوبیدن ال‌کلاسیکو" href="https://www.varzesh3.com/news/1994497/نمایش-خاص-رئال-برای-در-هم-کوبیدن-ال-کلاسیکو" data-nt-link> <span class="news-type"></span>نمایش خاص رئال برای در هم کوبیدن ال‌کلاسیکو</a>
                            </li>
                            <li data-newsid="322016" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قلعه‌نویی: تیم ضعیف در این تورنمنت وجود ندارد" href="https://video.varzesh3.com/video/322016/قلعه-نویی-تیم-ضعیف-در-این-تورنمنت-وجود-ندارد" data-nt-link> <span class="news-type"></span>قلعه‌نویی: تیم ضعیف در این تورنمنت وجود ندارد</a>
                            </li>
                            <li data-newsid="322015" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قدوس: هرجا که سرمربی بخواهد بازی می‌کنم" href="https://video.varzesh3.com/video/322015/قدوس-هرجا-که-سرمربی-بخواهد-بازی-می-کنم" data-nt-link> <span class="news-type"></span>قدوس: هرجا که سرمربی بخواهد بازی می‌کنم</a>
                            </li>
                            <li data-newsid="322014" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="خلاصه بازی رئال مادرید 4 - بارسلونا 1" href="https://video.varzesh3.com/video/322014/خلاصه-بازی-رئال-مادرید-4-بارسلونا-1" data-nt-link> <span class="news-type"></span>خلاصه بازی رئال مادرید 4 - بارسلونا 1</a>
                            </li>
                            <li data-newsid="1994548" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="راز درخشش قدوس مشخص شد" href="https://www.varzesh3.com/news/1994548/راز-درخشش-قدوس-مشخص-شد" data-nt-link> <span class="news-type"></span>راز درخشش قدوس مشخص شد</a>
                            </li>
                            <li data-newsid="1994552" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="دفاع وسط فلسطین اسپانیایی حرف می‌زد" href="https://www.varzesh3.com/news/1994552/دفاع-وسط-فلسطین-اسپانیایی-حرف-می-زد" data-nt-link> <span class="news-type"></span>دفاع وسط فلسطین اسپانیایی حرف می‌زد</a>
                            </li>
                            <li data-newsid="1994545" class="text-type" data-origin="3"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="طارمی: زدن 4 گل در جام ملت‌ها راحت نیست" href="https://www.varzesh3.com/news/1994545/طارمی-زدن-4-گل-در-جام-ملت-ها-راحت-نیست" data-nt-link> <span class="news-type"></span>طارمی: زدن 4 گل در جام ملت‌ها راحت نیست</a>
                            </li>
                            <li data-newsid="1994543" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="وینیسیوس همه‌جوره زهرش را به بارسا ریخت! (عکس)" href="https://www.varzesh3.com/news/1994543/وینیسیوس-همه-جوره-زهرش-را-به-بارسا-ریخت-عکس" data-nt-link> <span class="news-type"></span>وینیسیوس همه‌جوره زهرش را به بارسا ریخت! (عکس)</a>
                            </li>
                            <li data-newsid="322012" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تیموریان: فوتبال آسیا پیشرفت خوبی کرده" href="https://video.varzesh3.com/video/322012/تیموریان-فوتبال-آسیا-پیشرفت-خوبی-کرده" data-nt-link> <span class="news-type"></span>تیموریان: فوتبال آسیا پیشرفت خوبی کرده</a>
                            </li>
                            <li data-newsid="322013" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پروین: استقلال و پرسپولیس باید خصوصی باشند" href="https://video.varzesh3.com/video/322013/پروین-استقلال-و-پرسپولیس-باید-خصوصی-باشند" data-nt-link> <span class="news-type"></span>پروین: استقلال و پرسپولیس باید خصوصی باشند</a>
                            </li>
                            <li data-newsid="1994538" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="همه نگران شجاع، خدا به خیر بگذراند (عکس)" href="https://www.varzesh3.com/news/1994538/همه-نگران-شجاع-خدا-بخیر-بگذراند-عکس" data-nt-link> <span class="news-type"></span>همه نگران شجاع، خدا به خیر بگذراند (عکس)</a>
                            </li>
                            <li data-newsid="1994535" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="تیموریان: خوشحالم که کریم به رکوردم رسید" href="https://www.varzesh3.com/news/1994535/تیموریان-خوشحالم-که-کریم-به-رکوردم-رسید" data-nt-link> <span class="news-type"></span>تیموریان: خوشحالم که کریم به رکوردم رسید</a>
                            </li>
                            <li data-newsid="322011" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="نیازمند: هر بازی با همین قدرت پیش می‌رویم" href="https://video.varzesh3.com/video/322011/نیازمند-هربازی-با-همین-قدرت-پیش-می-رویم" data-nt-link> <span class="news-type"></span>نیازمند: هر بازی با همین قدرت پیش می‌رویم</a>
                            </li>
                            <li data-newsid="1994531" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کنعانی‌زادگان مانع دبل شدن بیرانوند" href="https://www.varzesh3.com/news/1994531/کنعانی-زادگان-مانع-دبل-شدن-بیرانوند" data-nt-link> <span class="news-type"></span>کنعانی‌زادگان مانع دبل شدن بیرانوند</a>
                            </li>
                            <li data-newsid="322010" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پیش‌بینی مایکل اوون از قهرمان جام ملت‌های آسیا" href="https://video.varzesh3.com/video/322010/پیش-بینی-مایکل-اوون-از-قهرمان-جام-ملت-های-آسیا" data-nt-link> <span class="news-type"></span>پیش‌بینی مایکل اوون از قهرمان جام ملت‌های آسیا</a>
                            </li>
                            <li data-newsid="1994533" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="شب برزیلی‌ها در ال‌کلاسیکو تکمیل شد! (عکس)" href="https://www.varzesh3.com/news/1994533/شب-برزیلی-ها-در-ال-کلاسیکو-تکمیل-شد-عکس" data-nt-link> <span class="news-type"></span>شب برزیلی‌ها در ال‌کلاسیکو تکمیل شد! (عکس)</a>
                            </li>
                            <li data-newsid="1994529" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رازگشایی دلیل بازشدن دروازه بیرانوند از نظر نیازمند" href="https://www.varzesh3.com/news/1994529/رازگشایی-دلیل-بازشدن-دروازه-بیرانوند-از-نظر-نیازمند" data-nt-link> <span class="news-type"></span>رازگشایی دلیل بازشدن دروازه بیرانوند از نظر نیازمند</a>
                            </li>
                            <li data-newsid="1994527" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="قلعه‌نویی: هم من عصبانی شدم هم بیرانوند!" href="https://www.varzesh3.com/news/1994527/قلعه-نویی-به-موقع-گل-زدیم-اما-راضی-نیستم" data-nt-link> <span class="news-type"></span>قلعه‌نویی: هم من عصبانی شدم هم بیرانوند!</a>
                            </li>
                            <li data-newsid="322009" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گل چهارم رئال مادرید به بارسلونا توسط رودریگو" href="https://video.varzesh3.com/video/322009/گل-چهارم-رئال-مادرید-به-بارسلونا-توسط-رودریگو" data-nt-link> <span class="news-type"></span>گل چهارم رئال مادرید به بارسلونا توسط رودریگو</a>
                            </li>
                            <li data-newsid="1994526" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سرمربی قهرمان ایران، میهمان ویژه قطری‌ها (عکس)" href="https://www.varzesh3.com/news/1994526/سرمربی-قهرمان-ایران-میهمان-ویژه-قطری-ها-عکس" data-nt-link> <span class="news-type"></span>سرمربی قهرمان ایران، میهمان ویژه قطری‌ها (عکس)</a>
                            </li>
                            <li data-newsid="1994524" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="فلسطین مقابل ایران دست و پا بسته نبود (عکس) " href="https://www.varzesh3.com/news/1994524/فلسطین-مقابل-ایران-دست-و-پا-بسته-نبود-عکس" data-nt-link> <span class="news-type"></span>فلسطین مقابل ایران دست و پا بسته نبود (عکس) </a>
                            </li>
                            <li data-newsid="322008" class="video-type" data-origin="2"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="گل اول آث میلان به آاس رم توسط عدلی" href="https://video.varzesh3.com/video/322008/گل-اول-آث-میلان-به-آاس-رم-توسط-عدلی" data-nt-link> <span class="news-type"></span>گل اول آث میلان به آاس رم توسط عدلی</a>
                            </li>
                            <li data-newsid="1994525" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="کارشناس داوری مارکا: داور پنالتی را به رئال هدیه داده!" href="https://www.varzesh3.com/news/1994525/کارشناس-داوری-مارکا-داور-پنالتی-را-به-رئال-هدیه-داده" data-nt-link> <span class="news-type"></span>کارشناس داوری مارکا: داور پنالتی را به رئال هدیه داده!</a>
                            </li>
                            <li data-newsid="1994523" class="text-type" data-origin="2"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="هر بار تیمم از مشکلات سربلند بیرون می‌آید!" href="https://www.varzesh3.com/news/1994523/هر-بار-تیمم-از-مشکلات-سربلند-بیرون-می-آید" data-nt-link> <span class="news-type"></span>هر بار تیمم از مشکلات سربلند بیرون می‌آید!</a>
                            </li>
                            <li data-newsid="322007" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پروین: فوتبال ایران را با نام علی دایی می‌شناسند" href="https://video.varzesh3.com/video/322007/پروین-فوتبال-ایران-را-با-نام-علی-دایی-می-شناسند" data-nt-link> <span class="news-type"></span>پروین: فوتبال ایران را با نام علی دایی می‌شناسند</a>
                            </li>
                            <li data-newsid="1994522" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="سرمربی فلسطین: خوشحال هستیم" href="https://www.varzesh3.com/news/1994522/سرمربی-فلسطین-خوشحال-هستیم" data-nt-link> <span class="news-type"></span>سرمربی فلسطین: خوشحال هستیم</a>
                            </li>
                            <li data-newsid="1994521" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="هدیه فلسطینی به نبی اهدا شد (عکس) " href="https://www.varzesh3.com/news/1994521/هدیه-فلسطینی-به-نبی-اهدا-شد-عکس" data-nt-link> <span class="news-type"></span>هدیه فلسطینی به نبی اهدا شد (عکس) </a>
                            </li>
                            <li data-newsid="1994519" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="امیر قطر: همزمان کنار ایران و فلسطین (عکس) " href="https://www.varzesh3.com/news/1994519/امیر-قطر-همزمان-کنار-ایران-و-فلسطین-عکس" data-nt-link> <span class="news-type"></span>امیر قطر: همزمان کنار ایران و فلسطین (عکس) </a>
                            </li>
                            <li data-newsid="322006" class="video-type" data-origin="1"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="پروین: با رفتن هاشمی نسب به استقلال موافق بودم" href="https://video.varzesh3.com/video/322006/پروین-با-رفتن-هاشمی-نسب-به-استقلال-موافق-بودم" data-nt-link> <span class="news-type"></span>پروین: با رفتن هاشمی نسب به استقلال موافق بودم</a>
                            </li>
                            <li data-newsid="1994518" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="رفتار حرفه‌ای قلعه‌نویی در قبال سرمربی فلسطین (عکس)" href="https://www.varzesh3.com/news/1994518/رفتار-حرفه-ای-قلعه-نویی-در-قبال-سرمربی-فلسطین-عکس" data-nt-link> <span class="news-type"></span>رفتار حرفه‌ای قلعه‌نویی در قبال سرمربی فلسطین (عکس)</a>
                            </li>
                            <li data-newsid="1994517" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="ماجراجویی جدید تیم ملی شروع شد" href="https://www.varzesh3.com/news/1994517/ماجراجویی-جدید-تیم-ملی-شروع-شد" data-nt-link> <span class="news-type"></span>ماجراجویی جدید تیم ملی شروع شد</a>
                            </li>
                            <li data-newsid="322005" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="اختلاف در تیم ملی از زبان علی پروین" href="https://video.varzesh3.com/video/322005/اختلاف-در-تیم-ملی-از-زبان-علی-پروین" data-nt-link> <span class="news-type"></span>اختلاف در تیم ملی از زبان علی پروین</a>
                            </li>
                            <li data-newsid="1994520" class="text-type" data-origin="1"
                                    data-media="1" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="نفر به نفر با عملکرد بازیکنان ایران مقابل فلسطین" href="https://www.varzesh3.com/news/1994520/نفر-به-نفر-با-عملکرد-بازیکنان-ایران-مقابل-فلسطین" data-nt-link> <span class="news-type"></span>نفر به نفر با عملکرد بازیکنان ایران مقابل فلسطین</a>
                            </li>
                            <li data-newsid="322004" class="video-type" data-origin="3"
                                    data-media="2" 
                                    data-tag="" 
                                    data-sport="1">
                                <a title="منصوریان: حق حسن یزدانی هم حواله خودرو هست" href="https://video.varzesh3.com/video/322004/منصوریان-حق-حسن-یزدانی-هم-حواله-خودرو-هست" data-nt-link> <span class="news-type"></span>منصوریان: حق حسن یزدانی هم حواله خودرو هست</a>
                            </li>
                </ul>
            </div>
        </div>
    </div>
</div>
                </div>
            </div>
            


        



            <div class="widget-holder">
                <div id="83" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ های خارجی</span>
    </h2>
    <div class="select-options">
        <select id="stage-83">
                    <option value="902323" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902323">لیگ برتر انگلیس </option>
                    <option value="902339" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902339">بوندسلیگا آلمان </option>
                    <option value="902331" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902331">لالیگا اسپانیا </option>
                    <option value="902330" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902330">سری آ ایتالیا </option>
                    <option value="902332" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902332">لیگ یک فرانسه </option>
                    <option value="902340" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/83/league/902340">پریمیرلیگ پرتغال </option>
        </select>
        <select id="round-83">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15">هفته 15</option>
                    <option value="16">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21" selected="selected">هفته 21</option>
                    <option value="22">هفته 22</option>
                    <option value="23">هفته 23</option>
                    <option value="24">هفته 24</option>
                    <option value="25">هفته 25</option>
                    <option value="26">هفته 26</option>
                    <option value="27">هفته 27</option>
                    <option value="28">هفته 28</option>
                    <option value="29">هفته 29</option>
                    <option value="30">هفته 30</option>
                    <option value="31">هفته 31</option>
                    <option value="32">هفته 32</option>
                    <option value="33">هفته 33</option>
                    <option value="34">هفته 34</option>
                    <option value="35">هفته 35</option>
                    <option value="36">هفته 36</option>
                    <option value="37">هفته 37</option>
                    <option value="38">هفته 38</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#4285f4"><h3>لیگ برتر انگلیس</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 22 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356250/بازی-برنلی-لوتون"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356250/بازی-برنلی-لوتون" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>برنلی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>لوتون</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321790/خلاصه-بازی-برنلی-1-لوتون-1"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>شنبه 23 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356251/بازی-چلسی-فولام"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356251/بازی-چلسی-فولام" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>چلسی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>فولام</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321824/خلاصه-بازی-چلسی-1-فولام-0-گزارش-اختصاصی"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356254/بازی-نیوکسل-منچسترسیتی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356254/بازی-نیوکسل-منچسترسیتی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نیوکسل</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">3</span></div>
                                    <div class="fixture-result-match-guest"><span>منچسترسیتی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321848/خلاصه-بازی-نیوکسل-2-منچسترسیتی-3-گزارش-اختصاصی"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 24 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356252/بازی-اورتون-استون-ویلا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356252/بازی-اورتون-استون-ویلا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اورتون</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>استون ویلا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/322029/خلاصه-بازی-اورتون-0-استون-ویلا-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356253/بازی-منچستریونایتد-تاتنهام"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356253/بازی-منچستریونایتد-تاتنهام" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>منچستریونایتد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><span>تاتنهام</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321987/خلاصه-بازی-منچستر-یونایتد-2-تاتنهام-2"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>شنبه 30 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356246/بازی-آرسنال-کریستال-پالاس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356246/بازی-آرسنال-کریستال-پالاس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آرسنال</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>کریستال پالاس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356248/بازی-برنتفورد-ناتینگهام-فارست"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356248/بازی-برنتفورد-ناتینگهام-فارست" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>برنتفورد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ناتینگهام فارست</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">21:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 1 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356255/بازی-شفیلد-یونایتد-وستهم"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356255/بازی-شفیلد-یونایتد-وستهم" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>شفیلد یونایتد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>وستهم</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">17:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356247/بازی-بورنموث-لیورپول"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356247/بازی-بورنموث-لیورپول" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>بورنموث</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لیورپول</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>دوشنبه 2 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/356249/بازی-برایتون-ولورهمپتون"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/356249/بازی-برایتون-ولورهمپتون" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>برایتون</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ولورهمپتون</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">23:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/3/لیگ-برتر-انگلیس/بازی-ها" >برنامه بازی های لیگ برتر انگلیس</a></div>
                </div>
            </div>
            


        
        
        <div class="adbox" data-id="346">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-3545"></div>
                </div>
    </div>




            <div class="widget-holder">
                <div id="84" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">جدول لیگ های خارجی</span>
    </h2>
    <div class="select-options">
        <select id="stage-84">
                    <option value="902323" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902323">لیگ برتر انگلیس </option>
                    <option value="902339" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902339">بوندسلیگا آلمان </option>
                    <option value="902331" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902331">لالیگا اسپانیا </option>
                    <option value="902330" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902330">سری آ ایتالیا </option>
                    <option value="902332" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902332">لیگ یک فرانسه </option>
                    <option value="902340" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902340">پریمیرلیگ پرتغال </option>
                    <option value="902343" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902343">اردیویسه هلند </option>
                    <option value="902357" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902357">لیگ حرفه‌ای عربستان </option>
                    <option value="902342" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902342">ژوپیر لیگ بلژیک </option>
                    <option value="902341" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902341">لیگ برتر روسیه </option>
                    <option value="902344" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902344">لیگ برتر امارات </option>
                    <option value="902368" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902368">سوپر لیگ ترکیه </option>
                    <option value="902286" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902286">سری آ برزیل </option>
                    <option value="902202" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902202">سوپرلیگ آرژانتین </option>
                    <option value="902403" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902403">لیگ ستارگان قطر </option>
                    <option value="902262" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902262">جی لیگ ژاپن </option>
                    <option value="902261" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902261">کی لیگ کره جنوبی </option>
                    <option value="902383" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902383">پریمیرشیپ اسکاتلند </option>
                    <option value="902384" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902384">سوپرلیگ سوئیس </option>
                    <option value="902397" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902397">بوندسلیگا اتریش </option>
                    <option value="902398" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902398">لیگ برتر کرواسی </option>
                    <option value="902399" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902399">سوپرلیگ دانمارک </option>
                    <option value="902396" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902396">سوپرلیگ یونان </option>
                    <option value="902401" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902401">لیگ برتر قبرس </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#4285f4"><h3>جدول لیگ برتر انگلیس</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول لیگ برتر انگلیس</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><a href="/football/team/83/لیورپول"> لیورپول</a></td>
                                <td>20</td>
                                <td>45</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><a href="/football/team/84/منچسترسیتی"> منچسترسیتی</a></td>
                                <td>20</td>
                                <td>43</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><a href="/football/team/85/استون-ویلا"> استون ویلا</a></td>
                                <td>21</td>
                                <td>43</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><a href="/football/team/87/آرسنال"> آرسنال</a></td>
                                <td>20</td>
                                <td>40</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row"><a href="/football/team/86/تاتنهام"> تاتنهام</a></td>
                                <td>21</td>
                                <td>40</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row"><a href="/football/team/96/وستهم"> وستهم</a></td>
                                <td>20</td>
                                <td>34</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row"><a href="/football/team/82/منچستریونایتد"> منچستریونایتد</a></td>
                                <td>21</td>
                                <td>32</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row"><a href="/football/team/413/برایتون"> برایتون</a></td>
                                <td>20</td>
                                <td>31</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row"><a href="/football/team/81/چلسی"> چلسی</a></td>
                                <td>21</td>
                                <td>31</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row"><a href="/football/team/274/نیوکسل"> نیوکسل</a></td>
                                <td>21</td>
                                <td>29</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row"><a href="/football/team/92/ولورهمپتون"> ولورهمپتون</a></td>
                                <td>20</td>
                                <td>28</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row"><a href="/football/team/901069/بورنموث"> بورنموث</a></td>
                                <td>19</td>
                                <td>25</td>
                            </tr>
                            <tr>
                                <td>13</td>
                                <td scope="row"><a href="/football/team/94/فولام"> فولام</a></td>
                                <td>21</td>
                                <td>24</td>
                            </tr>
                            <tr>
                                <td>14</td>
                                <td scope="row"><a href="/football/team/900872/کریستال-پالاس"> کریستال پالاس</a></td>
                                <td>20</td>
                                <td>21</td>
                            </tr>
                            <tr>
                                <td>15</td>
                                <td scope="row"><a href="/football/team/340/ناتینگهام-فارست"> ناتینگهام فارست</a></td>
                                <td>20</td>
                                <td>20</td>
                            </tr>
                            <tr>
                                <td>16</td>
                                <td scope="row"><a href="/football/team/900810/برنتفورد"> برنتفورد</a></td>
                                <td>19</td>
                                <td>19</td>
                            </tr>
                            <tr>
                                <td>17</td>
                                <td scope="row"><a href="/football/team/93/اورتون"> اورتون</a></td>
                                <td>21</td>
                                <td>17</td>
                            </tr>
                            <tr>
                                <td>18</td>
                                <td scope="row"><a href="/football/team/902352/لوتون"> لوتون</a></td>
                                <td>20</td>
                                <td>16</td>
                            </tr>
                            <tr>
                                <td>19</td>
                                <td scope="row"><a href="/football/team/89/برنلی"> برنلی</a></td>
                                <td>21</td>
                                <td>12</td>
                            </tr>
                            <tr>
                                <td>20</td>
                                <td scope="row"><a href="/football/team/900956/شفیلد-یونایتد"> شفیلد یونایتد</a></td>
                                <td>20</td>
                                <td>9</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/3/لیگ-برتر-انگلیس" >جدول کامل لیگ برتر انگلیس</a></div>
                </div>
            </div>
            


        



            <div class="widget-holder">
                <div id="117" class="widget league schedual football">
                                

<div class="widget-header">
    <h2>جام‌های حذفی باشگاهی</h2>
    <div class="select-options">
        <select id="league-117">
                    <option value="22" selected="selected">جام حذفی ایران </option>
                    <option value="14">جام حذفی انگلیس </option>
                    <option value="13">جام اتحادیه انگلیس </option>
                    <option value="15">جام حذفی اسپانیا </option>
                    <option value="11">جام حذفی آلمان </option>
                    <option value="19">جام حذفی ایتالیا </option>
                    <option value="8">جام حذفی فرانسه </option>
                    <option value="68">جام حذفی پرتغال </option>
        </select>
        <select id="stage-117">
                    <option style='display: block' value="902503" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902503" data-league-default-stage="False">مرحله دوم </option>
                    <option style='display: none' value="902480" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902480" data-league-default-stage="False">مرحله اول </option>
                    <option style='display: none' value="902375" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902375" data-league-default-stage="False">مرحله اول </option>
                    <option style='display: none' value="902486" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902486" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: none' value="902376" data-league="11" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902376" data-league-default-stage="False">سی و دوم نهایی </option>
                    <option style='display: none' value="902379" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902379" data-league-default-stage="False">مرحله اول </option>
                    <option style='display: none' value="902520" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902520" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: none' value="902461" data-league="68" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902461" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: block' value="902522" selected="selected" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902522" data-league-default-stage="True">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902483" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902483" data-league-default-stage="False">مرحله دوم </option>
                    <option style='display: none' value="902391" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902391" data-league-default-stage="False">مرحله دوم </option>
                    <option style='display: none' value="902505" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902505" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902456" data-league="11" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902456" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902380" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902380" data-league-default-stage="False">یک سی و دوم  </option>
                    <option style='display: none' value="902525" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902525" data-league-default-stage="True">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902484" data-league="68" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902484" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902497" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902497" data-league-default-stage="False">مرحله سوم </option>
                    <option style='display: none' value="902422" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902422" data-league-default-stage="False">مرحله سوم </option>
                    <option style='display: none' value="902523" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902523" data-league-default-stage="True">یک هشتم نهایی </option>
                    <option style='display: none' value="902472" data-league="11" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902472" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: none' value="902405" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902405" data-league-default-stage="False">یک شانزدهم </option>
                    <option style='display: none' value="902496" data-league="68" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902496" data-league-default-stage="True">یک هشتم نهایی </option>
                    <option style='display: none' value="902524" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902524" data-league-default-stage="True">مرحله چهارم </option>
                    <option style='display: none' value="902454" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902454" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: none' value="902504" data-league="11" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902504" data-league-default-stage="True">یک چهارم نهایی </option>
                    <option style='display: none' value="902473" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902473" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: none' value="902467" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902467" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: none' value="902519" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902519" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: none' value="902510" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902510" data-league-default-stage="True">نیمه نهایی </option>
                    <option style='display: none' value="902526" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902526" data-league-default-stage="True">نیمه نهایی </option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:600px">
        <div class="scroll-list-content">
            <div class="widget-subtitle" style="background-color:#4285f4"><h3>یک شانزدهم نهایی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>چهارشنبه 18 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399566/بازی-پیکان-ستارگان-بهمن-جوان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399566/بازی-پیکان-ستارگان-بهمن-جوان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پیکان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ستارگان بهمن جوان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 19 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399557/بازی-نیروی-زمینی-فجر-سپاسی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399557/بازی-نیروی-زمینی-فجر-سپاسی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نیروی زمینی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>فجر سپاسی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399560/بازی-سپنتا-تربت-حیدریه-مس-کرمان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399560/بازی-سپنتا-تربت-حیدریه-مس-کرمان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سپنتا تربت حیدریه</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>مس کرمان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399570/بازی-چوکا-تالش-تراکتور"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399570/بازی-چوکا-تالش-تراکتور" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>چوکا تالش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>تراکتور</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399559/بازی-سایپا-پارس-جنوبی-جم"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399559/بازی-سایپا-پارس-جنوبی-جم" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سایپا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>پارس جنوبی جم</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">14:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399564/بازی-گل-گهرسیرجان-نیکاپارس-چالوس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399564/بازی-گل-گهرسیرجان-نیکاپارس-چالوس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>گل گهرسیرجان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نیکاپارس چالوس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399568/بازی-ذوب-آهن-آکادمی-کیا-تهران"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399568/بازی-ذوب-آهن-آکادمی-کیا-تهران" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ذوب آهن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آکادمی کیا تهران</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399572/بازی-صنعت-نفت-آبادان-استقلال-آبی-پوش-ملاثانی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399572/بازی-صنعت-نفت-آبادان-استقلال-آبی-پوش-ملاثانی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>صنعت نفت آبادان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>استقلال آبی پوش ملاثانی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399562/بازی-فولاد-چادرملو-اردکان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399562/بازی-فولاد-چادرملو-اردکان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>فولاد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>چادرملو اردکان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399571/بازی-مس-سونگون-شناورسازی-قشم"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399571/بازی-مس-سونگون-شناورسازی-قشم" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مس سونگون</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>شناورسازی قشم</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>جمعه 20 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399558/بازی-ملوان-شهر-راز-شیراز"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399558/بازی-ملوان-شهر-راز-شیراز" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ملوان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>شهر راز شیراز</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399561/بازی-نساجی-مازندران-آلومینیوم-اراک"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399561/بازی-نساجی-مازندران-آلومینیوم-اراک" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نساجی مازندران</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>آلومینیوم اراک</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399563/بازی-هوادار-استقلال-خوزستان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399563/بازی-هوادار-استقلال-خوزستان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>هوادار</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>استقلال خوزستان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399567/بازی-مس-رفسنجان-استقلال"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399567/بازی-مس-رفسنجان-استقلال" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مس رفسنجان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>استقلال</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399565/بازی-سپاهان-شمس-آذر-قزوین"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399565/بازی-سپاهان-شمس-آذر-قزوین" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>سپاهان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>شمس آذر قزوین</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399569/بازی-پرسپولیس-نفت-و-گاز-گچساران"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                 <a href="/football/match/399569/بازی-پرسپولیس-نفت-و-گاز-گچساران" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پرسپولیس</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نفت و گاز گچساران</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">18:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/playoffs/22/جام-حذفی-ایران">نمودار جام حذفی ایران</a></div>
                </div>
            </div>
            <div class="widget-holder">
                <div id="86" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">جام ملت‌های آفریقا 2023</span>
    </h2>
    <div class="select-options">
        <select id="stage-86">
                    <option value="902511" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902511">گروه A </option>
                    <option value="902512" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902512">گروه B </option>
                    <option value="902513" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902513">گروه C </option>
                    <option value="902514" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902514">گروه D </option>
                    <option value="902515" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902515">گروه E </option>
                    <option value="902516" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/86/league/902516">گروه F </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:300px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#004c1f"><h3>گروه A</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>شنبه 23 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399650/بازی-ساحل-عاج-گینه-بیسائو"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399650/بازی-ساحل-عاج-گینه-بیسائو" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ساحل عاج</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>گینه بیسائو</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 24 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399381/بازی-نیجریه-گینه-استوایی"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399381/بازی-نیجریه-گینه-استوایی" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>نیجریه</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>گینه استوایی</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321957/خلاصه-بازی-نیجریه-1-گینه-1"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 28 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399392/بازی-گینه-استوایی-گینه-بیسائو"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399392/بازی-گینه-استوایی-گینه-بیسائو" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>گینه استوایی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>گینه بیسائو</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">17:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399393/بازی-ساحل-عاج-نیجریه"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399393/بازی-ساحل-عاج-نیجریه" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ساحل عاج</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نیجریه</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>دوشنبه 2 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399404/بازی-گینه-استوایی-ساحل-عاج"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399404/بازی-گینه-استوایی-ساحل-عاج" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>گینه استوایی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>ساحل عاج</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399405/بازی-گینه-بیسائو-نیجریه"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/399405/بازی-گینه-بیسائو-نیجریه" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>گینه بیسائو</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>نیجریه</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#004c1f"><h3>جدول گروه A</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول گروه A</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><span> ساحل عاج</span></td>
                                <td>1</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><span> گینه استوایی</span></td>
                                <td>1</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><a href="/football/team/343/نیجریه"> نیجریه</a></td>
                                <td>1</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><span> گینه بیسائو</span></td>
                                <td>1</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/38/جام-ملت-های-آفریقا?group=902511" >جدول کامل جام ملت های آفریقا</a></div>
                </div>
            </div>
            <div class="widget-holder">
                <div id="77" class="widget league schedual football">
                                


<div class="widget-header" style="">
    <h2>
        
        <span style="">لیگ های ایران</span>
    </h2>
    <div class="select-options">
        <select id="stage-77">
                    <option value="902337" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/77/league/902337">لیگ برتر ایران </option>
                    <option value="902404" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/77/league/902404">لیگ آزادگان </option>
                    <option value="901969" data-api="https://web-api.varzesh3.com/v1.0/futsal/widgets/77/league/901969">لیگ برتر فوتسال </option>
                    <option value="17" data-api="https://web-api.varzesh3.com/v1.0/beach-soccer/widgets/77/league/17">لیگ برتر فوتبال ساحلی </option>
                    <option value="902469" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/77/league/902469">لیگ برتر زنان </option>
                    <option value="901970" data-api="https://web-api.varzesh3.com/v1.0/futsal/widgets/77/league/901970">سوپرلیگ فوتسال زنان </option>
        </select>
        <select id="round-77">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15" selected="selected">هفته 15</option>
                    <option value="16">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21">هفته 21</option>
                    <option value="22">هفته 22</option>
                    <option value="23">هفته 23</option>
                    <option value="24">هفته 24</option>
                    <option value="25">هفته 25</option>
                    <option value="26">هفته 26</option>
                    <option value="27">هفته 27</option>
                    <option value="28">هفته 28</option>
                    <option value="29">هفته 29</option>
                    <option value="30">هفته 30</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#f3b500"><h3>لیگ برتر ایران</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>شنبه 9 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392213/بازی-تراکتور-صنعت-نفت-آبادان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392213/بازی-تراکتور-صنعت-نفت-آبادان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>تراکتور</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>صنعت نفت آبادان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/320787/خلاصه-بازی-تراکتور-3-صنعت-نفت-آبادان-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392203/بازی-استقلال-پیکان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392203/بازی-استقلال-پیکان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>استقلال</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>پیکان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/320798/خلاصه-بازی-استقلال-2-پیکان-1"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 10 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392204/بازی-هوادار-استقلال-خوزستان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392204/بازی-هوادار-استقلال-خوزستان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>هوادار</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>استقلال خوزستان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/320902/خلاصه-بازی-هوادار-2-استقلال-خوزستان-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392207/بازی-آلومینیوم-اراک-ملوان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392207/بازی-آلومینیوم-اراک-ملوان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آلومینیوم اراک</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>ملوان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/320908/خلاصه-بازی-آلومینیوم-1-ملوان-1"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>دوشنبه 11 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392202/بازی-شمس-آذر-قزوین-سپاهان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392202/بازی-شمس-آذر-قزوین-سپاهان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>شمس آذر قزوین</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>سپاهان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/320991/خلاصه-بازی-شمس-آذر-1-سپاهان-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392214/بازی-مس-رفسنجان-پرسپولیس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392214/بازی-مس-رفسنجان-پرسپولیس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مس رفسنجان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>پرسپولیس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321008/خلاصه-بازی-مس-رفسنجان-1-پرسپولیس-1"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 13 دی</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392216/بازی-ذوب-آهن-گل-گهرسیرجان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392216/بازی-ذوب-آهن-گل-گهرسیرجان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ذوب آهن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>گل گهرسیرجان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321137/خلاصه-بازی-ذوب-آهن-0-گل-گهر-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/392206/بازی-فولاد-نساجی-مازندران"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>
                                    
                                </div>
                                <a href="/football/match/392206/بازی-فولاد-نساجی-مازندران" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>فولاد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>نساجی مازندران</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/321168/خلاصه-بازی-فولاد-1-نساجی-0"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/6/لیگ-برتر-ایران/بازی-ها" >برنامه بازی های لیگ برتر ایران</a></div>
                </div>
            </div>

                </div>
            </div>
        </div>
        <div class="left-side-ad-col ">
            <div class="side-banner-zone tb-holder widgets-parent-col">
                <div class="forfix">
                            
        <div class="adbox" data-id="3155">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3155" rel="nofollow"
                    style="background-color: #f5f5f5;height:200px">
                        <img class="adimage" id="img-3155" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/12/30/59fda90d-7ee2-4a6c-b670-17b2fc7f9b11.gif" 
                                                        width="160" 
                                                        height="200" alt="قصر شیرین" />
                </a>
    </div>

                            
        <div class="adbox" data-id="587">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/587" rel="nofollow"
                    style="background-color: #f5f5f5;height:200px">
                        <img class="adimage" id="img-587" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/06/1a046b21-fba3-41cb-8172-f766451f2830.gif" 
                                                        width="160" 
                                                        height="200" alt="سفیر" />
                </a>
    </div>

                            
        <div class="adbox" data-id="1935">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/1935" rel="nofollow"
                    style="background-color: #f5f5f5;height:400px">
                        <img class="adimage" id="img-1935" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/11/29/14947661-ba21-4fc0-b088-4fc4a684cb06.gif" 
                                                        width="160" 
                                                        height="400" alt="ویپی" />
                </a>
    </div>

                            
        <div class="adbox" data-id="2542">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2542" rel="nofollow"
                    style="background-color: #f5f5f5;height:300px">
                        <img class="adimage" id="img-2542" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/11/19/7cb04c40-5105-4451-ae2d-b5e7bd521325.gif" 
                                                        width="160" 
                                                        height="300" alt="افرانت " />
                </a>
    </div>

                            
        <div class="adbox" data-id="3405">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/3405" rel="nofollow"
                    style="background-color: #f5f5f5;height:200px">
                        <img class="adimage" id="img-3405" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/11/a1a05e60-a596-4d1d-a16d-b4388407c7df.gif" 
                                                        width="160" 
                                                        height="200" alt="بیت" />
                </a>
    </div>

                            
        <div class="adbox" data-id="182">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/182" rel="nofollow"
                    style="background-color: #f5f5f5;height:246px">
                        <img class="adimage" id="img-182" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2023/08/09/00954d89-d64f-4d8c-a070-02287f56052c.gif" 
                                                        width="160" 
                                                        height="246" alt="kwc" />
                </a>
    </div>

                            
        <div class="adbox" data-id="2840">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2840" rel="nofollow"
                    style="background-color: #f5f5f5;height:400px">
                        <img class="adimage" id="img-2840" src="https://static.varzesh3.com/img/blank.png" 
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/01/09/3014989a-3309-4cd1-b7e2-56ed6cc1a054.gif" 
                                                        width="160" 
                                                        height="400" alt="بیمه دات کام" />
                </a>
    </div>

                </div>
            </div>
        </div>
    </div>
</div>

        </main>
    </section>
    
<footer>
    <div class="allfooter">
        <div class="container">
            <div class="allfooter-menus">
                <div class="row">
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="راهنما" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/uqsoneco.svg?w=20" />
                                            راهنما
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/contact">ارتباط با ما</a></li>
                                            <li><a href="https://www.varzesh3.com/advertisement">تبلیغات</a></li>
                                            <li><a href="https://www.varzesh3.com/about">درباره ما</a></li>
                                            <li><a href="https://www.varzesh3.com/developer-tools">ابزار توسعه دهندگان</a></li>
                                            <li><a href="https://www.varzesh3.com/careers">فرصت های شغلی</a></li>
                                            <li><a href="https://www.varzesh3.com/policy">قوانین و مقررات</a></li>
                                            <li><a href="https://www.varzesh3.com/dmca">DMCA</a></li>
                                            <li><a href="https://www.varzesh3.com/bulletins">آگهی دولتی</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3q33ppav.svg?w=20" />
                                            سرویس ها
                                        </span>
                                    </li>
                                            <li><a href="https://video.varzesh3.com/freereporter">سوژه‌های ورزشی شما</a></li>
                                            <li><a href="https://www.varzesh3.com/news">اخبار ورزشی</a></li>
                                            <li><a href="https://www.varzesh3.com/podcast">پادکست</a></li>
                                            <li><a href="https://www.varzesh3.com/leagues">لیگ ها و رقابت ها</a></li>
                                            <li><a href="https://video.varzesh3.com/">ویدئو</a></li>
                                            <li><a href="https://www.varzesh3.com/newspaper">روزنامه</a></li>
                                            <li><a href="https://www.varzesh3.com/livescore">نتایج زنده</a></li>
                                            <li><a href="https://www.anten.ir/">آنتن</a></li>
                                            <li><a href="https://pishbini.varzesh3.com/">پیش بینی</a></li>
                                            <li><a href="https://www.varzesh3.com/پخش-زنده">پخش زنده</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="تیم های داخلی" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/4q4ntaac.svg?w=20" />
                                            تیم های داخلی
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/team/4/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84">استقلال</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/6/%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3">پرسپولیس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/18/%D8%AA%D8%B1%D8%A7%DA%A9%D8%AA%D9%88%D8%B1">تراکتور</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/1/%D8%B0%D9%88%D8%A8-%D8%A7%D9%93%D9%87%D9%86">ذوب آهن</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/10/%D8%B3%D9%BE%D8%A7%D9%87%D8%A7%D9%86">سپاهان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/21/%D8%B5%D9%86%D8%B9%D8%AA-%D9%86%D9%81%D8%AA-%D8%A7%D9%93%D8%A8%D8%A7%D8%AF%D8%A7%D9%86">صنعت نفت آبادان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/488/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AE%D9%88%D8%B2%D8%B3%D8%AA%D8%A7%D9%86">استقلال خوزستان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/9/%D9%81%D9%88%D9%84%D8%A7%D8%AF">فولاد</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/37/%D9%86%D8%B3%D8%A7%D8%AC%DB%8C-%D9%85%D8%A7%D8%B2%D9%86%D8%AF%D8%B1%D8%A7%D9%86">نساجی مازندران</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/14/%D9%85%D9%84%D9%88%D8%A7%D9%86">ملوان</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="تیم های خارجی" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/nupvsdov.svg?w=20" />
                                            تیم های خارجی
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/team/68/%D8%A7%D9%93%D8%AB-%D9%85%DB%8C%D9%84%D8%A7%D9%86">آث میلان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/63/%D8%A7%DB%8C%D9%86%D8%AA%D8%B1">اینتر میلان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/101/%D8%A8%D8%A7%D8%B1%D8%B3%D9%84%D9%88%D9%86%D8%A7">بارسلونا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/145/%D9%BE%D8%A7%D8%B1%DB%8C-%D8%B3%D9%86-%DA%98%D8%B1%D9%85%D9%86">پاری سن ژرمن</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/81/%DA%86%D9%84%D8%B3%DB%8C">چلسی</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/102/%D8%B1%D9%8A%D9%94%D8%A7%D9%84-%D9%85%D8%A7%D8%AF%D8%B1%DB%8C%D8%AF">رئال مادرید</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/83/%D9%84%DB%8C%D9%88%D8%B1%D9%BE%D9%88%D9%84">لیورپول</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/82/%D9%85%D9%86%DA%86%D8%B3%D8%AA%D8%B1%DB%8C%D9%88%D9%86%D8%A7%DB%8C%D8%AA%D8%AF">منچستریونایتد</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/62/%DB%8C%D9%88%D9%88%D9%86%D8%AA%D9%88%D8%B3">یوونتوس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/123/%D8%A8%D8%A7%DB%8C%D8%B1%D9%86-%D9%85%D9%88%D9%86%DB%8C%D8%AE">بایرن مونیخ</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            
                                            لیگ های پرطرفدار
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86">جدول لیگ برتر ایران (خلیج فارس)</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/24/%D9%84%DB%8C%DA%AF-%D8%A7%D9%93%D8%B2%D8%A7%D8%AF%DA%AF%D8%A7%D9%86">لیگ آزادگان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3">لیگ برتر انگلیس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7">لالیگا اسپانیا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/4/%D8%B3%D8%B1%DB%8C-%D8%A7%D9%93-%D8%A7%DB%8C%D8%AA%D8%A7%D9%84%DB%8C%D8%A7">سری آ ایتالیا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/25/%D9%84%DB%8C%DA%AF-%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86%D8%A7%D9%86-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7">لیگ قهرمانان اروپا</a></li>
                                            <li><a href="https://www.varzesh3.com/futsal/league/27/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D9%81%D9%88%D8%AA%D8%B3%D8%A7%D9%84">لیگ برتر فوتسال</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سایر" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3szclmgh.svg?w=20" />
                                            سایر
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/%D8%AC%D8%A7%D9%85-%D9%85%D9%84%D8%AA-%D9%87%D8%A7%DB%8C-%D8%A2%D8%B3%DB%8C%D8%A7-2023">جام ملت های آسیا</a></li>
                                            <li><a href="https://www.varzesh3.com/%D8%A8%D8%A7%D8%B2%DB%8C-%D9%87%D8%A7%DB%8C-%D8%A2%D8%B3%DB%8C%D8%A7%DB%8C%DB%8C-%D9%87%D8%A7%D9%86%DA%AF%DA%98%D9%88">بازی‌های آسیایی هانگژو</a></li>
                                            <li><a href="https://www.varzesh3.com/football/world-cup/qatar-2022">جام جهانی 2022 قطر</a></li>
                                            <li><a href="https://www.varzesh3.com/football/fifa-ranking">رنکینگ فیفا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/transfers/euro/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7">نقل و انتقالات اروپا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/transfers/iran/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1">نقل و انتقالات ایران</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/403/%D9%BE%D9%88%D8%B1%D8%AA%D9%88">پورتو</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/162/%D9%81%D8%A7%DB%8C%D9%86%D9%88%D8%B1%D8%AF">فاینورد</a></li>
                                </ul>
                            </div>
                </div>
            </div>
            <div class="allfooter-copy">
                <div class="footerlogo"><span class="footer-logo-holder"><img alt="ورزش سه" width="20" height="20" src="https://static.varzesh3.com/img/shared/footer/logo.svg?w=20" /></span><span>ورزش سه</span></div>
                <div class="copyright" data-nosnippet>تمام حقوق مادی و معنوی این سایت متعلق به ورزش سه می باشد. شما می توانید از سایت ورزش سه در صورت پذیرش موافقت نامه کاربری استفاده نمایید.</div>
                <div class="socials">
                    <a target="_blank" rel="noopener noreferrer" href="https://facebook.com/varzesh3"> <img alt="فیس بوک" width="8" height="15" src="https://static.varzesh3.com/img/shared/footer/social/facebook.svg?w=8" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@Varzesh3."> <img alt="یوتیوب" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/youtube.svg?w=15" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/varzesh3"><img alt="توییتر" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/twitter.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.instagram.com/varzesh3"><img alt="اینستاگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/instagram.svg?w=15" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://t.me/varzesh3"><img alt="تلگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/telegram.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.varzesh3.com/rss/list"><img alt="خبرخوان" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/rss.svg?w=15" /></a>
                </div>
            </div>
        </div>
    </div>
</footer>

    

<div class="searchbox" data-search-url="https://search-api.varzesh3.com/v1.0/query?q=">
    <form id="vrz-search-form" method="GET" role="search" autocomplete="off" action="/search">
        <div class="input-holder">
            <input id="main-search" class="search" type="search" name="q" placeholder="جستجوی اخبار، تیم‌ها، بازیکنان، ویدیوهای ورزشی …" />
            <span class="close-search">
                <img alt="close" src="https://static.varzesh3.com/img/icons/close-icon.svg" />
            </span>
        </div>
    </form>
</div>

<div class="search-ajax-result">
    <div id="search-result-tags tagbox ">
        <div class="search-content-type-title">
            برچسب ها
        </div>
        <div class="result-box tags-res tags"></div>
    </div>
    <div id="search-result-news">
        <div class="search-content-type-title">
            اخبار
        </div>
        <div class="result-box  news-res row"></div>
    </div>
    <div id="search-result-videos">
        <div class="search-content-type-title">
            ویدیوها
        </div>
        <div class="result-box  videos-res row"></div>
    </div>
    <div class="see-all">
        مشاهده همه نتایج
    </div>
</div>
    <div class="dark-shadow"></div>
    <span id="gotop"></span>
    <div id="alertModal" class="modal fade alerts-show" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                <div class="modal-body"></div>
            </div>
        </div>
    </div>
    <script>
        window.appSettings = {
            imageServer: "https://static.varzesh3.com/",
            ssoClientId:"0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568",
            ssoUrl:"https://sso.varzesh3.com",
            newsSocket: "https://ksocket.varzesh3.com/news",
            livescoreSocket: "https://ksocket.varzesh3.com/live",
            adsViewUrl: "https://biz.varzesh3.com/events/view",
            adsViewSamplePercentage: 10,
            newsViewSamplePercentage: 20,
            profileUrl : "https://www.varzesh3.com/profile",
            notification:{
                getNotifications: "https://web-api.varzesh3.com/v1.0/notifications",
                hasUnread: "https://web-api.varzesh3.com/v1.0/notifications/has-unread",
                readAll: "https://web-api.varzesh3.com/v1.0/notifications/read-all"
            },
            push:{
                subscribe: "https://web-api.varzesh3.com/push/subscribe",
                unsubscribe: "https://web-api.varzesh3.com/push/unsubscribe",
                vapidPublicKey: "BDV-XVXf3EnF9Bpd0XRNy6Sb6mULOlg5ThoeL0aEYYbKMHNCgKObnYqNkD5xD6kSrsyYGWilcFkf-hhdRC-EPfA"
            }
        };
    </script>
    <script src="https://static.varzesh3.com/js/global.vendor.js?v=1.99.12"></script>
    <script src="https://static.varzesh3.com/js/sharedLayout.js?v=1.99.12"></script>
    <script src="https://static.varzesh3.com/js/home.js?v=1.99.12"></script>
<script>
            !function(e,t,n){e.yektanetAnalyticsObject=n,e[n]=e[n]||function(){e[n].q.push(arguments)},e[n].q=e[n].q||[];var a=t.getElementsByTagName("head")[0],r=new Date,c="https://cdn.yektanet.com/superscript/IYoZo4ye/article.v1/yn_pub.js?v="+r.getFullYear().toString()+"0"+r.getMonth()+"0"+r.getDate()+"0"+r.getHours(),s=t.createElement("link");s.rel="preload",s.as="script",s.href=c,a.appendChild(s);var l=t.createElement("script");l.async=!0,l.src=c,a.appendChild(l)}(window,document,"yektanet");
        </script>
    <script src="https://static.varzesh3.com/js/vrzLazy.js?v=1.99.12"></script>

</body>
</html>

    '''


app.run(port=5000,debug=True)